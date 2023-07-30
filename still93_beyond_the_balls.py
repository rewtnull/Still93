from still93_runtime_hooker import MEGA05
MEGA5 = MEGA05()
### GLOBAL
screen_w = MEGA5.screen_w
screen_h = MEGA5.screen_h
screen = MEGA5.screen
pg = MEGA5.pg
np = MEGA5.np
os = MEGA5.os
sys = MEGA5.sys
c_void_p = MEGA5.c_void_p
c_float = MEGA5.c_float
resource_path = MEGA5.resource_path
glEnable = MEGA5.glEnable
glDisable = MEGA5.glDisable
glBlendFunc = MEGA5.glBlendFunc
glClearDepth = MEGA5.glClearDepth
glClearColor = MEGA5.glClearColor
glClear = MEGA5.glClear
glViewport = MEGA5.glViewport
glMatrixMode = MEGA5.glMatrixMode
glLoadIdentity = MEGA5.glLoadIdentity
glGenBuffers = MEGA5.glGenBuffers
glBindBuffer = MEGA5.glBindBuffer
glBufferData = MEGA5.glBufferData
glBufferSubData = MEGA5.glBufferSubData
glDeleteBuffers = MEGA5.glDeleteBuffers
glGenTextures = MEGA5.glGenTextures
glBindTexture = MEGA5.glBindTexture
glDeleteTextures = MEGA5.glDeleteTextures
glTexImage2D = MEGA5.glTexImage2D
glTexParameteri = MEGA5.glTexParameteri
glDrawArrays = MEGA5.glDrawArrays
glPushMatrix = MEGA5.glPushMatrix
glPopMatrix = MEGA5.glPopMatrix
GL_COLOR_BUFFER_BIT = MEGA5.GL_COLOR_BUFFER_BIT
GL_DEPTH_BUFFER_BIT = MEGA5.GL_DEPTH_BUFFER_BIT
GL_PROJECTION = MEGA5.GL_PROJECTION
GL_MODELVIEW = MEGA5.GL_MODELVIEW
GL_ARRAY_BUFFER = MEGA5.GL_ARRAY_BUFFER
GL_TEXTURE_2D = MEGA5.GL_TEXTURE_2D
GL_RGBA = MEGA5.GL_RGBA
GL_UNSIGNED_BYTE = MEGA5.GL_UNSIGNED_BYTE
GL_FLOAT = MEGA5.GL_FLOAT
GL_TEXTURE_MIN_FILTER = MEGA5.GL_TEXTURE_MIN_FILTER
GL_TEXTURE_MAG_FILTER = MEGA5.GL_TEXTURE_MAG_FILTER
GL_LINEAR = MEGA5.GL_LINEAR
### LOCAL
sqrt = MEGA5.sqrt
time = MEGA5.time
glBegin = MEGA5.glBegin
glEnd = MEGA5.glEnd
glColor3f = MEGA5.glColor3f
glVertex3f = MEGA5.glVertex3f
gluPerspective = MEGA5.gluPerspective
glOrtho = MEGA5.glOrtho
glDepthFunc = MEGA5.glDepthFunc
glDepthMask = MEGA5.glDepthMask
glColorPointer = MEGA5.glColorPointer
glNormalPointer = MEGA5.glNormalPointer
glTranslatef = MEGA5.glTranslatef
glLightfv = MEGA5.glLightfv
glFogfv = MEGA5.glFogfv
glFogf = MEGA5.glFogf
glFogi = MEGA5.glFogi
glHint = MEGA5.glHint
glScalef = MEGA5.glScalef
glColor4f = MEGA5.glColor4f
glTexCoordPointer = MEGA5.glTexCoordPointer
glRotatef = MEGA5.glRotatef
glIndexPointer = MEGA5.glIndexPointer
glDrawElements = MEGA5.glDrawElements
glEnableClientState = MEGA5.glEnableClientState
glDisableClientState = MEGA5.glDisableClientState
glVertexPointer = MEGA5.glVertexPointer
glVertex2f = MEGA5.glVertex2f
GL_DYNAMIC_DRAW = MEGA5.GL_DYNAMIC_DRAW
GL_NEAREST = MEGA5.GL_NEAREST
GL_DEPTH_TEST = MEGA5.GL_DEPTH_TEST
GL_LEQUAL = MEGA5.GL_LEQUAL
GL_TRUE = MEGA5.GL_TRUE
GL_COLOR_ARRAY = MEGA5.GL_COLOR_ARRAY
GL_NORMAL_ARRAY = MEGA5.GL_NORMAL_ARRAY
GL_TRIANGLES = MEGA5.GL_TRIANGLES
GL_LIGHTING = MEGA5.GL_LIGHTING
GL_LIGHT0 = MEGA5.GL_LIGHT0
GL_LIGHT1 = MEGA5.GL_LIGHT1
GL_LIGHT2 = MEGA5.GL_LIGHT2
GL_LIGHT3 = MEGA5.GL_LIGHT3
GL_POSITION = MEGA5.GL_POSITION
GL_DIFFUSE = MEGA5.GL_DIFFUSE
GL_AMBIENT = MEGA5.GL_AMBIENT
GL_LIGHT_MODEL_AMBIENT = MEGA5.GL_LIGHT_MODEL_AMBIENT
GL_NORMALIZE = MEGA5.GL_NORMALIZE
GL_COLOR_MATERIAL = MEGA5.GL_COLOR_MATERIAL
GL_FRONT = MEGA5.GL_FRONT
GL_FOG = MEGA5.GL_FOG
GL_FOG_COLOR = MEGA5.GL_FOG_COLOR
GL_FOG_MODE = MEGA5.GL_FOG_MODE
GL_FOG_START = MEGA5.GL_FOG_START
GL_FOG_END = MEGA5.GL_FOG_END
GL_INT = MEGA5.GL_INT
GL_UNSIGNED_INT = MEGA5.GL_UNSIGNED_INT
GL_ELEMENT_ARRAY_BUFFER = MEGA5.GL_ELEMENT_ARRAY_BUFFER
GL_INDEX_ARRAY = MEGA5.GL_INDEX_ARRAY
GL_FOG_HINT = MEGA5.GL_FOG_HINT
GL_NICEST = MEGA5.GL_NICEST
GL_SRC_ALPHA = MEGA5.GL_SRC_ALPHA
GL_VERTEX_ARRAY = MEGA5.GL_VERTEX_ARRAY
GL_ONE_MINUS_SRC_ALPHA = MEGA5.GL_ONE_MINUS_SRC_ALPHA
GL_BLEND = MEGA5.GL_BLEND
GL_QUADS = MEGA5.GL_QUADS
GL_TEXTURE_COORD_ARRAY = MEGA5.GL_TEXTURE_COORD_ARRAY

pg.mixer.init()
pg.mixer.music.load(resource_path('resources/goto80-sound_off_show.mod'))
pg.mixer.music.play(-1)

balls_aspect = 45
balls_near = 5.0
balls_far = 12.0

glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LEQUAL)
glDepthMask(GL_TRUE)
glEnable(GL_COLOR_MATERIAL)
glClearDepth(1.0)
glClearColor(0.0, 0.1, 0.1, 1.0)
glViewport(0, 0, screen_w, screen_h)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(balls_aspect, (screen_w / screen_h), balls_near, balls_far)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glTranslatef(0.0, 0.0, -8.0)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glEnable(GL_LIGHT1)
glEnable(GL_LIGHT2)
glEnable(GL_LIGHT3)
glLightfv(GL_LIGHT0, GL_POSITION, (0.1, 0.5, -0.5, -1.0))
glLightfv(GL_LIGHT0, GL_AMBIENT, (0.3, 0.3, 0.3, 0.5))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.7, 0.7, 0.8, 0.8))
glLightfv(GL_LIGHT1, GL_POSITION, (1.0, -0.5, 1.0, 1.0))
glLightfv(GL_LIGHT1, GL_AMBIENT, (0.2, 0.1, 0.1, 1.0))
glLightfv(GL_LIGHT1, GL_DIFFUSE, (0.4, 0.8, 0.6, 0.8))
glLightfv(GL_LIGHT2, GL_POSITION, (-1.0, -1.0, -1.0, -0.5))
glLightfv(GL_LIGHT2, GL_AMBIENT, (0.1, 0.2, 1.0, 1.0))
glLightfv(GL_LIGHT2, GL_DIFFUSE, (0.2, 0.5, 0.9, 0.9))
glLightfv(GL_LIGHT3, GL_POSITION, (0.3, -0.8, 0.0, 0.0))
glLightfv(GL_LIGHT3, GL_AMBIENT, (0.1, 0.2, 1.0, 1.0))
glLightfv(GL_LIGHT3, GL_DIFFUSE, (0.3, 0.9, 0.9, 0.9))

font_atlas_img_path = resource_path('resources/boheme-still93_font_blue.png')
font_atlas_surf = pg.image.load(font_atlas_img_path).convert_alpha()
font_atlas_w, font_atlas_h = font_atlas_surf.get_size()
font_atlas = pg.image.tostring(font_atlas_surf, "RGBA")
font_char_w, font_char_h = 50, 50

character_spacing = -10
text_scale = 1.0
text_speed = 8.0
scroll_scale_factor = 3.3
text_pos_x = screen_w * 3
text_pos_y = screen_h * 2 - font_char_h * 13
num_chars_x = font_atlas_w // font_char_w
num_chars_y = font_atlas_w // font_char_h
scroll_text = "                                                              *** HELLO, SPIKEY BALL ***                                                    ... BUT WE CAN DO BETTER THAN THIS! ...                                                      PRESENTING THE SPIKIER BALL!!!                                                                                             DID YOU REALLY THINK THAT'S ALL WE'VE GOT???                                                                                                                    NO MORE SPIKEY BALLS!!!!!                                                             BAH, THIS IS CHILD'S PLAY....... TIME TO KICK IT UP A NOTCH!!!!!!                                                                         *** PENROSE TILE GLENZ DMGHEDRON ***                                                                                                                                                            TIME TO FINISH THIS...                                                                                                                                                                                                                                                                                                                                                                                                                                                                          * KISS OUR CONVERSE *                                                                                                                                                                                                                                                                                                                                                                                           "
rotation_angle_x = 0.0
rotation_angle_y = 0.0
rotation_angle_z = 0.0
rotation_speed_x = 0.0
rotation_speed_y = 0.0
rotation_speed_z = 0.0
rotation_x = 0.0
rotation_y = 0.0
rotation_z = 0.0
position_x = 0.0
position_y = 0.0
position_z = 1.0

fx1_draw_type = "triangles"
fx1_depth = False
sub_level1 = 2
sub_div1 = 1
time_offset1 = True
fx1_triggered = True
fx1_blend = False

fx2_draw_type = "triangles"
fx2_depth = True
sub_level2 = 2
sub_div2 = 1
time_offset2 = True
fx2_triggered = True
fx2_blend = False

fx3_draw_type = "quads"
fx3_depth = False
sub_level3 = 4
sub_div3 = 1
time_offset3 = True
fx3_triggered = True
fx3_blend = False

fx4_draw_type = "triangles"
fx4_depth = True
sub_level4 = 4
sub_div4 = 0
time_offset4 = True
fx4_triggered = True
fx4_blend = True

