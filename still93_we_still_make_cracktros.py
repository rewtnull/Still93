from still93_runtime_hooker import MEGA01
MEGA1 = MEGA01()
### GLOBAL
screen_w = MEGA1.screen_w
screen_h = MEGA1.screen_h
screen = MEGA1.screen
pg = MEGA1.pg
np = MEGA1.np
os = MEGA1.os
sys = MEGA1.sys
c_void_p = MEGA1.c_void_p
c_float = MEGA1.c_float
resource_path = MEGA1.resource_path
glEnable = MEGA1.glEnable
glDisable = MEGA1.glDisable
glBlendFunc = MEGA1.glBlendFunc
glClearDepth = MEGA1.glClearDepth
glClearColor = MEGA1.glClearColor
glClear = MEGA1.glClear
glViewport = MEGA1.glViewport
glMatrixMode = MEGA1.glMatrixMode
glLoadIdentity = MEGA1.glLoadIdentity
glGenBuffers = MEGA1.glGenBuffers
glBindBuffer = MEGA1.glBindBuffer
glBufferData = MEGA1.glBufferData
glBufferSubData = MEGA1.glBufferSubData
glDeleteBuffers = MEGA1.glDeleteBuffers
glGenTextures = MEGA1.glGenTextures
glBindTexture = MEGA1.glBindTexture
glDeleteTextures = MEGA1.glDeleteTextures
glTexImage2D = MEGA1.glTexImage2D
glTexParameteri = MEGA1.glTexParameteri
glDrawArrays = MEGA1.glDrawArrays
glPushMatrix = MEGA1.glPushMatrix
glPopMatrix = MEGA1.glPopMatrix
GL_COLOR_BUFFER_BIT = MEGA1.GL_COLOR_BUFFER_BIT
GL_DEPTH_BUFFER_BIT = MEGA1.GL_DEPTH_BUFFER_BIT
GL_PROJECTION = MEGA1.GL_PROJECTION
GL_MODELVIEW = MEGA1.GL_MODELVIEW
GL_ARRAY_BUFFER = MEGA1.GL_ARRAY_BUFFER
GL_TEXTURE_2D = MEGA1.GL_TEXTURE_2D
GL_RGBA = MEGA1.GL_RGBA
GL_UNSIGNED_BYTE = MEGA1.GL_UNSIGNED_BYTE
GL_FLOAT = MEGA1.GL_FLOAT
GL_TEXTURE_MIN_FILTER = MEGA1.GL_TEXTURE_MIN_FILTER
GL_TEXTURE_MAG_FILTER = MEGA1.GL_TEXTURE_MAG_FILTER
GL_LINEAR = MEGA1.GL_LINEAR
### LOCAL
randint = MEGA1.randint
time = MEGA1.time
pi = MEGA1.pi
sin = MEGA1.sin
cos = MEGA1.cos
radians = MEGA1.radians
glDepthFunc = MEGA1.glDepthFunc
glDepthMask = MEGA1.glDepthMask
glOrtho = MEGA1.glOrtho
glTexCoordPointer = MEGA1.glTexCoordPointer
glColor4f = MEGA1.glColor4f
glVertexPointer = MEGA1.glVertexPointer
glEnableClientState = MEGA1.glEnableClientState
glDisableClientState = MEGA1.glDisableClientState
glTranslatef = MEGA1.glTranslatef
glGetAttribLocation = MEGA1.glGetAttribLocation
glEnableVertexAttribArray = MEGA1.glEnableVertexAttribArray
glDisableVertexAttribArray = MEGA1.glDisableVertexAttribArray
glVertexAttribPointer = MEGA1.glVertexAttribPointer
glUniform2f = MEGA1.glUniform2f
glColorPointer = MEGA1.glColorPointer
GL_DYNAMIC_DRAW = MEGA1.GL_DYNAMIC_DRAW
GL_TEXTURE_WRAP_S = MEGA1.GL_TEXTURE_WRAP_S
GL_TEXTURE_WRAP_T = MEGA1.GL_TEXTURE_WRAP_T
GL_CLAMP_TO_EDGE = MEGA1.GL_CLAMP_TO_EDGE
GL_FALSE = MEGA1.GL_FALSE
GL_NEAREST = MEGA1.GL_NEAREST
GL_VERTEX_ARRAY = MEGA1.GL_VERTEX_ARRAY
GL_DEPTH_TEST = MEGA1.GL_DEPTH_TEST
GL_LEQUAL = MEGA1.GL_LEQUAL
GL_TRUE = MEGA1.GL_TRUE
GL_COLOR_ARRAY = MEGA1.GL_COLOR_ARRAY
GL_SRC_ALPHA = MEGA1.GL_SRC_ALPHA
GL_ONE_MINUS_SRC_ALPHA = MEGA1.GL_ONE_MINUS_SRC_ALPHA
GL_BLEND = MEGA1.GL_BLEND
GL_QUADS = MEGA1.GL_QUADS
GL_TEXTURE_COORD_ARRAY = MEGA1.GL_TEXTURE_COORD_ARRAY
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
pg.time.wait(5000)
pg.mixer.init()
pg.mixer.music.load(resource_path('resources/skope-ending_of_some_sort.mod'))
pg.mixer.music.play(-1)

glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LEQUAL)
glDepthMask(GL_TRUE)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glClearDepth(1.0)
glClearColor(0.0, 0.0, 0.0, 1.0)
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, screen_w, screen_h, 0, -1, 1)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

def stars_init(bar_stop_pos):
    star_colors = [(5,5,5), (25,25,112), (75,75,195)]
    stars_w, stars_h = screen_w, screen_h - (bar_stop_pos * 2)
    stars_surf = pg.Surface((stars_w, stars_h), pg.SRCALPHA)
    stars = []
    for i in range(3):
        layer = []
        for stars_j in range(100):
            stars_x = randint(0, screen_w)
            stars_y = randint(0, screen_h)
            stars_size = randint(1, 5) * (i + 1)
            stars_spd = (i + 1) * 0.5
            layer.append([stars_x, stars_y, stars_size, stars_spd])
        stars.append(layer)
    return stars, stars_surf, star_colors, stars_w, stars_h

def stars_opengl_init(stars_w, stars_h, bar_stop_pos):
    glViewport(0, bar_stop_pos, stars_w, stars_h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, stars_w, 0, stars_h, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def stars_layer(stars, stars_surf, star_colors, stars_w, stars_h):
    for star_layer in stars:
        for star in star_layer:
            star[0] += star[3]
            if star[0] > stars_w:
                star[0] = 0
    stars_surf.fill(pg.Color(0,0,0,0))
    for i, star_layer in enumerate(stars):
        for star in star_layer:
            pg.draw.circle(stars_surf, star_colors[i], (int(star[0]), int(star[1])), int(star[2]))
    return stars_surf

def stars_verts_buffer(stars_w, stars_h):
    stars_verts = np.array([
        (0, 0),
        (stars_w, 0),
        (stars_w, stars_h),
        (0, stars_h)
    ], dtype=np.float32)
    stars_coords = np.array([
        (0, 0),
        (1, 0),
        (1, 1),
        (0, 1)
    ], dtype=np.float32)
    stars_vbo = glGenBuffers(1)
    stars_vbo = np.uint32(stars_vbo)

    glBindBuffer(GL_ARRAY_BUFFER, stars_vbo)
    glBufferData(GL_ARRAY_BUFFER, stars_verts.nbytes + stars_coords.nbytes, None, GL_DYNAMIC_DRAW)
    glBufferSubData(GL_ARRAY_BUFFER, 0, stars_verts.nbytes, stars_verts)
    glBufferSubData(GL_ARRAY_BUFFER, stars_verts.nbytes, stars_coords.nbytes, stars_coords)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    stars_verts_nbytes = stars_verts.nbytes
    stars_verts_size = stars_verts.size
    return stars_vbo, stars_verts_nbytes, stars_verts_size

def stars_texture_buffer(stars_w, stars_h, stars_surf):
    stars_texture_id = glGenTextures(1)
    stars_texture_id = np.uint32(stars_texture_id)
    glBindTexture(GL_TEXTURE_2D, stars_texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, stars_w, stars_h, 0, GL_RGBA, GL_UNSIGNED_BYTE, pg.image.tostring(stars_surf, 'RGBA'))
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glBindTexture(GL_TEXTURE_2D, 0)
    return stars_texture_id

def stars_draw(stars_texture_id, stars_vbo, stars_verts_nbytes, stars_verts_size):
    glDisable(GL_BLEND)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, stars_texture_id)
    glBindBuffer(GL_ARRAY_BUFFER, stars_vbo)
    glVertexPointer(2, GL_FLOAT, 0, None)
    glEnableClientState(GL_VERTEX_ARRAY)
    glTexCoordPointer(2, GL_FLOAT, 0, c_void_p(stars_verts_nbytes))
    glEnableClientState(GL_TEXTURE_COORD_ARRAY)
    glDrawArrays(GL_QUADS, 0, stars_verts_size)
    glDisableClientState(GL_TEXTURE_COORD_ARRAY)
    glDisableClientState(GL_VERTEX_ARRAY)
    glBindTexture(GL_TEXTURE_2D, 0)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glDeleteTextures(stars_texture_id)
    glDisable(GL_TEXTURE_2D)

