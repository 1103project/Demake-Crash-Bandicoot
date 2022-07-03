from .. import setup, tools
from ..components import info
from ..components import player, stuff, brick, crate, enemy, fruit
from .. import constants as C
import pygame
import json
import os


class Level:
    def start(self, game_info):
        self.game_info = game_info
        self.finished = False
        self.next = 'game_over'
        self.info = info.Info('level', game_info)
        self.load_map_data()
        self.setup_background()
        self.setup_start_position()
        self.setup_player()
        self.setup_ground_items()
        self.setup_bricks_and_crates()
        self.setup_enemies()
        self.setup_checkpoints()
        self.setup_fruit()

    def load_map_data(self):
        file_name = 'level.json'
        file_path = os.path.join('source/data', file_name)
        with open(file_path) as f:
            self.map_data = json.load(f)

    def setup_background(self):
        self.image_name = self.map_data['image_name']
        self.background = setup.GRAPHICS[self.image_name]
        rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background,
                                                 (int(rect.width * 3), int(rect.height * 3)))  # 放大，同mainMenu
        self.background_rect = self.background.get_rect()
        self.game_window = setup.SCREEN.get_rect()
        self.game_ground = pygame.Surface((self.background_rect.width, self.background_rect.height))

    def setup_start_position(self):
        self.positions = []
        data = self.map_data['map']
        self.positions.append((data['start_x'], data['end_x'], data['player_x'], data['player_y']))
        self.start_x, self.end_x, self.player_x, self.player_y = self.positions[0]

    def setup_player(self):
        self.player = player.Player('bandicoot')
        self.player.rect.x = self.game_window.x + self.player_x
        self.player.rect.bottom = self.player_y

    def setup_ground_items(self):
        self.ground_items_group = pygame.sprite.Group()
        for name in ['ground', 'ice']:
            for item in self.map_data[name]:
                self.ground_items_group.add(stuff.Item(item['x'], item['y'], item['width'], item['height'], name))

    def setup_bricks_and_crates(self):
        self.brick_group = pygame.sprite.Group()
        self.crate_group = pygame.sprite.Group()
        if 'brick' in self.map_data:
            for brick_data in self.map_data['brick']:
                x, y = brick_data['x'], brick_data['y']
                brick_type = brick_data['type']
                if 'brick_num' in brick_data:

                    pass
                else:
                    self.brick_group.add(brick.Brick(x, y, brick_type))

        if 'crate' in self.map_data:
            for crate_data in self.map_data['crate']:
                x, y = crate_data['x'], crate_data['y']
                crate_type = crate_data['type']


                self.crate_group.add(crate.Crate(x, y, crate_type))

    def setup_enemies(self):
        self.dying_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.enemy_group_dict = {}
        for enemy_group_data in self.map_data['enemy']:
            group = pygame.sprite.Group()
            for enemy_group_id, enemy_list in enemy_group_data.items():
                for enemy_data in enemy_list:
                    group.add(enemy.create_enemy(enemy_data))
                self.enemy_group_dict[enemy_group_id] = group

    def setup_checkpoints(self):
        self.checkpoint_group = pygame.sprite.Group()
        for item in self.map_data['checkpoint']:
            x, y, w, h = item['x'], item['y'], item['width'], item['height']
            checkpoint_type = item['type']
            enemy_groupid = item.get('enemy_groupid')
            self.checkpoint_group.add(stuff.Checkpoint(x, y, w, h, checkpoint_type, enemy_groupid))


    def setup_fruit(self):
        self.fruit_group = pygame.sprite.Group()
        if 'fruit' in self.map_data:
            for fruit_data in self.map_data['fruit']:
                x, y = fruit_data['x'], fruit_data['y']
                self.fruit_group.add(fruit.Fruit(x, y))

    def update(self, surface, keys):
        self.current_time = pygame.time.get_ticks()
        self.player.update(keys)

        if self.player.dead:
            if self.current_time - self.player.death_timer > 2000:
                self.finished = True
                self.update_game_info()
        else:
            self.update_player_position()
            self.check_checkpoints()
            self.check_if_go_die()
            self.update_game_window()
            self.info.update(surface)
            self.crate_group.update()
            self.enemy_group.update(self)
            self.dying_group.update(self)
            self.fruit_group.update(self)
            self.life_fruit_append()
            self.jump_strengthen()

        self.draw(surface)

    def update_player_position(self):
        # x direction
        self.player.rect.x += self.player.x_vel
        if self.player.rect.x < self.start_x:
            self.player.rect.x = self.start_x
        elif self.player.rect.right > self.end_x:
            self.player.rect.right = self.end_x
        self.check_x_collision()

        # y direction
        self.player.rect.y += self.player.y_vel
        self.check_y_collision()
        self.check_fruit_collistion()
        self.check_if_on_ice()
        # self.life_fruit_append()


    def check_x_collision(self):
        checkcrate_group = pygame.sprite.Group.copy(self.crate_group)
        cratecollide = pygame.sprite.spritecollideany(self.player, checkcrate_group)
        if cratecollide:
            if cratecollide.crate_type == 0:
                pass

            if cratecollide.crate_type == 1:
                pass

            if cratecollide.crate_type == 2:
                if self.player.span == True:
                    self.crate_group.remove(cratecollide)
                    self.game_info['fruit'] += 1
                    self.game_info['life_append'] += 1

            if cratecollide.crate_type == 3:
                pass

            if cratecollide.crate_type == 4:
                pass

            if cratecollide.crate_type == 5:
                if self.player.span == True:
                    self.crate_group.remove(cratecollide)
                    self.game_info['life'] += 1

            if cratecollide.crate_type == 6:
                pass

            if cratecollide.crate_type == 7:
                if self.player.span == True:
                    self.player.go_die()
            self.adjust_player_x(cratecollide)

        check_group = pygame.sprite.Group.copy(self.ground_items_group)

        # tools.sprite_group_add(check_group, self.crate_group)
        ground_item = pygame.sprite.spritecollideany(self.player, check_group)
        if ground_item and ground_item.name == 'ground':
            self.adjust_player_x(ground_item)
        elif ground_item and ground_item.name == 'ice':
            self.player_tp(ground_item)


        enemy = pygame.sprite.spritecollideany(self.player, self.enemy_group)
        if enemy:
            self.enemy_group.remove(enemy)
            self.dying_group.add(enemy)
            if self.player.span:
                enemy.go_die('span')
            else:
                self.player.go_die()

    def check_y_collision(self):

        checkcrate_group = pygame.sprite.Group.copy(self.crate_group)
        cratecollide = pygame.sprite.spritecollideany(self.player, checkcrate_group)


        if cratecollide :
            if cratecollide.crate_type == 0:
                pass

            if cratecollide.crate_type == 1:
                self.game_info['arrow'] = 1

            if cratecollide.crate_type == 2:
                if self.player.span == True:
                    self.crate_group.remove(cratecollide)
                    self.game_info['fruit'] += 1
                    self.game_info['life_append'] += 1

            if cratecollide.crate_type == 3:
                if self.player.span == True:
                    self.crate_group.remove(cratecollide)
                    self.game_info['fruit'] += 10
                    self.game_info['life'] += 1

            if cratecollide.crate_type == 4:
                pass

            if cratecollide.crate_type == 5:
                if self.player.span == True:
                    self.crate_group.remove(cratecollide)
                    self.game_info['life'] += 1

            if cratecollide.crate_type == 6:
                pass


            if cratecollide.crate_type == 7:
                if self.player.span == True:
                    self.player.go_die()

            self.adjust_player_y(cratecollide)


        check_group = pygame.sprite.Group.copy(self.ground_items_group)
        # tools.sprite_group_add(check_group, self.crate_group)
        ground_item = pygame.sprite.spritecollideany(self.player, check_group)

        if ground_item and ground_item.name == 'ground':
            self.adjust_player_y(ground_item)
        elif ground_item and ground_item.name == 'ice':
            self.adjust_player_y(ground_item)
            self.player_tp(ground_item)

        self.check_will_fall(self.player)
        enemy = pygame.sprite.spritecollideany(self.player, self.enemy_group)
        if enemy:
            self.enemy_group.remove(enemy)
            self.dying_group.add(enemy)
            if self.player.span == True:
                how = 'span'
            elif self.player.y_vel >= 0:
                if enemy.name == 'turtle':
                    how = 'trampled'
                    self.player.state = 'jump'
                    self.player.rect.bottom = enemy.rect.top
                    self.player.y_vel = self.player.jump_vel * 1.2
                    enemy.x_vel *= -1
                    enemy.direction = 1 if enemy.direction == 0 else 0
                elif enemy.name == 'flyingfish':
                    self.player.die()
                    how = 'trampled'
            enemy.go_die(how)


    def adjust_player_x(self, sprite):
        if self.player.rect.x < sprite.rect.x:
            self.player.rect.right = sprite.rect.left
        else:
            self.player.rect.left = sprite.rect.right
        self.player.x_vel = 0


    def player_tp(self, sprite):

        if self.player.face_right == True:
            if self.player.rect.x < sprite.rect.right:
                self.player.rect.x += 50

        if self.player.face_right == False:
            if self.player.rect.right > sprite.rect.left:
                self.player.rect.x -= 50
        self.player.state = 'tp'


    def check_if_on_ice(self):

        if  self.player.face_right == True:
            if self.player.rect.left > 4720 and self.player.rect.right < 4770:
                self.player.state = 'walk'
        if self.player.face_right == False:
            if self.player.rect.right < 4225 and self.player.rect.left > 4175:
                self.player.state = 'walk'


    def adjust_player_y(self, sprite):
        # downwords
        if self.player.rect.bottom < sprite.rect.bottom:
            self.player.y_vel = 0
            self.player.rect.bottom = sprite.rect.top
            self.player.state = 'walk'
        # upwards
        else:
            self.player.y_vel = 7
            self.player.rect.top = sprite.rect.bottom
            self.player.state = 'fall'

    #
    def check_will_fall(self, sprite):
        sprite.rect.y += 1
        check_group = pygame.sprite.Group.copy(self.ground_items_group)
        tools.sprite_group_add(check_group, self.crate_group)
        collided = pygame.sprite.spritecollideany(sprite, check_group)
        if not collided and sprite.state != 'jump':
            sprite.state = 'fall'
        sprite.rect.y -= 1

    def check_fruit_collistion(self):
        check_fruit_group = pygame.sprite.Group.copy(self.fruit_group)
        fruit_collistion = pygame.sprite.spritecollideany(self.player, check_fruit_group)
        if fruit_collistion:
            self.game_info['fruit'] += 1
            self.game_info['life_append'] += 1
            fruit_collistion.kill()

    def life_fruit_append(self):
        if self.game_info['life_append'] != 0 and self.game_info['life_append'] % 10 == 0:
            self.game_info['life'] += 1
            self.game_info['life_append'] = 0








    def update_game_window(self):
        half = self.game_window.x + self.game_window.width / 2
        if self.player.x_vel > 0 and self.player.rect.centerx > half and self.game_window.right < self.end_x:
            self.game_window.x += self.player.x_vel

    def draw(self, surface):
        self.game_ground.blit(self.background, self.game_window, self.game_window)
        self.game_ground.blit(self.player.image, self.player.rect)
        self.brick_group.draw(self.game_ground)
        self.crate_group.draw(self.game_ground)
        self.enemy_group.draw(self.game_ground)
        self.fruit_group.draw(self.game_ground)

        surface.blit(self.game_ground, (0, 0), self.game_window)
        self.info.draw(surface)

    def check_checkpoints(self):
        checkpoint = pygame.sprite.spritecollideany(self.player, self.checkpoint_group)
        if checkpoint:
            if checkpoint.checkpoint_type == 0:
                self.enemy_group.add(self.enemy_group_dict[str(checkpoint.enemy_groupid)])
            checkpoint.kill()

    def check_if_go_die(self):
        if self.player.rect.y > C.SCREEN_H:
            self.player.go_die()

    def update_game_info(self):
        if self.player.dead:
            self.game_info['life'] -= 1
        if self.game_info['life'] == 0:
            self.next = 'game_over'

    def check_crate(self, cratecollide):


        if cratecollide and self.player.span == True:
            if cratecollide.crate_type == 1:

                self.game_info['arrow'] = 1
            if cratecollide.crate_type == 2:
                self.crate_group.remove(cratecollide)
            if cratecollide.crate_type == 3:
                self.crate_group.remove(cratecollide)
            if cratecollide.crate_type == 4:
                self.crate_group.remove(cratecollide)
            if cratecollide.crate_type == 5:
                self.crate_group.remove(cratecollide)
            if cratecollide.crate_type == 7:
                self.player.go_die()
            if cratecollide.crate_type == 8:
                self.player.go_die()

    def jump_strengthen(self):
        if self.game_info['arrow'] == 1 and self.player.state == 'jump':
            self.player.rect.y -= 100
            self.game_info['arrow'] = 0


