from still93_runtime_hooker import MEGA06
MEGA6 = MEGA06()
### GLOBAL
screen_w = MEGA6.screen_w
screen_h = MEGA6.screen_h
screen = MEGA6.screen
pg = MEGA6.pg
np = MEGA6.np
os = MEGA6.os
sys = MEGA6.sys
c_void_p = MEGA6.c_void_p
c_float = MEGA6.c_float
resource_path = MEGA6.resource_path
glEnable = MEGA6.glEnable
glDisable = MEGA6.glDisable
glBlendFunc = MEGA6.glBlendFunc
glClearDepth = MEGA6.glClearDepth
glClearColor = MEGA6.glClearColor
glClear = MEGA6.glClear
glViewport = MEGA6.glViewport
glMatrixMode = MEGA6.glMatrixMode
glLoadIdentity = MEGA6.glLoadIdentity
glGenBuffers = MEGA6.glGenBuffers
glBindBuffer = MEGA6.glBindBuffer
glBufferData = MEGA6.glBufferData
glBufferSubData = MEGA6.glBufferSubData
glDeleteBuffers = MEGA6.glDeleteBuffers
glGenTextures = MEGA6.glGenTextures
glBindTexture = MEGA6.glBindTexture
glDeleteTextures = MEGA6.glDeleteTextures
glTexImage2D = MEGA6.glTexImage2D
glTexParameteri = MEGA6.glTexParameteri
glDrawArrays = MEGA6.glDrawArrays
glPushMatrix = MEGA6.glPushMatrix
glPopMatrix = MEGA6.glPopMatrix
GL_COLOR_BUFFER_BIT = MEGA6.GL_COLOR_BUFFER_BIT
GL_DEPTH_BUFFER_BIT = MEGA6.GL_DEPTH_BUFFER_BIT
GL_PROJECTION = MEGA6.GL_PROJECTION
GL_MODELVIEW = MEGA6.GL_MODELVIEW
GL_ARRAY_BUFFER = MEGA6.GL_ARRAY_BUFFER
GL_TEXTURE_2D = MEGA6.GL_TEXTURE_2D
GL_RGBA = MEGA6.GL_RGBA
GL_UNSIGNED_BYTE = MEGA6.GL_UNSIGNED_BYTE
GL_FLOAT = MEGA6.GL_FLOAT
GL_TEXTURE_MIN_FILTER = MEGA6.GL_TEXTURE_MIN_FILTER
GL_TEXTURE_MAG_FILTER = MEGA6.GL_TEXTURE_MAG_FILTER
GL_LINEAR = MEGA6.GL_LINEAR
### LOCAL
compileProgram = MEGA6.compileProgram
compileShader = MEGA6.compileShader
glDeleteProgram = MEGA6.glDeleteProgram
glUseProgram = MEGA6.glUseProgram
glOrtho = MEGA6.glOrtho
glUniform1i = MEGA6.glUniform1i
glUniform1f = MEGA6.glUniform1f
glGetUniformLocation = MEGA6.glGetUniformLocation
glGenVertexArrays = MEGA6.glGenVertexArrays
glBindVertexArray = MEGA6.glBindVertexArray
glDeleteVertexArrays = MEGA6.glDeleteVertexArrays
glGetAttribLocation = MEGA6.glGetAttribLocation
glEnableVertexAttribArray = MEGA6.glEnableVertexAttribArray
glDisableVertexAttribArray = MEGA6.glDisableVertexAttribArray
glVertexAttribPointer = MEGA6.glVertexAttribPointer
glActiveTexture = MEGA6.glActiveTexture
GL_FALSE = MEGA6.GL_FALSE
GL_SRC_ALPHA = MEGA6.GL_SRC_ALPHA
GL_ONE_MINUS_SRC_ALPHA = MEGA6.GL_ONE_MINUS_SRC_ALPHA
GL_BLEND = MEGA6.GL_BLEND
GL_VERTEX_SHADER = MEGA6.GL_VERTEX_SHADER
GL_FRAGMENT_SHADER = MEGA6.GL_FRAGMENT_SHADER
GL_TEXTURE_WRAP_S = MEGA6.GL_TEXTURE_WRAP_S
GL_TEXTURE_WRAP_T = MEGA6.GL_TEXTURE_WRAP_T
GL_CLAMP_TO_EDGE = MEGA6.GL_CLAMP_TO_EDGE
GL_DYNAMIC_DRAW = MEGA6.GL_DYNAMIC_DRAW
GL_TEXTURE0 = MEGA6.GL_TEXTURE0
GL_QUADS = MEGA6.GL_QUADS

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

