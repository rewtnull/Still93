from still93_runtime_hooker import MEGA03
MEGA3 = MEGA03()
### GLOBAL
screen_w = MEGA3.screen_w
screen_h = MEGA3.screen_h
screen = MEGA3.screen
pg = MEGA3.pg
np = MEGA3.np
os = MEGA3.os
sys = MEGA3.sys
c_void_p = MEGA3.c_void_p
c_float = MEGA3.c_float
resource_path = MEGA3.resource_path
glEnable = MEGA3.glEnable
glDisable = MEGA3.glDisable
glBlendFunc = MEGA3.glBlendFunc
glClearDepth = MEGA3.glClearDepth
glClearColor = MEGA3.glClearColor
glClear = MEGA3.glClear
glViewport = MEGA3.glViewport
glMatrixMode = MEGA3.glMatrixMode
glLoadIdentity = MEGA3.glLoadIdentity
glGenBuffers = MEGA3.glGenBuffers
glBindBuffer = MEGA3.glBindBuffer
glBufferData = MEGA3.glBufferData
glBufferSubData = MEGA3.glBufferSubData
glDeleteBuffers = MEGA3.glDeleteBuffers
glGenTextures = MEGA3.glGenTextures
glBindTexture = MEGA3.glBindTexture
glDeleteTextures = MEGA3.glDeleteTextures
glTexImage2D = MEGA3.glTexImage2D
glTexParameteri = MEGA3.glTexParameteri
glDrawArrays = MEGA3.glDrawArrays
glPushMatrix = MEGA3.glPushMatrix
glPopMatrix = MEGA3.glPopMatrix
GL_COLOR_BUFFER_BIT = MEGA3.GL_COLOR_BUFFER_BIT
GL_DEPTH_BUFFER_BIT = MEGA3.GL_DEPTH_BUFFER_BIT
GL_PROJECTION = MEGA3.GL_PROJECTION
GL_MODELVIEW = MEGA3.GL_MODELVIEW
GL_ARRAY_BUFFER = MEGA3.GL_ARRAY_BUFFER
GL_TEXTURE_2D = MEGA3.GL_TEXTURE_2D
GL_RGBA = MEGA3.GL_RGBA
GL_UNSIGNED_BYTE = MEGA3.GL_UNSIGNED_BYTE
GL_FLOAT = MEGA3.GL_FLOAT
GL_TEXTURE_MIN_FILTER = MEGA3.GL_TEXTURE_MIN_FILTER
GL_TEXTURE_MAG_FILTER = MEGA3.GL_TEXTURE_MAG_FILTER
GL_LINEAR = MEGA3.GL_LINEAR
### LOCAL
sin = MEGA3.sin
cos = MEGA3.cos
radians = MEGA3.radians
glActiveTexture = MEGA3.glActiveTexture
glUniform3d = MEGA3.glUniform3d
glUniform1d = MEGA3.glUniform1d
glUniform1i = MEGA3.glUniform1i
glTranslatef = MEGA3.glTranslatef
glVertexPointer = MEGA3.glVertexPointer
glEnableClientState = MEGA3.glEnableClientState
glDisableClientState = MEGA3.glDisableClientState
glDeleteProgram = MEGA3.glDeleteProgram
glUseProgram = MEGA3.glUseProgram
compileProgram = MEGA3.compileProgram
compileShader = MEGA3.compileShader
glScalef = MEGA3.glScalef
glOrtho = MEGA3.glOrtho
glTexCoordPointer = MEGA3.glTexCoordPointer
glColor4f = MEGA3.glColor4f
glGetUniformLocation = MEGA3.glGetUniformLocation
glGetAttribLocation = MEGA3.glGetAttribLocation
glEnableVertexAttribArray = MEGA3.glEnableVertexAttribArray
glDisableVertexAttribArray = MEGA3.glDisableVertexAttribArray
glVertexAttribPointer = MEGA3.glVertexAttribPointer
glUniform2f = MEGA3.glUniform2f
glTranslate = MEGA3.glTranslate
GL_TEXTURE0 = MEGA3.GL_TEXTURE0
GL_TEXTURE_WRAP_S = MEGA3.GL_TEXTURE_WRAP_S
GL_TEXTURE_WRAP_T = MEGA3.GL_TEXTURE_WRAP_T
GL_CLAMP_TO_EDGE = MEGA3.GL_CLAMP_TO_EDGE
GL_FALSE = MEGA3.GL_FALSE
GL_NEAREST = MEGA3.GL_NEAREST
GL_VERTEX_ARRAY = MEGA3.GL_VERTEX_ARRAY
GL_DYNAMIC_DRAW = MEGA3.GL_DYNAMIC_DRAW
GL_SRC_ALPHA = MEGA3.GL_SRC_ALPHA
GL_ONE_MINUS_SRC_ALPHA = MEGA3.GL_ONE_MINUS_SRC_ALPHA
GL_BLEND = MEGA3.GL_BLEND
GL_QUADS = MEGA3.GL_QUADS
GL_TEXTURE_COORD_ARRAY = MEGA3.GL_TEXTURE_COORD_ARRAY
GL_VERTEX_SHADER = MEGA3.GL_VERTEX_SHADER
GL_FRAGMENT_SHADER = MEGA3.GL_FRAGMENT_SHADER
GL_REPEAT = MEGA3.GL_REPEAT
GL_TRIANGLE_STRIP = MEGA3.GL_TRIANGLE_STRIP
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