fx5_draw_type = "quads"
fx5_depth = True
sub_level5 = 4
sub_div5 = 1
time_offset5 = True
fx5_triggered = True
fx5_blend = True

prev_position, prev_rotation, prev_timestamp = None, None, None
next_position, next_rotation, next_timestamp = None, None, None

def generatre_font_metrics(num_chars_x, font_char_w, font_char_h):
    font_metrics = {}
    for char_code in range(32, 256):
        char = chr(char_code)
        row = (char_code - 32) // num_chars_x
        col = (char_code - 32) % num_chars_x
        font_metrics[char] = (col * font_char_w, row * font_char_h)
    return font_metrics

def create_verts_and_coords(text, x, y, font_metrics):
    text_verts = []
    text_coords = []
    for i, char in enumerate(text):
        font_char_x_position, font_char_y_position = font_metrics.get(char, (0, 0))
        tex_left = font_char_x_position / font_atlas_w
        tex_right = (font_char_x_position + font_char_w) / font_atlas_w
        tex_bottom = font_char_y_position / font_atlas_h
        tex_top = (font_char_y_position + font_char_h) / font_atlas_h
        char_pos_x = x + i * (font_char_w * text_scale + character_spacing)
        char_pos_y = y
        corners = np.array([[0, 0],
                            [font_char_w * text_scale, 0],
                            [font_char_w * text_scale, font_char_h * text_scale],
                            [0, font_char_h * text_scale]])
        center = np.array([font_char_w * text_scale, font_char_h * text_scale])
        rotated_corners = corners - center

        text_verts.extend([char_pos_x + rotated_corners[0, 0], char_pos_y + rotated_corners[0, 1],
                         char_pos_x + rotated_corners[1, 0], char_pos_y + rotated_corners[1, 1],
                         char_pos_x + rotated_corners[2, 0], char_pos_y + rotated_corners[2, 1],
                         char_pos_x + rotated_corners[3, 0], char_pos_y + rotated_corners[3, 1]])
        text_coords.extend([tex_left, tex_bottom, tex_right, tex_bottom, tex_right, tex_top, tex_left, tex_top])

    text_verts = np.array(text_verts, dtype=np.float32)
    text_coords = np.array(text_coords, dtype=np.float32)
    text_vbo = glGenBuffers(1)
    text_vbo = np.uint32(text_vbo)
    glBindBuffer(GL_ARRAY_BUFFER, text_vbo)
    glBufferData(GL_ARRAY_BUFFER, text_verts.nbytes + text_coords.nbytes, None, GL_DYNAMIC_DRAW)
    glBufferSubData(GL_ARRAY_BUFFER, 0, text_verts.nbytes, text_verts)
    glBufferSubData(GL_ARRAY_BUFFER, text_verts.nbytes, text_coords.nbytes, text_coords)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    return text_vbo, text_verts.nbytes, text_verts.size

def text_draw(vbo, font_atlas_id, verts_size, verts_nbytes):
    glEnable(GL_BLEND)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, font_atlas_id)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glVertexPointer(2, GL_FLOAT, 0, None)
    glEnableClientState(GL_VERTEX_ARRAY)
    glTexCoordPointer(2, GL_FLOAT, 0, c_void_p(verts_nbytes))
    glEnableClientState(GL_TEXTURE_COORD_ARRAY)
    glDrawArrays(GL_QUADS, 0, verts_size // 2)
    glDisableClientState(GL_TEXTURE_COORD_ARRAY)
    glDisableClientState(GL_VERTEX_ARRAY)
    glBindTexture(GL_TEXTURE_2D, 0)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glDisable(GL_BLEND)
    glDisable(GL_TEXTURE_2D)
    glDeleteBuffers(1, [vbo])

def font_atlas_texture_buffer(font_atlas, font_atlas_w, font_atlas_h):
    font_atlas_texture_id = glGenTextures(1)
    font_atlas_texture_id = np.uint32(font_atlas_texture_id)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, font_atlas_texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, font_atlas_w, font_atlas_h, 0, GL_RGBA, GL_UNSIGNED_BYTE, font_atlas)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)
    return font_atlas_texture_id

def create_dmghedron(subdivide_level, depth=False, subdivisions=0):
    a = 1
    phi = (1 + sqrt(5)) / 2
    verts = np.array([
        (0.0, a, phi * a),
        (0.0, a, -phi * a),
        (0.0, -a, phi * a),
        (0.0, -a, -phi * a),
        (phi * a, 0.0, a),
        (phi * a, 0.0, -a),
        (-phi * a, 0.0, a),
        (-phi * a, 0.0, -a),
        (a, phi * a, 0.0),
        (a, -phi * a, 0.0),
        (-a, phi * a, 0.0),
        (-a, -phi * a, 0.0)
    ], dtype=np.float32)

    indices = np.array([
        (0, 8, 4),
        (0, 5, 10),
        (2, 4, 9),
        (2, 11, 5),
        (1, 6, 8),
        (1, 10, 7),
        (3, 9, 6),
        (3, 7, 11),
        (0, 10, 8),
        (1, 8, 10),
        (2, 9, 11),
        (3, 11, 9),
        (4, 2, 0),
        (5, 0, 2),
        (6, 1, 3),
        (7, 3, 1),
        (8, 6, 4),
        (9, 4, 6),
        (10, 5, 7),
        (11, 7, 5)
    ], dtype=np.uint32)

    colors = np.array([
        (1.0, 0.5, 0.6, 0.8),
        (0.0, 0.0, 0.0, 0.7),
        (0.0, 0.5, 1.0, 0.6),
        (1.0, 1.0, 0.0, 0.8),
        (1.0, 0.0, 0.0, 0.7),
        (1.0, 0.0, 1.0, 0.6),
        (0.0, 1.0, 0.0, 0.8),
        (1.0, 0.0, 0.0, 0.7),
        (0.0, 0.0, 1.0, 0.6),
        (1.0, 1.0, 0.0, 0.8),
        (1.0, 0.0, 1.0, 0.7),
        (1.0, 0.0, 0.0, 0.6)
    ], dtype=np.float32)

    if subdivide_level > 0:

        for _ in range(subdivide_level):
            new_verts = []
            new_indices = []
            new_colors = []

            for triangle in indices:
                v1 = verts[triangle[0]]
                v2 = verts[triangle[1]]
                v3 = verts[triangle[2]]

                v12 = ((v1[0] + v2[0]) / 2, (v1[1] + v2[1]) / 2, (v1[2] + v2[2]) / 2)
                v23 = ((v2[0] + v3[0]) / 2, (v2[1] + v3[1]) / 2, (v2[2] + v3[2]) / 2)
                v31 = ((v3[0] + v1[0]) / 2, (v3[1] + v1[1]) / 2, (v3[2] + v1[2]) / 2)

                new_verts.extend([v1, v12, v31, v2, v23, v12, v3, v31, v23, v12, v23, v31])

                index_offset = len(new_verts) - 12

                new_indices.extend([
                    (index_offset, index_offset + 1, index_offset + 2),
                    (index_offset + 3, index_offset + 4, index_offset + 5),
                    (index_offset + 6, index_offset + 7, index_offset + 8),
                    (index_offset + 9, index_offset + 10, index_offset + 11)
                ])

                new_colors.extend([(*colors[triangle[0]], colors[triangle[0]][3]),
                                   (*colors[triangle[1]], colors[triangle[1]][3]),
                                   (*colors[triangle[2]], colors[triangle[2]][3])] * 4)

            if depth:
                verts = new_verts
                indices = new_indices
                colors = new_colors

        if not depth:
            verts = new_verts
            indices = new_indices
            colors = new_colors

    if subdivisions > 0:

        for _ in range(subdivisions):
            new_indices = []
            midpoints = []

            for triangle in indices:
                v1 = verts[triangle[0]]
                v2 = verts[triangle[1]]
                v3 = verts[triangle[2]]

                v4 = normalize(midpoint(v1, v2))
                v5 = normalize(midpoint(v2, v3))
                v6 = normalize(midpoint(v3, v1))

                if v4 not in midpoints:
                    midpoints.append(v4)
                if v5 not in midpoints:
                    midpoints.append(v5)
                if v6 not in midpoints:
                    midpoints.append(v6)

                i1 = len(verts) + midpoints.index(v4)
                i2 = len(verts) + midpoints.index(v5)
                i3 = len(verts) + midpoints.index(v6)

                new_indices.extend([
                    (triangle[0], i1, i3),
                    (i1, triangle[1], i2),
                    (i3, i2, triangle[2]),
                    (i1, i2, i3)
                ])
            if subdivide_level > 0:
                verts.extend(midpoints)
            else:
                verts = np.concatenate((verts, midpoints))
            indices = new_indices
    verts = np.array(verts, dtype=np.float32)
    indices = np.array(indices, dtype=np.uint32)
    colors = np.array(colors, dtype=np.float32)
    verts_nbytes = verts.nbytes
    colors_nbytes = colors.nbytes
    indices_size = indices.size
    return verts, colors, indices, verts_nbytes, colors_nbytes, indices_size

def midpoint(v1, v2):
    return (
        (v1[0] + v2[0]) / 2,
        (v1[1] + v2[1]) / 2,
        (v1[2] + v2[2]) / 2
    )

def normalize(vector):
    length = sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)
    return (
        vector[0] / length,
        vector[1] / length,
        vector[2] / length
    )

def calculate_normals(verts, indices):
    normals = []
    for triangle in indices:
        v1 = verts[triangle[0]]
        v2 = verts[triangle[1]]
        v3 = verts[triangle[2]]
        normal = (
            (v2[1] - v1[1]) * (v3[2] - v1[2]) - (v2[2] - v1[2]) * (v3[1] - v1[1]),
            (v2[2] - v1[2]) * (v3[0] - v1[0]) - (v2[0] - v1[0]) * (v3[2] - v1[2]),
            (v2[0] - v1[0]) * (v3[1] - v1[1]) - (v2[1] - v1[1]) * (v3[0] - v1[0])
        )
        length = sqrt(normal[0] ** 2 + normal[1] ** 2 + normal[2] ** 2)
        normal = (normal[0] / length, normal[1] / length, normal[2] / length)
        normals.append(normal)
    normals = np.array(normals, dtype=np.float32)
    return normals

def object_update_movement(object_movement_list, rotation_angle_x, rotation_angle_y, rotation_angle_z, time_offset):
    current_time = time() + time_offset
    for position, rotation, timestamp in object_movement_list:
        if timestamp <= current_time:
            prev_position, prev_rotation, prev_timestamp = position, rotation, timestamp
        else:
            next_position, next_rotation, next_timestamp = position, rotation, timestamp
            break
    try:
        position_x, position_y, position_z = 0.0, 0.0, 0.0
        rotation_x, rotation_y, rotation_z = 0.0, 0.0, 0.0
        if prev_position is not None and next_position is not None:
            position_time_diff = next_timestamp - prev_timestamp
            if position_time_diff > 0:
                t = (current_time - prev_timestamp) / position_time_diff
                position_x = prev_position[0] + t * (next_position[0] - prev_position[0])
                position_y = prev_position[1] + t * (next_position[1] - prev_position[1])
                position_z = prev_position[2] + t * (next_position[2] - prev_position[2])
            rotation_time_diff = next_timestamp - prev_timestamp
            if rotation_time_diff > 0:
                t = (current_time - prev_timestamp) / rotation_time_diff
                rotation_x = prev_rotation[0] + t * (next_rotation[0] - prev_rotation[0])
                rotation_y = prev_rotation[1] + t * (next_rotation[1] - prev_rotation[1])
                rotation_z = prev_rotation[2] + t * (next_rotation[2] - prev_rotation[2])
    except UnboundLocalError:
        verts = False
        colors = False
        indices = False
        normals = False
        verts_nbytes = False
        colors_nbytes = False
        indices_size = False
        object_movement_list = False
        pass
    rotation_angle_x += rotation_speed_x
    rotation_angle_y += rotation_speed_y
    rotation_angle_z += rotation_speed_z
    return position_x, position_y, position_z, rotation_x, rotation_y, rotation_z, rotation_angle_x, rotation_angle_y, rotation_angle_z, object_movement_list, current_time