def logo_init(logo_name):
    logo_path = resource_path(logo_name)
    logo = pg.image.load(logo_path).convert_alpha()
    logo_w, logo_h = logo.get_size()
    logo_scroll_duration = 2000
    logo_current_alpha = 0
    logo1_fade_in_duration = 8500
    logo2_fade_in_duration = 7000
    logo1_fade_out_duration = 3000
    logo2_fade_out_duration = 3000
    logo1_stay_duration = 6000
    logo2_stay_duration = 6000
    logo_scroll_speed = (screen_w + logo_w) / logo_scroll_duration
    logo1_offset_x = int((screen_w - logo_w) / 2)
    logo2_offset_x = int((screen_w - logo_w) / 2) + screen_w
    logo_elapsed_time = 0
    logo_phase = 0
    logo_transition_completed = False
    logo_fade_out_triggered = False
    logo_triggered = False
    return logo, logo_w, logo_h, logo_current_alpha, logo1_fade_in_duration,\
    logo2_fade_in_duration, logo1_fade_out_duration, logo2_fade_out_duration,\
    logo1_stay_duration, logo2_stay_duration, logo_scroll_speed, logo1_offset_x,\
    logo2_offset_x, logo_elapsed_time, logo_phase, logo_transition_completed,\
    logo_fade_out_triggered, logo_triggered

def logo_opengl_init(logo_w, logo_h):
    offset_y = int((screen_h - logo_h) / 2)
    glViewport(0, offset_y, screen_w, logo1_h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, screen_w, 0, logo1_h, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def logo_buffers(logo, logo_w, logo_h):
    logo_verts = np.array([
        (0, 0),
        (logo_w, 0),
        (logo_w, logo_h),
        (0, logo_h)
    ], dtype=np.float32)
    logo_coords = np.array([
        (0, 0),
        (1, 0),
        (1, 1),
        (0, 1)
    ], dtype=np.float32)
    logo_vbo = glGenBuffers(1)
    logo_vbo = np.uint32(logo_vbo)
    glBindBuffer(GL_ARRAY_BUFFER, logo_vbo)
    glBufferData(GL_ARRAY_BUFFER, logo_verts.nbytes + logo_coords.nbytes, None, GL_DYNAMIC_DRAW)
    glBufferSubData(GL_ARRAY_BUFFER, 0, logo_verts.nbytes, logo_verts)
    glBufferSubData(GL_ARRAY_BUFFER, logo_verts.nbytes, logo_coords.nbytes, logo_coords)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    logo_texture_id = glGenTextures(1)
    logo_texture_id = np.uint32(logo_texture_id)
    glBindTexture(GL_TEXTURE_2D, logo_texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, logo_w, logo_h, 0, GL_RGBA, GL_UNSIGNED_BYTE, pg.image.tostring(logo, "RGBA", True))
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glBindTexture(GL_TEXTURE_2D, 0)
    logo_verts_nbytes = logo_verts.nbytes
    logo_verts_size = logo_verts.size
    return logo_vbo, logo_texture_id, logo_verts_nbytes, logo_verts_size

def logo_draw(logo_current_alpha, logo_texture_id, logo_vbo, logo_verts_nbytes, logo_verts_size):
    glEnable(GL_BLEND)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, logo_texture_id)
    glBindBuffer(GL_ARRAY_BUFFER, logo_vbo)
    glVertexPointer(2, GL_FLOAT, 0, None)
    glEnableClientState(GL_VERTEX_ARRAY)
    glTexCoordPointer(2, GL_FLOAT, 0, c_void_p(logo_verts_nbytes))
    glEnableClientState(GL_TEXTURE_COORD_ARRAY)
    glColor4f(1.0, 1.0, 1.0, logo_current_alpha / 255.0)
    glDrawArrays(GL_QUADS, 0, logo_verts_size)
    glDisableClientState(GL_TEXTURE_COORD_ARRAY)
    glDisableClientState(GL_VERTEX_ARRAY)
    glBindTexture(GL_TEXTURE_2D, 0)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glDisable(GL_TEXTURE_2D)
    glDisable(GL_BLEND)
    return logo_current_alpha