pg.mixer.init()
pg.mixer.music.load(resource_path('resources/repe-deflected-v3.mod'))
pg.mixer.music.play(0)

vertex_shader = """
#version 400
in vec2 position;

void main()
{
    gl_Position = vec4(position, 0.0, 1.0);
}
"""

fragment_shader = """
#version 400

out vec4 out_color;

uniform vec2 resolution;
uniform dvec3 center;
uniform double zoom;
uniform double tweakform1;
uniform double tweakform2;
uniform double tweakform3;
uniform sampler2D texture;

const float max_iterations = 30000;
const float glowAmount = 0.0090;
const float glowRadius = 0.0100;
const float aoStrength = 32.0;
const float aoSamples = 128.0;
const int tmult1 = 32;
const int tmult2 = 16;

float calculateAO(vec3 position, vec3 normal)
{
    float ao = 0.0;
    for (int i = 0; i < aoSamples; i++)
    {
        float angle = float(i) / float(aoSamples) * 6.28318530718;
        vec3 hemisphereDir = vec3(sin(angle), sin(angle), 0.0);
        vec3 samplePos = position + hemisphereDir * 0.01;
        float sampleDepth = texture2D(texture, samplePos.xy).a;
        float sampleDistance = position.z - sampleDepth;
        ao += smoothstep(0.0, 1.0, sampleDistance * 150.0);
    }
    ao /= aoSamples;
    ao = 1.0 - ao * aoStrength;
    return ao;
}

void main()
{
    dvec2 uv = (gl_FragCoord.xy - resolution / 4.0) / zoom;
    dvec3 c = dvec3(-0.2, 0.67015, 0.2);
    dvec3 z = dvec3(uv.x, uv.y, center / zoom) - center;
    int iterations = 0;

    while (dot(z, z) < 4.0 && iterations < max_iterations)
    {
        z = dvec3(tweakform1 * z.x * z.x - z.y * z.y, tweakform2 * z.x * z.y, z.z * 2.0 * z.z - tweakform3 * z.y * z.y) + c;
        iterations++;
    }

    double t = iterations / max_iterations;
    t = smoothstep(0.0, 1.0, t * tmult1);

    vec4 textureColor = texture2D(texture, vec2(t * tmult2, 0.0));

    vec3 position = textureColor.rgb;
    float distance = length(position - textureColor.rgb);

    float ao = calculateAO(position, normalize(vec3(uv, distance)));

    vec3 glowColor = vec3(0.4, 0.2, 0.2);
    vec3 finalColor = position + glowColor * ao * glowAmount;

    finalColor = finalColor / (finalColor + vec3(1.0));

    out_color = vec4(finalColor, textureColor.a);
}
"""

glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glClearDepth(1.0)
glClearColor(0.0, 0.0, 0.0, 0.0)
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
glViewport(0, 0, screen_w, screen_h)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, screen_w, screen_h, 0, -1, 1)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

flash_color = (0.0, 0.0, 0.0)
flash_x = 0
flash_y = 0
flash_duration = 1000
flash_delay = 500

julia_start_x =  0.27851183786542233
julia_start_y = -0.39507047310114846
julia_start_z = 0.0
julia_zoom = 1.0
julia_tweak_formula1 = 1.0
julia_tweak_formula2 = 2.50
julia_tweak_formula3 = 3.36
julia_pause = True

scroll_text = "....................................THE AIM OF SCIENCE IS NOT TO OPEN THE DOOR TO INFINITE WISDOM\
...................................................BUT TO SET A LIMIT TO INFINITE ERROR.................."
scroller_char_spacing = 0
scroller_amplitude = 50.0
scroller_frequency = 0.014
scroller_top_rotation_factor = 5.0
scroller_bottom_rotation_factor = -5.0
scroller_tweak_1 = 0.0
scroller_tweak_2 = 0.0
scroller_tweak_3 = 20.0
scroller_tweak_4 = 20.0
scroller_tweak_5 = 200.0
scroller_tweak_6 = -100.0
scroller_text_scale = 1.0
scroller_text_speed = 8.0
scroll_scale_factor = 2.0