def dmghedron_buffers(verts, indices, colors, normals):
    dmghedron_data_size = verts.nbytes + colors.nbytes + normals.nbytes
    dmghedron_verts_vbo = glGenBuffers(1)
    dmghedron_verts_vbo = np.uint32(dmghedron_verts_vbo)
    glBindBuffer(GL_ARRAY_BUFFER, dmghedron_verts_vbo)
    glBufferData(GL_ARRAY_BUFFER, dmghedron_data_size, None, GL_DYNAMIC_DRAW)
    glBufferSubData(GL_ARRAY_BUFFER, 0, verts.nbytes, verts)
    glBufferSubData(GL_ARRAY_BUFFER, verts.nbytes, colors.nbytes, colors)
    glBufferSubData(GL_ARRAY_BUFFER, verts.nbytes + colors.nbytes, normals.nbytes, normals)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    dmghedron_indices_vbo = glGenBuffers(1)
    dmghedron_indices_vbo = np.uint32(dmghedron_indices_vbo)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, dmghedron_indices_vbo)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_DYNAMIC_DRAW)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)
    return dmghedron_verts_vbo, dmghedron_indices_vbo

def draw_dmghedron(dmghedron_verts_vbo, dmghedron_indices_vbo, verts_nbytes, colors_nbytes, indices_size, draw_type="triangles"):
    glBindBuffer(GL_ARRAY_BUFFER, dmghedron_verts_vbo)
    glVertexPointer(3, GL_FLOAT, 0, None)
    glEnableClientState(GL_VERTEX_ARRAY)
    glColorPointer(4, GL_FLOAT, 0, c_void_p(verts_nbytes))
    glEnableClientState(GL_COLOR_ARRAY)
    glNormalPointer(GL_FLOAT, 0, c_void_p(verts_nbytes + colors_nbytes))
    glEnableClientState(GL_NORMAL_ARRAY)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, dmghedron_indices_vbo)
    glIndexPointer(GL_INT, 0, None)
    glEnableClientState(GL_INDEX_ARRAY)
    if draw_type == "triangles":
        glDrawElements(GL_TRIANGLES, indices_size, GL_UNSIGNED_INT, None)
    elif draw_type == "quads":
        glDrawElements(GL_QUADS, indices_size * 3, GL_UNSIGNED_INT, None)
    elif draw_type == "dots":
        glDrawElements(GL_POINTS, indices_size, GL_UNSIGNED_INT, None)
    else:
        print(f"{draw_type}: Invalid draw type")
    glDisableClientState(GL_VERTEX_ARRAY)
    glDisableClientState(GL_COLOR_ARRAY)
    glDisableClientState(GL_NORMAL_ARRAY)
    glDisableClientState(GL_INDEX_ARRAY)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)
    glBindBuffer(GL_ARRAY_BUFFER, 0)

def backgrounds_buffers():
    bg1_vbo = glGenBuffers(1)
    bg1_vbo = np.uint32(bg1_vbo)
    glBindBuffer(GL_ARRAY_BUFFER, bg1_vbo)

    bg1_verts = np.array([
        -5.0, -4.0, 0.0, 0.0, 0.0, 1.0,
        5.0, -4.0, 0.0, 0.0, 0.0, 1.0,
        5.0, 4.0, 0.03666666666666667, 0.1607843137254902, 0.20980392156862746, 1.0,
        -5.0, 4.0, 0.03666666666666667, 0.1607843137254902, 0.20980392156862746, 1.0
    ], dtype=np.float32)

    glBufferData(GL_ARRAY_BUFFER, bg1_verts, GL_DYNAMIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, 0)

    bg1_stride = 6 * bg1_verts.itemsize

    bg2_vbo = glGenBuffers(1)
    bg2_vbo = np.uint32(bg2_vbo)
    glBindBuffer(GL_ARRAY_BUFFER, bg2_vbo)

    bg2_verts = np.array([
        -5.0, -4.0, 0.1, 0.1, 0.1, 0.5,
        5.0, -4.0, 0.1, 0.1, 0.1, 0.5,
        5.0, 4.0, 0.0, 0.0, 0.0, 1.0,
        -5.0, 4.0, 0.0, 0.0, 0.0, 1.0
    ], dtype=np.float32)

    glBufferData(GL_ARRAY_BUFFER, bg2_verts, GL_DYNAMIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, 0)

    bg2_stride = 6 * bg2_verts.itemsize

    bg3_vbo = glGenBuffers(1)
    bg3_vbo = np.uint32(bg3_vbo)
    glBindBuffer(GL_ARRAY_BUFFER, bg3_vbo)

    bg3_verts = np.array([
        -5.0, -4.0, 1.0, 0.0, 0.0, 1.0,
        5.0, -4.0, 1.0, 0.0, 0.0, 1.0,
        5.0, 4.0, 0.0, 0.0, 1.0, 1.0,
        -5.0, 4.0, 0.0, 0.0, 1.0, 1.0
    ], dtype=np.float32)

    glBufferData(GL_ARRAY_BUFFER, bg3_verts, GL_DYNAMIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, 0)

    bg3_stride = 6 * bg3_verts.itemsize

    bg4_vbo = glGenBuffers(1)
    bg4_vbo = np.uint32(bg4_vbo)
    glBindBuffer(GL_ARRAY_BUFFER, bg4_vbo)

    bg4_verts = np.array([
        -5.0, -4.0, 0.0, 0.3, 0.1, 1.0,
        5.0, -4.0, 0.0, 0.0, 0.0, 1.0,
        5.0, 4.0, 0.0, 0.3, 0.1, 1.0,
        -5.0, 4.0, 0.0, 0.0, 0.0, 1.0
    ], dtype=np.float32)

    glBufferData(GL_ARRAY_BUFFER, bg4_verts, GL_DYNAMIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, 0)

    bg4_stride = 6 * bg4_verts.itemsize

    bg5_vbo = glGenBuffers(1)
    bg5_vbo = np.uint32(bg5_vbo)
    glBindBuffer(GL_ARRAY_BUFFER, bg5_vbo)

    bg5_verts = np.array([
        -5.0, -4.0, 0.0, 0.0, 0.0, 1.0,
        5.0, -4.0, 0.5, 0.0, 0.0, 1.0,
        5.0, 4.0, 0.0, 0.2, 0.0, 1.0,
        -5.0, 4.0, 0.0, 0.0, 0.0, 1.0
    ], dtype=np.float32)

    glBufferData(GL_ARRAY_BUFFER, bg5_verts, GL_DYNAMIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, 0)

    bg5_stride = 6 * bg5_verts.itemsize

    return bg1_vbo, bg2_vbo, bg3_vbo, bg4_vbo, bg5_vbo,\
    bg1_stride, bg2_stride, bg3_stride, bg4_stride, bg5_stride,\
    bg1_verts.itemsize, bg2_verts.itemsize, bg3_verts.itemsize, bg4_verts.itemsize, bg5_verts.itemsize

def enable_fog(color, mode, near, far, hint):
    glEnable(GL_FOG)
    glFogfv(GL_FOG_COLOR, color)
    glFogi(GL_FOG_MODE, mode)
    glFogf(GL_FOG_START, near)
    glFogf(GL_FOG_END, far)
    glHint(GL_FOG_HINT, hint)

