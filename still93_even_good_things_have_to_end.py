from still93_runtime_hooker import MEGA07
MEGA7 = MEGA07()
### GLOBAL
screen_w = MEGA7.screen_w
screen_h = MEGA7.screen_h
screen = MEGA7.screen
pg = MEGA7.pg
np = MEGA7.np
os = MEGA7.os
sys = MEGA7.sys
c_void_p = MEGA7.c_void_p
c_float = MEGA7.c_float
resource_path = MEGA7.resource_path
glEnable = MEGA7.glEnable
glDisable = MEGA7.glDisable
glBlendFunc = MEGA7.glBlendFunc
glClearDepth = MEGA7.glClearDepth
glClearColor = MEGA7.glClearColor
glClear = MEGA7.glClear
glViewport = MEGA7.glViewport
glMatrixMode = MEGA7.glMatrixMode
glLoadIdentity = MEGA7.glLoadIdentity
glGenBuffers = MEGA7.glGenBuffers
glBindBuffer = MEGA7.glBindBuffer
glBufferData = MEGA7.glBufferData
glBufferSubData = MEGA7.glBufferSubData
glDeleteBuffers = MEGA7.glDeleteBuffers
glGenTextures = MEGA7.glGenTextures
glBindTexture = MEGA7.glBindTexture
glDeleteTextures = MEGA7.glDeleteTextures
glDeleteVertexArrays = MEGA7.glDeleteVertexArrays
glTexImage2D = MEGA7.glTexImage2D
glTexParameteri = MEGA7.glTexParameteri
glDrawArrays = MEGA7.glDrawArrays
glPushMatrix = MEGA7.glPushMatrix
glPopMatrix = MEGA7.glPopMatrix
GL_COLOR_BUFFER_BIT = MEGA7.GL_COLOR_BUFFER_BIT
GL_DEPTH_BUFFER_BIT = MEGA7.GL_DEPTH_BUFFER_BIT
GL_PROJECTION = MEGA7.GL_PROJECTION
GL_MODELVIEW = MEGA7.GL_MODELVIEW
GL_ARRAY_BUFFER = MEGA7.GL_ARRAY_BUFFER
GL_TEXTURE_2D = MEGA7.GL_TEXTURE_2D
GL_RGBA = MEGA7.GL_RGBA
GL_UNSIGNED_BYTE = MEGA7.GL_UNSIGNED_BYTE
GL_FLOAT = MEGA7.GL_FLOAT
GL_TEXTURE_MIN_FILTER = MEGA7.GL_TEXTURE_MIN_FILTER
GL_TEXTURE_MAG_FILTER = MEGA7.GL_TEXTURE_MAG_FILTER
GL_LINEAR = MEGA7.GL_LINEAR
### LOCAL
time = MEGA7.time
sin = MEGA7.sin
cos = MEGA7.cos
radians = MEGA7.radians
glVertexPointer = MEGA7.glVertexPointer
glEnableClientState = MEGA7.glEnableClientState
glDisableClientState = MEGA7.glDisableClientState
glCreateShader = MEGA7.glCreateShader
glShaderSource = MEGA7.glShaderSource
glCompileShader = MEGA7.glCompileShader
glGetShaderiv = MEGA7.glGetShaderiv
glCreateProgram = MEGA7.glCreateProgram
glAttachShader = MEGA7.glAttachShader
glLinkProgram = MEGA7.glLinkProgram
glGetProgramiv = MEGA7.glGetProgramiv
glValidateProgram = MEGA7.glValidateProgram
glDetachShader = MEGA7.glDetachShader
glDeleteProgram = MEGA7.glDeleteProgram
glUseProgram = MEGA7.glUseProgram
compileProgram = MEGA7.compileProgram
compileShader = MEGA7.compileShader
glScalef = MEGA7.glScalef
glOrtho = MEGA7.glOrtho
glTexCoordPointer = MEGA7.glTexCoordPointer
glColor4f = MEGA7.glColor4f
glGetUniformLocation = MEGA7.glGetUniformLocation
glGetAttribLocation = MEGA7.glGetAttribLocation
glEnableVertexAttribArray = MEGA7.glEnableVertexAttribArray
glDisableVertexAttribArray = MEGA7.glDisableVertexAttribArray
glVertexAttribPointer = MEGA7.glVertexAttribPointer
glUniform2f = MEGA7.glUniform2f
glTranslate = MEGA7.glTranslate
glVertexPointer = MEGA7.glVertexPointer
glIndexPointer = MEGA7.glIndexPointer
glHint = MEGA7.glHint
glDrawElements = MEGA7.glDrawElements
glGenVertexArrays = MEGA7.glGenVertexArrays
glBindVertexArray = MEGA7.glBindVertexArray
glDeleteVertexArrays = MEGA7.glDeleteVertexArrays
glUniform1f = MEGA7.glUniform1f
GL_COMPILE_STATUS = MEGA7.GL_COMPILE_STATUS
GL_VALIDATE_STATUS = MEGA7.GL_VALIDATE_STATUS
GL_LINK_STATUS = MEGA7.GL_LINK_STATUS
GL_TEXTURE0 = MEGA7.GL_TEXTURE0
GL_TEXTURE_WRAP_S = MEGA7.GL_TEXTURE_WRAP_S
GL_TEXTURE_WRAP_T = MEGA7.GL_TEXTURE_WRAP_T
GL_CLAMP_TO_EDGE = MEGA7.GL_CLAMP_TO_EDGE
GL_FALSE = MEGA7.GL_FALSE
GL_NEAREST = MEGA7.GL_NEAREST
GL_VERTEX_ARRAY = MEGA7.GL_VERTEX_ARRAY
GL_DYNAMIC_DRAW = MEGA7.GL_DYNAMIC_DRAW
GL_SRC_ALPHA = MEGA7.GL_SRC_ALPHA
GL_ONE_MINUS_SRC_ALPHA = MEGA7.GL_ONE_MINUS_SRC_ALPHA
GL_BLEND = MEGA7.GL_BLEND
GL_QUADS  = MEGA7.GL_QUADS
GL_TEXTURE_COORD_ARRAY = MEGA7.GL_TEXTURE_COORD_ARRAY
GL_VERTEX_SHADER = MEGA7.GL_VERTEX_SHADER
GL_FRAGMENT_SHADER = MEGA7.GL_FRAGMENT_SHADER
GL_REPEAT = MEGA7.GL_REPEAT
GL_TRIANGLE_STRIP = MEGA7.GL_TRIANGLE_STRIP
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