def julia_colors_texture():
    color_texture_path = resource_path('resources/julia_palette.png')
    color_texture_surf = pg.image.load(color_texture_path).convert_alpha()
    color_texture_w, color_texture_h = color_texture_surf.get_size()
    color_texture = pg.image.tostring(color_texture_surf, "RGBA")
    julia_color_texture_id = glGenTextures(1)
    julia_color_texture_id = np.uint32(julia_color_texture_id)
    glBindTexture(GL_TEXTURE_2D, julia_color_texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, color_texture_w, color_texture_h, 0, GL_RGBA, GL_UNSIGNED_BYTE, color_texture)
    glBindTexture(GL_TEXTURE_2D, 0)
    return julia_color_texture_id

def julia_shader():
    julia_shader = compileProgram(
        compileShader(vertex_shader, GL_VERTEX_SHADER),
        compileShader(fragment_shader, GL_FRAGMENT_SHADER)
    )
    return julia_shader

def julia_buffer():
    julia_verts = [-1, -1, 1, -1, -1, 1, 1, 1]
    julia_verts = np.array(julia_verts, dtype=np.float32)
    julia_vbo = glGenBuffers(1)
    julia_vbo = np.uint32(julia_vbo)
    glBindBuffer(GL_ARRAY_BUFFER, julia_vbo)
    glBufferData(GL_ARRAY_BUFFER, julia_verts.nbytes, (c_float * julia_verts.nbytes)(*julia_verts), GL_DYNAMIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    return julia_vbo

def julia_attribs(julia_vbo, julia_shader):
    glBindBuffer(GL_ARRAY_BUFFER, julia_vbo)
    position_loc = glGetAttribLocation(julia_shader, 'position')
    glEnableVertexAttribArray(position_loc)
    glVertexAttribPointer(position_loc, 2, GL_FLOAT, GL_FALSE, 0, None)
    glDisableVertexAttribArray(position_loc)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    return position_loc

def julia_draw(julia_shader, julia_position_loc, julia_vbo, julia_texture_unit, julia_color_texture_id, julia_zoom_loc, julia_zoom):
    glUseProgram(julia_shader)
    glEnableVertexAttribArray(julia_position_loc)
    glBindBuffer(GL_ARRAY_BUFFER, julia_vbo)
    glActiveTexture(GL_TEXTURE0 + julia_texture_unit)
    glBindTexture(GL_TEXTURE_2D, julia_color_texture_id)
    glUniform1d(julia_zoom_loc, julia_zoom)
    glPushMatrix()
    glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)
    glPopMatrix()
    glDisableVertexAttribArray(julia_position_loc)
    glBindTexture(GL_TEXTURE_2D, 0)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glActiveTexture(GL_TEXTURE0)
    glUseProgram(0)

def julia_uniforms(screen_w, screen_h, julia_start_x, julia_start_y, julia_start_z, julia_zoom, julia_tweak_formula1, julia_tweak_formula2, julia_tweak_formula3):
    julia_resolution_loc = glGetUniformLocation(julia_shader, 'resolution')
    glUniform2f(julia_resolution_loc, *(screen_w, screen_h))
    julia_center_loc = glGetUniformLocation(julia_shader, 'center')
    glUniform3d(julia_center_loc, julia_start_x, julia_start_y, julia_start_z)
    julia_zoom_loc = glGetUniformLocation(julia_shader, 'zoom')
    glUniform1d(julia_zoom_loc, julia_zoom)
    julia_tweakform_loc = glGetUniformLocation(julia_shader, 'tweakform1')
    glUniform1d(julia_tweakform_loc, julia_tweak_formula1)
    julia_tweakform2_loc = glGetUniformLocation(julia_shader, 'tweakform2')
    glUniform1d(julia_tweakform2_loc, julia_tweak_formula2)
    julia_tweakform3_loc = glGetUniformLocation(julia_shader, 'tweakform3')
    glUniform1d(julia_tweakform3_loc, julia_tweak_formula3)
    julia_texture_unit = 1
    julia_texture_loc = glGetUniformLocation(julia_shader, 'texture')
    glUniform1i(julia_texture_loc, julia_texture_unit)
    return julia_texture_unit, julia_resolution_loc, julia_center_loc, julia_zoom_loc, julia_tweakform_loc, julia_tweakform2_loc, julia_tweakform3_loc

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
    font_atlas_img_path = resource_path('resources/boheme-still93_font_fire.png')
    font_atlas_surf = pg.image.load(font_atlas_img_path).convert_alpha()
    font_atlas_w, font_atlas_h = font_atlas_surf.get_size()
    font_atlas = pg.image.tostring(font_atlas_surf, "RGBA")
    font_char_w, font_char_h = 50, 50
    text_pos_x = screen_w
    text_pos_y = screen_h // 2
    num_chars_x = font_atlas_w // font_char_w
    num_chars_y = font_atlas_w // font_char_h
    return font_atlas, font_atlas_w, font_atlas_h, font_char_w, font_char_h, \
    text_pos_x, text_pos_y, num_chars_x, num_chars_y