def logo_phase_handling(logo_phase, logo_elapsed_time, logo_scroll_speed, logo1_fade_in_duration, logo2_fade_in_duration, logo1_current_alpha, logo2_current_alpha, logo_transition_completed, logo1_offset_x, logo2_offset_x, logo_triggered):
    if logo_phase == 0:
        if logo_elapsed_time <= logo1_fade_in_duration:
            if logo1_current_alpha < 255:
                logo1_current_alpha = int((logo_elapsed_time / logo1_fade_in_duration) * 255)
                logo2_current_alpha = int((logo_elapsed_time / logo2_fade_in_duration) * 255)
            else:
                logo1_current_alpha = 255
                logo2_current_alpha = 255
        elif logo_elapsed_time >= logo1_fade_in_duration:
            logo_phase = 1
            logo_elapsed_time = 0
            logo_triggered = True
            logo_transition_completed = False
    elif logo_phase == 1:
        logo1_offset_x = int((screen_w - logo1_w) // 2)
        if logo_elapsed_time >= logo1_stay_duration:
            if not logo_transition_completed:
                logo_phase = 2
                logo_elapsed_time = 0
                logo_transition_completed = True
    elif logo_phase == 2:
        logo1_offset_x -= logo_scroll_speed * clock.get_time()
        logo2_offset_x -= logo_scroll_speed * clock.get_time()
        if logo1_offset_x <= -logo1_w - (screen_w - logo2_w) // 2:
            logo_phase = 3
            logo_elapsed_time = 0
            logo_transition_completed = False
    elif logo_phase == 3:
        logo2_offset_x = int((screen_w - logo2_w) // 2)
        if logo_elapsed_time >= logo2_stay_duration:
            if not logo_transition_completed:
                logo_phase = 4
                logo_elapsed_time = 0
                logo_transition_completed = True
    elif logo_phase == 4:
        logo1_offset_x += logo_scroll_speed * clock.get_time()
        logo2_offset_x += logo_scroll_speed * clock.get_time()
        if logo1_offset_x >= (screen_w - logo1_w) // 2:
            logo_phase = 1
            logo_elapsed_time = 0
            logo_transition_completed = False
    return logo1_current_alpha, logo2_current_alpha, logo1_offset_x, logo2_offset_x, logo_elapsed_time, logo_phase, logo_triggered

def logo_fade_out(logo1_current_alpha, logo2_current_alpha, logo1_fade_out_duration, logo2_fade_out_duration):
        if logo1_current_alpha > 0:
            logo1_current_alpha = max(0, logo1_current_alpha - (clock.get_time() / logo1_fade_out_duration) * 255)
        else:
            logo1_current_alpha = 0
        if logo2_current_alpha > 0:
            logo2_current_alpha = max(0, logo2_current_alpha - (clock.get_time() / logo2_fade_out_duration) * 255)
        else:
            logo2_current_alpha = 0
        return logo1_current_alpha, logo2_current_alpha

scroll_text = "YOU ARE WITNESSING GENESIS... THE BRIGHTEST STAR IN THE SKY a DIVINE STYLERS a IS BORN!!!!!! IN THIS BLESSED YEAR OF 1993 TOGETHER WITH THE FUTURE CREW OF c STYLE c  WE PRESENT THIS PHAT MEGA DEMO!!!!!!! ...HOLD ON TO YOUR CATS 'CUZ HERE WE GO.........."

def scroller_init():
    scroller_char_spacing = 8
    scroller_amplitude = 130.0
    scroller_frequency = 0.01
    scroller_top_rotation_factor = 2.0
    scroller_bottom_rotation_factor = 2.0
    scroller_tweak_1 = 20.0
    scroller_tweak_2 = 20.0
    scroller_tweak_3 = 20.0
    scroller_tweak_4 = 20.0
    scroller_tweak_5 = 0.0
    scroller_tweak_6 = 0.0
    scroller_text_scale = 1.0
    scroller_text_speed = 8.0
    scroller_rainbow_speed = 0.4
    return scroller_char_spacing, scroller_amplitude, scroller_frequency, scroller_top_rotation_factor, scroller_bottom_rotation_factor,\
    scroller_tweak_1, scroller_tweak_2, scroller_tweak_3, scroller_tweak_4, scroller_tweak_5, scroller_tweak_6, scroller_text_scale,\
    scroller_text_speed, scroller_rainbow_speed

def scroller_opengl_init(screen_w, screen_h, bar_stop_pos):
    glViewport(0, 0, screen_w, screen_h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, screen_w, screen_h, 0, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def scroller_rainbow_color(speed):
    r = (sin(speed * pg.time.get_ticks() / 1000) + 1) / 2 * 255
    g = (sin(speed * pg.time.get_ticks() / 1000 + 2*pi/3) + 1) / 2 * 255
    b = (sin(speed * pg.time.get_ticks() / 1000 + 4*pi/3) + 1) / 2 * 255
    return (r, g, b)

def scroller_pulse_gradient(t, pulse_color, darkness_threshold=0.4):
    r, g, b = pulse_color
    brightness = (sin(t) + 1) / 2
    if brightness < darkness_threshold:
        brightness = darkness_threshold
    r = brightness * r
    g = brightness * g
    b = brightness * b
    return r/255, g/255, b/255

def scroller_font_metrics(num_chars_x, font_char_w, font_char_h):
    font_metrics = {}
    for char_code in range(32, 256):
        char = chr(char_code)
        row = (char_code - 32) // num_chars_x
        col = (char_code - 32) % num_chars_x
        font_metrics[char] = (col * font_char_w, row * font_char_h)
    return font_metrics

def scroller_verts_and_coords(scroll_text, text_pos_x, text_pos_y, font_metrics, scroller_amplitude, scroller_frequency, scroller_text_scale, scroller_char_spacing, scroller_tweak_1, scroller_tweak_2, scroller_tweak_3, scroller_tweak_4, scroller_tweak_5, scroller_tweak_6, font_atlas_w, font_atlas_h, font_char_w, font_char_h):
    scroller_verts = []
    scroller_coords = []
    for i, char in enumerate(scroll_text):
        font_char_x_position, font_char_y_position = font_metrics.get(char, (0, 0))
        tex_left = font_char_x_position / font_atlas_w
        tex_right = (font_char_x_position + font_char_w) / font_atlas_w
        tex_bottom = font_char_y_position / font_atlas_h
        tex_top = (font_char_y_position + font_char_h) / font_atlas_h
        char_pos_x = text_pos_x + i * (font_char_w * scroller_text_scale + scroller_char_spacing)
        char_pos_y = text_pos_y + sin(char_pos_x * scroller_frequency) * scroller_amplitude
        top_rotation_angle = cos(char_pos_x * scroller_frequency) * scroller_top_rotation_factor
        bottom_rotation_angle = sin(char_pos_x * scroller_frequency) * scroller_bottom_rotation_factor
        corners = np.array([[0, 0],
                            [font_char_w * scroller_text_scale + scroller_tweak_1, 0],
                            [font_char_w * scroller_text_scale + scroller_tweak_2, font_char_h * scroller_text_scale + scroller_tweak_3],
                            [0, font_char_h * scroller_text_scale + scroller_tweak_4]])
        center = np.array([font_char_w * scroller_text_scale + scroller_tweak_5 / 2, font_char_h * scroller_text_scale + scroller_tweak_6 / 2])
        rotated_corners = corners - center
        top_rotation_matrix = np.array([[cos(radians(top_rotation_angle)), -sin(radians(top_rotation_angle))],
                                        [sin(radians(top_rotation_angle)), cos(radians(top_rotation_angle))]])
        bottom_rotation_matrix = np.array([[cos(radians(bottom_rotation_angle)), -sin(radians(bottom_rotation_angle))],
                                           [sin(radians(bottom_rotation_angle)), cos(radians(bottom_rotation_angle))]])
        rotated_top_corners = np.dot(rotated_corners[:2], top_rotation_matrix.T)
        rotated_bottom_corners = np.dot(rotated_corners[2:], bottom_rotation_matrix.T)
        rotated_corners = np.concatenate((rotated_top_corners, rotated_bottom_corners)) + center
        scroller_verts.extend([char_pos_x + rotated_corners[0, 0], char_pos_y + rotated_corners[0, 1],
                         char_pos_x + rotated_corners[1, 0], char_pos_y + rotated_corners[1, 1],
                         char_pos_x + rotated_corners[2, 0], char_pos_y + rotated_corners[2, 1],
                         char_pos_x + rotated_corners[3, 0], char_pos_y + rotated_corners[3, 1]])
        scroller_coords.extend([tex_left, tex_bottom, tex_right, tex_bottom, tex_right, tex_top, tex_left, tex_top])
    scroller_verts = np.array(scroller_verts, dtype=np.float32)
    scroller_coords = np.array(scroller_coords, dtype=np.float32)
    scroller_vbo = glGenBuffers(1)
    scroller_vbo = np.uint32(scroller_vbo)
    glBindBuffer(GL_ARRAY_BUFFER, scroller_vbo)
    glBufferData(GL_ARRAY_BUFFER, scroller_verts.nbytes + scroller_coords.nbytes, None, GL_DYNAMIC_DRAW)
    glBufferSubData(GL_ARRAY_BUFFER, 0, scroller_verts.nbytes, scroller_verts)
    glBufferSubData(GL_ARRAY_BUFFER, scroller_verts.nbytes, scroller_coords.nbytes, scroller_coords)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    scroller_verts_nbytes = scroller_verts.nbytes
    scroller_verts_size = scroller_verts.size
    return scroller_vbo, scroller_verts_nbytes, scroller_verts_size

def scroller_font_texture():
    font_atlas_img_path = resource_path('resources/boheme-still93_font_white.png')
    font_atlas_surf = pg.image.load(font_atlas_img_path).convert_alpha()
    font_atlas_w, font_atlas_h = font_atlas_surf.get_size()
    font_atlas = pg.image.tostring(font_atlas_surf, "RGBA")
    font_char_w, font_char_h = 50, 50
    text_pos_x = screen_w
    text_pos_y = screen_h // 2 - font_char_h +15
    num_chars_x = font_atlas_w // font_char_w
    num_chars_y = font_atlas_w // font_char_h
    return font_atlas, font_atlas_w, font_atlas_h, font_char_w, font_char_h, \
    text_pos_x, text_pos_y, num_chars_x, num_chars_y

def scroller_font_atlas_buffer(font_atlas, font_atlas_w, font_atlas_h):
    font_atlas_texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, font_atlas_texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, font_atlas_w, font_atlas_h, 0, GL_RGBA, GL_UNSIGNED_BYTE, font_atlas)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glBindTexture(GL_TEXTURE_2D, 0)
    return font_atlas_texture_id

def scroller_render(scroller_vbo, font_atlas_texture_id, scroller_verts_nbytes, scroller_verts_size):
    glEnable(GL_BLEND)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, font_atlas_texture_id)
    glBindBuffer(GL_ARRAY_BUFFER, scroller_vbo)
    glVertexPointer(2, GL_FLOAT, 0, None)
    glEnableClientState(GL_VERTEX_ARRAY)
    glTexCoordPointer(2, GL_FLOAT, 0, c_void_p(scroller_verts_nbytes))
    glEnableClientState(GL_TEXTURE_COORD_ARRAY)
    glDrawArrays(GL_QUADS, 0, scroller_verts_size // 2)
    glDisableClientState(GL_TEXTURE_COORD_ARRAY)
    glDisableClientState(GL_VERTEX_ARRAY)
    glBindTexture(GL_TEXTURE_2D, 0)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glDisable(GL_BLEND)
    glDisable(GL_TEXTURE_2D)
    glDeleteBuffers(1, [scroller_vbo])

def raster_bar_init():
    bar_gradi = [(255.0, 0.0, 0.0), (255.0, 128.0, 0.0), (255.0, 255.0, 0.0), (0.0, 255.0, 255.0), (0.0, 255.0, 0.0)]
    bar_gradi_color = np.zeros((screen_w, 3), dtype=np.float32)
    bar_gradi_len = len(bar_gradi)
    bar_gradi_spd = 0.05
    bar_fill_alpha = 255
    bar_col = (0/255, 1/255, 26/255, bar_fill_alpha/255)
    bar_fill_col = np.array([c for c in bar_col * 4], dtype=np.float32)
    bar_spd = 1.5
    bar_stop_pos = 80
    bar_dir = "up"
    bar1_h = 3
    bar2_h = 3
    bar1_w = screen_w
    bar2_w = screen_w
    bar1_y = screen_h // 2 - bar1_h // 2
    bar2_y = screen_h // 2 - bar2_h // 2
    bar1_col_index = 0
    bar2_col_index = 9
    return bar_gradi, bar_gradi_color, bar_gradi_len, bar_gradi_spd, bar_fill_col, bar_spd, bar_stop_pos, bar_dir, bar1_h, bar2_h, bar1_w, bar2_w, bar1_y, bar2_y, bar1_col_index, bar2_col_index

def raster_opengl_init(screen_w, screen_h):
    glViewport(0, 0, screen_w, screen_h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, screen_w, screen_h, 0, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def update_raster_bars(bar_dir, bar_spd, bar1_y, bar2_y, bar_stop_pos, bar1_col_index, bar2_col_index):
    if bar_dir == "up":
        if bar_stop_pos < bar1_y <= screen_h // 2:
            bar1_y = max(bar1_y - bar_spd, bar_stop_pos)
            bar2_y = min(bar2_y + bar_spd, screen_h - bar_stop_pos)
    elif bar_dir == "down":
        if screen_h - bar_stop_pos >= bar2_y >= screen_h // 2:
            bar1_y = min(bar1_y + bar_spd, screen_h // 2)
            bar2_y = max(bar2_y - bar_spd, screen_h // 2)
    bar1_col_index = (bar1_col_index - bar_gradi_spd) % bar_gradi_len
    bar2_col_index = (bar2_col_index + bar_gradi_spd) % bar_gradi_len
    return bar1_y, bar2_y, bar1_col_index, bar2_col_index

def lerp_color(color1, color2, t):
    return tuple(float((1 - t) * color1[i]/255 + t * color2[i]/255) for i in range(3))

def create_raster_bar(bar_pos, y, color_index, bar1_w):
    if bar_pos == "lower":
        bar_verts = np.array([[0, bar1_y], [0, bar1_y - bar1_h], [screen_w, bar1_y - bar1_h], [screen_w, bar1_y]], dtype=np.float32)
    elif bar_pos == "upper":
        bar_verts = np.array([[0, bar2_y], [0, bar2_y + bar2_h], [screen_w, bar2_y + bar2_h], [screen_w, bar2_y]], dtype=np.float32)
    for x in range(screen_w):
        t = (x / screen_w) + (color_index / bar_gradi_len)
        t %= 1.0
        bar_color1 = bar_gradi[int(t * bar_gradi_len)]
        bar_color2 = bar_gradi[(int(t * bar_gradi_len) + 1) % bar_gradi_len]
        color = lerp_color(bar_color1, bar_color2, t * bar_gradi_len % 1.0)
        bar_gradi_color[x] = np.array(color)
    raster_vbo = glGenBuffers(1)
    raster_vbo = np.uint32(raster_vbo)
    glBindBuffer(GL_ARRAY_BUFFER, raster_vbo)
    glBufferData(GL_ARRAY_BUFFER, bar_verts.nbytes + bar_gradi_color.nbytes, None, GL_DYNAMIC_DRAW)
    glBufferSubData(GL_ARRAY_BUFFER, 0, bar_verts.nbytes, bar_verts)
    glBufferSubData(GL_ARRAY_BUFFER, bar_verts.nbytes, bar_gradi_color.nbytes, bar_gradi_color)
    glEnableClientState(GL_COLOR_ARRAY)
    glColorPointer(4, GL_FLOAT, 0, c_void_p(bar_verts.nbytes))
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(2, GL_FLOAT, 0, None)
    glDrawArrays(GL_QUADS, 0, bar_verts.size)
    glDisableClientState(GL_COLOR_ARRAY)
    glDisableClientState(GL_VERTEX_ARRAY)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glDeleteBuffers(1, [raster_vbo])

def fill_raster_area(bar1_y, bar2_y, bar_fill_col):
    bar1_vbo = glGenBuffers(1)
    bar1_vbo = np.uint32(bar1_vbo)
    glBindBuffer(GL_ARRAY_BUFFER, bar1_vbo)
    bar1_verts = [(-bar1_w, -bar1_y/2), (bar1_w, -bar1_y/2), (bar1_w, bar1_y), (-bar1_w, bar1_y)]
    bar1_verts = np.array(bar1_verts, dtype=np.float32)
    glBufferData(GL_ARRAY_BUFFER, bar1_verts.nbytes, bar1_verts, GL_DYNAMIC_DRAW)
    bar2_vbo = glGenBuffers(1)
    bar2_vbo = np.uint32(bar2_vbo)
    glBindBuffer(GL_ARRAY_BUFFER, bar2_vbo)
    bar2_verts = [(-bar2_w, screen_h // 2 + bar2_y + bar_spd), (bar2_w, screen_h // 2 + bar2_y + bar_spd), (bar2_w, bar2_y), (-bar2_w, bar2_y)]
    bar2_verts = np.array(bar2_verts, dtype=np.float32)
    glBufferData(GL_ARRAY_BUFFER, bar2_verts.nbytes, bar2_verts, GL_DYNAMIC_DRAW)
    bar_cbo = glGenBuffers(1)
    bar_cbo = np.uint32(bar_cbo)
    glBindBuffer(GL_ARRAY_BUFFER, bar_cbo)
    glBufferData(GL_ARRAY_BUFFER, bar_fill_col.nbytes, bar_fill_col, GL_DYNAMIC_DRAW)
    glEnableVertexAttribArray(0)
    glBindBuffer(GL_ARRAY_BUFFER, bar_cbo)
    glEnableClientState(GL_COLOR_ARRAY)
    glColorPointer(4, GL_FLOAT, 0, None)
    glBindBuffer(GL_ARRAY_BUFFER, bar1_vbo)
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, None)
    glDrawArrays(GL_QUADS, 0, bar1_verts.size)
    glBindBuffer(GL_ARRAY_BUFFER, bar2_vbo)
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, None)
    glDrawArrays(GL_QUADS, 0, bar2_verts.size)
    glDisableClientState(GL_COLOR_ARRAY)
    glDisableVertexAttribArray(0)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glDeleteBuffers(1, [bar1_vbo])
    glDeleteBuffers(1, [bar2_vbo])
    glDeleteBuffers(1, [bar_cbo])
    return bar1_y, bar2_y

bar_gradi, bar_gradi_color, bar_gradi_len, bar_gradi_spd, bar_fill_col,\
bar_spd, bar_stop_pos, bar_dir, bar1_h, bar2_h, bar1_w, bar2_w, bar1_y,\
bar2_y, bar1_col_index, bar2_col_index = raster_bar_init()

logo1, logo1_w, logo1_h, logo1_current_alpha, logo1_fade_in_duration, logo2_fade_in_duration,\
logo1_fade_out_duration, logo2_fade_out_duration, logo1_stay_duration, logo2_stay_duration,\
logo_scroll_speed, logo1_offset_x, logo2_offset_x, logo_elapsed_time, logo_phase,\
logo_transition_completed, logo_fade_out_triggered, logo_triggered = logo_init("resources/boheme-divinestylers.png")
logo2, logo2_w, logo2_h, logo2_current_alpha, logo1_fade_in_duration, logo2_fade_in_duration,\
logo1_fade_out_duration, logo2_fade_out_duration, logo1_stay_duration, logo2_stay_duration,\
logo_scroll_speed, logo1_offset_x, logo2_offset_x, logo_elapsed_time, logo_phase,\
logo_transition_completed, logo_fade_out_triggered, logo_triggered = logo_init("resources/boheme-style.png")
logo1_vbo, logo1_texture_id, logo1_verts_nbytes, logo1_verts_size = logo_buffers(logo1, logo1_w, logo1_h)
logo2_vbo, logo2_texture_id, logo2_verts_nbytes, logo2_verts_size = logo_buffers(logo2, logo2_w, logo2_h)

scroller_char_spacing, scroller_amplitude, scroller_frequency, scroller_top_rotation_factor, scroller_bottom_rotation_factor,\
scroller_tweak_1, scroller_tweak_2, scroller_tweak_3, scroller_tweak_4, scroller_tweak_5, scroller_tweak_6, scroller_text_scale,\
scroller_text_speed, scroller_rainbow_speed = scroller_init()
font_atlas, font_atlas_w, font_atlas_h, font_char_w, font_char_h, text_pos_x, text_pos_y, num_chars_x, num_chars_y = scroller_font_texture()
font_metrics = scroller_font_metrics(num_chars_x, font_char_w, font_char_h)
font_atlas_texture_id = scroller_font_atlas_buffer(font_atlas, font_atlas_w, font_atlas_h)

stars, stars_surf, star_colors, stars_w, stars_h = stars_init(bar_stop_pos)
stars_vbo, stars_verts_nbytes, stars_verts_size = stars_verts_buffer(stars_w, stars_h)

clock = pg.time.Clock()
start_time = pg.time.get_ticks() // 1000

MEGA = True
while MEGA:
    clock.tick(30)
    pg.display.set_caption(str(int(clock.get_fps())))
    current_time = pg.time.get_ticks() // 1000 - start_time
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

    stars_opengl_init(stars_w, stars_h, bar_stop_pos)
    stars_surf = stars_layer(stars, stars_surf, star_colors, stars_w, stars_h)
    stars_texture_id = stars_texture_buffer(stars_w, stars_h, stars_surf)
    glPushMatrix()
    stars_draw(stars_texture_id, stars_vbo, stars_verts_nbytes, stars_verts_size)
    glPopMatrix()

    logo1_current_alpha, logo2_current_alpha, logo1_offset_x, logo2_offset_x,\
    logo_elapsed_time, logo_phase, logo_triggered = logo_phase_handling(
        logo_phase, logo_elapsed_time,
        logo_scroll_speed,
        logo1_fade_in_duration,
        logo2_fade_in_duration,
        logo1_current_alpha,
        logo2_current_alpha,
        logo_transition_completed,
        logo1_offset_x,
        logo2_offset_x,
        logo_triggered
    )

    if logo_phase in (2, 3, 4):
        logo_opengl_init(logo2_w, logo2_h)
        glPushMatrix()
        glTranslatef(logo2_offset_x, 0, 0)
        glTranslatef(0, 0, 0)
        logo2_current_alpha = logo_draw(logo2_current_alpha, logo2_texture_id, logo2_vbo, logo2_verts_nbytes, logo2_verts_size)
        glPopMatrix()
    if logo_phase in (0, 1, 2, 4):
        logo_opengl_init(logo1_w, logo1_h)
        glPushMatrix()
        glTranslatef(logo1_offset_x, 0, 0)
        logo1_current_alpha = logo_draw(logo1_current_alpha, logo1_texture_id, logo1_vbo, logo1_verts_nbytes, logo1_verts_size)
        glPopMatrix()
    if logo_fade_out_triggered:
        logo1_current_alpha, logo2_current_alpha = logo_fade_out(logo1_current_alpha, logo2_current_alpha, logo1_fade_out_duration, logo2_fade_out_duration)

    logo_elapsed_time += clock.get_time()

    scroller_opengl_init(screen_w, screen_h, bar_stop_pos)
    if logo_triggered:
        scroller_vbo, scroller_verts_nbytes, scroller_verts_size = scroller_verts_and_coords(
            scroll_text,
            text_pos_x,
            text_pos_y,
            font_metrics,
            scroller_amplitude,
            scroller_frequency,
            scroller_text_scale,
            scroller_char_spacing,
            scroller_tweak_1,
            scroller_tweak_2,
            scroller_tweak_3,
            scroller_tweak_4,
            scroller_tweak_5,
            scroller_tweak_6,
            font_atlas_w,
            font_atlas_h,
            font_char_w,
            font_char_h
        )

        color = scroller_rainbow_color(scroller_rainbow_speed)
        char_color = scroller_pulse_gradient(800, color, darkness_threshold=0.3)
        glPushMatrix()
        glColor4f(*char_color, 0.7)
        scroller_render(scroller_vbo, font_atlas_texture_id, scroller_verts_nbytes, scroller_verts_size)
        glPopMatrix()

        text_pos_x -= scroller_text_speed

    if text_pos_x + len(scroll_text) * (font_char_w * scroller_text_scale + scroller_char_spacing) + font_char_w < 0:
        pg.mixer.music.fadeout(logo1_fade_out_duration)
        logo_fade_out_triggered = True
        bar_dir = "down"
        if bar1_y >= screen_h // 2 >= bar2_y:
            break

    bar1_y, bar2_y, bar1_col_index, bar2_col_index = update_raster_bars(
        bar_dir,
        bar_spd,
        bar1_y,
        bar2_y,
        bar_stop_pos,
        bar1_col_index,
        bar2_col_index
    )

    glPushMatrix()
    bar1_y, bar2_y = fill_raster_area(bar1_y, bar2_y, bar_fill_col)
    glPopMatrix()

    glPushMatrix()
    create_raster_bar("lower", bar1_y, bar1_col_index, bar1_w)
    create_raster_bar("upper", bar2_y, bar2_col_index, bar2_w)
    glPopMatrix()

    pg.display.flip()

glDeleteBuffers(1, [stars_vbo, logo1_vbo, logo2_vbo])
glDeleteTextures(1, [stars_texture_id, logo1_texture_id, logo2_texture_id, font_atlas_texture_id])