vertex_shader = """
#version 330 core

layout (location = 0) in vec4 position;
layout (location = 1) in vec2 positionTexCoord;

out vec2 fragTexcoord;

void main()
{
    gl_Position = position;
    fragTexcoord = positionTexCoord;
}
"""

fragment_shader_fade_in = """
#version 330 core

in vec2 fragTexcoord;
uniform sampler2D texture_sampler;
uniform float fade_value;

out vec4 frag_color;

void main()
{
    vec4 tex_color = texture(texture_sampler, fragTexcoord);
    frag_color = vec4(tex_color.rgb, tex_color.a * fade_value);
}
"""

fragment_shader_breaking = """
#version 330 core

in vec2 fragTexcoord;
uniform sampler2D texture_sampler;
uniform float time;
uniform float duration;
uniform float screen_w;
uniform float screen_h;

out vec4 frag_color;

float random(vec2 st) {
    return fract(sin(dot(st.xy, vec2(12.9898, 78.233))) * 43758.5453123);
}

void main() {
    vec2 st = gl_FragCoord.xy / vec2(screen_w, screen_h);

    float progress = smoothstep(0.0, duration, time);

    const float numSquares = 16.0;
    vec2 squareSize = vec2(1.0 / numSquares);

    vec2 coords = floor(fragTexcoord / squareSize) * squareSize;
    vec2 center = coords + squareSize * 0.5;

    float r = random(floor(coords)) * 0.3;

    float distance = max(abs(center.x - fragTexcoord.x), abs(center.y - fragTexcoord.y));
    float mask = smoothstep(progress - r, progress + r, distance);

    vec4 background_color = vec4(0.0, 0.0, 0.0, 1.0);
    // vec4 background_color = vec4(0.47058823529411764, 0.6862745098039216, 0.7647058823529411, 1.0);

    vec4 tex_color = texture(texture_sampler, fragTexcoord);
    frag_color = mix(background_color, tex_color, mask);
}
"""

glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
glClearDepth(1.0)
glClearColor(0.0, 0.0, 0.0, 0.0)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

def compile_shader(vertex_shader, fragment_shader):
    shader = compileProgram(
        compileShader(vertex_shader, GL_VERTEX_SHADER),
        compileShader(fragment_shader, GL_FRAGMENT_SHADER)
    )
    return shader

def logo_texture(logo_name):
    logo_path = logo_name
    logo = pg.image.load(logo_path).convert_alpha()
    logo_w, logo_h = logo.get_size()
    logo = pg.image.tostring(logo, "RGBA", True)
    logo_texture_id = glGenTextures(1)
    logo_texture_id = np.uint32(logo_texture_id)
    glBindTexture(GL_TEXTURE_2D, logo_texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, logo_w, logo_h, 0, GL_RGBA, GL_UNSIGNED_BYTE, logo)
    glBindTexture(GL_TEXTURE_2D, 0)
    return logo_texture_id