def scroller_font_atlas_buffer(font_atlas, font_atlas_w, font_atlas_h):
    font_atlas_id = glGenTextures(1)
    font_atlas_id = np.uint32(font_atlas_id)
    glBindTexture(GL_TEXTURE_2D, font_atlas_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, font_atlas_w, font_atlas_h, 0, GL_RGBA, GL_UNSIGNED_BYTE, font_atlas)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glBindTexture(GL_TEXTURE_2D, 0)
    return font_atlas_id

def scroller_render(scroller_vbo, font_atlas_id, scroller_verts_nbytes, scroller_verts_size):
    glEnable(GL_BLEND)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, font_atlas_id)
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

def logo_init(logo_name):
    logo_path = resource_path(logo_name)
    logo = pg.image.load(logo_path).convert_alpha()
    logo_w, logo_h = logo.get_size()
    logo_w, logo_h = int(logo_w // 2.5), int(logo_h // 2.5)
    logo = pg.transform.scale(logo, (logo_w, logo_h))
    logo_scroll_duration = 500
    logo_current_alpha = 0
    logo1_fade_in_duration = 8500
    logo2_fade_in_duration = 8500
    logo1_fade_out_duration = 3000
    logo2_fade_out_duration = 3000
    logo1_stay_duration = 5000
    logo2_stay_duration = 5000
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
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, logo_w, logo_h, 0, GL_RGBA, GL_UNSIGNED_BYTE, pg.image.tostring(logo, "RGBA", False))
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