pg.mixer.init()
pg.mixer.music.load(resource_path('resources/skope-005agima.mod'))
pg.mixer.music.play(-1)

glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
glClearDepth(1.0)
glClearColor(0.0, 0.0, 0.0, 0.0)
glViewport(0, 0, screen_w, screen_h)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, screen_w, screen_h, 0, -1, 1)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

plasma_time = -427000.0
plasma_pixel_size = 100
plasma_turbulence = 1.0
plasma_scale = 52.0
plasma_speed = 51.8
plasma_w = screen_w
plasma_h = screen_h
plasma_speed = 55.60000000000005
plasma_offset_1x = 5.099999999999998
plasma_offset_1y = 2.1000000000000005
plasma_offset_2x = 1.3
plasma_offset_2y = 2.9000000000000004
plasma_offset_3x = 0.7
plasma_offset_3y = 0.1

logo_amplitude = 50.0
logo_frequency = 0.006
logo_speed = 1.0
logo_offset_x = 0.0
logo_offset_y = 0.93
logo_pixel_size = 1
logo_trigger = True
logo_end_time = 0

scroll_text = "* UP ROUGH * HOUSE OF STYLE * TITAN * IMPURE * AEROHOLICS * VENOM * DEZIGN * TRISTAR AND RED SECTOR * TWISTED \
* LIGHTFORCE * BAD KARMA * ROYAL * PARADOX * BOMBSQUAD * CRUDE * RAZOR 1911 * CAPITAL * DUAL CREW SHINING * KALISTO * EPSILON DESIGN \
* SKID ROW * ECHELON * DEKADENCE * ARCLITE * MODE7 * LOW PROFILE * CODEX * REBELS * HOODLUM * ODDITY * DIMENSION * CENSOR DESIGN \
* BLOCKTRONICS * CHALLENGE OF REVERSE ENGINEERING * DESIRE * PIRATES WITH ATTITUDE * PHROZEN HELL * GENESIS PROJECT \
* BREAK THE COPYRIGHT * DEVOTION * LAXITY * 13 * XFORCE * HAUJOBB * FAITH * HYMN * GODS * HELLFIRE * BACKLASH * CENTROPY * NOIR \
* SCOOPEX * KINDA * CHEMICAL REACTION * THE PLANET OF LEATHER MOOMINS * BABAS * FAIRLIGHT * GROOVEMISSION * CLASSIC * SHELTER \
* AEROSOL * SICK OF IT ALL * PANZERKNACKERS * DIGITAL GRAFFITI * FUCK THE DUMB * BASS * PHANTASY * DRUNKEN * PSYCZ * HEIRLOOM \
* RISING SUN * LEGACY * LIGHT SPEED DISTRIBUTION * DUPLEX * SUXXORS * BLACK MAIDEN * FARBRAUSCH * QUARTEX * EMBRACE \
* FANTASTIC 4 CRACKING GROUP * VIBES * LORENZ * FAITH *"

scroller_char_spacing = 2
scroller_amplitude = 10.0
scroller_frequency = 0.02
scroller_top_rotation_factor = 3.0
scroller_bottom_rotation_factor = -3.0
scroller_tweak_1 = 0.0
scroller_tweak_2 = 0.0
scroller_tweak_3 = 5.0
scroller_tweak_4 = 5.0
scroller_tweak_5 = 0.0
scroller_tweak_6 = 0.0
scroller_text_scale = 1.0
scroller_text_speed = 20.0
scroll_scale_factor = 1.0
scroller_pos_x = screen_w
scroller_pos_y = -60

credits_text = "STILL93$A MEGA DEMO BY DIVINE STYLERS AND STYLE$RELEASED AT EVOKE 1993$$GRAPHICS ... BOHEME/STYLE$GRAPHICS ... HELLBEARD/DIVINE STYLERS$$$MUSIC ... SKOPE/DIVINE STYLERS$MUSIC ... GOTO80/DIVINE STYLERS$MUSIC ... REPE/STYLE$$ART DIRECTION ... BOHEME/STYLE$ART DIRECTION ... DMG/DIVINE STYLERS$$$CODE ... CHATGPT V3.5$FREE RESEARCH PREVIEW (MARCH-MAY BUILDS)$$$PROMPT LAMER ... DMG/DIVINE STYLERS$TIMINGS & PARAMS ... DMG/DIVINE STYLERS$CONCEPT & IDEA ... DMG/DIVINE STYLERS$$THE SOURCE CODE WILL SOON BE UP AT$HTTPS://GITHUB.COM/REWTNULL$KEEP YOUR BANANAS AND EYES PEELED!$$-----------------------------------$DIVINE STYLERS 30 YEARS (1993-2023)$-----------------------------------$$-----------------------------------$STYLE-LOVED BY YOUR MOM SINCE 1995!$-----------------------------------$$$BACKWARDS MOTION WITH SHIFT OR ALT?$$"
credits_ctrl_char = "$"
credits_parts = credits_text.split(credits_ctrl_char)
credits_char_spacing = -5
credits_y_spacing = 15
credits_amplitude = 0.0
credits_frequency = 0.0
credits_top_rotation_factor = 0.0
credits_bottom_rotation_factor = 0.0
credits_tweak_1 = 0.0
credits_tweak_2 = 0.0
credits_tweak_3 = 6.0
credits_tweak_4 = 0.0
credits_tweak_5 = 0.0
credits_tweak_6 = 0.0
credits_text_scale = 0.4
credits_text_speed = 7.1
credits_pos_x = screen_w
credits_y_offset = 90
credits_timer_duration = 6.4
credits_center_tolerance = 4
credits_num_lines = 4
credits_pause_triggered = False
credits_timer_triggered = False
credits_pause_done = False
credits_current_index = 0
credits_line_lengths = [len(part) for part in credits_parts]