object5_movement_list = [
    ((0.0, 0.0, 4.999999999999999), (-478.80000000000206, -372.39999999999884, 133.0), 1690226152.1025467),
    ((0.0, 0.0, 4.999999999999999), (-532.8000000000018, -414.39999999999816, 148.0), 1690226153.1039498),
    ((0.0, 0.0, 4.8), (-586.8000000000004, -456.3999999999975, 163.0), 1690226154.1047573),
    ((0.0, 0.0, 4.7), (-640.799999999999, -498.3999999999968, 178.0), 1690226155.1099539),
    ((0.0, 0.0, 4.500000000000001), (-694.7999999999977, -540.3999999999961, 193.0), 1690226156.1162467),
    ((0.0, 0.0, 4.500000000000001), (-748.7999999999963, -582.3999999999954, 208.0), 1690226157.1298819),
    ((0.0, 0.0, 4.500000000000001), (-802.799999999995, -624.3999999999947, 223.0), 1690226158.136926),
    ((0.0, 0.0, 4.400000000000001), (-856.7999999999936, -666.3999999999941, 238.0), 1690226159.1466537),
    ((0.0, 0.0, 4.200000000000002), (-910.7999999999922, -708.3999999999934, 253.0), 1690226160.154839),
    ((0.0, 0.0, 4.200000000000002), (-964.7999999999909, -750.3999999999927, 268.0), 1690226161.1619492),
    ((0.0, 0.0, 4.100000000000002), (-1018.7999999999895, -792.399999999992, 283.0), 1690226162.1697638),
    ((0.0, 0.0, 4.000000000000003), (-1072.7999999999881, -834.3999999999913, 298.0), 1690226163.1779537),
    ((0.0, 0.0, 4.000000000000003), (-1126.7999999999868, -876.3999999999907, 313.0), 1690226164.1872845),
    ((0.0, 0.0, 3.7000000000000024), (-1180.7999999999854, -918.39999999999, 328.0), 1690226165.1943285),
    ((0.0, 0.0, 3.7000000000000024), (-1234.799999999984, -960.3999999999893, 343.0), 1690226166.1991403),
    ((0.0, 0.0, 3.7000000000000024), (-1288.7999999999827, -1002.3999999999886, 358.0), 1690226167.2027252),
    ((0.0, 0.0, 3.7000000000000024), (-1342.7999999999813, -1044.3999999999896, 373.0), 1690226168.2054887),
    ((0.0, 0.0, 3.7000000000000024), (-1396.79999999998, -1086.3999999999924, 388.0), 1690226169.2071877),
    ((0.0, 0.0, 3.7000000000000024), (-1450.7999999999786, -1128.399999999995, 403.0), 1690226170.2146392),
    ((0.0, 0.0, 3.7000000000000024), (-1504.7999999999772, -1170.3999999999978, 418.0), 1690226171.2239432),
    ((0.0, 0.0, 3.7000000000000024), (-1558.7999999999759, -1212.4000000000005, 433.0), 1690226172.228367),
    ((0.0, 0.0, 3.7000000000000024), (-1612.7999999999745, -1254.4000000000033, 448.0), 1690226173.234459),
    ((0.0, 0.0, 3.7000000000000024), (-1666.7999999999731, -1296.400000000006, 463.0), 1690226174.2434304),
    ((0.0, 0.0, 3.7000000000000024), (-1720.7999999999718, -1338.4000000000087, 478.0), 1690226175.2533689),
    ((0.0, 0.0, 3.6000000000000023), (-1774.7999999999704, -1380.4000000000115, 493.0), 1690226176.2629883),
    ((0.0, 0.0, 3.6000000000000023), (-1828.799999999969, -1422.4000000000142, 508.0), 1690226177.2757225),
    ((0.0, 0.0, 3.6000000000000023), (-1882.7999999999677, -1464.400000000017, 523.0), 1690226178.2868874),
    ((0.0, 0.0, 3.6000000000000023), (-1936.7999999999663, -1506.4000000000196, 538.0), 1690226179.3002512),
    ((0.0, 0.0, 3.400000000000002), (-1990.799999999965, -1548.4000000000224, 553.0), 1690226180.3054252),
    ((0.0, 0.0, 3.400000000000002), (-2044.7999999999636, -1590.400000000025, 568.0), 1690226181.3141708),
    ((0.0, 0.0, 3.400000000000002), (-2098.799999999969, -1632.4000000000278, 583.0), 1690226182.3247058),
    ((0.0, 0.0, 3.400000000000002), (-2152.7999999999743, -1674.4000000000306, 598.0), 1690226183.3319862),
    ((0.0, 0.0, 3.300000000000002), (-2206.7999999999797, -1716.4000000000333, 613.0), 1690226184.337759),
    ((0.0, 0.0, 3.300000000000002), (-2260.799999999985, -1758.400000000036, 628.0), 1690226185.343901),
    ((0.0, 0.0, 3.300000000000002), (-2314.7999999999906, -1800.4000000000387, 643.0), 1690226186.3526094),
    ((0.0, 0.0, 3.200000000000002), (-2368.799999999996, -1842.4000000000415, 658.0), 1690226187.3626893),
    ((0.0, 0.0, 3.200000000000002), (-2422.8000000000015, -1884.4000000000442, 673.0), 1690226188.3675082),
    ((0.0, 0.0, 3.200000000000002), (-2476.800000000007, -1926.400000000047, 688.0), 1690226189.373531),
    ((0.0, 0.0, 3.200000000000002), (-2530.8000000000125, -1968.4000000000497, 703.0), 1690226190.3813412),
    ((0.0, 0.0, 3.200000000000002), (-2584.800000000018, -2010.4000000000524, 718.0), 1690226191.3895113),
    ((0.0, 0.0, 3.200000000000002), (-2638.8000000000234, -2052.400000000055, 733.0), 1690226192.3977394),
    ((0.0, 0.0, 3.200000000000002), (-2692.800000000029, -2094.400000000058, 748.0), 1690226193.4038875),
    ((0.0, 0.0, 3.0000000000000018), (-2746.8000000000343, -2136.4000000000606, 763.0), 1690226194.4096243),
    ((0.0, 0.0, 3.0000000000000018), (-2800.8000000000397, -2178.4000000000633, 778.0), 1690226195.4145436),
    ((0.0, 0.0, 2.9000000000000017), (-2854.800000000045, -2220.400000000066, 793.0), 1690226196.418493),
    ((0.0, 0.0, 2.8000000000000016), (-2908.8000000000507, -2262.4000000000688, 808.0), 1690226197.421993),
    ((0.0, 0.0, 2.8000000000000016), (-2962.800000000056, -2304.4000000000715, 823.0), 1690226198.4263237),
    ((0.0, 0.0, 2.7000000000000015), (-3016.8000000000616, -2346.400000000074, 838.0), 1690226199.4329762),
    ((0.0, 0.0, 2.6000000000000014), (-3070.800000000067, -2388.400000000077, 853.0), 1690226200.4426293),
    ((0.0, 0.0, 2.6000000000000014), (-3124.8000000000725, -2430.4000000000797, 868.0), 1690226201.4475331),
    ((0.0, 0.0, 2.5000000000000013), (-3178.800000000078, -2472.4000000000824, 883.0), 1690226202.4540846),
    ((0.0, 0.0, 2.4000000000000012), (-3232.8000000000834, -2514.400000000085, 898.0), 1690226203.4603615),
    ((0.0, 0.0, 2.4000000000000012), (-3286.800000000089, -2556.400000000088, 913.0), 1690226204.468172),
    ((0.0, 0.0, 2.4000000000000012), (-3340.8000000000943, -2598.4000000000906, 928.0), 1690226205.476992),
    ((0.0, 0.0, 2.4000000000000012), (-3394.8000000000998, -2640.4000000000933, 943.0), 1690226206.4822786),
    ((0.0, 0.0, 2.4000000000000012), (-3448.8000000001052, -2682.400000000096, 958.0), 1690226207.4896274),
    ((0.0, 0.0, 2.4000000000000012), (-3502.8000000001107, -2724.4000000000988, 973.0), 1690226208.500469),
    ((0.0, 0.0, 2.4000000000000012), (-3556.800000000116, -2766.4000000001015, 988.0), 1690226209.5101132),
    ((0.0, 0.0, 2.100000000000001), (-3610.8000000001216, -2808.4000000001042, 1003.0), 1690226210.5154731),
    ((0.0, 0.0, 1.9000000000000008), (-3664.800000000127, -2850.400000000107, 1018.0), 1690226211.5219617),
    ((0.0, 0.0, 1.9000000000000008), (-3718.8000000001325, -2892.4000000001097, 1033.0), 1690226212.5271108),
    ((0.0, 0.0, 1.9000000000000008), (-3772.800000000138, -2934.4000000001124, 1048.0), 1690226213.5337243),
    ((0.0, 0.0, 1.9000000000000008), (-3826.8000000001434, -2976.400000000115, 1063.0), 1690226214.5451365),
    ((0.0, 0.0, 1.9000000000000008), (-3880.800000000149, -3018.400000000118, 1078.0), 1690226215.551969),
    ((0.0, 0.0, 1.9000000000000008), (-3934.8000000001543, -3060.4000000001206, 1093.0), 1690226216.5594015),
    ((0.0, 0.0, 1.9000000000000008), (-3988.80000000016, -3102.4000000001233, 1108.0), 1690226217.5677762),
    ((0.0, 0.0, 1.9000000000000008), (-4042.8000000001653, -3144.400000000126, 1123.0), 1690226218.576781),
    ((0.0, 0.0, 1.9000000000000008), (-4096.80000000017, -3186.400000000129, 1138.0), 1690226219.5854828),
    ((0.0, 0.0, 1.9000000000000008), (-4145.800000000176, -3228.4000000001315, 1153.0), 1690226220.5874777),
    ((0.0, 0.0, 1.9000000000000008), (-4199.800000000181, -3270.4000000001342, 1168.0), 1690226221.5941777),
    ((0.0, 0.0, 1.9000000000000008), (-4253.800000000187, -3312.400000000137, 1183.0), 1690226222.6054306),
    ((0.0, 0.0, 1.6000000000000005), (-4307.800000000192, -3354.4000000001397, 1198.0), 1690226223.6147444),
    ((0.0, 0.0, 1.0), (-4361.8000000001975, -3396.4000000001424, 1213.0), 1690226224.6234825),
    ((0.0, 0.0, 0.30000000000000016), (-4415.800000000203, -3438.400000000145, 1228.0), 1690226225.6294076),
    ((0.0, 0.0, -0.3999999999999999), (-4469.8000000002085, -3480.400000000148, 1243.0), 1690226226.6359804),
    ((0.0, 0.0, -1.0999999999999999), (-4523.800000000214, -3522.4000000001506, 1258.0), 1690226227.648219),
    ((0.0, 0.0, -1.7000000000000004), (-4577.800000000219, -3564.4000000001533, 1273.0), 1690226228.650688),
    ((0.0, 0.0, -2.400000000000001), (-4631.800000000225, -3606.400000000156, 1288.0), 1690226229.6558628),
    ((0.0, 0.0, -3.1000000000000014), (-4685.80000000023, -3648.400000000159, 1303.0), 1690226230.6637573),
    ((0.0, 0.0, -3.700000000000002), (-4739.800000000236, -3690.4000000001615, 1318.0), 1690226231.6706634),
    ((0.0, 0.0, -4.4), (-4793.800000000241, -3732.4000000001643, 1333.0), 1690226232.6771061),
    ((0.0, 0.0, -5.099999999999998), (-4847.800000000247, -3774.400000000167, 1348.0), 1690226233.68433),
    ((0.0, 0.0, -5.699999999999996), (-4901.800000000252, -3816.4000000001697, 1363.0), 1690226234.6958501),
    ((0.0, 0.0, -5.899999999999995), (-4955.800000000258, -3858.4000000001724, 1378.0), 1690226235.7031493),
]