def logo_buffers(logo_shader):
    glUseProgram(logo_shader)
    logo_vao = glGenVertexArrays(1)
    glBindVertexArray(logo_vao)

    logo_verts = np.array([-1.0, -1.0, 0.0, 0.0,
                           -1.0,  1.0, 0.0, 1.0,
                            1.0,  1.0, 1.0, 1.0,
                            1.0, -1.0, 1.0, 0.0], dtype=np.float32)

    logo_vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, logo_vbo)
    glBufferData(GL_ARRAY_BUFFER, logo_verts.nbytes, logo_verts, GL_DYNAMIC_DRAW)

    logo_verts_loc = glGetAttribLocation(logo_shader, "position")
    glEnableVertexAttribArray(logo_verts_loc)
    glVertexAttribPointer(logo_verts_loc, 2, GL_FLOAT, GL_FALSE, 4 * logo_verts.itemsize, None)

    logo_coords_loc = glGetAttribLocation(logo_shader, "positionTexCoord")
    glEnableVertexAttribArray(logo_coords_loc)
    glVertexAttribPointer(logo_coords_loc, 2, GL_FLOAT, GL_FALSE, 4 * logo_verts.itemsize, c_void_p(2 * logo_verts.itemsize))

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)
    glUseProgram(0)
    return logo_vao, logo_vbo

def merge_vbos(vbo1, vbo2, logo_shader):
    glUseProgram(logo_shader)
    merged_vao = glGenVertexArrays(1)
    glBindVertexArray(merged_vao)

    glBindBuffer(GL_ARRAY_BUFFER, vbo1)

    logo1_verts_loc = glGetAttribLocation(logo_shader, "position")
    glEnableVertexAttribArray(logo1_verts_loc)
    glVertexAttribPointer(logo1_verts_loc, 2, GL_FLOAT, GL_FALSE, 4 * np.float32().itemsize, None)
    logo1_coords_loc = glGetAttribLocation(logo_shader, "positionTexCoord")
    glEnableVertexAttribArray(logo1_coords_loc)
    glVertexAttribPointer(logo1_coords_loc, 2, GL_FLOAT, GL_FALSE, 4 * np.float32().itemsize, c_void_p(2 * np.float32().itemsize))

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    glBindBuffer(GL_ARRAY_BUFFER, vbo1)

    logo2_verts_loc = glGetAttribLocation(logo_shader, "position")
    glEnableVertexAttribArray(logo2_verts_loc)
    glVertexAttribPointer(logo2_verts_loc, 2, GL_FLOAT, GL_FALSE, 4 * np.float32().itemsize, None)
    logo2_coords_loc = glGetAttribLocation(logo_shader, "positionTexCoord")
    glEnableVertexAttribArray(logo2_coords_loc)
    glVertexAttribPointer(logo2_coords_loc, 2, GL_FLOAT, GL_FALSE, 4 * np.float32().itemsize, c_void_p(2 * np.float32().itemsize))

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    glUseProgram(0)
    glDeleteBuffers(1, [ice_cube_vbo, ice_ice_baby_vbo])

    return merged_vao

fade_in_shader = compile_shader(vertex_shader, fragment_shader_fade_in)
breaking_shader = compile_shader(vertex_shader, fragment_shader_breaking)

ice_cube_texture_id = logo_texture(resource_path('resources/boheme-ice_cube_in_ice_cube.jpg'))
ice_cube_vao, ice_cube_vbo = logo_buffers(fade_in_shader)

ice_ice_baby_texture_id = logo_texture(resource_path('resources/boheme-still93_ice_ice_baby.png'))
ice_ice_baby_vao, ice_ice_baby_vbo = logo_buffers(fade_in_shader)

ice_ice_vao = merge_vbos(ice_cube_vbo, ice_ice_baby_vbo, breaking_shader)

fade_duration = 4.0
texture2_delay = 8.0
breaking_start_time = 12.0
breaking_duration = 16.0
texture2_fade_time = None
breaking_effect_time = None
texture1_show_time = True
end_delay = 3

clock = pg.time.Clock()
start_time = pg.time.get_ticks() / 1000.0