vertex_shader = """
#version 330
layout (location = 0) in vec4 position;
layout (location = 1) in vec2 positionTexCoord;
out vec2 fragTexcoord;

void main()
{
    gl_Position = position;
    fragTexcoord = positionTexCoord;
}
"""

logo_fragment_shader = """
#version 330
uniform float time;
uniform float pixelSize;
uniform vec2 resolution;
uniform float image_offset_x;
uniform float image_offset_y;
uniform sampler2D text;
uniform float amplitude;
uniform float frequency;
uniform float speed;

in vec2 fragTexcoord;
out vec4 fragColor;

void main()
{
    float x = gl_FragCoord.x;
    float y = gl_FragCoord.y;

    float offset = sin(time * speed + x * frequency) * amplitude;
    float normalizedY = (y + offset) / (resolution.y / 2);
    normalizedY -= image_offset_y;

    vec2 uv = vec2(fragTexcoord.x + image_offset_x, normalizedY);
    vec2 roundedUV = floor(uv * pixelSize) / pixelSize;
    uv = roundedUV;

    vec4 textColor = texture(text, vec2(fragTexcoord.x + image_offset_x, normalizedY));

    fragColor = textColor;
}
"""

plasma_fragment_shader = """
#version 330
out vec4 fragColor;

uniform float time;
uniform float scale;
uniform float turbulence;
uniform float speed;
uniform float pixelSize;
uniform vec2 resolution;
uniform vec2 offset1Direction;
uniform vec2 offset2Direction;
uniform vec2 offset3Direction;

void main()
{
    vec2 uv = (gl_FragCoord.xy - 0.5 * resolution) / min(resolution.x, resolution.y);
    vec2 roundedUV = floor(uv * pixelSize) / pixelSize;
    uv = roundedUV;

    vec2 offset1 = vec2(sin(uv.x * scale + time * speed * offset1Direction.x), sin(uv.y * scale + time * speed * offset1Direction.y)) * turbulence;
    vec2 offset2 = vec2(sin((uv.x + uv.y) * scale + time * speed * offset2Direction.x), sin((uv.x - uv.y) * scale + time * speed * offset2Direction.y)) * turbulence;
    vec2 offset3 = vec2(sin((uv.x - uv.y) * scale + time * speed * offset3Direction.x), sin((uv.x + uv.y) * scale + time * speed * offset3Direction.y)) * turbulence;

    float r = sin(uv.x * scale + offset1.x + offset2.x + offset3.x);
    float g = sin(uv.y * scale + offset1.y + offset2.y + offset3.y);
    float b = sin((uv.x + uv.y) * scale + offset1.x + offset1.y + offset2.x + offset3.y);

    r = floor(r * 8.0) / 8.0;
    g = floor(g * 8.0) / 8.0;
    b = floor(b * 8.0) / 8.0;

    vec3 color = vec3(r, g, b);

    fragColor = vec4(color, 1.0);
}
"""

def compile_shader(shader_source, shader_type):
    shader = glCreateShader(shader_type)
    glShaderSource(shader, shader_source)
    glCompileShader(shader)
    if not glGetShaderiv(shader, GL_COMPILE_STATUS):
        error_message = glGetShaderInfoLog(shader).decode()
        print(f"Shader compilation error:\n{error_message}")
        glDeleteShader(shader)
        return None
    return shader

def create_shader_program(vertex_shader_source, fragment_shader_source):
    vertex_shader = compile_shader(vertex_shader_source, GL_VERTEX_SHADER)
    if vertex_shader is None:
        return None
    fragment_shader = compile_shader(fragment_shader_source, GL_FRAGMENT_SHADER)
    if fragment_shader is None:
        glDeleteShader(vertex_shader)
        return None
    shader_program = glCreateProgram()
    glAttachShader(shader_program, vertex_shader)
    glAttachShader(shader_program, fragment_shader)
    glLinkProgram(shader_program)
    if not glGetProgramiv(shader_program, GL_LINK_STATUS):
        error_message = glGetProgramInfoLog(shader_program).decode()
        print(f"Shader program linking error:\n{error_message}")
        glDeleteProgram(shader_program)
        glDeleteShader(vertex_shader)
        glDeleteShader(fragment_shader)
        return None
    glValidateProgram(shader_program)
    if not glGetProgramiv(shader_program, GL_VALIDATE_STATUS):
        error_message = glGetProgramInfoLog(shader_program).decode()
        print(f"Shader program validation error:\n{error_message}")
        glDeleteProgram(shader_program)
        glDeleteShader(vertex_shader)
        glDeleteShader(fragment_shader)
        return None
    glDetachShader(shader_program, vertex_shader)
    glDetachShader(shader_program, fragment_shader)
    return shader_program