object4_movement_list = [
    ((6.799999999999992, 0.0, 0.20000000000000015), (-15593.399999997593, -12128.199999998102, 4332.5), 1688904547.6398165),
    ((6.499999999999993, 0.0, 0.20000000000000015), (-15645.599999997572, -12168.799999998091, 4347.0), 1688904548.6421094),
    ((5.799999999999995, 0.0, 0.20000000000000015), (-15699.59999999755, -12210.79999999808, 4362.0), 1688904549.642809),
    ((5.1999999999999975, 0.0, 0.20000000000000015), (-15753.599999997528, -12252.79999999807, 4377.0), 1688904550.6464584),
    ((4.5, 0.0, 0.20000000000000015), (-15809.399999997506, -12296.199999998058, 4392.5), 1688904551.647027),
    ((3.8000000000000016, 0.0, 0.20000000000000015), (-15865.199999997483, -12339.599999998047, 4408.0), 1688904552.6496346),
    ((3.200000000000001, 0.0, 0.20000000000000015), (-15915.599999997463, -12378.799999998037, 4422.0), 1688904553.657589),
    ((2.5000000000000004, 0.0, 0.20000000000000015), (-15969.599999997441, -12420.799999998026, 4437.0), 1688904554.6634529),
    ((1.7999999999999998, 0.0, 0.20000000000000015), (-16023.59999999742, -12462.799999998015, 4452.0), 1688904555.6730819),
    ((1.1999999999999993, 0.0, 0.20000000000000015), (-16079.399999997397, -12506.199999998003, 4467.5), 1688904556.680615),
    ((0.49999999999999933, 0.0, 0.20000000000000015), (-16135.199999997374, -12549.599999997992, 4483.0), 1688904557.6921163),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-16192.79999999735, -12594.39999999798, 4499.0), 1688904558.6955616),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-16246.799999997329, -12636.39999999797, 4514.0), 1688904559.7039425),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-16302.599999997306, -12679.799999997958, 4529.5), 1688904560.7099123),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-16361.999999997282, -12725.999999997946, 4546.0), 1688904561.7136667),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-16419.59999999726, -12770.799999997935, 4562.0), 1688904562.7196803),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-16478.999999997235, -12816.999999997923, 4578.5), 1688904563.7213848),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-16534.799999997213, -12860.399999997911, 4594.0), 1688904564.7244468),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-16588.79999999719, -12902.3999999979, 4609.0), 1688904565.7334538),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-16648.199999997167, -12948.599999997889, 4625.5), 1688904566.739331),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-16705.799999997143, -12993.399999997877, 4641.5), 1688904567.743437),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-16765.19999999712, -13039.599999997865, 4658.0), 1688904568.750272),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-16820.999999997097, -13082.999999997854, 4673.5), 1688904569.7533493),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-16874.999999997075, -13124.999999997843, 4688.5), 1688904570.7563329),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-16934.39999999705, -13171.19999999783, 4705.0), 1688904571.7624962),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-16993.799999997027, -13217.399999997819, 4721.5), 1688904572.7710052),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-17053.199999997003, -13263.599999997807, 4738.0), 1688904573.7924693),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-17108.99999999698, -13306.999999997795, 4753.5), 1688904574.811212),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-17164.799999996958, -13350.399999997784, 4769.0), 1688904575.8134887),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-17224.199999996934, -13396.599999997772, 4785.5), 1688904576.8315058),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-17281.79999999691, -13441.39999999776, 4801.5), 1688904577.8348064),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-17341.199999996887, -13487.599999997748, 4818.0), 1688904578.8365057),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-17396.999999996864, -13530.999999997737, 4833.5), 1688904579.8532286),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-17452.79999999684, -13574.399999997726, 4849.0), 1688904580.860845),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-17512.199999996817, -13620.599999997714, 4865.5), 1688904581.8629045),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-17569.799999996794, -13665.399999997702, 4881.5), 1688904582.8684464),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-17629.19999999677, -13711.59999999769, 4898.0), 1688904583.877677),
    ((-6.38378239159465e-16, 0.0, 0.20000000000000015), (-17683.19999999675, -13753.59999999768, 4913.0), 1688904584.8842542),
    ((-0.30000000000000066, 0.0, 0.20000000000000015), (-17738.999999996726, -13796.999999997668, 4928.5), 1688904585.893172),
    ((-1.0000000000000007, 0.0, 0.20000000000000015), (-17794.799999996703, -13840.399999997657, 4944.0), 1688904586.8976462),
    ((-1.7000000000000013, 0.0, 0.20000000000000015), (-17852.39999999668, -13885.199999997645, 4960.0), 1688904587.9033194),
    ((-2.3000000000000016, 0.0, 0.20000000000000015), (-17906.399999996658, -13927.199999997634, 4975.0), 1688904588.9055653),
    ((-3.000000000000002, 0.0, 0.20000000000000015), (-17962.199999996636, -13970.599999997623, 4990.5), 1688904589.9096673),
    ((-3.700000000000003, 0.0, 0.20000000000000015), (-18016.199999996614, -14012.599999997612, 5005.5), 1688904590.9256117),
    ((-4.300000000000002, 0.0, 0.20000000000000015), (-18071.99999999659, -14055.9999999976, 5021.0), 1688904591.933134),
    ((-4.999999999999999, 0.0, 0.20000000000000015), (-18127.79999999657, -14099.39999999759, 5036.5), 1688904592.9424896),
    ((-5.699999999999997, 0.0, 0.20000000000000015), (-18185.399999996545, -14144.199999997578, 5052.5), 1688904593.9548247),
    ((-6.2999999999999945, 0.0, 0.20000000000000015), (-18237.599999996524, -14184.799999997567, 5067.0), 1688904594.957105),
    ((-6.999999999999992, 0.0, 0.20000000000000015), (-18291.599999996502, -14226.799999997556, 5082.0), 1688904595.9623291),
]

object3_movement_list = [
    ((0.0, 0.0, -6.299999999999994), (-3722.400000000133, -2895.20000000011, 1035.0), 1688903994.4693854),
    ((0.0, 0.0, -5.799999999999995), (-3774.600000000138, -2935.8000000001125, 1049.5), 1688903995.472727),
    ((0.0, 0.0, -5.4999999999999964), (-3830.400000000144, -2979.2000000001153, 1065.0), 1688903996.4815633),
    ((0.0, 0.0, -5.4999999999999964), (-3875.4000000001483, -3014.2000000001176, 1077.5), 1688903997.2792728),
    ((0.0, 0.0, -5.4999999999999964), (-3886.2000000001494, -3022.600000000118, 1080.5), 1688903997.4848268),
    ((0.0, 0.0, -4.999999999999998), (-3931.200000000154, -3057.6000000001204, 1093.0), 1688903998.2833552),
    ((0.0, 0.0, -4.899999999999999), (-3942.000000000155, -3066.000000000121, 1096.0), 1688903998.4918454),
    ((0.0, 0.0, -4.4), (-3987.0000000001596, -3101.0000000001232, 1108.5), 1688903999.285058),
    ((0.0, 0.0, -4.200000000000001), (-3997.8000000001607, -3109.400000000124, 1111.5), 1688903999.4949796),
    ((0.0, 0.0, -3.7000000000000015), (-4041.000000000165, -3143.000000000126, 1123.5), 1688904000.3022282),
    ((0.0, 0.0, -3.5000000000000013), (-4051.800000000166, -3151.4000000001265, 1126.5), 1688904000.5017066),
    ((0.0, 0.0, -3.000000000000001), (-4096.80000000017, -3186.400000000129, 1139.0), 1688904001.3124309),
    ((0.0, 0.0, -2.900000000000001), (-4107.600000000171, -3194.8000000001293, 1142.0), 1688904001.5046937),
    ((0.0, 0.0, -2.3000000000000003), (-4154.400000000176, -3231.2000000001317, 1155.0), 1688904002.3163571),
    ((0.0, 0.0, -2.2), (-4165.200000000177, -3239.6000000001322, 1158.0), 1688904002.5122967),
    ((0.0, 0.0, -1.6999999999999997), (-4212.000000000182, -3276.0000000001346, 1171.0), 1688904003.3218293),
    ((0.0, 0.0, -1.4999999999999996), (-4222.800000000183, -3284.400000000135, 1174.0), 1688904003.5163167),
    ((0.0, 0.0, -0.9999999999999992), (-4267.8000000001875, -3319.4000000001374, 1186.5), 1688904004.3346689),
    ((0.0, 0.0, -0.8999999999999992), (-4278.600000000189, -3327.800000000138, 1189.5), 1688904004.5300426),
    ((0.0, 0.0, -0.2999999999999994), (-4321.800000000193, -3361.40000000014, 1201.5), 1688904005.3414593),
    ((0.0, 0.0, -0.19999999999999937), (-4332.600000000194, -3369.8000000001407, 1204.5), 1688904005.5327058),
    ((0.0, 0.0, 0.30000000000000066), (-4379.400000000199, -3406.200000000143, 1217.5), 1688904006.3460207),
    ((0.0, 0.0, 0.5000000000000007), (-4388.4000000002, -3413.2000000001435, 1220.0), 1688904006.538269),
    ((0.0, 0.0, 1.0000000000000007), (-4435.200000000204, -3449.600000000146, 1233.0), 1688904007.346749),
    ((0.0, 0.0, 1.1000000000000008), (-4446.000000000206, -3458.0000000001464, 1236.0), 1688904007.542485),
    ((0.0, 0.0, 1.2000000000000008), (-4494.6000000002105, -3495.800000000149, 1249.5), 1688904008.351478),
    ((0.0, 0.0, 1.2000000000000008), (-4505.400000000212, -3504.2000000001494, 1252.5), 1688904008.5439885),
    ((0.0, 0.0, 1.2000000000000008), (-4552.200000000216, -3540.600000000152, 1265.5), 1688904009.3525128),
    ((0.0, 0.0, 1.2000000000000008), (-4563.000000000217, -3549.0000000001523, 1268.5), 1688904009.546024),
    ((0.0, 0.0, 1.2000000000000008), (-4608.000000000222, -3584.0000000001546, 1281.0), 1688904010.3568077),
    ((0.0, 0.0, 1.2000000000000008), (-4618.800000000223, -3592.400000000155, 1284.0), 1688904010.559106),
    ((0.0, 0.0, 1.2000000000000008), (-4667.400000000228, -3630.2000000001576, 1297.5), 1688904011.372332),
    ((0.0, 0.0, 1.2000000000000008), (-4678.200000000229, -3638.600000000158, 1300.5), 1688904011.5626469),
    ((0.0, 0.0, 1.2000000000000008), (-4726.800000000234, -3676.4000000001606, 1314.0), 1688904012.378768),
    ((0.0, 0.0, 1.2000000000000008), (-4737.600000000235, -3684.800000000161, 1317.0), 1688904012.5700936),
    ((0.0, 0.0, 1.2000000000000008), (-4786.20000000024, -3722.6000000001636, 1330.5), 1688904013.3799977),
    ((0.0, 0.0, 1.2000000000000008), (-4798.800000000241, -3732.4000000001643, 1334.0), 1688904013.5731826),
    ((0.0, 0.0, 1.2000000000000008), (-4843.800000000246, -3767.4000000001665, 1346.5), 1688904014.382522),
    ((0.0, 0.0, 1.2000000000000008), (-4854.600000000247, -3775.800000000167, 1349.5), 1688904014.5782974),
    ((0.0, 0.0, 1.2000000000000008), (-4899.600000000251, -3810.8000000001693, 1362.0), 1688904015.389322),
    ((0.0, 0.0, 1.2000000000000008), (-4910.4000000002525, -3819.20000000017, 1365.0), 1688904015.5831292),
    ((0.0, 0.0, 1.2000000000000008), (-4959.000000000257, -3857.0000000001723, 1378.5), 1688904016.3903751),
    ((0.0, 0.0, 1.2000000000000008), (-4969.8000000002585, -3865.400000000173, 1381.5), 1688904016.5900896),
    ((0.0, 0.0, 1.2000000000000008), (-5016.600000000263, -3901.8000000001753, 1394.5), 1688904017.3924477),
    ((0.0, 0.0, 1.2000000000000008), (-5027.400000000264, -3910.200000000176, 1397.5), 1688904017.593769),
    ((0.0, 0.0, 1.2000000000000008), (-5076.000000000269, -3948.0000000001783, 1411.0), 1688904018.4021647),
    ((0.0, 0.0, 1.2000000000000008), (-5086.80000000027, -3956.400000000179, 1414.0), 1688904018.5961099),
    ((0.0, 0.0, 1.2000000000000008), (-5133.600000000275, -3992.800000000181, 1427.0), 1688904019.4049118),
    ((0.0, 0.0, 1.2000000000000008), (-5144.400000000276, -4001.2000000001817, 1430.0), 1688904019.5964162),
    ((0.0, 0.0, 1.2000000000000008), (-5189.400000000281, -4036.200000000184, 1442.5), 1688904020.4094136),
    ((0.0, 0.0, 1.2000000000000008), (-5200.200000000282, -4044.6000000001845, 1445.5), 1688904020.6091828),
    ((0.0, 0.0, 1.2000000000000008), (-5248.800000000287, -4082.400000000187, 1459.0), 1688904021.4191055),
    ((0.0, 0.0, 1.2000000000000008), (-5261.400000000288, -4092.2000000001876, 1462.5), 1688904021.6159399),
    ((0.0, 0.0, 1.2000000000000008), (-5308.200000000293, -4128.6000000001795, 1475.5), 1688904022.4214919),
    ((0.0, 0.0, 1.2000000000000008), (-5320.800000000294, -4138.400000000177, 1479.0), 1688904022.6184435),
    ((0.0, 0.0, 1.2000000000000008), (-5367.600000000299, -4174.8000000001675, 1492.0), 1688904023.434046),
    ((0.0, 0.0, 1.2000000000000008), (-5380.2000000003, -4184.600000000165, 1495.5), 1688904023.6213593),
    ((0.0, 0.0, 1.2000000000000008), (-5427.000000000305, -4221.0000000001555, 1508.5), 1688904024.434106),
    ((0.0, 0.0, 1.2000000000000008), (-5437.800000000306, -4229.400000000153, 1511.5), 1688904024.636515),
    ((0.0, 0.0, 1.2000000000000008), (-5481.00000000031, -4263.000000000145, 1523.5), 1688904025.4363036),
    ((0.0, 0.0, 1.2000000000000008), (-5493.600000000311, -4272.800000000142, 1527.0), 1688904025.6511314),
    ((0.0, 0.0, 1.2000000000000008), (-5540.400000000316, -4309.200000000133, 1540.0), 1688904026.4419208),
    ((0.0, 0.0, 1.2000000000000008), (-5553.000000000317, -4319.00000000013, 1543.5), 1688904026.6578717),
    ((0.0, 0.0, 1.2000000000000008), (-5599.800000000322, -4355.400000000121, 1556.5), 1688904027.444512),
    ((0.0, 0.0, 1.2000000000000008), (-5614.200000000324, -4366.600000000118, 1560.5), 1688904027.6593556),
    ((0.0, 0.0, 1.2000000000000008), (-5661.000000000328, -4403.000000000108, 1573.5), 1688904028.4493265),
    ((0.0, 0.0, 1.2000000000000008), (-5673.60000000033, -4412.800000000106, 1577.0), 1688904028.662363),
    ((0.0, 0.0, 1.2000000000000008), (-5718.600000000334, -4447.800000000097, 1589.5), 1688904029.452918),
    ((0.0, 0.0, 1.2000000000000008), (-5731.200000000335, -4457.600000000094, 1593.0), 1688904029.6658742),
    ((0.0, 0.0, 1.2000000000000008), (-5774.40000000034, -4491.200000000085, 1605.0), 1688904030.4659305),
    ((0.0, 0.0, 1.2000000000000008), (-5787.000000000341, -4501.000000000083, 1608.5), 1688904030.6802657),
    ((0.0, 0.0, 1.2000000000000008), (-5833.800000000346, -4537.400000000073, 1621.5), 1688904031.4696748),
    ((0.0, 0.0, 1.2000000000000008), (-5846.400000000347, -4547.200000000071, 1625.0), 1688904031.6825173),
    ((0.0, 0.0, 1.2000000000000008), (-5893.200000000352, -4583.600000000061, 1638.0), 1688904032.4735627),
    ((0.0, 0.0, 1.2000000000000008), (-5905.800000000353, -4593.400000000059, 1641.5), 1688904032.6936188),
    ((0.0, 0.0, 1.500000000000001), (-5950.800000000358, -4628.40000000005, 1654.0), 1688904033.4803252),
    ((0.0, 0.0, 1.7000000000000013), (-5963.400000000359, -4638.200000000047, 1657.5), 1688904033.694343),
    ((0.0, 0.0, 2.2000000000000015), (-6006.600000000363, -4671.800000000038, 1669.5), 1688904034.4825556),
    ((0.0, 0.0, 2.4000000000000017), (-6019.2000000003645, -4681.600000000036, 1673.0), 1688904034.6977682),
    ((0.0, 0.0, 2.900000000000002), (-6060.600000000369, -4713.8000000000275, 1684.5), 1688904035.4862642),
    ((0.0, 0.0, 3.000000000000002), (-6073.20000000037, -4723.600000000025, 1688.0), 1688904035.706386),
    ((0.0, 0.0, 3.5000000000000027), (-6116.400000000374, -4757.200000000016, 1700.0), 1688904036.492192),
    ((0.0, 0.0, 3.700000000000003), (-6129.000000000376, -4767.000000000014, 1703.5), 1688904036.7094078),
    ((0.0, 0.0, 4.200000000000002), (-6174.00000000038, -4802.000000000005, 1716.0), 1688904037.4936829),
    ((0.0, 0.0, 4.400000000000001), (-6186.600000000381, -4811.800000000002, 1719.5), 1688904037.7125564),
    ((0.0, 0.0, 4.8999999999999995), (-6231.600000000386, -4846.799999999993, 1732.0), 1688904038.4957829),
    ((0.0, 0.0, 4.999999999999999), (-6244.200000000387, -4856.59999999999, 1735.5), 1688904038.7223008),
]