MEGA = True
while MEGA:
    clock.tick(30)
    current_time = pg.time.get_ticks() / 1000.0

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                print(f"Something Wonderful Has Happened!")
                pg.quit()
                sys.exit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    elapsed_time = current_time - start_time
    fade_value_texture1 = min(1.0, elapsed_time / fade_duration)

    if texture1_show_time:
        glUseProgram(fade_in_shader)
        glUniform1i(glGetUniformLocation(fade_in_shader, "texture_sampler"), 0)
        glUniform1f(glGetUniformLocation(fade_in_shader, "fade_value"), fade_value_texture1)
        glEnable(GL_BLEND)
        glEnable(GL_TEXTURE_2D)
        glActiveTexture(GL_TEXTURE0)
        glBindVertexArray(ice_cube_vao)
        glBindTexture(GL_TEXTURE_2D, ice_cube_texture_id)
        glDrawArrays(GL_QUADS, 0, 4)
        glBindVertexArray(0)
        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_BLEND)
        glDisable(GL_TEXTURE_2D)
        glUseProgram(0)

    if elapsed_time >= texture2_delay and texture2_fade_time is None:
        texture2_fade_time = current_time

    if texture2_fade_time:
        time_since_texture2_fade = current_time - texture2_fade_time
        fade_value_texture2 = min(1.0, time_since_texture2_fade / fade_duration)
        glUseProgram(fade_in_shader)
        glUniform1i(glGetUniformLocation(fade_in_shader, "texture_sampler"), 0)
        glUniform1f(glGetUniformLocation(fade_in_shader, "fade_value"), fade_value_texture2)
        glEnable(GL_BLEND)
        glEnable(GL_TEXTURE_2D)
        glActiveTexture(GL_TEXTURE0)
        glBindVertexArray(ice_ice_baby_vao)
        glBindTexture(GL_TEXTURE_2D, ice_ice_baby_texture_id)
        glDrawArrays(GL_QUADS, 0, 4)
        glBindVertexArray(0)
        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_BLEND)
        glDisable(GL_TEXTURE_2D)
        glUseProgram(0)

    if texture2_fade_time and breaking_effect_time is None:
        time_since_texture2_fade = current_time - texture2_fade_time
        if time_since_texture2_fade >= breaking_start_time - texture2_delay:
            breaking_effect_time = current_time
            texture2_fade_time = False
            texture1_show_time = False

    if breaking_effect_time:
        breaking_time = current_time - breaking_effect_time - (breaking_start_time - texture2_delay)
        glUseProgram(breaking_shader)
        glUniform1i(glGetUniformLocation(breaking_shader, "texture_sampler"), 0)
        glUniform1f(glGetUniformLocation(breaking_shader, 'time'), breaking_time)
        glUniform1f(glGetUniformLocation(breaking_shader, 'duration'), breaking_duration)
        glUniform1f(glGetUniformLocation(breaking_shader, 'screen_w'), screen_w)
        glUniform1f(glGetUniformLocation(breaking_shader, 'screen_h'), screen_h)
        glEnable(GL_BLEND)
        glEnable(GL_TEXTURE_2D)
        glActiveTexture(GL_TEXTURE0)
        glBindVertexArray(ice_ice_vao)
        glBindTexture(GL_TEXTURE_2D, ice_cube_texture_id)
        glDrawArrays(GL_QUADS, 0, 4)
        glBindTexture(GL_TEXTURE_2D, ice_ice_baby_texture_id)
        glDrawArrays(GL_QUADS, 0, 4)
        glBindVertexArray(0)
        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_BLEND)
        glDisable(GL_TEXTURE_2D)
        glUseProgram(0)

        if breaking_time >= fade_duration + end_delay:
            break

    pg.display.flip()

glBindBuffer(GL_ARRAY_BUFFER, 0)
glBindVertexArray(0)
glDeleteVertexArrays(1, [ice_cube_vao, ice_ice_baby_vao, ice_ice_vao])
glDeleteTextures(1, [ice_cube_texture_id, ice_ice_baby_texture_id])
glUseProgram(0)
glDeleteProgram(fade_in_shader)
glDeleteProgram(breaking_shader)