def plasma_uniforms(plasma_shader):
    plasma_time_uniform = glGetUniformLocation(plasma_shader, "time")
    plasma_resolution_uniform = glGetUniformLocation(plasma_shader, "resolution")
    plasma_offset1_direction_uniform = glGetUniformLocation(plasma_shader, "offset1Direction")
    plasma_offset2_direction_uniform = glGetUniformLocation(plasma_shader, "offset2Direction")
    plasma_offset3_direction_uniform = glGetUniformLocation(plasma_shader, "offset3Direction")
    plasma_scale_uniform = glGetUniformLocation(plasma_shader, "scale")
    plasma_turbulence_uniform = glGetUniformLocation(plasma_shader, "turbulence")
    plasma_speed_uniform = glGetUniformLocation(plasma_shader, "speed")
    plasma_pixelsize_uniform = glGetUniformLocation(plasma_shader, "pixelSize")
    return plasma_time_uniform, plasma_resolution_uniform, plasma_offset1_direction_uniform,\
    plasma_offset2_direction_uniform, plasma_offset3_direction_uniform, plasma_scale_uniform,\
    plasma_turbulence_uniform, plasma_speed_uniform, plasma_pixelsize_uniform

def plasma_buffer():
    plasma_vao = glGenVertexArrays(1)
    glBindVertexArray(plasma_vao)
    plasma_verts = [-1, -1, 1, -1, -1, 1, 1, 1]
    plasma_verts = np.array(plasma_verts, dtype=np.float32)
    plasma_vbo = glGenBuffers(1)
    plasma_vbo = np.uint32(plasma_vbo)
    glBindBuffer(GL_ARRAY_BUFFER, plasma_vbo)
    glBufferData(GL_ARRAY_BUFFER, plasma_verts.nbytes, (c_float * plasma_verts.nbytes)(*plasma_verts), GL_DYNAMIC_DRAW)
    plasma_position_loc = glGetAttribLocation(plasma_shader, 'position')
    glEnableVertexAttribArray(plasma_position_loc)
    glVertexAttribPointer(plasma_position_loc, 2, GL_FLOAT, GL_FALSE, 0, None)
    glDisableVertexAttribArray(plasma_position_loc)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    return plasma_vao, plasma_position_loc

def plasma_draw(plasma_shader, plasma_position_loc, plasma_vao, plasma_time, plasma_pixel_size, plasma_turbulence, plasma_scale, plasma_speed, plasma_w, plasma_h, plasma_offset_1x, plasma_offset_1y, plasma_offset_2x, plasma_offset_2y, plasma_offset_3x, plasma_offset_3y):
    glUseProgram(plasma_shader)
    glUniform1f(plasma_time_uniform, pg.time.get_ticks() / plasma_time)
    glUniform1f(plasma_pixelsize_uniform, plasma_pixel_size)
    glUniform1f(plasma_turbulence_uniform, plasma_turbulence)
    glUniform1f(plasma_scale_uniform, plasma_scale)
    glUniform1f(plasma_speed_uniform, plasma_speed)
    glUniform2f(plasma_resolution_uniform, plasma_w, plasma_h)
    glUniform2f(plasma_offset1_direction_uniform, plasma_offset_1x, plasma_offset_1y)
    glUniform2f(plasma_offset2_direction_uniform, plasma_offset_2x, plasma_offset_2y)
    glUniform2f(plasma_offset3_direction_uniform, plasma_offset_3x, plasma_offset_3y)
    glBindVertexArray(plasma_vao)
    glEnableVertexAttribArray(plasma_position_loc)
    glPushMatrix()
    glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)
    glPopMatrix()
    glUseProgram(0)
    glDisableVertexAttribArray(plasma_position_loc)
    glBindVertexArray(0)

def logo_texture(logo_name):
    logo_path = resource_path(logo_name)
    logo = pg.image.load(logo_path).convert_alpha()

    logo_w, logo_h = logo.get_size()
    logo = pg.image.tostring(logo, "RGBA", True)
    return logo, logo_w, logo_h

def logo_buffers(logo, logo_w, logo_h, logo_shader):
    logo_texture_id = glGenTextures(1)
    logo_texture_id = np.uint32(logo_texture_id)
    glBindTexture(GL_TEXTURE_2D, logo_texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, logo_w, logo_h, 0, GL_RGBA, GL_UNSIGNED_BYTE, logo)
    glBindTexture(GL_TEXTURE_2D, 0)
    logo_verts = np.array([-1.0, -1.0, 0.0, 0.0,
                         -1.0, 1.0, 0.0, 0.0,
                         1.0, 1.0, 1.0, 0.0,
                         1.0, -1.0, 1.0, 0.0], dtype=np.float32)
    logo_vao = glGenVertexArrays(1)
    logo_vao = np.uint32(logo_vao)
    glBindVertexArray(logo_vao)
    logo_vbo = glGenBuffers(1)
    logo_vbo = np.uint32(logo_vbo)
    glBindBuffer(GL_ARRAY_BUFFER, logo_vbo)
    glBufferData(GL_ARRAY_BUFFER, logo_verts.nbytes, logo_verts, GL_DYNAMIC_DRAW)
    logo_position = glGetAttribLocation(logo_shader, "position")
    glEnableVertexAttribArray(logo_position)
    glVertexAttribPointer(logo_position, 2, GL_FLOAT, GL_FALSE, 4 * logo_verts.itemsize, None)
    logo_texcoord = glGetAttribLocation(logo_shader, "positionTexCoord")
    glEnableVertexAttribArray(logo_texcoord)
    glVertexAttribPointer(logo_texcoord, 2, GL_FLOAT, GL_FALSE, 4 * logo_verts.itemsize, c_void_p(2 * logo_verts.itemsize))
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glDisableVertexAttribArray(logo_position)
    glDisableVertexAttribArray(logo_texcoord)
    return logo_vao, logo_texture_id, logo_position, logo_texcoord