object2_movement_list = [
    ((0.0, 0.0, 5.099999999999999), (-460.80000000000194, -358.39999999999907, 128.0), 1690228977.9389226),
    ((0.0, 0.0, 5.099999999999999), (-514.8000000000022, -400.3999999999984, 143.0), 1690228978.940324),
    ((0.0, 0.0, 4.500000000000001), (-568.8000000000009, -442.3999999999977, 158.0), 1690228979.9409933),
    ((0.0, 0.0, 3.9000000000000026), (-622.7999999999995, -484.399999999997, 173.0), 1690228980.9419394),
    ((0.0, 0.0, 3.200000000000002), (-676.7999999999981, -526.3999999999963, 188.0), 1690228981.9450877),
    ((0.0, 0.0, 2.5000000000000013), (-730.7999999999968, -568.3999999999957, 203.0), 1690228982.9490745),
    ((0.0, 0.0, 1.9000000000000008), (-784.7999999999954, -610.399999999995, 218.0), 1690228983.949502),
    ((0.0, 0.0, 1.2000000000000002), (-838.799999999994, -652.3999999999943, 233.0), 1690228984.950623),
    ((0.0, 0.0, 0.7000000000000001), (-892.7999999999927, -694.3999999999936, 248.0), 1690228985.9533966),
    ((0.0, 0.0, 0.7000000000000001), (-946.7999999999913, -736.3999999999929, 263.0), 1690228986.9604652),
    ((0.0, 0.0, 0.7000000000000001), (-1000.79999999999, -778.3999999999922, 278.0), 1690228987.9663749),
    ((0.0, 0.0, 0.7000000000000001), (-1054.7999999999886, -820.3999999999916, 293.0), 1690228988.9726684),
    ((0.0, 0.0, 0.7000000000000001), (-1108.7999999999872, -862.3999999999909, 308.0), 1690228989.9790552),
    ((0.0, 0.0, 0.7000000000000001), (-1162.7999999999859, -904.3999999999902, 323.0), 1690228990.9845665),
    ((0.0, 0.0, 0.7000000000000001), (-1216.7999999999845, -946.3999999999895, 338.0), 1690228991.9916375),
    ((0.0, 0.0, 0.7000000000000001), (-1270.7999999999831, -988.3999999999888, 353.0), 1690228993.0004358),
    ((0.0, 0.0, 0.7000000000000001), (-1324.7999999999818, -1030.3999999999887, 368.0), 1690228994.009703),
    ((0.0, 0.0, 0.7000000000000001), (-1378.7999999999804, -1072.3999999999915, 383.0), 1690228995.011395),
    ((0.0, 0.0, 0.7000000000000001), (-1432.799999999979, -1114.3999999999942, 398.0), 1690228996.0159674),
    ((0.0, 0.0, 0.7000000000000001), (-1486.7999999999777, -1156.399999999997, 413.0), 1690228997.0186548),
    ((0.0, 0.0, 0.7000000000000001), (-1540.7999999999763, -1198.3999999999996, 428.0), 1690228998.020996),
    ((0.0, 0.0, 0.7000000000000001), (-1594.799999999975, -1240.4000000000024, 443.0), 1690228999.0281157),
    ((0.0, 0.0, 0.7000000000000001), (-1648.7999999999736, -1282.400000000005, 458.0), 1690229000.0315866),
    ((0.0, 0.0, 0.7000000000000001), (-1702.7999999999722, -1324.4000000000078, 473.0), 1690229001.0389314),
    ((0.0, 0.0, 0.7000000000000001), (-1756.7999999999709, -1366.4000000000106, 488.0), 1690229002.0500274),
    ((0.0, 0.0, 0.7000000000000001), (-1810.7999999999695, -1408.4000000000133, 503.0), 1690229003.0530827),
    ((0.0, 0.0, 0.7000000000000001), (-1864.7999999999681, -1450.400000000016, 518.0), 1690229004.0593784),
    ((0.0, 0.0, 0.7000000000000001), (-1918.7999999999668, -1492.4000000000187, 533.0), 1690229005.0673344),
    ((0.4, 0.0, 0.7000000000000001), (-1972.7999999999654, -1534.4000000000215, 548.0), 1690229006.0723968),
    ((1.0999999999999999, 0.0, 0.7000000000000001), (-2026.799999999964, -1576.4000000000242, 563.0), 1690229007.0792608),
    ((1.7000000000000004, 0.0, 0.7000000000000001), (-2080.799999999967, -1618.400000000027, 578.0), 1690229008.0875125),
    ((2.400000000000001, 0.0, 0.7000000000000001), (-2134.7999999999724, -1660.4000000000296, 593.0), 1690229009.0953603),
    ((3.1000000000000014, 0.0, 0.7000000000000001), (-2188.799999999978, -1702.4000000000324, 608.0), 1690229010.1004677),
    ((3.700000000000002, 0.0, 0.7000000000000001), (-2242.7999999999834, -1744.400000000035, 623.0), 1690229011.100609),
    ((4.4, 0.0, 0.7000000000000001), (-2296.799999999989, -1786.4000000000378, 638.0), 1690229012.107117),
    ((5.099999999999998, 0.0, 0.7000000000000001), (-2350.7999999999943, -1828.4000000000406, 653.0), 1690229013.1159055),
    ((5.699999999999996, 0.0, 0.7000000000000001), (-2404.7999999999997, -1870.4000000000433, 668.0), 1690229014.1213117),
    ((6.399999999999993, 0.0, 0.7000000000000001), (-2458.800000000005, -1912.400000000046, 683.0), 1690229015.1232603),
    ((6.999999999999991, 0.0, 0.7000000000000001), (-2512.8000000000106, -1954.4000000000487, 698.0), 1690229016.1306064),
]