def logo_phase_handing(logo_phase, logo_elapsed_time, logo_scroll_speed, logo1_fade_in_duration, logo2_fade_in_duration, logo1_current_alpha, logo2_current_alpha, logo_transition_completed, logo1_offset_x, logo2_offset_x, logo_triggered):
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
        if logo1_offset_x < -logo1_w - int((screen_w - logo2_w) // 2):
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
        if logo1_offset_x > int((screen_w - logo1_w) // 2):
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

julia_color_texture_id = julia_colors_texture()
julia_shader = julia_shader()
glUseProgram(julia_shader)
julia_vbo = julia_buffer()
julia_position_loc = julia_attribs(julia_vbo, julia_shader)

julia_texture_unit, julia_resolution_loc, julia_center_loc, julia_zoom_loc,\
julia_tweakform_loc, julia_tweakform2_loc, julia_tweakform3_loc = julia_uniforms(
    screen_w, screen_h,
    julia_start_x, julia_start_y, julia_start_z,
    julia_zoom,
    julia_tweak_formula1, julia_tweak_formula2, julia_tweak_formula3
)
glUseProgram(0)

font_atlas, font_atlas_w, font_atlas_h, font_char_w, font_char_h, text_pos_x, text_pos_y, num_chars_x, num_chars_y = scroller_font_texture()
font_metrics = scroller_font_metrics(num_chars_x, font_char_w, font_char_h)
font_atlas_id = scroller_font_atlas_buffer(font_atlas, font_atlas_w, font_atlas_h)

logo1, logo1_w, logo1_h, logo1_current_alpha, logo1_fade_in_duration, logo2_fade_in_duration,\
logo1_fade_out_duration, logo2_fade_out_duration, logo1_stay_duration, logo2_stay_duration,\
logo_scroll_speed, logo1_offset_x, logo2_offset_x, logo_elapsed_time, logo_phase,\
logo_transition_completed, logo_fade_out_triggered, logo_triggered = logo_init("resources/hellbeard-divinestylers.png")
logo1_vbo, logo1_texture_id, logo1_verts_nbytes, logo1_verts_size = logo_buffers(logo1, logo1_w, logo1_h)

logo2, logo2_w, logo2_h, logo2_current_alpha, logo1_fade_in_duration, logo2_fade_in_duration,\
logo1_fade_out_duration, logo2_fade_out_duration, logo1_stay_duration, logo2_stay_duration,\
logo_scroll_speed, logo1_offset_x, logo2_offset_x, logo_elapsed_time, logo_phase,\
logo_transition_completed, logo_fade_out_triggered, logo_triggered = logo_init("resources/hellbeard-style.png")
logo2_vbo, logo2_texture_id, logo2_verts_nbytes, logo2_verts_size = logo_buffers(logo2, logo2_w, logo2_h)

clock = pg.time.Clock()
key_held_shift = False
pg.key.set_repeat(10)

MEGA = True
while MEGA:
    clock.tick(30)
    pg.display.set_caption(str(int(clock.get_fps())))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LSHIFT or event.key == pg.K_RSHIFT:
                key_held_shift = True
            if event.key == pg.K_ESCAPE:
                print(f"Something Wonderful Has Happened!")
                pg.quit()
                sys.exit()
            elif event.key == pg.K_RETURN:
                MEGA = False
        elif event.type == pg.KEYUP:
            if event.key == pg.K_LSHIFT or event.key == pg.K_RSHIFT:
                key_held_shift = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    julia_draw(julia_shader,
        julia_position_loc,
        julia_vbo,
        julia_texture_unit,
        julia_color_texture_id,
        julia_zoom_loc,
        julia_zoom
    )

    glUseProgram(julia_shader)

    julia_tweak_formula3 += 0.002

    julia_tweakform_loc = glGetUniformLocation(julia_shader, 'tweakform1')
    glUniform1d(julia_tweakform_loc, julia_tweak_formula1)
    julia_tweakform2_loc = glGetUniformLocation(julia_shader, 'tweakform2')
    glUniform1d(julia_tweakform2_loc, julia_tweak_formula2)
    julia_tweakform3_loc = glGetUniformLocation(julia_shader, 'tweakform3')
    glUniform1d(julia_tweakform3_loc, julia_tweak_formula3)
    julia_center_loc = glGetUniformLocation(julia_shader, 'center')
    glUniform3d(julia_center_loc, julia_start_x, julia_start_y, julia_start_z)
    julia_zoom_loc = glGetUniformLocation(julia_shader, 'zoom')
    glUniform1d(julia_zoom_loc, julia_zoom)
    glUseProgram(0)
    if julia_pause:
        julia_zoom *= 1.03

    logo1_current_alpha, logo2_current_alpha, logo1_offset_x, logo2_offset_x,\
    logo_elapsed_time, logo_phase, logo_triggered = logo_phase_handing(
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
        glPushMatrix()
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslate(0.0, 30.0, 0.0)
        glTranslatef(logo2_offset_x, 0, 0)
        glTranslatef(0, 0, 0)
        logo2_current_alpha = logo_draw(logo2_current_alpha, logo2_texture_id, logo2_vbo, logo2_verts_nbytes, logo2_verts_size)
        glPopMatrix()
    if logo_phase in (0, 1, 2, 4):
        glPushMatrix()
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslate(0.0, 30.0, 0.0)
        glTranslatef(logo1_offset_x, 0, 0)
        logo1_current_alpha = logo_draw(logo1_current_alpha, logo1_texture_id, logo1_vbo, logo1_verts_nbytes, logo1_verts_size)
        glPopMatrix()

    logo_elapsed_time += clock.get_time()

    scroller_vbo, scroller_verts_nbytes, scroller_verts_size = scroller_verts_and_coords(
        scroll_text,
        text_pos_x, text_pos_y,
        font_metrics,
        scroller_amplitude, scroller_frequency,
        scroller_text_scale,
        scroller_char_spacing,
        scroller_tweak_1, scroller_tweak_2,
        scroller_tweak_3, scroller_tweak_4,
        scroller_tweak_5, scroller_tweak_6,
        font_atlas_w,font_atlas_h,
        font_char_w, font_char_h
    )

    glPushMatrix()
    glTranslate(0.0, screen_h - font_char_h * 14.5, 0.0)
    glScalef(scroll_scale_factor, scroll_scale_factor, 1.0)
    scroller_render(scroller_vbo, font_atlas_id, scroller_verts_nbytes, scroller_verts_size)
    glPopMatrix()

    text_pos_x -= scroller_text_speed

    if text_pos_x + len(scroll_text) * (font_char_w * scroller_text_scale + scroller_char_spacing) + font_char_w * 8 < 0:
        break

    pg.display.flip()

glDeleteTextures(1, [julia_color_texture_id, font_atlas_id, logo1_texture_id, logo2_texture_id])
glDeleteBuffers(1, [scroller_vbo, julia_vbo, logo1_vbo, logo2_vbo])
glUseProgram(0)
glDeleteProgram(julia_shader)