def logo_uniforms(screen_w, screen_h):
    glUseProgram(logo_shader)
    logo_time_loc = glGetUniformLocation(logo_shader, "time")
    glUniform1f(logo_time_loc, pg.time.get_ticks() / 1000.0)
    logo_offset_x_loc = glGetUniformLocation(logo_shader, "image_offset_x")
    glUniform1f(logo_offset_x_loc, logo_offset_x)
    logo_offset_y_loc = glGetUniformLocation(logo_shader, "image_offset_y")
    glUniform1f(logo_offset_y_loc, logo_offset_y)
    logo_resolution_uniform_loc = glGetUniformLocation(logo_shader, "resolution")
    glUniform2f(logo_resolution_uniform_loc, screen_w, screen_h)
    logo_pixelsize_uniform_loc = glGetUniformLocation(logo_shader, "pixelSize")
    glUniform1f(logo_pixelsize_uniform_loc, logo_pixel_size)
    logo_amplitude_uniform_loc = glGetUniformLocation(logo_shader, "amplitude")
    glUniform1f(logo_amplitude_uniform_loc, logo_amplitude)
    logo_frequency_uniform_loc = glGetUniformLocation(logo_shader, "frequency")
    glUniform1f(logo_frequency_uniform_loc, logo_frequency)
    logo_speed_uniform_loc = glGetUniformLocation(logo_shader, "speed")
    glUniform1f(logo_speed_uniform_loc, logo_speed)
    glUseProgram(0)
    return logo_time_loc, logo_offset_x_loc, logo_offset_y_loc, logo_resolution_uniform_loc,\
    logo_pixelsize_uniform_loc, logo_amplitude_uniform_loc, logo_frequency_uniform_loc,\
    logo_speed_uniform_loc

def logo_draw(logo_shader, logo_time_loc, logo_vao, logo_texture_id, logo_pixelsize_uniform_loc, logo_pixel_size, logo_position, logo_texcoord):
    glEnable(GL_BLEND)
    glUseProgram(logo_shader)
    glUniform1f(logo_time_loc, pg.time.get_ticks() / 1000.0)
    glBindVertexArray(logo_vao)
    glEnableVertexAttribArray(logo_position)
    glEnableVertexAttribArray(logo_texcoord)
    glBindTexture(GL_TEXTURE_2D, logo_texture_id)
    glDrawArrays(GL_QUADS, 0, 4)
    glUniform1f(logo_pixelsize_uniform_loc, logo_pixel_size)
    glDisableVertexAttribArray(logo_position)
    glDisableVertexAttribArray(logo_texcoord)
    glBindTexture(GL_TEXTURE_2D, 0)
    glUseProgram(0)
    glDisable(GL_BLEND)

def text_font_metrics(num_chars_x, font_char_w, font_char_h):
    font_metrics = {}
    for char_code in range(32, 256):
        char = chr(char_code)
        row = (char_code - 32) // num_chars_x
        col = (char_code - 32) % num_chars_x
        font_metrics[char] = (col * font_char_w, row * font_char_h)
    return font_metrics

def text_effects_verts_and_coords(text, pos_x, pos_y, font_metrics, amplitude, frequency, text_scale, char_spacing, top_rotation_factor, bottom_rotation_factor, tweak_1, tweak_2, tweak_3, tweak_4, tweak_5, tweak_6, font_atlas_w, font_atlas_h, font_char_w, font_char_h):
    verts = []
    coords = []
    for i, char in enumerate(text):
        font_char_x_position, font_char_y_position = font_metrics.get(char, (0, 0))
        tex_left = font_char_x_position / font_atlas_w
        tex_right = (font_char_x_position + font_char_w) / font_atlas_w
        tex_bottom = font_char_y_position / font_atlas_h
        tex_top = (font_char_y_position + font_char_h) / font_atlas_h
        char_pos_x = pos_x + i * (font_char_w * text_scale + char_spacing)
        char_pos_y = pos_y + sin(char_pos_x * frequency) * amplitude
        top_rotation_angle = cos(char_pos_x * frequency) * top_rotation_factor
        bottom_rotation_angle = sin(char_pos_x * frequency) * bottom_rotation_factor
        corners = np.array([[0, 0],
                            [font_char_w * text_scale + tweak_1, 0],
                            [font_char_w * text_scale + tweak_2, font_char_h * text_scale + tweak_3],
                            [0, font_char_h * text_scale + tweak_4]])
        center = np.array([font_char_w * text_scale + tweak_5 / 2, font_char_h * text_scale + tweak_6 / 2])
        rotated_corners = corners - center
        top_rotation_matrix = np.array([[cos(radians(top_rotation_angle)), -sin(radians(top_rotation_angle))],
                                        [sin(radians(top_rotation_angle)), cos(radians(top_rotation_angle))]])
        bottom_rotation_matrix = np.array([[cos(radians(bottom_rotation_angle)), -sin(radians(bottom_rotation_angle))],
                                           [sin(radians(bottom_rotation_angle)), cos(radians(bottom_rotation_angle))]])
        rotated_top_corners = np.dot(rotated_corners[:2], top_rotation_matrix.T)
        rotated_bottom_corners = np.dot(rotated_corners[2:], bottom_rotation_matrix.T)
        rotated_corners = np.concatenate((rotated_top_corners, rotated_bottom_corners)) + center
        verts.extend([char_pos_x + rotated_corners[0, 0], char_pos_y + rotated_corners[0, 1],
                         char_pos_x + rotated_corners[1, 0], char_pos_y + rotated_corners[1, 1],
                         char_pos_x + rotated_corners[2, 0], char_pos_y + rotated_corners[2, 1],
                         char_pos_x + rotated_corners[3, 0], char_pos_y + rotated_corners[3, 1]])
        coords.extend([tex_left, tex_bottom, tex_right, tex_bottom, tex_right, tex_top, tex_left, tex_top])
    verts = np.array(verts, dtype=np.float32)
    coords = np.array(coords, dtype=np.float32)
    vbo = glGenBuffers(1)
    vbo = np.uint32(vbo)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, verts.nbytes + coords.nbytes, None, GL_DYNAMIC_DRAW)
    glBufferSubData(GL_ARRAY_BUFFER, 0, verts.nbytes, verts)
    glBufferSubData(GL_ARRAY_BUFFER, verts.nbytes, coords.nbytes, coords)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    return vbo, verts.nbytes, verts.size