object1_movement_list = [
    ((-7.600000000000000, 0.0, 1.0), (-46898.80000001722, -37662.400000019734, 13537.5), 1688902965.750000),
    ((-7.600000000000000, 0.0, 1.0), (-46898.80000001722, -37662.400000019734, 13537.5), 1688902966.360000),
    ((-7.600000000000000, 0.0, 1.0), (-46898.80000001722, -37662.400000019734, 13537.5), 1688902966.360000),
    ((-7.600000000000000, 0.0, 1.0), (-46898.80000001722, -37662.400000019734, 13537.5), 1688902966.360000),
    ((-7.600000000000000, 0.0, 1.0), (-46898.80000001722, -37662.400000019734, 13537.5), 1688902966.370000),
    ((-7.600000000000000, 0.0, 1.0), (-46898.80000001722, -37662.400000019734, 13537.5), 1688902966.370000),
    ((-7.600000000000000, 0.0, 1.0), (-46898.80000001722, -37662.400000019734, 13537.5), 1688902966.380000),
    ((-7.600000000000000, 0.0, 1.0), (-46898.80000001722, -37662.400000019734, 13537.5), 1688902966.390000),
    ((-7.600000000000000, 0.0, 1.0), (-46898.80000001722, -37662.400000019734, 13537.5), 1688902966.396000),
    ((-7.600000000000000, 0.0, 1.0), (-46898.80000001722, -37662.400000019734, 13537.5), 1688902966.400000),
    ((-7.600000000000000, 0.0, 1.0), (-46898.80000001722, -37662.400000019734, 13537.5), 1688902966.415942),
    ((-7.500000000000000, 0.0, 1.0), (-46898.80000001722, -37662.400000019734, 13537.5), 1688902966.179242),
    ((-6.900000000000000, 0.0, 1.0), (-48798.80000001722, -37902.400000019734, 13620.5), 1688902967.179242),
    ((-6.600009999999995, 0.0, 1.0), (-49000.80000001722, -38102.400000019734, 13647.5), 1688902968.179242),
    ((-5.999999999999995, 0.0, 1.0), (-49198.80000001722, -38262.400000019734, 13707.5), 1688902969.179242),
    ((-5.699999999999996, 0.0, 1.0), (-49256.40000001731, -38307.20000001978, 13723.5), 1688902970.1816227),
    ((-5.099999999999998, 0.0, 1.0), (-49312.2000000174, -38350.600000019826, 13739.0), 1688902971.1851056),
    ((-4.4, 0.0, 1.0), (-49368.00000001749, -38394.00000001987, 13754.5), 1688902972.1882455),
    ((-3.7000000000000015, 0.0, 1.0), (-49425.600000017585, -38438.80000001992, 13770.5), 1688902973.1929698),
    ((-3.100000000000001, 0.0, 1.0), (-49481.400000017675, -38482.20000001996, 13786.0), 1688902974.2054105),
    ((-2.4000000000000004, 0.0, 1.0), (-49537.200000017765, -38525.60000002001, 13801.5), 1688902975.208148),
    ((-1.6999999999999997, 0.0, 1.0), (-49593.000000017855, -38569.00000002005, 13817.0), 1688902976.2179542),
    ((-1.0999999999999992, 0.0, 1.0), (-49648.800000017945, -38612.4000000201, 13832.5), 1688902977.2217374),
    ((-0.39999999999999936, 0.0, 1.0), (-49706.40000001804, -38657.200000020144, 13848.5), 1688902978.2230616),
    ((6.38378239159465e-16, 0.0, 1.0), (-49762.20000001813, -38700.60000002019, 13864.0), 1688902979.2334578),
    ((6.38378239159465e-16, 0.0, 1.0), (-49819.80000001822, -38745.400000020236, 13880.0), 1688902980.242666),
    ((6.38378239159465e-16, 0.0, 1.0), (-49877.400000018315, -38790.20000002028, 13896.0), 1688902981.2624362),
    ((6.38378239159465e-16, 0.0, 1.0), (-49936.80000001841, -38836.40000002033, 13912.5), 1688902982.2636917),
    ((6.38378239159465e-16, 0.0, 1.0), (-49996.20000001851, -38882.60000002038, 13929.0), 1688902983.266361),
    ((6.38378239159465e-16, 0.0, 1.0), (-50055.6000000186, -38928.80000002043, 13945.5), 1688902984.2750268),
    ((6.38378239159465e-16, 0.0, 1.0), (-50111.40000001869, -38972.20000002047, 13961.0), 1688902985.277627),
    ((6.38378239159465e-16, 0.0, 1.0), (-50170.80000001879, -39018.40000002052, 13977.5), 1688902986.2861032),
    ((6.38378239159465e-16, 0.0, 1.0), (-50232.00000001889, -39066.00000002057, 13994.5), 1688902987.3054488),
    ((6.38378239159465e-16, 0.0, 1.0), (-50291.400000018984, -39112.20000002062, 14011.0), 1688902988.3122926),
    ((6.38378239159465e-16, 0.0, 1.0), (-50350.80000001908, -39158.400000020665, 14027.5), 1688902989.314246),
    ((6.38378239159465e-16, 0.0, 1.0), (-50406.60000001917, -39201.80000002071, 14043.0), 1688902990.325202),
    ((6.38378239159465e-16, 0.0, 1.0), (-50466.00000001927, -39248.00000002076, 14059.5), 1688902991.3274267),
    ((6.38378239159465e-16, 0.0, 1.0), (-50525.40000001936, -39294.200000020806, 14076.0), 1688902992.3369172),
    ((6.38378239159465e-16, 0.0, 1.0), (-50584.80000001946, -39340.400000020854, 14092.5), 1688902993.341539),
    ((6.38378239159465e-16, 0.0, 1.0), (-50642.40000001955, -39385.2000000209, 14108.5), 1688902994.3487515),
    ((6.38378239159465e-16, 0.0, 1.0), (-50698.20000001964, -39428.600000020946, 14124.0), 1688902995.365075),
    ((6.38378239159465e-16, 0.0, 1.0), (-50757.60000001974, -39474.800000020994, 14140.5), 1688902996.3700879),
    ((6.38378239159465e-16, 0.0, 1.0), (-50817.000000019834, -39521.00000002104, 14157.0), 1688902997.3747725),
    ((6.38378239159465e-16, 0.0, 1.0), (-50876.40000001993, -39567.20000002109, 14173.5), 1688902998.3897407),
    ((6.38378239159465e-16, 0.0, 1.0), (-50935.800000020026, -39613.40000002114, 14190.0), 1688902999.3912354),
    ((6.38378239159465e-16, 0.0, 1.0), (-50991.60000002012, -39656.80000002118, 14205.5), 1688903000.3961618),
    ((6.38378239159465e-16, 0.0, 1.0), (-51051.00000002021, -39703.00000002123, 14222.0), 1688903001.4150276),
    ((6.38378239159465e-16, 0.0, 1.6000000000000005), (-51110.40000002031, -39749.20000002128, 14238.5), 1688903002.4159715),
    ((6.38378239159465e-16, 0.0, 2.300000000000001), (-51168.0000000204, -39794.000000021326, 14254.5), 1688903003.4360282),
    ((6.38378239159465e-16, 0.0, 2.9000000000000017), (-51223.80000002049, -39837.40000002137, 14270.0), 1688903004.4435315),
    ((6.38378239159465e-16, 0.0, 3.6000000000000023), (-51277.80000002058, -39879.400000021415, 14285.0), 1688903005.450447),
    ((6.38378239159465e-16, 0.0, 4.300000000000002), (-51333.60000002067, -39922.80000002146, 14300.5), 1688903006.452908),
]

font_metrics = generatre_font_metrics(num_chars_x, font_char_w, font_char_h)
font_atlas_texture_id = font_atlas_texture_buffer(font_atlas, font_atlas_w, font_atlas_h)
bg1_vbo, bg2_vbo, bg3_vbo, bg4_vbo, bg5_vbo, bg1_stride, bg2_stride, bg3_stride, bg4_stride, bg5_stride,\
bg1_verts_itemsize, bg2_verts_itemsize, bg3_verts_itemsize, bg4_verts_itemsize, bg5_verts_itemsize = backgrounds_buffers()

clock = pg.time.Clock()

balls_timer_duration = 255
balls_start_time = time()

