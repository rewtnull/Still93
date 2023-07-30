from still93_runtime_hooker import MEGA04
MEGA4 = MEGA04()
### GLOBAL
screen_w = MEGA4.screen_w
screen_h = MEGA4.screen_h
screen = MEGA4.screen
pg = MEGA4.pg
np = MEGA4.np
os = MEGA4.os
sys = MEGA4.sys
c_void_p = MEGA4.c_void_p
c_float = MEGA4.c_float
resource_path = MEGA4.resource_path
glEnable = MEGA4.glEnable
glDisable = MEGA4.glDisable
glBlendFunc = MEGA4.glBlendFunc
glClearDepth = MEGA4.glClearDepth
glClearColor = MEGA4.glClearColor
glClear = MEGA4.glClear
glViewport = MEGA4.glViewport
glMatrixMode = MEGA4.glMatrixMode
glLoadIdentity = MEGA4.glLoadIdentity
glGenBuffers = MEGA4.glGenBuffers
glBindBuffer = MEGA4.glBindBuffer
glBufferData = MEGA4.glBufferData
glBufferSubData = MEGA4.glBufferSubData
glDeleteBuffers = MEGA4.glDeleteBuffers
glGenTextures = MEGA4.glGenTextures
glBindTexture = MEGA4.glBindTexture
glDeleteTextures = MEGA4.glDeleteTextures
glDeleteVertexArrays = MEGA4.glDeleteVertexArrays
glTexImage2D = MEGA4.glTexImage2D
glTexParameteri = MEGA4.glTexParameteri
glDrawArrays = MEGA4.glDrawArrays
glPushMatrix = MEGA4.glPushMatrix
glPopMatrix = MEGA4.glPopMatrix
GL_COLOR_BUFFER_BIT = MEGA4.GL_COLOR_BUFFER_BIT
GL_DEPTH_BUFFER_BIT = MEGA4.GL_DEPTH_BUFFER_BIT
GL_DYNAMIC_DRAW = MEGA4.GL_DYNAMIC_DRAW
GL_PROJECTION = MEGA4.GL_PROJECTION
GL_MODELVIEW = MEGA4.GL_MODELVIEW
GL_ARRAY_BUFFER = MEGA4.GL_ARRAY_BUFFER
GL_TEXTURE_2D = MEGA4.GL_TEXTURE_2D
GL_RGBA = MEGA4.GL_RGBA
GL_UNSIGNED_BYTE = MEGA4.GL_UNSIGNED_BYTE
GL_FLOAT = MEGA4.GL_FLOAT
GL_TEXTURE_MIN_FILTER = MEGA4.GL_TEXTURE_MIN_FILTER
GL_TEXTURE_MAG_FILTER = MEGA4.GL_TEXTURE_MAG_FILTER
GL_LINEAR = MEGA4.GL_LINEAR
### LOCAL
time = MEGA4.time
Timer = MEGA4.Timer
glDepthFunc = MEGA4.glDepthFunc
glDepthMask = MEGA4.glDepthMask
glColorPointer = MEGA4.glColorPointer
glNormalPointer = MEGA4.glNormalPointer
glRotatef = MEGA4.glRotatef
glLightfv  = MEGA4.glLightfv
glFogfv = MEGA4.glFogfv
glFogf = MEGA4.glFogf
gluPerspective = MEGA4.gluPerspective
glTranslatef = MEGA4.glTranslatef
glVertexPointer = MEGA4.glVertexPointer
glEnableClientState = MEGA4.glEnableClientState
glDisableClientState = MEGA4.glDisableClientState
glScalef = MEGA4.glScalef
glOrtho = MEGA4.glOrtho
glTexCoordPointer = MEGA4.glTexCoordPointer
glColor4f = MEGA4.glColor4f
glIndexPointer = MEGA4.glIndexPointer
glHint = MEGA4.glHint
glDrawElements = MEGA4.glDrawElements
compileProgram = MEGA4.compileProgram
compileShader = MEGA4.compileShader
glDeleteProgram = MEGA4.glDeleteProgram
glUseProgram = MEGA4.glUseProgram
glGenVertexArrays = MEGA4.glGenVertexArrays
glBindVertexArray = MEGA4.glBindVertexArray
glGetAttribLocation = MEGA4.glGetAttribLocation
glEnableVertexAttribArray = MEGA4.glEnableVertexAttribArray
glDisableVertexAttribArray = MEGA4.glDisableVertexAttribArray
glVertexAttribPointer = MEGA4.glVertexAttribPointer
glGetUniformLocation = MEGA4.glGetUniformLocation
glUniform1f = MEGA4.glUniform1f
glUniform2f = MEGA4.glUniform2f
GL_VERTEX_SHADER = MEGA4.GL_VERTEX_SHADER
GL_FRAGMENT_SHADER = MEGA4.GL_FRAGMENT_SHADER
GL_TEXTURE_WRAP_S = MEGA4.GL_TEXTURE_WRAP_S
GL_TEXTURE_WRAP_T = MEGA4.GL_TEXTURE_WRAP_T
GL_CLAMP_TO_EDGE = MEGA4.GL_CLAMP_TO_EDGE
GL_FALSE = MEGA4.GL_FALSE
GL_SRC_ALPHA = MEGA4.GL_SRC_ALPHA
GL_ONE_MINUS_SRC_ALPHA = MEGA4.GL_ONE_MINUS_SRC_ALPHA
GL_BLEND = MEGA4.GL_BLEND
GL_QUADS = MEGA4.GL_QUADS
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
glClearDepth(1.0)
glClearColor(0.0, 0.0, 0.0, 0.0)
glViewport(0, 0, screen_w, screen_h)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