def font_texture():
    font_atlas_img_path = resource_path('resources/boheme-still93_font_white.png')
    font_atlas_surf = pg.image.load(font_atlas_img_path).convert_alpha()
    font_atlas_w, font_atlas_h = font_atlas_surf.get_size()
    font_atlas = pg.image.tostring(font_atlas_surf, "RGBA")
    font_char_w, font_char_h = 50, 50
    num_chars_x = font_atlas_w // font_char_w
    num_chars_y = font_atlas_w // font_char_h
    font_atlas_id = glGenTextures(1)
    font_atlas_id = np.uint32(font_atlas_id)
    glBindTexture(GL_TEXTURE_2D, font_atlas_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, font_atlas_w, font_atlas_h, 0, GL_RGBA, GL_UNSIGNED_BYTE, font_atlas)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glBindTexture(GL_TEXTURE_2D, 0)
    return font_atlas_id, font_atlas_w, font_atlas_h, font_char_w, font_char_h,\
    num_chars_x, num_chars_y

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

font_atlas_id, font_atlas_w, font_atlas_h, font_char_w, font_char_h, num_chars_x, num_chars_y = font_texture()
font_metrics = text_font_metrics(num_chars_x, font_char_w, font_char_h)

compile_shader(vertex_shader, GL_VERTEX_SHADER)
compile_shader(plasma_fragment_shader, GL_FRAGMENT_SHADER)
plasma_shader = create_shader_program(vertex_shader, plasma_fragment_shader)

glUseProgram(plasma_shader)
plasma_vao, plasma_position_loc = plasma_buffer()
plasma_time_uniform, plasma_resolution_uniform, plasma_offset1_direction_uniform,\
plasma_offset2_direction_uniform, plasma_offset3_direction_uniform, plasma_scale_uniform,\
plasma_turbulence_uniform, plasma_speed_uniform, plasma_pixelsize_uniform = plasma_uniforms(plasma_shader)
glUseProgram(0)

compile_shader(vertex_shader, GL_VERTEX_SHADER)
compile_shader(logo_fragment_shader, GL_FRAGMENT_SHADER)
logo_shader = create_shader_program(vertex_shader, logo_fragment_shader)

glUseProgram(logo_shader)
logo, logo_w, logo_h = logo_texture("resources/boheme-still93_final.png")
logo_vao, logo_texture_id, logo_position, logo_texcoord = logo_buffers(logo, logo_w, logo_h, logo_shader)
logo_time_loc, logo_offset_x_loc, logo_offset_y_loc, logo_resolution_uniform_loc,\
logo_pixelsize_uniform_loc, logo_amplitude_uniform_loc, logo_frequency_uniform_loc,\
logo_speed_uniform_loc = logo_uniforms(screen_w, screen_h)
glUseProgram(0)

fx_timer_events = {
    (None, pg.K_3): 28200,
    (None, pg.K_2): 30700,
    (None, pg.K_1): 30700,
    (None, pg.K_4): 30700,
    (None, pg.K_5): 30700,
    (None, pg.K_6): 30700,
}
fx_timer_index = 0
fx_timer_delay = 1800
fx_timer_event = pg.USEREVENT + 1
last_fx = False

key_held_shift = False
key_held_alt = False

clock = pg.time.Clock()
pg.time.set_timer(fx_timer_event, fx_timer_delay)
pg.key.set_repeat(80)