MEGA = True
while MEGA:
    clock.tick(30)
    pg.display.set_caption(str(int(clock.get_fps())))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                print(f"Something Wonderful Has Happened!")
                pg.quit()
                sys.exit()
            elif event.key == pg.K_RETURN:
                MEGA = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    if fx1_triggered or fx2_triggered or fx3_triggered:

        glDisable(GL_DEPTH_TEST)
        glPushMatrix()
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -8.0)
        glBindBuffer(GL_ARRAY_BUFFER, bg1_vbo)
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)
        glVertexPointer(2, GL_FLOAT, bg1_stride, None)
        glColorPointer(4, GL_FLOAT, bg1_stride, c_void_p(2 * bg1_verts_itemsize))
        glDrawArrays(GL_QUADS, 0, 4)
        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_COLOR_ARRAY)
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glPopMatrix()
        glEnable(GL_DEPTH_TEST)

    if object1_movement_list:

        if time_offset1:
            time_offset = object1_movement_list[0][2] - time()
            time_offset1 = False

        position_x, position_y, position_z, rotation_x, rotation_y, rotation_z,\
        rotation_angle_x, rotation_angle_y, rotation_angle_z, object1_movement_list, current_time = object_update_movement(
            object1_movement_list,
            rotation_angle_x,
            rotation_angle_y,
            rotation_angle_z,
            time_offset
        )

        rotation_angle_x += 2.0
        rotation_angle_y += 1.0
        rotation_angle_z += 1.0

        if fx1_triggered:
            verts = []
            colors = []
            indices = []
            normals = []
            verts_nbytes = []
            colors_nbytes = []
            indices_size = []
            verts, colors, indices, verts_nbytes, colors_nbytes, indices_size = create_dmghedron(subdivide_level=sub_level1, depth=fx1_depth, subdivisions=sub_div1)
            normals = calculate_normals(verts, indices)
            dmghedron_verts_vbo, dmghedron_indices_vbo = dmghedron_buffers(verts, indices, colors, normals)
            fx1_triggered = False
            fx_blend = fx1_blend

        else:
            if fx_blend:
                glEnable(GL_BLEND)
            glPushMatrix()
            enable_fog((0.0, 0.0, 0.0, 0.8), GL_LINEAR, 7.0, 8.8, GL_NICEST)
            glTranslatef(position_x, position_y, position_z)
            glRotatef(rotation_angle_x, rotation_x, 0.0, 0.0)
            glRotatef(rotation_angle_y, 0.0, rotation_y, 0.0)
            glRotatef(rotation_angle_z, 0.0, 0.0, rotation_z)
            draw_dmghedron(dmghedron_verts_vbo, dmghedron_indices_vbo, verts_nbytes, colors_nbytes, indices_size, draw_type=fx1_draw_type)
            glDisable(GL_FOG)
            glPopMatrix()
            if fx_blend:
                glDisable(GL_BLEND)

    if object2_movement_list and not object1_movement_list:

        if time_offset2:
            time_offset = object2_movement_list[0][2] - time()
            time_offset2 = False

        position_x, position_y, position_z, rotation_x, rotation_y, rotation_z,\
        rotation_angle_x, rotation_angle_y, rotation_angle_z, object2_movement_list, current_time = object_update_movement(
            object2_movement_list,
            rotation_angle_x,
            rotation_angle_y,
            rotation_angle_z,
            time_offset
        )

        rotation_angle_x += 2.0
        rotation_angle_y += 1.0

        if fx2_triggered:
            verts = []
            colors = []
            indices = []
            normals = []
            verts_nbytes = []
            colors_nbytes = []
            indices_size = []
            verts, colors, indices, verts_nbytes, colors_nbytes, indices_size = create_dmghedron(subdivide_level=sub_level2, depth=fx2_depth, subdivisions=sub_div2)
            normals = calculate_normals(verts, indices)
            dmghedron_verts_vbo, dmghedron_indices_vbo = dmghedron_buffers(verts, indices, colors, normals)
            fx2_triggered = False
            fx_blend = fx2_blend
        else:

            glDisable(GL_DEPTH_TEST)
            glPushMatrix()
            glLoadIdentity()
            glTranslatef(0.0, 0.0, -8.0)
            glBindBuffer(GL_ARRAY_BUFFER, bg3_vbo)
            glEnableClientState(GL_VERTEX_ARRAY)
            glEnableClientState(GL_COLOR_ARRAY)
            glVertexPointer(2, GL_FLOAT, bg3_stride, None)
            glColorPointer(4, GL_FLOAT, bg3_stride, c_void_p(2 * bg3_verts_itemsize))
            glDrawArrays(GL_QUADS, 0, 4)
            glDisableClientState(GL_VERTEX_ARRAY)
            glDisableClientState(GL_COLOR_ARRAY)
            glBindBuffer(GL_ARRAY_BUFFER, 0)
            glPopMatrix()
            glEnable(GL_DEPTH_TEST)

            if fx_blend:
                glEnable(GL_BLEND)
            glPushMatrix()
            enable_fog((0.0, 0.0, 0.0, 0.8), GL_LINEAR, 7.0, 8.8, GL_NICEST)
            glTranslatef(position_x, position_y, position_z)
            glRotatef(rotation_angle_x, rotation_x, 0.0, 0.0)
            glRotatef(rotation_angle_y, 0.0, rotation_y, 0.0)
            glRotatef(rotation_angle_z, 0.0, 0.0, rotation_z)
            draw_dmghedron(dmghedron_verts_vbo, dmghedron_indices_vbo, verts_nbytes, colors_nbytes, indices_size, draw_type=fx2_draw_type)
            glDisable(GL_FOG)
            glPopMatrix()
            if fx_blend:
                glDisable(GL_BLEND)

    if object3_movement_list and not object1_movement_list and not object2_movement_list:

        if time_offset3:
            time_offset = object3_movement_list[0][2] - time()
            time_offset3 = False

        position_x, position_y, position_z, rotation_x, rotation_y, rotation_z,\
        rotation_angle_x, rotation_angle_y, rotation_angle_z, object3_movement_list, current_time = object_update_movement(
            object3_movement_list,
            rotation_angle_x,
            rotation_angle_y,
            rotation_angle_z,
            time_offset
        )

        rotation_angle_x += 2.0
        rotation_angle_y += 1.0
        rotation_angle_z += 1.0

        if fx3_triggered:
            verts = []
            colors = []
            indices = []
            normals = []
            verts_nbytes = []
            colors_nbytes = []
            indices_size = []
            verts, colors, indices, verts_nbytes, colors_nbytes, indices_size = create_dmghedron(subdivide_level=sub_level3, depth=fx3_depth, subdivisions=sub_div3)
            normals = calculate_normals(verts, indices)
            dmghedron_verts_vbo, dmghedron_indices_vbo = dmghedron_buffers(verts, indices, colors, normals)
            fx3_triggered = False
            fx_blend = fx3_blend
        else:
            glDisable(GL_DEPTH_TEST)
            glPushMatrix()
            glLoadIdentity()
            glTranslatef(0.0, 0.0, -8.0)
            glBindBuffer(GL_ARRAY_BUFFER, bg4_vbo)
            glEnableClientState(GL_VERTEX_ARRAY)
            glEnableClientState(GL_COLOR_ARRAY)
            glVertexPointer(2, GL_FLOAT, bg4_stride, None)
            glColorPointer(4, GL_FLOAT, bg4_stride, c_void_p(2 * bg4_verts_itemsize))
            glDrawArrays(GL_QUADS, 0, 4)
            glDisableClientState(GL_VERTEX_ARRAY)
            glDisableClientState(GL_COLOR_ARRAY)
            glBindBuffer(GL_ARRAY_BUFFER, 0)
            glPopMatrix()
            glEnable(GL_DEPTH_TEST)
            if fx_blend:
                glEnable(GL_BLEND)
            glPushMatrix()
            enable_fog((0.0, 0.0, 0.0, 0.8), GL_LINEAR, 7.0, 8.8, GL_NICEST)
            glTranslatef(position_x, position_y, position_z)
            glRotatef(rotation_angle_x, rotation_x, 0.0, 0.0)
            glRotatef(rotation_angle_y, 0.0, rotation_y, 0.0)
            glRotatef(rotation_angle_z, 0.0, 0.0, rotation_z)
            draw_dmghedron(dmghedron_verts_vbo, dmghedron_indices_vbo, verts_nbytes, colors_nbytes, indices_size, draw_type=fx3_draw_type)
            glDisable(GL_FOG)
            glPopMatrix()
            if fx_blend:
                glDisable(GL_BLEND)

    if object4_movement_list and not object1_movement_list and not object2_movement_list and not object3_movement_list:

        if time_offset4:
            time_offset = object4_movement_list[0][2] - time()
            time_offset4 = False

        position_x, position_y, position_z, rotation_x, rotation_y, rotation_z,\
        rotation_angle_x, rotation_angle_y, rotation_angle_z, object4_movement_list, current_time = object_update_movement(
            object4_movement_list,
            rotation_angle_x,
            rotation_angle_y,
            rotation_angle_z,
            time_offset
        )

        rotation_angle_x -= 0.8
        rotation_angle_y -= 1.2
        rotation_angle_z -= 0.8

        if fx4_triggered:
            verts = []
            colors = []
            indices = []
            normals = []
            verts_nbytes = []
            colors_nbytes = []
            indices_size = []
            verts, colors, indices, verts_nbytes, colors_nbytes, indices_size = create_dmghedron(subdivide_level=sub_level4, depth=fx4_depth, subdivisions=sub_div4)
            normals = calculate_normals(verts, indices)
            dmghedron_verts_vbo, dmghedron_indices_vbo = dmghedron_buffers(verts, indices, colors, normals)
            fx4_triggered = False
            fx_blend = fx4_blend
        else:
            glDisable(GL_DEPTH_TEST)
            glPushMatrix()
            glLoadIdentity()
            glTranslatef(0.0, 0.0, -8.0)
            glBindBuffer(GL_ARRAY_BUFFER, bg5_vbo)
            glEnableClientState(GL_VERTEX_ARRAY)
            glEnableClientState(GL_COLOR_ARRAY)
            glVertexPointer(2, GL_FLOAT, bg5_stride, None)
            glColorPointer(4, GL_FLOAT, bg5_stride, c_void_p(2 * bg5_verts_itemsize))
            glDrawArrays(GL_QUADS, 0, 4)
            glDisableClientState(GL_VERTEX_ARRAY)
            glDisableClientState(GL_COLOR_ARRAY)
            glBindBuffer(GL_ARRAY_BUFFER, 0)
            glPopMatrix()
            glEnable(GL_DEPTH_TEST)
            if fx_blend:
                glEnable(GL_BLEND)
            glPushMatrix()
            enable_fog((0.0, 0.0, 0.0, 0.8), GL_LINEAR, 7.0, 8.8, GL_NICEST)
            glTranslatef(position_x, position_y, position_z)
            glRotatef(rotation_angle_x, rotation_x, 0.0, 0.0)
            glRotatef(rotation_angle_y, 0.0, rotation_y, 0.0)
            glRotatef(rotation_angle_z, 0.0, 0.0, rotation_z)
            draw_dmghedron(dmghedron_verts_vbo, dmghedron_indices_vbo, verts_nbytes, colors_nbytes, indices_size, draw_type=fx4_draw_type)
            glDisable(GL_FOG)
            glPopMatrix()
            if fx_blend:
                glDisable(GL_BLEND)

    if object5_movement_list and not object1_movement_list and not object2_movement_list and not object3_movement_list and not object4_movement_list:

        if time_offset5:
            time_offset = object5_movement_list[0][2] - time()
            time_offset5 = False

        position_x, position_y, position_z, rotation_x, rotation_y, rotation_z,\
        rotation_angle_x, rotation_angle_y, rotation_angle_z, object5_movement_list, current_time = object_update_movement(
            object5_movement_list,
            rotation_angle_x,
            rotation_angle_y,
            rotation_angle_z,
            time_offset
        )

        rotation_angle_x -= 0.7
        rotation_angle_y -= 1.2
        rotation_angle_z -= 0.7

        if fx5_triggered:
            verts = []
            colors = []
            indices = []
            normals = []
            verts_nbytes = []
            colors_nbytes = []
            indices_size = []
            verts, colors, indices, verts_nbytes, colors_nbytes, indices_size = create_dmghedron(subdivide_level=sub_level5, depth=fx5_depth, subdivisions=sub_div5)
            normals = calculate_normals(verts, indices)
            dmghedron_verts_vbo, dmghedron_indices_vbo = dmghedron_buffers(verts, indices, colors, normals)
            fx5_triggered = False
            fx_blend = fx5_blend
        else:
            glDisable(GL_DEPTH_TEST)
            glPushMatrix()
            glLoadIdentity()
            glTranslatef(0.0, 0.0, -8.0)
            glBindBuffer(GL_ARRAY_BUFFER, bg2_vbo)
            glEnableClientState(GL_VERTEX_ARRAY)
            glEnableClientState(GL_COLOR_ARRAY)
            glVertexPointer(2, GL_FLOAT, bg2_stride, None)
            glColorPointer(4, GL_FLOAT, bg2_stride, c_void_p(2 * bg2_verts_itemsize))
            glDrawArrays(GL_QUADS, 0, 4)
            glDisableClientState(GL_VERTEX_ARRAY)
            glDisableClientState(GL_COLOR_ARRAY)
            glBindBuffer(GL_ARRAY_BUFFER, 0)
            glPopMatrix()
            glEnable(GL_DEPTH_TEST)
            if fx_blend:
                glEnable(GL_BLEND)
            glPushMatrix()
            enable_fog((0.0, 0.0, 0.0, 0.8), GL_LINEAR, 7.0, 8.8, GL_NICEST)
            glTranslatef(position_x, position_y, position_z)
            glRotatef(rotation_angle_x, rotation_x, 0.0, 0.0)
            glRotatef(rotation_angle_y, 0.0, rotation_y, 0.0)
            glRotatef(rotation_angle_z, 0.0, 0.0, rotation_z)
            draw_dmghedron(dmghedron_verts_vbo, dmghedron_indices_vbo, verts_nbytes, colors_nbytes, indices_size, draw_type=fx5_draw_type)
            glDisable(GL_FOG)
            glPopMatrix()
            if fx_blend:
                glDisable(GL_BLEND)

    text_vbo, text_verts_nbytes, text_verts_size = create_verts_and_coords(scroll_text, text_pos_x, text_pos_y, font_metrics)

    glPushMatrix()
    glOrtho(0, screen_w, screen_h, 0, -1, 1)
    glColor4f(1.0, 1.0, 1.0, 1.0)
    glScalef(scroll_scale_factor, scroll_scale_factor, 1.0)
    text_draw(text_vbo, font_atlas_texture_id, text_verts_size, text_verts_nbytes)
    glPopMatrix()

    text_pos_x -= text_speed
    if text_pos_x + len(scroll_text) * (font_char_w * text_scale + character_spacing) + font_char_w * 200 < 0:
        text_pos_x = screen_w * 3 + font_char_w

    balls_elapsed_time = time() - balls_start_time

    if balls_elapsed_time >= balls_timer_duration - 12:
        pg.mixer.music.fadeout(29000)
    if balls_elapsed_time >= balls_timer_duration:
        break

    pg.display.flip()

glDeleteBuffers(1, [dmghedron_verts_vbo, dmghedron_indices_vbo, bg1_vbo, bg2_vbo, bg3_vbo, bg4_vbo, bg5_vbo])
glDeleteTextures(1, [font_atlas_texture_id])