logo_amplitude = 20.0
logo_frequency = 0.01
logo_speed = 1.0
logo_offset_x = 0.0
logo_offset_y = 0.5
logo_pixel_size = 1
logo_trigger = True
logo_end_time = 0

golden_timer_duration = 9

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

raymarching_fragment_shader = """
#version 330

uniform vec2 resolution;
uniform float time;

const int MAX_STEPS = 1000;
const float MAX_DIST = 100.0;
const float EPSILON = 0.02;

struct Sphere {
    vec3 position;
    float radius;
    vec3 color;
};

const int SPHERE_COUNT = 4;
Sphere spheres[SPHERE_COUNT];

struct Light {
    vec3 position;
    vec3 color;
};

const int LIGHT_COUNT = 4;
Light lights[LIGHT_COUNT];

const vec3 FLOOR_COLOR_1 = vec3(1.0, 1.0, 1.0);
const vec3 FLOOR_COLOR_2 = vec3(0.5, 0.0, 0.0);
const float FLOOR_TILE_SIZE = 0.9;

void createScene() {
    spheres[0] = Sphere(vec3(-3.5, 0.1, -4.0), 0.7, vec3(0.0, 0.0, 0.0));
    spheres[1] = Sphere(vec3(-1.0, 0.5, -2.0), 0.5, vec3(0.0, 0.0, 0.0));
    spheres[2] = Sphere(vec3(-0.3, 0.1, -3.0), 0.3, vec3(0.0, 0.0, 0.0));
    spheres[3] = Sphere(vec3(3.5, 3.0, -6.0), 2.0, vec3(0.0, 0.0, 0.0));

    lights[0] = Light(vec3(3.0, 2.0, -5.0), vec3(1.0, 0.0, 0.0));
    lights[1] = Light(vec3(0.0, 3.0, -5.0), vec3(0.0, 1.0, 0.0));
    lights[2] = Light(vec3(-0.0, -2.0, -3.0), vec3(0.0, 0.0, 1.0));
    lights[3] = Light(vec3(-3.0, 9.0, -3.0), vec3(1.0, 1.0, 0.0));
}

float sphereDistance(vec3 p, Sphere sphere) {
    return length(p - sphere.position) - sphere.radius;
}

vec3 getNormal(vec3 p) {
    vec3 epsilon = vec3(EPSILON, 0.0, 0.0);
    vec3 normal = vec3(0.0, 0.0, 0.1);

    for (int j = 0; j < SPHERE_COUNT; j++) {
        vec3 sphereCenter = spheres[j].position;
        float sphereRadius = spheres[j].radius;
        float sphereDist = sphereDistance(p, Sphere(sphereCenter, sphereRadius, vec3(0.0)));

        if (sphereDist < EPSILON) {
            vec3 closestNormal = vec3(
                sphereDistance(p + epsilon.xyy, Sphere(sphereCenter, sphereRadius, vec3(0.0))) - sphereDistance(p - epsilon.xyy, Sphere(sphereCenter, sphereRadius, vec3(0.0))),
                sphereDistance(p + epsilon.yxy, Sphere(sphereCenter, sphereRadius, vec3(0.0))) - sphereDistance(p - epsilon.yxy, Sphere(sphereCenter, sphereRadius, vec3(0.0))),
                sphereDistance(p + epsilon.yyx, Sphere(sphereCenter, sphereRadius, vec3(0.0))) - sphereDistance(p - epsilon.yyx, Sphere(sphereCenter, sphereRadius, vec3(0.0)))
            );

            normal += normalize(closestNormal);
        }
    }

    return normalize(normal);
}

float rayMarch(vec3 origin, vec3 direction) {
    float totalDistance = 1.0;
    for (int i = 0; i < MAX_STEPS; i++) {
        vec3 p = origin + direction * totalDistance;

        // Distance to the floor (y = -1.0)
        float floorDist = p.y + 1.0;
        if (floorDist < EPSILON) {
            return totalDistance;
        }

        // Distance to the spheres
        float minSphereDist = MAX_DIST;
        for (int j = 0; j < SPHERE_COUNT; j++) {
            float sphereDist = sphereDistance(p, spheres[j]);
            minSphereDist = min(minSphereDist, sphereDist);
        }

        if (minSphereDist < EPSILON) {
            return totalDistance;
        }

        totalDistance += min(minSphereDist, floorDist);
        if (totalDistance >= MAX_DIST) {
            return MAX_DIST;
        }
    }
    return MAX_DIST;
}

vec3 calculateLighting(vec3 p, vec3 normal) {
    vec3 ambient = vec3(0.3, 0.2, 0.4);
    vec3 diffuse = vec3(0.0);
    vec3 specular = vec3(0.0);

    for (int i = 0; i < LIGHT_COUNT; i++) {
        vec3 lightDir = normalize(lights[i].position - p);
        float diffuseIntensity = max(dot(normal, lightDir), 0.1);
        diffuse += lights[i].color * diffuseIntensity;

        vec3 reflectionDir = reflect(-lightDir, normal);
        float specularIntensity = pow(max(dot(reflectionDir, normalize(p)), 0.0), 128.0);
        specular += lights[i].color * specularIntensity;
    }

    return ambient + diffuse + specular;
}

void main() {
    createScene();

    vec2 uv = (gl_FragCoord.xy / resolution.xy) * 2.0 - 1.0;
    uv.x *= resolution.x / resolution.y;

    vec3 origin = vec3(0.0, 0.1, 0.9);
    vec3 direction = normalize(vec3(uv, -1.0));

    float distance = rayMarch(origin, direction);
    if (distance >= MAX_DIST) {
        // bg color
        gl_FragColor = vec4(0.0, 0.0, 0.3, 1.0);
        return;
    }

    vec3 hitPoint = origin + direction * distance;

    vec2 floorCoords = floor(hitPoint.xz / FLOOR_TILE_SIZE);
    float floorPattern = mod(floorCoords.x + floorCoords.y, 2.5);
    vec3 floorColor = mix(FLOOR_COLOR_1, FLOOR_COLOR_2, floorPattern);

    vec3 normal = getNormal(hitPoint);
    vec3 color = calculateLighting(hitPoint, normal);

    color = mix(floorColor, color, 0.7);

    gl_FragColor = vec4(color, 0.0);
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

def compile_shader(vertex_shader, fragment_shader):
    shader = compileProgram(
        compileShader(vertex_shader, GL_VERTEX_SHADER),
        compileShader(fragment_shader, GL_FRAGMENT_SHADER)
    )
    return shader

def logo_texture(logo_name):
    logo_path = resource_path(logo_name)
    logo = pg.image.load(logo_path).convert_alpha()
    logo_w, logo_h = logo.get_size()
    logo = pg.image.tostring(logo, "RGBA", True)
    return logo, logo_w, logo_h

def logo_buffers(logo, logo_w, logo_h, logo_shader):
    glUseProgram(logo_shader)
    logo_texture_id = glGenTextures(1)
    logo_texture_id = np.uint32(logo_texture_id)
    glBindTexture(GL_TEXTURE_2D, logo_texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, logo_w, logo_h, 0, GL_RGBA, GL_UNSIGNED_BYTE, logo)
    glBindTexture(GL_TEXTURE_2D, 0)
    logo_vao = glGenVertexArrays(1)
    logo_vao = np.uint32(logo_vao)
    glBindVertexArray(logo_vao)
    logo_verts = np.array([-1.0, -1.0, 0.0, 0.0,
                         -1.0, 1.0, 0.0, 0.0,
                         1.0, 1.0, 1.0, 0.0,
                         1.0, -1.0, 1.0, 0.0], dtype=np.float32)
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
    glUseProgram(0)
    return logo_vao, logo_texture_id, logo_position, logo_texcoord, logo_vbo

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
    glUseProgram(logo_shader)
    glUniform1f(logo_time_loc, pg.time.get_ticks() / 1000.0)
    glBindVertexArray(logo_vao)
    glEnableVertexAttribArray(logo_position)
    glEnableVertexAttribArray(logo_texcoord)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, logo_texture_id)
    glEnable(GL_BLEND)
    glDrawArrays(GL_QUADS, 0, 4)
    glDisable(GL_BLEND)
    glUniform1f(logo_pixelsize_uniform_loc, logo_pixel_size)
    glDisableVertexAttribArray(logo_position)
    glDisableVertexAttribArray(logo_texcoord)
    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)
    glUseProgram(0)

def raymarching_buffer():
    vao = glGenVertexArrays(1)
    vao = np.uint32(vao)
    glBindVertexArray(vao)

    vbo = glGenBuffers(1)
    vbo = np.uint32(vbo)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)

    vertices = np.array([
        -1.0, -1.0, 0.0,
        1.0, -1.0, 0.0,
        1.0, 1.0, 0.0,
        -1.0, 1.0, 0.0
    ], dtype=np.float32)

    normals = np.array([
        0.0, 0.0, 1.0,
        0.0, 0.0, 1.0,
        0.0, 0.0, 1.0,
        0.0, 0.0, 1.0
    ], dtype=np.float32)

    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes + normals.nbytes, None, GL_DYNAMIC_DRAW)
    glBufferSubData(GL_ARRAY_BUFFER, 0, vertices.nbytes, vertices)
    glBufferSubData(GL_ARRAY_BUFFER, vertices.nbytes, normals.nbytes, normals)

    raymarching_position_loc = glGetAttribLocation(raymarching_shader, "position")
    glEnableVertexAttribArray(raymarching_position_loc)
    glVertexAttribPointer(raymarching_position_loc, 3, GL_FLOAT, GL_FALSE, 0, None)
    glDisableVertexAttribArray(raymarching_position_loc)
    glBindVertexArray(0)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glDeleteBuffers(1, vbo)
    return vao, raymarching_position_loc

def raymarching_draw(raymarching_shader, vao, raymarching_position_loc):
    glUseProgram(raymarching_shader)
    glBindVertexArray(vao)
    glEnableVertexAttribArray(raymarching_position_loc)
    glDrawArrays(GL_QUADS, 0, 4)
    glDisableVertexAttribArray(raymarching_position_loc)
    glBindVertexArray(0)
    glUseProgram(0)

logo_shader = compile_shader(vertex_shader, logo_fragment_shader)
glUseProgram(logo_shader)
logo, logo_w, logo_h = logo_texture("resources/boheme-still93_golden_tag.png")
logo_vao, logo_texture_id, logo_position, logo_texcoord, logo_vbo = logo_buffers(logo, logo_w, logo_h, logo_shader)
logo_time_loc, logo_offset_x_loc, logo_offset_y_loc, logo_resolution_uniform_loc,\
    logo_pixelsize_uniform_loc, logo_amplitude_uniform_loc, logo_frequency_uniform_loc,\
    logo_speed_uniform_loc = logo_uniforms(screen_w, screen_h)
glUseProgram(0)

raymarching_shader = compile_shader(vertex_shader, raymarching_fragment_shader)
glUseProgram(raymarching_shader)
raymarching_time_loc = glGetUniformLocation(raymarching_shader, "time")
glUniform1f(raymarching_time_loc, pg.time.get_ticks() / 1000.0)
raymarching_resolution_loc = glGetUniformLocation(raymarching_shader, "resolution")
glUniform2f(raymarching_resolution_loc, screen_w, screen_h)
raymarching_vao, raymarching_position_loc = raymarching_buffer()
glUseProgram(0)
glDeleteBuffers(1, logo_vbo)

clock = pg.time.Clock()
golden_start_time = time()

MEGA = True
while MEGA:
    clock.tick(30)
    pg.display.set_caption(str(int(clock.get_fps())))
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

    glPushMatrix()
    raymarching_draw(raymarching_shader, raymarching_vao, raymarching_position_loc)
    glPopMatrix()

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

    golden_elapsed_time = time() - golden_start_time

    if golden_elapsed_time >= golden_timer_duration:
        break

    pg.display.flip()

glBindBuffer(GL_ARRAY_BUFFER, 0)
glBindVertexArray(0)
glDeleteVertexArrays(1, [logo_vao, raymarching_vao])
glDeleteTextures(1, [logo_texture_id])
glUseProgram(0)
glDeleteProgram(raymarching_shader)
glDeleteProgram(logo_shader)
logo_texcoord = 0
raymarching_shader = 0
logo_shader = 0