MEGA = True
while MEGA:

    clock.tick(30)
    pg.display.set_caption(str(int(clock.get_fps())))
    logo_current_time = pg.time.get_ticks() - logo_end_time

    for event in pg.event.get():
        if event.type == pg.QUIT:
            MEGA = False
        elif event.type == fx_timer_event:
            fx_qualifier_keys = list(fx_timer_events.keys())
            if fx_timer_index < len(fx_qualifier_keys):
                qualifier_key, target_key = fx_qualifier_keys[fx_timer_index]
                fx_timer_delay = fx_timer_events[(qualifier_key, target_key)]
                if (qualifier_key is None) or (qualifier_key == pg.key.get_mods() & qualifier_key):
                    pg.event.post(pg.event.Event(pg.KEYDOWN, key=target_key))
                    pg.event.post(pg.event.Event(pg.KEYUP, key=target_key))
                    fx_timer_index = (fx_timer_index + 1) % len(fx_qualifier_keys)
                    pg.time.set_timer(fx_timer_event, fx_timer_delay)
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                print(f"Something Wonderful Has Happened!")
                MEGA = False
            elif event.key == pg.K_LSHIFT or event.key == pg.K_RSHIFT:
                key_held_shift = True
            elif event.key == pg.K_LALT or event.key == pg.K_RALT:
                key_held_alt = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_LSHIFT or event.key == pg.K_RSHIFT:
                key_held_shift = False
            elif event.key == pg.K_LALT or event.key == pg.K_RALT:
                key_held_alt = False
        if key_held_alt:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    print("plasma_offset_3x +", plasma_offset_3x)
                    plasma_offset_3x += 0.1
                elif event.key == pg.K_LEFT:
                    print("plasma_offset_3x -", plasma_offset_3x)
                    plasma_offset_3x -= 0.1
                elif event.key == pg.K_UP:
                    print("plasma_offset_3y +", plasma_offset_3y)
                    plasma_offset_3y += 0.1
                elif event.key == pg.K_DOWN:
                    print("plasma_offset_3y -", plasma_offset_3y)
                    plasma_offset_3y -= 0.1
        elif key_held_shift:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    print("plasma_offset_2x +", plasma_offset_2x)
                    plasma_offset_2x += 0.1
                elif event.key == pg.K_LEFT:
                    print("plasma_offset_2x -", plasma_offset_2x)
                    plasma_offset_2x -= 0.1
                elif event.key == pg.K_UP:
                    print("plasma_offset_2y +", plasma_offset_2y)
                    plasma_offset_2y += 0.1
                elif event.key == pg.K_DOWN:
                    print("plasma_offset_2y -", plasma_offset_2y)
                    plasma_offset_2y -= 0.1
                elif event.key == pg.K_SPACE:
                    print("plasma_pixel_size -", plasma_pixel_size)
                    plasma_pixel_size -= 4
                elif event.key == pg.K_z:
                    print("plasma_time -", plasma_time)
                    if plasma_time <= 1000.0:
                       plasma_time -= 2000
                    plasma_time -= 1000
                elif event.key == pg.K_x:
                    print("plasma_turbulence -", plasma_turbulence)
                    plasma_turbulence -= 4
                elif event.key == pg.K_c:
                    print("plasma_scale -", plasma_scale)
                    plasma_scale -= 4
                elif event.key == pg.K_v:
                    print("plasma_speed -", plasma_speed)
                    plasma_speed -= 0.1
                elif event.key == pg.K_b:
                    print("plasma_w -", plasma_w)
                    plasma_w -= 1
                elif event.key == pg.K_n:
                    print("plasma_h -", plasma_h)
                    plasma_h -= 1
        else:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    print("plasma_offset_1x +", plasma_offset_1x)
                    plasma_offset_1x += 0.1
                elif event.key == pg.K_LEFT:
                    print("plasma_offset_1x -", plasma_offset_1x)
                    plasma_offset_1x -= 0.1
                elif event.key == pg.K_UP:
                    print("plasma_offset_1y +", plasma_offset_1y)
                    plasma_offset_1y += 0.1
                elif event.key == pg.K_DOWN:
                    print("plasma_offset_1y -", plasma_offset_1y)
                    plasma_offset_1y -= 0.1
                elif event.key == pg.K_SPACE:
                    print("plasma_pixel_size +", plasma_pixel_size)
                    plasma_pixel_size += 2
                elif event.key == pg.K_z:
                    print("plasma_time +", plasma_time)
                    plasma_time += 1000
                elif event.key == pg.K_x:
                    print("plasma_turbulence +", plasma_turbulence)
                    plasma_turbulence += 2
                elif event.key == pg.K_c:
                    print("plasma_scale +", plasma_scale)
                    plasma_scale += 2
                elif event.key == pg.K_v:
                    print("plasma_speed +", plasma_speed)
                    plasma_speed += 0.1
                elif event.key == pg.K_b:
                    print("plasma_w +", plasma_w)
                    plasma_w += 1
                elif event.key == pg.K_n:
                    print("plasma_h +", plasma_h)
                    plasma_h += 1
                elif event.key == pg.K_1:
                    plasma_time = 20000.0
                    plasma_pixel_size = 100.0
                    plasma_turbulence = 20.0
                    plasma_scale = 8.0
                    plasma_speed = 1.1
                    plasma_w = screen_w
                    plasma_h = screen_h
                    plasma_offset_1x = 1.2
                    plasma_offset_1y = 0.0
                    plasma_offset_2x = 1.2
                    plasma_offset_2y = 2.3
                    plasma_offset_3x = 0.6
                    plasma_offset_3y = -0.0
                elif event.key == pg.K_2:
                    plasma_time = -426000.0
                    plasma_pixel_size = 100
                    plasma_turbulence = -4.0
                    plasma_scale = 14
                    plasma_speed = 5.399999999999528
                    plasma_w = screen_w
                    plasma_h = screen_h
                    plasma_offset_1x = 43.300000000000345
                    plasma_offset_1y = 8.199999999999987
                    plasma_offset_2x = 1.3
                    plasma_offset_2y = 2.4
                    plasma_offset_3x = 0.7
                    plasma_offset_3y = 0.1
                elif event.key == pg.K_3:
                    plasma_time = -427000.0
                    plasma_pixel_size = 100
                    plasma_turbulence = 1.0
                    plasma_scale = 52.0
                    plasma_speed = 51.8
                    plasma_w = screen_w
                    plasma_h = screen_h
                    plasma_speed = 55.60000000000005
                    plasma_offset_1x = 5.099999999999998
                    plasma_offset_1y = 2.1000000000000005
                    plasma_offset_2x = 1.3
                    plasma_offset_2y = 2.9000000000000004
                    plasma_offset_3x = 0.7
                    plasma_offset_3y = 0.1
                elif event.key == pg.K_4:
                    plasma_time = -425000.0
                    plasma_pixel_size = 184
                    plasma_turbulence = 7.0
                    plasma_scale = 38.0
                    plasma_speed = 51.8
                    plasma_w = screen_w
                    plasma_h = screen_h
                    plasma_offset_1x = 5.099999999999998
                    plasma_offset_1y = 1.9000000000000006
                    plasma_offset_2x = 1.3
                    plasma_offset_2y = 2.4
                    plasma_offset_3x = 0.7
                    plasma_offset_3y = 0.1
                elif event.key == pg.K_5:
                    plasma_time = -425000.0
                    plasma_pixel_size = 114
                    plasma_turbulence = -5.0
                    plasma_scale = -4.0
                    plasma_speed = 47.09999999999993
                    plasma_w = screen_w
                    plasma_h = screen_h
                    plasma_offset_1x = 5.399999999999997
                    plasma_offset_1y = 2.2000000000000006
                    plasma_offset_2x = 1.3
                    plasma_offset_2y = 2.4
                    plasma_offset_3x = 0.7
                    plasma_offset_3y = 0.1
                elif event.key == pg.K_6:
                    plasma_time = -425000.0
                    plasma_pixel_size = 114
                    plasma_turbulence = 311.0
                    plasma_scale = 4.0
                    plasma_speed = 6.399999999999524
                    plasma_w = screen_w
                    plasma_h = screen_h
                    plasma_offset_1x = 5.399999999999997
                    plasma_offset_1y = 2.2000000000000006
                    plasma_offset_2x = 1.3
                    plasma_offset_2y = 2.4
                    plasma_offset_3x = 0.7
                    plasma_offset_3y = 0.1

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    plasma_draw(plasma_shader,
        plasma_position_loc,
        plasma_vao, plasma_time,
        plasma_pixel_size, plasma_turbulence,
        plasma_scale, plasma_speed,
        plasma_w, plasma_h,
        plasma_offset_1x, plasma_offset_1y,
        plasma_offset_2x, plasma_offset_2y,
        plasma_offset_3x, plasma_offset_3y
    )

    glPushMatrix()
    logo_draw(logo_shader, logo_time_loc, logo_vao, logo_texture_id, logo_pixelsize_uniform_loc, logo_pixel_size, logo_position, logo_texcoord)
    glPopMatrix()

    if logo_trigger:
        if logo_pixel_size < 50:
            logo_pixel_size += 0.5
        elif logo_pixel_size >= 50 and logo_pixel_size < 800:
            logo_pixel_size += 2.5
        elif logo_pixel_size >= 800:
            logo = False
            logo_current_time = 0
    else:
        if logo_pixel_size > 0:
            logo_pixel_size -= 1.5

    scroller_vbo, scroller_verts_nbytes, scroller_verts_size = text_effects_verts_and_coords(
        scroll_text,
        scroller_pos_x, scroller_pos_y,
        font_metrics,
        scroller_amplitude, scroller_frequency,
        scroller_text_scale,
        scroller_char_spacing,
        scroller_top_rotation_factor, scroller_bottom_rotation_factor,
        scroller_tweak_1, scroller_tweak_2,
        scroller_tweak_3, scroller_tweak_4,
        scroller_tweak_5, scroller_tweak_6,
        font_atlas_w,font_atlas_h,
        font_char_w, font_char_h
    )

    glPushMatrix()
    glTranslate(0.0, screen_h, 0.0)
    glColor4f(131.0/255, 206.0/255, 227.0/255, 255.0/255)
    text_draw(scroller_vbo, font_atlas_id, scroller_verts_size, scroller_verts_nbytes)
    glPopMatrix()

    scroller_pos_x -= scroller_text_speed
    if scroller_pos_x + len(scroll_text) * (font_char_w * scroller_text_scale + scroller_char_spacing + (font_char_w // 30)) < 0:
        scroller_pos_x = screen_w

    credits_pos_y = (screen_h - 3 * (font_char_h * credits_text_scale + credits_tweak_4)) / 2
    credits_pos_y = credits_pos_y + credits_y_offset

    for i in range(credits_num_lines):
        credits_index = (credits_current_index + i) % len(credits_parts)
        credits_part = credits_parts[credits_index]

        credits_vbo, credits_verts_nbytes, credits_verts_size = text_effects_verts_and_coords(
            credits_part,
            credits_pos_x, credits_pos_y, font_metrics,
            credits_amplitude, credits_frequency,
            credits_text_scale, credits_char_spacing,
            credits_top_rotation_factor, credits_bottom_rotation_factor,
            credits_tweak_1, credits_tweak_2, credits_tweak_3,
            credits_tweak_4, credits_tweak_5, credits_tweak_6,
            font_atlas_w, font_atlas_h, font_char_w, font_char_h
        )

        glPushMatrix()
        glColor4f(1.0, 1.0, 1.0, 1.0)
        text_draw(credits_vbo, font_atlas_id, credits_verts_size, credits_verts_nbytes)
        glPopMatrix()

        credits_pos_y += font_char_h * credits_text_scale + credits_tweak_4 + credits_y_spacing
    credits_pos_x -= credits_text_speed

    if credits_pos_x + (max(credits_line_lengths[credits_current_index:credits_current_index+credits_num_lines]) if i == credits_num_lines-1 else max(credits_line_lengths[(credits_current_index + 1) % len(credits_parts):(credits_current_index + credits_num_lines+1) % len(credits_parts)])) * (font_char_w * credits_text_scale + credits_char_spacing) < 0:
        credits_pos_x = screen_w
        credits_current_index = (credits_current_index + credits_num_lines) % len(credits_parts)
        credits_line_lengths = [len(part) for part in credits_parts]
    credits_longest_line = len(max(credits_parts[credits_current_index:credits_current_index + credits_num_lines], key=len))

    if not credits_pause_triggered and not credits_pause_done:
        pause_position = credits_pos_x + (credits_longest_line * (font_char_w * credits_text_scale + credits_char_spacing)) // 2 - screen_w // 2
        if abs(pause_position) <= credits_center_tolerance:
            credits_pause_speed = credits_text_speed
            credits_text_speed = 0
            start_time = time()
            credits_pause_triggered = True
    if credits_pause_triggered:
        elapsed_time = time() - start_time
        if elapsed_time >= credits_timer_duration:
            credits_text_speed = credits_pause_speed
            credits_pause_triggered = False
            credits_pause_done = True
    else:
        credits_pause_done = False
    if credits_current_index == 0:
        credits_pause_done = False

    pg.display.flip()

glDeleteBuffers(1, [scroller_vbo, credits_vbo])
glDeleteVertexArrays(1, [logo_vao, plasma_vao])
glDeleteTextures(1, [logo_texture_id, font_atlas_id])
glUseProgram(0)
glDeleteProgram(plasma_shader)

pg.quit()
sys.exit()
