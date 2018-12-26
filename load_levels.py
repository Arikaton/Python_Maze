from tiledtmxloader import tmxreader, helperspygame
import pygame as pg


def load_level(name):
    global player_x, player_y
    global total_level_width, total_level_height
    global sprite_layers

    world_map = tmxreader.TileMapParser().parse_decode('%s/%s.tmx' % (FILE_DIR, name))
    resources = helperspygame.ResourceLoaderPygame()
    resources.load(world_map)
    sprite_layers = helperspygame.get_layers_from_map(resources)

    ground = sprite_layers[0]

    for row in range(0, ground.num_tiles_x):
        for col in range(0, ground.num_tiles_y):
            wl = Walls.WoodWall(row, col)
            Walls.append(wl)

    total_level_width = ground.num_tiles_x*WALL_WIDTH
    total_level_height = ground.num_tiles_y*WALL_HEIGHT

for sprite_layer in sprite_layers:
    renderer.render_layer(screen, sprite_layer)