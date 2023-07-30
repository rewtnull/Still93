from still93_runtime_hooker import MEGA02
MEGA2 = MEGA02()
### GLOBAL
screen_w = MEGA2.screen_w
screen_h = MEGA2.screen_h
screen = MEGA2.screen
pg = MEGA2.pg
np = MEGA2.np
os = MEGA2.os
sys = MEGA2.sys
c_void_p = MEGA2.c_void_p
c_float = MEGA2.c_float
resource_path = MEGA2.resource_path
glEnable = MEGA2.glEnable
glDisable = MEGA2.glDisable
glBlendFunc = MEGA2.glBlendFunc
glClearDepth = MEGA2.glClearDepth
glClearColor = MEGA2.glClearColor
glClear = MEGA2.glClear
glViewport = MEGA2.glViewport
glMatrixMode = MEGA2.glMatrixMode
glLoadIdentity = MEGA2.glLoadIdentity
glGenBuffers = MEGA2.glGenBuffers
glBindBuffer = MEGA2.glBindBuffer
glBufferData = MEGA2.glBufferData
glBufferSubData = MEGA2.glBufferSubData
glDeleteBuffers = MEGA2.glDeleteBuffers
glGenTextures = MEGA2.glGenTextures
glBindTexture = MEGA2.glBindTexture
glDeleteTextures = MEGA2.glDeleteTextures
glTexImage2D = MEGA2.glTexImage2D
glTexParameteri = MEGA2.glTexParameteri
glDrawArrays = MEGA2.glDrawArrays
glPushMatrix = MEGA2.glPushMatrix
glPopMatrix = MEGA2.glPopMatrix
GL_COLOR_BUFFER_BIT = MEGA2.GL_COLOR_BUFFER_BIT
GL_DEPTH_BUFFER_BIT = MEGA2.GL_DEPTH_BUFFER_BIT
GL_PROJECTION = MEGA2.GL_PROJECTION
GL_MODELVIEW = MEGA2.GL_MODELVIEW
GL_ARRAY_BUFFER = MEGA2.GL_ARRAY_BUFFER
GL_TEXTURE_2D = MEGA2.GL_TEXTURE_2D
GL_RGBA = MEGA2.GL_RGBA
GL_UNSIGNED_BYTE = MEGA2.GL_UNSIGNED_BYTE
GL_FLOAT = MEGA2.GL_FLOAT
GL_TEXTURE0 = MEGA2.GL_TEXTURE0
GL_TEXTURE_MIN_FILTER = MEGA2.GL_TEXTURE_MIN_FILTER
GL_TEXTURE_MAG_FILTER = MEGA2.GL_TEXTURE_MAG_FILTER
GL_LINEAR = MEGA2.GL_LINEAR
GL_NORMAL_ARRAY = MEGA2.GL_NORMAL_ARRAY
GL_TRIANGLES = MEGA2.GL_TRIANGLES
GL_LIGHTING = MEGA2.GL_LIGHTING
GL_LIGHT0 = MEGA2.GL_LIGHT0
GL_POSITION = MEGA2.GL_POSITION
GL_DIFFUSE = MEGA2.GL_DIFFUSE
GL_AMBIENT= MEGA2.GL_AMBIENT
GL_LIGHT_MODEL_AMBIENT = MEGA2.GL_LIGHT_MODEL_AMBIENT
GL_NORMALIZE = MEGA2.GL_NORMALIZE
GL_COLOR_MATERIAL = MEGA2.GL_COLOR_MATERIAL
GL_FRONT = MEGA2.GL_FRONT
GL_FOG = MEGA2.GL_FOG
GL_FOG_COLOR = MEGA2.GL_FOG_COLOR
GL_FOG_MODE = MEGA2.GL_FOG_MODE
GL_FOG_START = MEGA2.GL_FOG_START
GL_FOG_END = MEGA2.GL_FOG_END
GL_RGB = MEGA2.GL_RGB
GL_POINTS = MEGA2.GL_POINTS
GL_AMBIENT_AND_DIFFUSE = MEGA2.GL_AMBIENT_AND_DIFFUSE
GL_SPECULAR = MEGA2.GL_SPECULAR
GL_EMISSION = MEGA2.GL_EMISSION
GL_SHININESS = MEGA2.GL_SHININESS
GL_TEXTURE_CUBE_MAP = MEGA2.GL_TEXTURE_CUBE_MAP
GL_TEXTURE_CUBE_MAP_POSITIVE_X = MEGA2.GL_TEXTURE_CUBE_MAP_POSITIVE_X
GL_TEXTURE_WRAP_R = MEGA2.GL_TEXTURE_WRAP_R
GL_VERTEX_SHADER = MEGA2.GL_VERTEX_SHADER
GL_FRAGMENT_SHADER = MEGA2.GL_FRAGMENT_SHADER
### LOCAL
pi = MEGA2.pi
sin = MEGA2.sin
cos = MEGA2.cos
radians = MEGA2.radians
atan2 = MEGA2.atan2
tan = MEGA2.tan
atan = MEGA2.atan
degrees = MEGA2.degrees
erf = MEGA2.erf
erfc = MEGA2.erfc
exp = MEGA2.exp
expm1 = MEGA2.expm1
gamma = MEGA2.gamma
lgamma = MEGA2.lgamma
sinh = MEGA2.sinh
cosh = MEGA2.cosh
asinh = MEGA2.asinh
acosh = MEGA2.acosh
log = MEGA2.log
log10 = MEGA2.log10
log1p = MEGA2.log1p
log2 = MEGA2.log2
e = MEGA2.e
pow = MEGA2.pow
sqrt = MEGA2.sqrt
add = MEGA2.add
sub = MEGA2.sub
mul = MEGA2.mul
truediv = MEGA2.truediv
eq = MEGA2.eq
mod = MEGA2.mod
snoise3 = MEGA2.snoise3
uniform = MEGA2.uniform
time = MEGA2.time
Timer = MEGA2.Timer
glColor4fv = MEGA2.glColor4fv
glPointSize = MEGA2.glPointSize
glLightModelfv = MEGA2.glLightModelfv
glColorMaterial = MEGA2.glColorMaterial
glMaterialfv = MEGA2.glMaterialfv
glCreateShader = MEGA2.glCreateShader
glShaderSource = MEGA2.glShaderSource
glCompileShader = MEGA2.glCompileShader
glGetShaderiv = MEGA2.glGetShaderiv
glCreateProgram = MEGA2.glCreateProgram
glAttachShader = MEGA2.glAttachShader
glLinkProgram = MEGA2.glLinkProgram
glGetProgramiv = MEGA2.glGetProgramiv
glValidateProgram = MEGA2.glValidateProgram
glDetachShader = MEGA2.glDetachShader
glActiveTexture = MEGA2.glActiveTexture
glTranslatef = MEGA2.glTranslatef
glVertexPointer = MEGA2.glVertexPointer
glEnableClientState = MEGA2.glEnableClientState
glDisableClientState = MEGA2.glDisableClientState
glDeleteProgram = MEGA2.glDeleteProgram
glUseProgram = MEGA2.glUseProgram
compileProgram = MEGA2.compileProgram
compileShader = MEGA2.compileShader
glDepthFunc = MEGA2.glDepthFunc
glDepthMask = MEGA2.glDepthMask
glColorPointer = MEGA2.glColorPointer
glNormalPointer = MEGA2.glNormalPointer
glRotatef = MEGA2.glRotatef
glLightfv = MEGA2.glLightfv
glFogfv = MEGA2.glFogfv
glFogf = MEGA2.glFogf
gluPerspective = MEGA2.gluPerspective
GL_COMPILE_STATUS = MEGA2.GL_COMPILE_STATUS
GL_VALIDATE_STATUS = MEGA2.GL_VALIDATE_STATUS
GL_LINK_STATUS = MEGA2.GL_LINK_STATUS
GL_TEXTURE_WRAP_S = MEGA2.GL_TEXTURE_WRAP_S
GL_TEXTURE_WRAP_T = MEGA2.GL_TEXTURE_WRAP_T
GL_CLAMP_TO_EDGE = MEGA2.GL_CLAMP_TO_EDGE
GL_FALSE = MEGA2.GL_FALSE
GL_NEAREST = MEGA2.GL_NEAREST
GL_VERTEX_ARRAY = MEGA2.GL_VERTEX_ARRAY
GL_DYNAMIC_DRAW = MEGA2.GL_DYNAMIC_DRAW
GL_DEPTH_TEST = MEGA2.GL_DEPTH_TEST
GL_LEQUAL = MEGA2.GL_LEQUAL
GL_TRUE = MEGA2.GL_TRUE
GL_COLOR_ARRAY = MEGA2.GL_COLOR_ARRAY
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

pg.mixer.init()
pg.mixer.music.load(resource_path('resources/goto80-fucktop4.mod'))
pg.mixer.music.play(-1)

sky_vertex_shader = """
#version 120
varying vec3 tex_coords;

void main()
{
    gl_Position = gl_ProjectionMatrix * gl_ModelViewMatrix * gl_Vertex;
    tex_coords = vec3(gl_Vertex) * vec3(1, 1, -1);
}
"""

sky_fragment_shader = """
#version 330

#extension GL_NV_shadow_samplers_cube : enable

varying vec3 tex_coords;
uniform samplerCube skybox;

void main()
{
    gl_FragColor = textureCube(skybox, tex_coords);
}
"""

LANDSCAPE_SIZE = 1024000
VERTEX_COUNT = 16
SCALE = LANDSCAPE_SIZE / VERTEX_COUNT
AMPLITUDE = 50000.0
fov = 65
min_height = 8000.0
max_height = 450000.0
landscape_edge = 1000.0
outline_color = (0.1, 0.5, 0.1)
outline_thickness = 1.0
MOVEMENT_SPEED = 200.0
TURN_SPEED = 1.0
KEY_REPEAT_RATE = 300
MOUSE_SENSITIVITY = 0.4
move_speed = 0.0
turn_speed = 0.0
camera_pos = [LANDSCAPE_SIZE / 2, min_height, LANDSCAPE_SIZE / 2]
camera_rot = [0.0, 0.0]
num_objects = 4
num_points = 4000
points_radius = 5000.0
point_size = 1.6
object_elasticity = 0.5
object_flatten_factor = 0.5
object1_pos_offset_x = 0.0
object1_pos_offset_y = -0.08
object1_pos_offset_z = 0.0
object2_pos_offset_x = 0.0
object2_pos_offset_y = 0.08
object2_pos_offset_z = 0.0
object3_pos_offset_x = 0.0
object3_pos_offset_y = 0.0
object3_pos_offset_z = 0.0
object4_pos_offset_x = 0.0
object4_pos_offset_y = 0.0
object4_pos_offset_z = 0.0
object1_rotation_angle_x = 0.0
object1_rotation_angle_y = 0.0
object1_rotation_angle_z = 0.0
object1_rotation_x = 0.0
object1_rotation_y = -0.04
object1_rotation_z =  0.0
object2_rotation_angle_x = 0.0
object2_rotation_angle_y = 0.0
object2_rotation_angle_z = 0.0
object2_rotation_x = 0.0
object2_rotation_y = 0.04
object2_rotation_z =  0.0
object3_rotation_angle_x = 0.0
object3_rotation_angle_y = 0.0
object3_rotation_angle_z = 0.0
object3_rotation_x = 0.01
object3_rotation_y = 1.0
object3_rotation_z = 0.0
object4_rotation_angle_x = 0.0
object4_rotation_angle_y = 0.0
object4_rotation_angle_z = 0.0
object4_rotation_x = -0.01
object4_rotation_y = -1.0
object4_rotation_z = 0.0
object_rotation_speed = 0.05
object_velocity_x = 1.519
object_velocity_y = 0.607
phi_tweak = 3.0
theta_tweak = 1.0
radius_tweak = 1.0
points_tweak_x = 1.0
points_tweak_y = 1.0
points_tweak_z = 1.0
points_size_x = 1.0
points_size_y = 1.0
points_size_z = 1.0
point_color = (1.0, 1.0, 1.0)
object1_color = (1.0, 1.0, 0.0, 0.1)
object2_color = (0.0, 1.0, 0.0, 0.1)
object3_color = (1.0, 0.0, 0.0, 1.0)
object4_color = (0.0, 0.0, 1.0, 1.0)
phi_op = "-"
phi_op_tweak_x = "*"
phi_op_tweak_z = "*"
phi_op_tweak_theta = ""
theta_op = "*"
theta_x = ""
theta_z = ""
math_op_x = "sin"
math_op_z = "sin"
math_op_theta_x = "cos"
math_op_theta_z = "sin"
math_op_radius = ""
math_op_radius_tweak_x = ""
math_op_radius_tweak_z = ""
points_position_x = 0.0
points_position_y = 0.0
points_triggered = False
object_y = 8000
object_pos = [LANDSCAPE_SIZE//2, object_y, LANDSCAPE_SIZE//2]
glClearColor(0.3, 0.2, 0.6, 1.0)
glClearDepth(1.0)
glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LEQUAL)
glDepthMask(GL_TRUE)
glViewport(0, 0, screen_w, screen_h)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(85, (screen_w / screen_h), 0, LANDSCAPE_SIZE + AMPLITUDE * 2)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glPointSize(point_size)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_POSITION, (100.0, 250.0, 100.0, 0.0))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.4, 0.4, 0.4, 0.0))
glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.3, 0.2, 0.0))
glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (0.3, 0.3, 0.0, 0.0))
glEnable(GL_NORMALIZE)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
glMaterialfv(GL_FRONT, GL_SPECULAR, (0.1, 0.0, 0.0, 0.0))
glMaterialfv(GL_FRONT, GL_EMISSION, (0.1, 0.1, 0.1, 0.0))
glMaterialfv(GL_FRONT, GL_SHININESS, 20)
glEnable(GL_FOG)
glFogfv(GL_FOG_COLOR, (0.0, 0.1, 0.0, 1.0))
glFogf(GL_FOG_MODE, GL_LINEAR)
glFogf(GL_FOG_START, AMPLITUDE)
glFogf(GL_FOG_END, AMPLITUDE * 8)

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

def generate_normal_map(height_map, VERTEX_COUNT, SCALE):
    normal_map = np.zeros((VERTEX_COUNT + 1, VERTEX_COUNT + 1, 3), dtype=np.float32)
    for i in range(VERTEX_COUNT + 1):
        for j in range(VERTEX_COUNT + 1):
            x = i * SCALE
            z = j * SCALE
            dX = (height_map[min(i+1, VERTEX_COUNT)][j] - height_map[max(i-1, 0)][j]) / (2 * SCALE)
            dZ = (height_map[i][min(j+1, VERTEX_COUNT)] - height_map[i][max(j-1, 0)]) / (2 * SCALE)
            normal = np.array([-dX, 1, -dZ])
            normal /= np.linalg.norm(normal)
            normal_map[i][j] = normal
    normals = np.zeros((VERTEX_COUNT * VERTEX_COUNT * 6, 3), dtype=np.float32)
    normal_index = 0
    for i in range(VERTEX_COUNT):
        for j in range(VERTEX_COUNT):
            normal1 = normal_map[i][j]
            normal2 = normal_map[i + 1][j]
            normal3 = normal_map[i][j + 1]
            normal4 = normal_map[i + 1][j + 1]
            normals[normal_index] = normal1
            normals[normal_index + 1] = normal2
            normals[normal_index + 2] = normal3
            normals[normal_index + 3] = normal2
            normals[normal_index + 4] = normal4
            normals[normal_index + 5] = normal3
            normal_index += 6
    return normals

def generate_landscape_height_map(VERTEX_COUNT, AMPLITUDE):
    height_map = np.zeros((VERTEX_COUNT + 1, VERTEX_COUNT + 1), dtype=np.float32)
    for i in range(VERTEX_COUNT + 1):
        for j in range(VERTEX_COUNT + 1):
            height = snoise3(i / VERTEX_COUNT, j / VERTEX_COUNT, 0.0)
            height_map[i][j] = height * AMPLITUDE
    return height_map

def generate_landscape(height_map, VERTEX_COUNT, SCALE):
    landscape = np.zeros((VERTEX_COUNT + 1, VERTEX_COUNT + 1, 3), dtype=np.float32)
    for i in range(VERTEX_COUNT + 1):
        for j in range(VERTEX_COUNT + 1):
            x = i * SCALE
            y = height_map[i][j]
            z = j * SCALE
            landscape[i][j] = np.array([x, y, z])
    vertices = np.zeros((VERTEX_COUNT * VERTEX_COUNT * 6, 3), dtype=np.float32)
    vertex_index = 0
    for i in range(VERTEX_COUNT):
        for j in range(VERTEX_COUNT):
            vertex1 = landscape[i][j]
            vertex2 = landscape[i + 1][j]
            vertex3 = landscape[i][j + 1]
            vertex4 = landscape[i + 1][j + 1]
            vertices[vertex_index] = vertex1
            vertices[vertex_index + 1] = vertex2
            vertices[vertex_index + 2] = vertex3
            vertices[vertex_index + 3] = vertex2
            vertices[vertex_index + 4] = vertex4
            vertices[vertex_index + 5] = vertex3
            vertex_index += 6
    return vertices

def generate_landscape_colors(heights, VERTEX_COUNT, SCALE, AMPLITUDE):
    colors = np.zeros((VERTEX_COUNT + 1, VERTEX_COUNT + 1, 3), dtype=np.float32)
    for i in range(VERTEX_COUNT + 1):
        for j in range(VERTEX_COUNT + 1):
            x = i * SCALE
            z = j * SCALE
            if heights[i][j] < AMPLITUDE * 0.1:
                color = np.array([0.1, 0.1, 0.3])
            elif heights[i][j] > AMPLITUDE * 0.8:
                color = np.array([0.1, 0.2, 0.1])
            else:
                green = uniform(0.1, 0.3)
                color = np.array([0.1, green, 0.1])
            colors[i][j] = color
    vertex_colors = np.zeros((VERTEX_COUNT * VERTEX_COUNT * 6, 3), dtype=np.float32)
    vertex_index = 0
    for i in range(VERTEX_COUNT):
        for j in range(VERTEX_COUNT):
            color1 = colors[i][j]
            color2 = colors[i + 1][j]
            color3 = colors[i][j + 1]
            color4 = colors[i + 1][j + 1]
            vertex_colors[vertex_index] = color1
            vertex_colors[vertex_index + 1] = color2
            vertex_colors[vertex_index + 2] = color3
            vertex_colors[vertex_index + 3] = color2
            vertex_colors[vertex_index + 4] = color4
            vertex_colors[vertex_index + 5] = color3
            vertex_index += 6
    return vertex_colors

def generate_landscape_buffers(vertices, colors, normal_map):
    vbo_data_size = vertices.nbytes + colors.nbytes
    verts_vbo = glGenBuffers(1)
    verts_vbo = np.uint32(verts_vbo)
    glBindBuffer(GL_ARRAY_BUFFER, verts_vbo)
    glBufferData(GL_ARRAY_BUFFER, vbo_data_size, None, GL_DYNAMIC_DRAW)
    glBufferSubData(GL_ARRAY_BUFFER, 0, vertices.nbytes, vertices)
    glBufferSubData(GL_ARRAY_BUFFER, vertices.nbytes, colors.nbytes, colors)
    normals_vbo = glGenBuffers(1)
    normals_vbo = np.uint32(normals_vbo)
    glBindBuffer(GL_ARRAY_BUFFER, normals_vbo)
    glBufferData(GL_ARRAY_BUFFER, normal_map.nbytes, normal_map, GL_DYNAMIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    return verts_vbo, normals_vbo

phi_ops = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": truediv,
    "=": eq,
    "%": mod,
    "atan2": atan2,
    "pow": pow,
    "": None
}

math_ops = {
    "sin": sin,
    "cos": cos,
    "tan": tan,
    "atan": atan,
    "radians": radians,
    "degrees": degrees,
    "erf": erf,
    "erfc": erfc,
    "exp": exp,
    "expm1": expm1,
    "gamma": gamma,
    "lgamma": lgamma,
    "sinh": sinh,
    "cosh": cosh,
    "asinh": asinh,
    "acosh": acosh,
    "log": log,
    "log10": log10,
    "log1p": log1p,
    "log2": log2
}

math_ops_keys = list(math_ops.keys())
phi_ops_keys = list(phi_ops.keys())
math_op_x_key_index = 0
math_op_z_key_index = 0
math_op_theta_x_key_index = 0
math_op_theta_z_key_index = 0
math_op_radius_key_index = 0
math_op_radius_tweak_x_key_index = 0
math_op_radius_tweak_z_key_index = 0
phi_op_key_index = 0
theta_op_key_index = 0
phi_op_tweak_x_key_index = 0
phi_op_tweak_z_key_index = 0
phi_op_tweak_theta_key_index = 0
theta_values_x_key_index = 0
theta_values_z_key_index = 0
if math_op_radius:
    math_op_radius_func = math_ops[math_op_radius]
if math_op_radius_tweak_x:
    math_op_radius_tweak_x_func = math_ops[math_op_radius_tweak_x]
if math_op_radius_tweak_z:
    math_op_radius_tweak_z_func = math_ops[math_op_radius_tweak_z]
math_op_x_func = math_ops[math_op_x]
math_op_z_func = math_ops[math_op_z]
math_op_theta_x_func = math_ops[math_op_theta_x]
math_op_theta_z_func = math_ops[math_op_theta_z]
if phi_op:
    phi_op_func = phi_ops[phi_op]
if theta_op:
    theta_op_func = phi_ops[theta_op]
if phi_op_tweak_theta:
    phi_op_tweak_theta_func = phi_ops[phi_op_tweak_theta]
phi_op_x_func = phi_ops[phi_op_tweak_x]
phi_op_z_func = phi_ops[phi_op_tweak_z]

theta_values = {
    "pi": pi,
    "phi": (1 + sqrt(5)) / 2,
    "euler": e,
    "euler_gamma": np.euler_gamma,
    "catalan": 0.91596,
    "khinchin": 2.6854520010,
    "sqrt2": sqrt(2),
    "": None
}

theta_keys = list(theta_values.keys())
theta_values_x_key_index = 0
theta_values_z_key_index = 0
theta_value_x = theta_values[theta_x]
theta_value_z = theta_values[theta_z]

def generate_points(num_points, points_array):
    phi = pi * phi_op_func(phi_tweak, sqrt(5.0))
    for i in range(num_points):
        y = 1 - (i / float(num_points * points_tweak_y - 1)) * 2
        if phi_op_tweak_theta:
            theta = phi_op_tweak_theta_func(phi, theta_op_func(i, theta_tweak) /2)
        else:
            theta = phi * theta_op_func(i, theta_tweak)
        if math_op_radius:
            radius = sqrt(1 - y * y * math_op_radius_func(pi)) * radius_tweak
        else:
            radius = sqrt(1 - y * y) * radius_tweak
        if phi_op_tweak_x and math_op_radius_tweak_x:
            if theta_x:
                x = math_op_theta_x_func(phi_op_x_func(theta_value_x, theta)) * phi_op_x_func(math_op_radius_tweak_x_func(radius), math_op_x_func(theta_value_x * theta)) * points_tweak_x
            else:
                x = math_op_theta_x_func(theta) * math_op_radius_tweak_x_func(radius) * math_op_x_func(phi_op_x_func(phi, theta)) * points_tweak_x
        else:
            x = math_op_theta_x_func(theta) * radius * math_op_x_func(phi * theta) * points_tweak_x
        if phi_op_tweak_z and math_op_radius_tweak_z:
            if theta_z:
                if theta_z:
                    z = math_op_theta_z_func(phi_op_z_func(theta_value_z, theta)) * phi_op_z_func(math_op_radius_tweak_z_func(radius), math_op_z_func(theta_value_z * theta)) * points_tweak_z
            else:
                z = math_op_theta_z_func(theta) * math_op_radius_tweak_z_func(radius) * math_op_z_func(phi_op_x_func(phi, theta)) * points_tweak_z
        else:
            z = math_op_theta_z_func(theta) * radius * math_op_z_func(phi * theta) * points_tweak_z
        points_array[i] = [x, y, z]
    return points_array

def calculate_point_positions(points, points_radius, points_size_x, points_size_y, points_size_z, point_positions):
    for i, point in enumerate(points):
        point_x = points_radius * point[0] * points_size_x
        point_y = points_radius * point[1] * points_size_y
        point_z = points_radius * point[2] * points_size_z
        point_positions[i] = [point_x, point_y, point_z]
    return point_positions

def update_vbo(point_positions):
    objects_vbo = glGenBuffers(1)
    objects_vbo = np.uint32(objects_vbo)
    glBindBuffer(GL_ARRAY_BUFFER, objects_vbo)
    glBufferData(GL_ARRAY_BUFFER, point_positions.nbytes, point_positions, GL_DYNAMIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    return objects_vbo

def generate_skybox_textures():
    sky_id = glGenTextures(1)
    sky_id = np.uint32(sky_id)
    sky_face_imgs = ["resources/skybox/boheme-left.jpg", "resources/skybox/boheme-right.jpg", "resources/skybox/boheme-top.jpg", "resources/skybox/boheme-bottom.jpg", "resources/skybox/boheme-far.jpg", "resources/skybox/boheme-near.jpg"]
    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_CUBE_MAP, sky_id)
    for i, sky_face in enumerate(sky_face_imgs):
        sky_path = resource_path(sky_face)
        sky_face_image = pg.image.load(sky_path).convert()
        sky_face_width, sky_face_height = sky_face_image.get_size()
        sky_face_surface = pg.image.tostring(sky_face_image, 'RGB')
        glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_X + i, 0, GL_RGB, sky_face_width, sky_face_height, 0, GL_RGB, GL_UNSIGNED_BYTE, sky_face_surface)
    glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_R, GL_CLAMP_TO_EDGE)
    glBindTexture(GL_TEXTURE_CUBE_MAP, 0)
    return sky_id

def generate_skybox_verts():
    sky_right = [1.0, -1.0, -1.0, 1.0, -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0]
    sky_left = [-1.0, -1.0,  1.0, -1.0, -1.0, -1.0, -1.0,  1.0, -1.0, -1.0,  1.0, -1.0, -1.0,  1.0,  1.0, -1.0, -1.0, 1.0]
    sky_top = [-1.0, 1.0, -1.0, 1.0, 1.0, -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0, 1.0, 1.0, -1.0, 1.0, -1.0]
    sky_bottom = [-1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, -1.0, -1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, -1.0, 1.0]
    sky_far = [-1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, -1.0, -1.0, 1.0, -1.0, -1.0, 1.0, 1.0, -1.0, -1.0, 1.0, -1.0]
    sky_near = [-1.0, -1.0, 1.0, -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, 1.0]
    sky_verts = np.array([sky_right, sky_left, sky_top, sky_bottom, sky_far, sky_near], dtype=np.float32).flatten()
    sky_vbo = glGenBuffers(1)
    sky_vbo = np.uint32(sky_vbo)
    glBindBuffer(GL_ARRAY_BUFFER, sky_vbo)
    glBufferData(GL_ARRAY_BUFFER, sky_verts.nbytes, sky_verts, GL_DYNAMIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    return sky_vbo, sky_verts

compile_shader(sky_vertex_shader, GL_VERTEX_SHADER)
compile_shader(sky_fragment_shader, GL_FRAGMENT_SHADER)
sky_shader = create_shader_program(sky_vertex_shader, sky_fragment_shader)
sky_id = generate_skybox_textures()
sky_vbo, sky_verts = generate_skybox_verts()

height_map = generate_landscape_height_map(VERTEX_COUNT, AMPLITUDE)
normal_map = generate_normal_map(height_map, VERTEX_COUNT, SCALE)
landscape = generate_landscape(height_map, VERTEX_COUNT, SCALE)
colors = generate_landscape_colors(height_map, VERTEX_COUNT, SCALE, AMPLITUDE)
verts_vbo, normals_vbo = generate_landscape_buffers(landscape, colors, normal_map)

points_array = np.zeros((num_points, 3), dtype=np.float32)
points = generate_points(num_points, points_array)
positions_array = np.zeros((len(points), 3), dtype=np.float32)
point_positions = calculate_point_positions(points, points_radius, points_size_x, points_size_y, points_size_z, positions_array)
objects_vbo = update_vbo(point_positions)

fx_timer_events = {
    (None, pg.K_q): 7300,
    (None, pg.K_w): 7300,
    (None, pg.K_e): 7000,
    (None, pg.K_r): 6800,
    (None, pg.K_i): 3400,
    (None, pg.K_y): 7400,
    (None, pg.K_u): 3400,
    (None, pg.K_o): 7200,
    (None, pg.K_t): 3400,
    (None, pg.K_p): 7100,
    (None, pg.K_a): 7000,
    (None, pg.K_s): 3500,
    (None, pg.K_d): 7100,
    (None, pg.K_f): 3300,
    (None, pg.K_g): 6700,
    (None, pg.K_h): 7300,
    (None, pg.K_j): 3400,
    (None, pg.K_k): 10500,
    (None, pg.K_l): 14500
}

fx_timer_index = 0
fx_timer_delay = 2000
fx_timer_event = pg.USEREVENT + 1
end_time = 0

clock = pg.time.Clock()
pg.time.set_timer(fx_timer_event, fx_timer_delay)

apocalypse_timer_duration = 125.6
apocalypse_start_time = time()

MEGA = True
while MEGA:
    clock.tick(30)
    pg.display.set_caption(str(int(clock.get_fps())))
    current_time = pg.time.get_ticks() - end_time

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == fx_timer_event:
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
                pg.quit()
                sys.exit()
            elif event.key == pg.K_RETURN:
                MEGA = False
            elif event.key == pg.K_q:
                ############################################
                # Still 93 Points Shape Effect v1.0 Preset #
                ############################################
                num_objects = 4
                num_points = 4000
                point_size = 1.6
                theta_tweak = 35.30000000000023
                radius_tweak = 1.3000000000000003
                phi_tweak = 5.399999999999996
                points_tweak_x = 2.8000000000000016
                points_tweak_y = 1.0
                points_tweak_z = -2.600000000000001
                points_size_x = 0.30000000000000004
                points_size_y = 1.0
                points_size_z = 0.40000000000000013
                object_rotation_speed = 1.2000000000000002
                object1_rotation_angle = 140.0499999999976
                object1_rotation_x = 0.0
                object1_rotation_y = -0.04
                object1_rotation_z = 0.0
                object2_rotation_angle = 140.0499999999976
                object2_rotation_x = 0.0
                object2_rotation_y = 0.04
                object2_rotation_z = 0.0
                object3_rotation_angle = 140.0499999999976
                object3_rotation_x = 0.01
                object3_rotation_y = 1.0
                object3_rotation_z = 0.0
                object4_rotation_angle = 140.0499999999976
                object4_rotation_x = -0.01
                object4_rotation_y = -1.0
                object4_rotation_z = 0.0
                object1_pos_offset_x = 0.0
                object1_pos_offset_y = -0.04
                object1_pos_offset_z = 0.0
                object2_pos_offset_x = 0.0
                object2_pos_offset_y = 0.04
                object2_pos_offset_z = 0.0
                object3_pos_offset_x = 0.01
                object3_pos_offset_y = 1.0
                object3_pos_offset_z = 0.0
                object4_pos_offset_x = -0.01
                object4_pos_offset_y = -1.0
                object4_pos_offset_z = 0.0
                object1_color = (1.0, 1.0, 0.0, 0.1)
                object2_color = (0.5, 0.5, 0.5, 0.1)
                object3_color = (1.0, 0.3, 0.0, 1.0)
                object4_color = (0.0, 0.4, 1.0, 1.0)
                camera_rot = [-57.19999999999995, 75.0]
                camera_pos = [736737.2295894534, 85319.65754349764, 681444.3102982284]
                object_pos = [739655.9497142502, 45000.2870105, 681433.9581796791]
                math_op_x = "sin"
                math_op_z = "sin"
                math_op_theta_x = "cos"
                math_op_theta_z = "sin"
                math_op_radius = "erf"
                math_op_radius_tweak_x = ""
                math_op_radius_tweak_z = ""
                phi_op = "-"
                phi_op_tweak_x = ""
                phi_op_tweak_z = ""
                phi_op_tweak_theta = ""
                theta_op = "*"
                theta_x = ""
                theta_z = ""
                math_op_x_func = math_ops[math_op_x]
                math_op_z_func = math_ops[math_op_z]
                math_op_theta_x_func = math_ops[math_op_theta_x]
                math_op_theta_z_func = math_ops[math_op_theta_z]
                if math_op_radius:
                    math_op_radius_func = math_ops[math_op_radius]
                if math_op_radius_tweak_x:
                    math_op_radius_tweak_x_func = math_ops[math_op_radius_tweak_x]
                if math_op_radius_tweak_z:
                    math_op_radius_tweak_z_func = math_ops[math_op_radius_tweak_z]
                if phi_op:
                    phi_op_func = phi_ops[phi_op]
                if phi_op_tweak_theta:
                    phi_op_tweak_theta_func = phi_ops[phi_op_tweak_theta]
                if theta_op:
                    theta_op_func = phi_ops[theta_op]
                theta_value_x = theta_values[theta_x]
                theta_value_z = theta_values[theta_z]
                points_triggered = True
                ##############
                # End Preset #
                ##############
            elif event.key == pg.K_w:
                ############################################
                # Still 93 Points Shape Effect v1.0 Preset #
                ############################################
                num_objects = 4
                num_points = 2700
                point_size = 1.6
                theta_tweak = 3.200000000000002
                radius_tweak = 0.9
                phi_tweak = 7.299999999999989
                points_tweak_x = 0.8
                points_tweak_y = 1.0
                points_tweak_z = 0.8
                points_size_x = 1.0
                points_size_y = 1.3000000000000003
                points_size_z = 0.9
                object_rotation_speed = 2.0000000000000013
                object1_rotation_angle = 210.0000000000051
                object1_rotation_x = 0.0
                object1_rotation_y = -0.08
                object1_rotation_z = 0.0
                object2_rotation_angle = 210.0000000000051
                object2_rotation_x = 0.0
                object2_rotation_y = 0.08
                object2_rotation_z = 0.0
                object3_rotation_angle = 210.0000000000051
                object3_rotation_x = 0.04
                object3_rotation_y = 2.0
                object3_rotation_z = 0.0
                object4_rotation_angle = 210.0000000000051
                object4_rotation_x = -0.04
                object4_rotation_y = -2.0
                object4_rotation_z = 0.0
                object1_pos_offset_x = 0.0
                object1_pos_offset_y = -0.08
                object1_pos_offset_z = 0.0
                object2_pos_offset_x = 0.0
                object2_pos_offset_y = 0.08
                object2_pos_offset_z = 0.0
                object3_pos_offset_x = 0.04
                object3_pos_offset_y = 2.0
                object3_pos_offset_z = 0.0
                object4_pos_offset_x = -0.04
                object4_pos_offset_y = -2.0
                object4_pos_offset_z = 0.0
                object1_color = (1.0, 1.0, 1.0, 1.0)
                object2_color = (0.0, 0.0, 1.0, 1.0)
                object3_color = (0.0, 0.0, 1.0, 1.0)
                object4_color = (1.0, 1.0, 1.0, 1.0)
                camera_rot = [-11.199999999999985, -40.0]
                camera_pos = [563083.5143910658, 1704.2628660617936, 684912.2630895384]
                object_pos = [540000.0298459905, 1500.0, 663337.3067660019]
                math_op_x = "sin"
                math_op_z = "sin"
                math_op_theta_x = "cos"
                math_op_theta_z = "sin"
                math_op_radius = "sin"
                math_op_radius_tweak_x = ""
                math_op_radius_tweak_z = ""
                phi_op = "-"
                phi_op_tweak_x = "*"
                phi_op_tweak_z = "*"
                phi_op_tweak_theta = ""
                theta_op = "*"
                theta_x = ""
                theta_z = ""
                math_op_x_func = math_ops[math_op_x]
                math_op_z_func = math_ops[math_op_z]
                math_op_theta_x_func = math_ops[math_op_theta_x]
                math_op_theta_z_func = math_ops[math_op_theta_z]
                if math_op_radius:
                    math_op_radius_func = math_ops[math_op_radius]
                if math_op_radius_tweak_x:
                    math_op_radius_tweak_x_func = math_ops[math_op_radius_tweak_x]
                if math_op_radius_tweak_z:
                    math_op_radius_tweak_z_func = math_ops[math_op_radius_tweak_z]
                if phi_op:
                    phi_op_func = phi_ops[phi_op]
                if phi_op_tweak_theta:
                    phi_op_tweak_theta_func = phi_ops[phi_op_tweak_theta]
                if theta_op:
                    theta_op_func = phi_ops[theta_op]
                theta_value_x = theta_values[theta_x]
                theta_value_z = theta_values[theta_z]
                points_triggered = True
                ##############
                # End Preset #
                ##############
            elif event.key == pg.K_e:
                ############################################
                # Still 93 Points Shape Effect v1.0 Preset #
                ############################################
                num_objects = 4
                num_points = 4000
                point_size = 1.6
                theta_tweak = 3.6000000000000023
                radius_tweak = 1.0
                phi_tweak = 12.99999999999997
                points_tweak_x = 1.5000000000000004
                points_tweak_y = 1.0
                points_tweak_z = 0.9
                points_size_x = 1.1
                points_size_y = 1.4000000000000004
                points_size_z = 1.1
                object_rotation_speed = 1.1500000000000004
                object1_rotation_angle = 81.19999999999753
                object1_rotation_x = 0.0
                object1_rotation_y = -0.04
                object1_rotation_z = 0.0
                object2_rotation_angle = 81.19999999999753
                object2_rotation_x = 0.0
                object2_rotation_y = 0.04
                object2_rotation_z = 0.0
                object3_rotation_angle = 81.19999999999753
                object3_rotation_x = 0.01
                object3_rotation_y = 1.0
                object3_rotation_z = 0.0
                object4_rotation_angle = 81.19999999999753
                object4_rotation_x = -0.01
                object4_rotation_y = -1.0
                object4_rotation_z = 0.0
                object1_pos_offset_x = 0.0
                object1_pos_offset_y = -0.04
                object1_pos_offset_z = 0.0
                object2_pos_offset_x = 0.0
                object2_pos_offset_y = 0.04
                object2_pos_offset_z = 0.0
                object3_pos_offset_x = 0.01
                object3_pos_offset_y = 1.0
                object3_pos_offset_z = 0.0
                object4_pos_offset_x = -0.01
                object4_pos_offset_y = -1.0
                object4_pos_offset_z = 0.0
                object1_color = (1.0, 1.0, 0.0, 0.1)
                object2_color = (0.0, 1.0, 0.0, 0.1)
                object3_color = (0.8, 0.6, 0.6, 1.0)
                object4_color = (0.0, 0.0, 1.0, 1.0)
                camera_rot = [-5.999999999999995, -55.0]
                camera_pos = [75219.62932610043, 86376.44085689932, 152037.2007814974]
                object_pos = [50152.25796193534, 47214.8282627755, 142503.18818378414]
                math_op_x = "sin"
                math_op_z = "atan"
                math_op_theta_x = "cos"
                math_op_theta_z = "sin"
                math_op_radius = ""
                math_op_radius_tweak_x = ""
                math_op_radius_tweak_z = ""
                phi_op = "-"
                phi_op_tweak_x = "*"
                phi_op_tweak_z = "*"
                phi_op_tweak_theta = ""
                theta_op = "*"
                theta_x = ""
                theta_z = ""
                math_op_x_func = math_ops[math_op_x]
                math_op_z_func = math_ops[math_op_z]
                math_op_theta_x_func = math_ops[math_op_theta_x]
                math_op_theta_z_func = math_ops[math_op_theta_z]
                if math_op_radius:
                    math_op_radius_func = math_ops[math_op_radius]
                if math_op_radius_tweak_x:
                    math_op_radius_tweak_x_func = math_ops[math_op_radius_tweak_x]
                if math_op_radius_tweak_z:
                    math_op_radius_tweak_z_func = math_ops[math_op_radius_tweak_z]
                if phi_op:
                    phi_op_func = phi_ops[phi_op]
                if phi_op_tweak_theta:
                    phi_op_tweak_theta_func = phi_ops[phi_op_tweak_theta]
                if theta_op:
                    theta_op_func = phi_ops[theta_op]
                theta_value_x = theta_values[theta_x]
                theta_value_z = theta_values[theta_z]
                points_triggered = True
                ##############
                # End Preset #
                ##############
            elif event.key == pg.K_r:
                ############################################
                # Still 93 Points Shape Effect v1.0 Preset #
                ############################################
                num_objects = 4
                num_points = 15000
                point_size = 1.4
                theta_tweak = 2.200000000000001
                radius_tweak = 0.8
                phi_tweak = 8.599999999999985
                points_tweak_x = 1.8000000000000007
                points_tweak_y = 3.7000000000000024
                points_tweak_z = -1.7000000000000002
                points_size_x = 6.899999999999992
                points_size_y = 7.299999999999991
                points_size_z = 7.299999999999991
                object_rotation_speed = 0.7499999999999998
                object1_rotation_angle = 350.7000000000452
                object1_rotation_x = 0.0
                object1_rotation_y = -0.04
                object1_rotation_z = 0.0
                object2_rotation_angle = 350.7000000000452
                object2_rotation_x = 0.0
                object2_rotation_y = 0.04
                object2_rotation_z = 0.0
                object3_rotation_angle = 350.7000000000452
                object3_rotation_x = 0.01
                object3_rotation_y = 1.0
                object3_rotation_z = 0.0
                object4_rotation_angle = 350.7000000000452
                object4_rotation_x = -0.01
                object4_rotation_y = -1.0
                object4_rotation_z = 0.0
                object1_pos_offset_x = 0.0
                object1_pos_offset_y = -0.04
                object1_pos_offset_z = 0.0
                object2_pos_offset_x = 0.0
                object2_pos_offset_y = 0.04
                object2_pos_offset_z = 0.0
                object3_pos_offset_x = 0.01
                object3_pos_offset_y = 1.0
                object3_pos_offset_z = 0.0
                object4_pos_offset_x = -0.01
                object4_pos_offset_y = -1.0
                object4_pos_offset_z = 0.0
                object1_color = (0.6, 0.4, 0.5, 0.1)
                object2_color = (0.5, 1.0, 0.0, 0.1)
                object3_color = (0.8, 0.0, 0.8, 1.0)
                object4_color = (0.1, 0.1, 0.8, 1.0)
                camera_rot = [-90.0, -155.0]
                camera_pos = [353023.42892806954, 213508.46500867134, 427302.13957349915]
                object_pos = [351394.10567944037, 123500.5656767803, 427090.66381399846]
                math_op_x = "sin"
                math_op_z = "sin"
                math_op_theta_x = "cos"
                math_op_theta_z = "sin"
                math_op_radius = ""
                math_op_radius_tweak_x = "erfc"
                math_op_radius_tweak_z = "erfc"
                phi_op = "*"
                phi_op_tweak_x = "*"
                phi_op_tweak_z = "*"
                phi_op_tweak_theta = ""
                theta_op = "*"
                theta_x = ""
                theta_z = ""
                math_op_x_func = math_ops[math_op_x]
                math_op_z_func = math_ops[math_op_z]
                math_op_theta_x_func = math_ops[math_op_theta_x]
                math_op_theta_z_func = math_ops[math_op_theta_z]
                if math_op_radius:
                    math_op_radius_func = math_ops[math_op_radius]
                if math_op_radius_tweak_x:
                    math_op_radius_tweak_x_func = math_ops[math_op_radius_tweak_x]
                if math_op_radius_tweak_z:
                    math_op_radius_tweak_z_func = math_ops[math_op_radius_tweak_z]
                if phi_op:
                    phi_op_func = phi_ops[phi_op]
                if phi_op_tweak_theta:
                    phi_op_tweak_theta_func = phi_ops[phi_op_tweak_theta]
                if theta_op:
                    theta_op_func = phi_ops[theta_op]
                theta_value_x = theta_values[theta_x]
                theta_value_z = theta_values[theta_z]
                points_triggered = True
                ##############
                # End Preset #
                ##############
            elif event.key == pg.K_t:
                ############################################
                # Still 93 Points Shape Effect v1.0 Preset #
                ############################################
                num_objects = 4
                num_points = 4000
                point_size = 1.6
                theta_tweak = 99.19999999999864
                radius_tweak = 1.3000000000000003
                phi_tweak = 4.000000000000001
                points_tweak_x = 1.9000000000000008
                points_tweak_y = 1.0
                points_tweak_z = -0.9999999999999998
                points_size_x = 0.5000000000000001
                points_size_y = 1.3000000000000003
                points_size_z = 0.9
                object_rotation_speed = 1.5500000000000007
                object1_rotation_angle = 13293.5499999468
                object1_rotation_x = 0.0
                object1_rotation_y = -0.04
                object1_rotation_z = 0.0
                object2_rotation_angle = 13293.5499999468
                object2_rotation_x = 0.0
                object2_rotation_y = 0.04
                object2_rotation_z = 0.0
                object3_rotation_angle = 13293.5499999468
                object3_rotation_x = 0.01
                object3_rotation_y = 1.0
                object3_rotation_z = 0.0
                object4_rotation_angle = 13293.5499999468
                object4_rotation_x = -0.01
                object4_rotation_y = -1.0
                object4_rotation_z = 0.0
                object1_pos_offset_x = 0.0
                object1_pos_offset_y = -0.04
                object1_pos_offset_z = 0.0
                object2_pos_offset_x = 0.0
                object2_pos_offset_y = 0.04
                object2_pos_offset_z = 0.0
                object3_pos_offset_x = 0.01
                object3_pos_offset_y = 1.0
                object3_pos_offset_z = 0.0
                object4_pos_offset_x = -0.01
                object4_pos_offset_y = -1.0
                object4_pos_offset_z = 0.0
                object1_color = (0.2, 0.7, 0.0, 0.1)
                object2_color = (0.1, 0.0, 0.3, 0.1)
                object3_color = (0.0, 0.4, 0.0, 1.0)
                object4_color = (0.5, 0.9, 0.4, 1.0)
                camera_rot = [-4.399999999999973, 12.0]
                camera_pos = [837794.1952629392, 13168.30847026491, 287335.8818766168]
                object_pos = [855000.407779635, 9000.0, 263332.04117208306]
                math_op_x = "sin"
                math_op_z = "sin"
                math_op_theta_x = "cos"
                math_op_theta_z = "sin"
                math_op_radius = "erf"
                math_op_radius_tweak_x = ""
                math_op_radius_tweak_z = ""
                phi_op = "-"
                phi_op_tweak_x = ""
                phi_op_tweak_z = ""
                phi_op_tweak_theta = ""
                theta_op = "*"
                theta_x = ""
                theta_z = ""
                math_op_x_func = math_ops[math_op_x]
                math_op_z_func = math_ops[math_op_z]
                math_op_theta_x_func = math_ops[math_op_theta_x]
                math_op_theta_z_func = math_ops[math_op_theta_z]
                if math_op_radius:
                    math_op_radius_func = math_ops[math_op_radius]
                if math_op_radius_tweak_x:
                    math_op_radius_tweak_x_func = math_ops[math_op_radius_tweak_x]
                if math_op_radius_tweak_z:
                    math_op_radius_tweak_z_func = math_ops[math_op_radius_tweak_z]
                if phi_op:
                    phi_op_func = phi_ops[phi_op]
                if phi_op_tweak_theta:
                    phi_op_tweak_theta_func = phi_ops[phi_op_tweak_theta]
                if theta_op:
                    theta_op_func = phi_ops[theta_op]
                theta_value_x = theta_values[theta_x]
                theta_value_z = theta_values[theta_z]
                points_triggered = True
                ##############
                # End Preset #
                ##############
            elif event.key == pg.K_y:
                ############################################
                # Still 93 Points Shape Effect v1.0 Preset #
                ############################################
                num_objects = 4
                num_points = 5700
                point_size = 1.6
                theta_tweak = 109.09997299999814
                radius_tweak = 1.3000000000000003
                phi_tweak = 4.000260000000037
                points_tweak_x = 1.9000000000000008
                points_tweak_y = 1.0
                points_tweak_z = -0.9999999999999998
                points_size_x = 0.5000000000000001
                points_size_y = 1.3000000000000003
                points_size_z = 0.9
                object_rotation_speed = 1.2000000000000004
                object1_rotation_angle = 30749.79999969278
                object1_rotation_x = 0.0
                object1_rotation_y = -0.04
                object1_rotation_z = 0.0
                object2_rotation_angle = 30749.79999969278
                object2_rotation_x = 0.0
                object2_rotation_y = 0.04
                object2_rotation_z = 0.0
                object3_rotation_angle = 30749.79999969278
                object3_rotation_x = 0.01
                object3_rotation_y = 1.0
                object3_rotation_z = 0.0
                object4_rotation_angle = 30749.79999969278
                object4_rotation_x = -0.01
                object4_rotation_y = -1.0
                object4_rotation_z = 0.0
                object1_pos_offset_x = 0.0
                object1_pos_offset_y = -0.04
                object1_pos_offset_z = 0.0
                object2_pos_offset_x = 0.0
                object2_pos_offset_y = 0.04
                object2_pos_offset_z = 0.0
                object3_pos_offset_x = 0.01
                object3_pos_offset_y = 1.0
                object3_pos_offset_z = 0.0
                object4_pos_offset_x = -0.01
                object4_pos_offset_y = -1.0
                object4_pos_offset_z = 0.0
                object1_color = (1.0, 1.0, 0.0, 0.1)
                object2_color = (0.0, 1.0, 0.0, 0.1)
                object3_color = (1.0, 0.2, 0.0, 1.0)
                object4_color = (0.4, 0.0, 0.8, 1.0)
                camera_rot = [-28.79999999999999, -20.0]
                camera_pos = [854870.1451946567, 15658.71034976572, 335625.1915631359]
                object_pos = [849000.407779635, 13000.0, 315332.04117208306]
                math_op_x = "cos"
                math_op_z = "atan"
                math_op_theta_x = "tan"
                math_op_theta_z = "sin"
                math_op_radius = "sin"
                math_op_radius_tweak_x = "atan"
                math_op_radius_tweak_z = "cos"
                phi_op = "-"
                phi_op_tweak_x = "+"
                phi_op_tweak_z = ""
                phi_op_tweak_theta = "*"
                theta_op = "+"
                theta_x = "euler_gamma"
                theta_z = ""
                math_op_x_func = math_ops[math_op_x]
                math_op_z_func = math_ops[math_op_z]
                math_op_theta_x_func = math_ops[math_op_theta_x]
                math_op_theta_z_func = math_ops[math_op_theta_z]
                if math_op_radius:
                    math_op_radius_func = math_ops[math_op_radius]
                if math_op_radius_tweak_x:
                    math_op_radius_tweak_x_func = math_ops[math_op_radius_tweak_x]
                if math_op_radius_tweak_z:
                    math_op_radius_tweak_z_func = math_ops[math_op_radius_tweak_z]
                if phi_op:
                    phi_op_func = phi_ops[phi_op]
                if phi_op_tweak_theta:
                    phi_op_tweak_theta_func = phi_ops[phi_op_tweak_theta]
                if theta_op:
                    theta_op_func = phi_ops[theta_op]
                theta_value_x = theta_values[theta_x]
                theta_value_z = theta_values[theta_z]
                points_triggered = True
                ##############
                # End Preset #
                ##############
            elif event.key == pg.K_u:
                ############################################
                # Still 93 Points Shape Effect v1.0 Preset #
                ############################################
                num_objects = 4
                num_points = 5000
                point_size = 1.6
                theta_tweak = 258.4000579999901
                radius_tweak = 1.4500000000000004
                phi_tweak = 6.500001999999992
                points_tweak_x = 3.1000000000000005
                points_tweak_y = 1.0
                points_tweak_z = 0.20000000000000012
                points_size_x = 0.5500000000000002
                points_size_y = 2.6000000000000014
                points_size_z = 1.0
                object_rotation_speed = 1.3500000000000005
                object1_rotation_angle = 7005.950000016722
                object1_rotation_x = 0.0
                object1_rotation_y = -0.04
                object1_rotation_z = 0.0
                object2_rotation_angle = 7005.950000016722
                object2_rotation_x = 0.0
                object2_rotation_y = 0.04
                object2_rotation_z = 0.0
                object3_rotation_angle = 7005.950000016722
                object3_rotation_x = 0.01
                object3_rotation_y = 1.0
                object3_rotation_z = 0.0
                object4_rotation_angle = 7005.950000016722
                object4_rotation_x = -0.01
                object4_rotation_y = -1.0
                object4_rotation_z = 0.0
                object1_pos_offset_x = 0.0
                object1_pos_offset_y = -0.04
                object1_pos_offset_z = 0.0
                object2_pos_offset_x = 0.0
                object2_pos_offset_y = 0.04
                object2_pos_offset_z = 0.0
                object3_pos_offset_x = 0.01
                object3_pos_offset_y = 1.0
                object3_pos_offset_z = 0.0
                object4_pos_offset_x = -0.01
                object4_pos_offset_y = -1.0
                object4_pos_offset_z = 0.0
                object1_color = (0.0, 0.0, 1.0, 1.0)
                object2_color = (0.2, 0.7, 0.7, 1.0)
                object3_color = (0.6, 0.5, 0.9, 1.0)
                object4_color = (0.9, 0.0, 0.0, 1.0)
                camera_rot = [-2.799999999999992, 58.0]
                camera_pos = [812718.5308296032, 41630.55690561261, 334022.7731353334]
                object_pos = [849000.407779635, 21000.0, 317332.04117208306]
                math_op_x = "atan"
                math_op_z = "sin"
                math_op_theta_x = "cos"
                math_op_theta_z = "atan"
                math_op_radius = "erf"
                math_op_radius_tweak_x = "cos"
                math_op_radius_tweak_z = "tan"
                phi_op = ""
                phi_op_tweak_x = "pow"
                phi_op_tweak_z = "+"
                phi_op_tweak_theta = "+"
                theta_op = "+"
                theta_x = "phi"
                theta_z = "euler"
                math_op_x_func = math_ops[math_op_x]
                math_op_z_func = math_ops[math_op_z]
                math_op_theta_x_func = math_ops[math_op_theta_x]
                math_op_theta_z_func = math_ops[math_op_theta_z]
                if math_op_radius:
                    math_op_radius_func = math_ops[math_op_radius]
                if math_op_radius_tweak_x:
                    math_op_radius_tweak_x_func = math_ops[math_op_radius_tweak_x]
                if math_op_radius_tweak_z:
                    math_op_radius_tweak_z_func = math_ops[math_op_radius_tweak_z]
                if phi_op:
                    phi_op_func = phi_ops[phi_op]
                if phi_op_tweak_theta:
                    phi_op_tweak_theta_func = phi_ops[phi_op_tweak_theta]
                if theta_op:
                    theta_op_func = phi_ops[theta_op]
                theta_value_x = theta_values[theta_x]
                theta_value_z = theta_values[theta_z]
                points_triggered = True
                ##############
                # End Preset #
                ##############
            elif event.key == pg.K_i:
                ############################################
                # Still 93 Points Shape Effect v1.0 Preset #
                ############################################
                num_objects = 4
                num_points = 4000
                point_size = 1.6
                theta_tweak = 152.49999999999562
                radius_tweak = 1.2000000000000002
                phi_tweak = 4.000000000000001
                points_tweak_x = 1.9000000000000008
                points_tweak_y = 1.0
                points_tweak_z = -0.9999999999999998
                points_size_x = 0.5000000000000001
                points_size_y = 1.0
                points_size_z = 1.0
                object_rotation_speed = 1.0500000000000003
                object1_rotation_angle = 1106.999999999541
                object1_rotation_x = 0.0
                object1_rotation_y = -0.04
                object1_rotation_z = 0.0
                object2_rotation_angle = 1106.999999999541
                object2_rotation_x = 0.0
                object2_rotation_y = 0.04
                object2_rotation_z = 0.0
                object3_rotation_angle = 1106.999999999541
                object3_rotation_x = 0.01
                object3_rotation_y = 1.0
                object3_rotation_z = 0.0
                object4_rotation_angle = 1106.999999999541
                object4_rotation_x = -0.01
                object4_rotation_y = -1.0
                object4_rotation_z = 0.0
                object1_pos_offset_x = 0.0
                object1_pos_offset_y = -0.04
                object1_pos_offset_z = 0.0
                object2_pos_offset_x = 0.0
                object2_pos_offset_y = 0.04
                object2_pos_offset_z = 0.0
                object3_pos_offset_x = 0.01
                object3_pos_offset_y = 1.0
                object3_pos_offset_z = 0.0
                object4_pos_offset_x = -0.01
                object4_pos_offset_y = -1.0
                object4_pos_offset_z = 0.0
                object1_color = (1.0, 1.0, 0.0, 0.1)
                object2_color = (0.0, 1.0, 0.0, 0.1)
                object3_color = (1.0, 1.0, 0.3, 1.0)
                object4_color = (0.1, 0.8, 0.5, 1.0)
                camera_rot = [-44.800000000000004, -275.0]
                camera_pos = [838374.851300633, 21961.531514874074, 316472.44146569504]
                object_pos = [849000.407779635, 16000.0, 317332.04117208306]
                math_op_x = "sin"
                math_op_z = "sin"
                math_op_theta_x = "cos"
                math_op_theta_z = "sin"
                math_op_radius = "log10"
                math_op_radius_tweak_x = ""
                math_op_radius_tweak_z = ""
                phi_op = "-"
                phi_op_tweak_x = "-"
                phi_op_tweak_z = ""
                phi_op_tweak_theta = "*"
                theta_op = "*"
                theta_x = ""
                theta_z = ""
                math_op_x_func = math_ops[math_op_x]
                math_op_z_func = math_ops[math_op_z]
                math_op_theta_x_func = math_ops[math_op_theta_x]
                math_op_theta_z_func = math_ops[math_op_theta_z]
                if math_op_radius:
                    math_op_radius_func = math_ops[math_op_radius]
                if math_op_radius_tweak_x:
                    math_op_radius_tweak_x_func = math_ops[math_op_radius_tweak_x]
                if math_op_radius_tweak_z:
                    math_op_radius_tweak_z_func = math_ops[math_op_radius_tweak_z]
                if phi_op:
                    phi_op_func = phi_ops[phi_op]
                if phi_op_tweak_theta:
                    phi_op_tweak_theta_func = phi_ops[phi_op_tweak_theta]
                if theta_op:
                    theta_op_func = phi_ops[theta_op]
                theta_value_x = theta_values[theta_x]
                theta_value_z = theta_values[theta_z]
                points_triggered = True
                ##############
                # End Preset #
                ##############
            elif event.key == pg.K_o:
                ############################################
                # Still 93 Points Shape Effect v1.0 Preset #
                ############################################
                num_objects = 1
                num_points = 15000
                point_size = 1.6
                theta_tweak = 4.6000000000000005
                radius_tweak = 1.0
                phi_tweak = 8.099993999999985
                points_tweak_x = 1.0
                points_tweak_y = 1.0
                points_tweak_z = 1.0
                points_size_x = 1.2
                points_size_y = 2.0
                points_size_z = 1.2
                object_rotation_speed = 2.000000000000001
                object1_rotation_angle = 648.4000000000789
                object1_rotation_x = 45.0
                object1_rotation_y = 45.0
                object1_rotation_z = 45.0
                object2_rotation_angle = 648.4000000000789
                object2_rotation_x = 0.0
                object2_rotation_y = 0.04
                object2_rotation_z = 0.0
                object3_rotation_angle = 648.4000000000789
                object3_rotation_x = 0.01
                object3_rotation_y = 1.0
                object3_rotation_z = 0.0
                object4_rotation_angle = 648.4000000000789
                object4_rotation_x = -0.01
                object4_rotation_y = -1.0
                object4_rotation_z = 0.0
                object1_pos_offset_x = 45.0
                object1_pos_offset_y = 45.0
                object1_pos_offset_z = 45.0
                object2_pos_offset_x = 0.0
                object2_pos_offset_y = 0.04
                object2_pos_offset_z = 0.0
                object3_pos_offset_x = 0.01
                object3_pos_offset_y = 1.0
                object3_pos_offset_z = 0.0
                object4_pos_offset_x = -0.01
                object4_pos_offset_y = -1.0
                object4_pos_offset_z = 0.0
                object1_color = (1.0, 0.3, 0.0, 0.1)
                object2_color = (0.0, 1.0, 0.0, 0.1)
                object3_color = (0.8, 0.6, 0.6, 1.0)
                object4_color = (0.0, 0.0, 1.0, 1.0)
                camera_rot = [-6.800000000000001, 115.0]
                camera_pos = [455503.40470627183, 19453.786351586037, 503902.236779424]
                object_pos = [490800, 12200, 512200]
                math_op_x = "atan"
                math_op_z = "sin"
                math_op_theta_x = "cos"
                math_op_theta_z = "atan"
                math_op_radius = "sin"
                math_op_radius_tweak_x = ""
                math_op_radius_tweak_z = ""
                phi_op = "-"
                phi_op_tweak_x = ""
                phi_op_tweak_z = ""
                phi_op_tweak_theta = ""
                theta_op = "*"
                theta_x = ""
                theta_z = ""
                math_op_x_func = math_ops[math_op_x]
                math_op_z_func = math_ops[math_op_z]
                math_op_theta_x_func = math_ops[math_op_theta_x]
                math_op_theta_z_func = math_ops[math_op_theta_z]
                if math_op_radius:
                    math_op_radius_func = math_ops[math_op_radius]
                if math_op_radius_tweak_x:
                    math_op_radius_tweak_x_func = math_ops[math_op_radius_tweak_x]
                if math_op_radius_tweak_z:
                    math_op_radius_tweak_z_func = math_ops[math_op_radius_tweak_z]
                if phi_op:
                    phi_op_func = phi_ops[phi_op]
                if phi_op_tweak_theta:
                    phi_op_tweak_theta_func = phi_ops[phi_op_tweak_theta]
                if theta_op:
                    theta_op_func = phi_ops[theta_op]
                theta_value_x = theta_values[theta_x]
                theta_value_z = theta_values[theta_z]
                points_triggered = True
                ##############
                # End Preset #
                ##############
            elif event.key == pg.K_p:
                ############################################
                # Still 93 Points Shape Effect v1.0 Preset #
                ############################################
                num_objects = 4
                num_points = 7000
                point_size = 1.6
                theta_tweak = 109.09988199999837
                radius_tweak = 1.3000000000000003
                phi_tweak = 3.999963999999996
                points_tweak_x = 2.000000000000001
                points_tweak_y = 1.0
                points_tweak_z = -0.8499999999999996
                points_size_x = 0.6500000000000005
                points_size_y = 1.4000000000000004
                points_size_z = 0.40000000000000013
                object_rotation_speed = 1.6000000000000008
                object1_rotation_angle = 18088.39999987936
                object1_rotation_x = 0.0
                object1_rotation_y = -0.04
                object1_rotation_z = 0.0
                object2_rotation_angle = 18088.39999987936
                object2_rotation_x = 0.0
                object2_rotation_y = 0.04
                object2_rotation_z = 0.0
                object3_rotation_angle = 18088.39999987936
                object3_rotation_x = 0.01
                object3_rotation_y = 1.0
                object3_rotation_z = 0.0
                object4_rotation_angle = 18088.39999987936
                object4_rotation_x = -0.01
                object4_rotation_y = -1.0
                object4_rotation_z = 0.0
                object1_pos_offset_x = 0.0
                object1_pos_offset_y = -0.04
                object1_pos_offset_z = 0.0
                object2_pos_offset_x = 0.0
                object2_pos_offset_y = 0.04
                object2_pos_offset_z = 0.0
                object3_pos_offset_x = 0.01
                object3_pos_offset_y = 1.0
                object3_pos_offset_z = 0.0
                object4_pos_offset_x = -0.01
                object4_pos_offset_y = -1.0
                object4_pos_offset_z = 0.0
                object1_color = (1.0, 1.0, 0.0, 0.1)
                object2_color = (0.0, 1.0, 0.0, 0.1)
                object3_color = (1.0, 0.2, 0.0, 1.0)
                object4_color = (0.4, 0.0, 0.8, 1.0)
                camera_rot = [3.630429290524262e-14, -5.0]
                camera_pos = [845579.8475343416, 14185.064859371338, 338464.5814591517]
                object_pos = [845000.407779635, 7000.0, 317332.04117208306]
                math_op_x = "sin"
                math_op_z = "sin"
                math_op_theta_x = "erf"
                math_op_theta_z = "tan"
                math_op_radius = "erf"
                math_op_radius_tweak_x = "sin"
                math_op_radius_tweak_z = "atan"
                phi_op = "-"
                phi_op_tweak_x = ""
                phi_op_tweak_z = "-"
                phi_op_tweak_theta = "*"
                theta_op = "*"
                theta_x = "catalan"
                theta_z = "catalan"
                math_op_x_func = math_ops[math_op_x]
                math_op_z_func = math_ops[math_op_z]
                math_op_theta_x_func = math_ops[math_op_theta_x]
                math_op_theta_z_func = math_ops[math_op_theta_z]
                if math_op_radius:
                    math_op_radius_func = math_ops[math_op_radius]
                if math_op_radius_tweak_x:
                    math_op_radius_tweak_x_func = math_ops[math_op_radius_tweak_x]
                if math_op_radius_tweak_z:
                    math_op_radius_tweak_z_func = math_ops[math_op_radius_tweak_z]
                if phi_op:
                    phi_op_func = phi_ops[phi_op]
                if phi_op_tweak_theta:
                    phi_op_tweak_theta_func = phi_ops[phi_op_tweak_theta]
                if theta_op:
                    theta_op_func = phi_ops[theta_op]
                theta_value_x = theta_values[theta_x]
                theta_value_z = theta_values[theta_z]
                points_triggered = True
                ##############
                # End Preset #
                ##############
            elif event.key == pg.K_a:
                ############################################
                # Still 93 Points Shape Effect v1.0 Preset #
                ############################################
                num_objects = 4
                num_points = 4000
                point_size = 1.6
                theta_tweak = 218.1999999999919
                radius_tweak = 1.2000000000000002
                phi_tweak = 4.000000000000001
                points_tweak_x = 1.9000000000000008
                points_tweak_y = 1.0
                points_tweak_z = -0.9999999999999998
                points_size_x = 0.30000000000000016
                points_size_y = 1.5000000000000004
                points_size_z = 0.8
                object_rotation_speed = 1.6500000000000008
                object1_rotation_angle = 3968.350000005671
                object1_rotation_x = 0.0
                object1_rotation_y = -0.04
                object1_rotation_z = 0.0
                object2_rotation_angle = 3968.350000005671
                object2_rotation_x = 0.0
                object2_rotation_y = 0.04
                object2_rotation_z = 0.0
                object3_rotation_angle = 3968.350000005671
                object3_rotation_x = 0.01
                object3_rotation_y = 1.0
                object3_rotation_z = 0.0
                object4_rotation_angle = 3968.350000005671
                object4_rotation_x = -0.01
                object4_rotation_y = -1.0
                object4_rotation_z = 0.0
                object1_pos_offset_x = 0.0
                object1_pos_offset_y = -0.04
                object1_pos_offset_z = 0.0
                object2_pos_offset_x = 0.0
                object2_pos_offset_y = 0.04
                object2_pos_offset_z = 0.0
                object3_pos_offset_x = 0.01
                object3_pos_offset_y = 1.0
                object3_pos_offset_z = 0.0
                object4_pos_offset_x = -0.01
                object4_pos_offset_y = -1.0
                object4_pos_offset_z = 0.0
                object1_color = (1.0, 1.0, 1.0, 0.1)
                object2_color = (1.0, 1.0, 1.0, 0.1)
                object3_color = (1.0, 0.0, 0.0, 1.0)
                object4_color = (0.1, 0.0, 1.0, 1.0)
                camera_rot = [-19.999999999999986, 26.0]
                camera_pos = [839568.2157003903, 14279.350464367537, 326229.42860044644]
                object_pos = [849000.407779635, 9000.0, 315332.04117208306]
                math_op_x = "sin"
                math_op_z = "sin"
                math_op_theta_x = "cos"
                math_op_theta_z = "sin"
                math_op_radius = "log10"
                math_op_radius_tweak_x = "cos"
                math_op_radius_tweak_z = "cos"
                phi_op = "*"
                phi_op_tweak_x = ""
                phi_op_tweak_z = ""
                phi_op_tweak_theta = "*"
                theta_op = "*"
                theta_x = ""
                theta_z = ""
                math_op_x_func = math_ops[math_op_x]
                math_op_z_func = math_ops[math_op_z]
                math_op_theta_x_func = math_ops[math_op_theta_x]
                math_op_theta_z_func = math_ops[math_op_theta_z]
                if math_op_radius:
                    math_op_radius_func = math_ops[math_op_radius]
                if math_op_radius_tweak_x:
                    math_op_radius_tweak_x_func = math_ops[math_op_radius_tweak_x]
                if math_op_radius_tweak_z:
                    math_op_radius_tweak_z_func = math_ops[math_op_radius_tweak_z]
                if phi_op:
                    phi_op_func = phi_ops[phi_op]
                if phi_op_tweak_theta:
                    phi_op_tweak_theta_func = phi_ops[phi_op_tweak_theta]
                if theta_op:
                    theta_op_func = phi_ops[theta_op]
                theta_value_x = theta_values[theta_x]
                theta_value_z = theta_values[theta_z]
                points_triggered = True
                ##############
                # End Preset #
                ##############
            elif event.key == pg.K_s:
                ############################################
                # Still 93 Points Shape Effect v1.0 Preset #
                ############################################
                num_objects = 4
                num_points = 8000
                point_size = 1.6
                theta_tweak = 39.20000000000029
                radius_tweak = -0.3999999999999999
                phi_tweak = 9.799999999999981
                points_tweak_x = 3.200000000000002
                points_tweak_y = 1.0
                points_tweak_z = -2.600000000000001
                points_size_x = 0.40000000000000013
                points_size_y = 1.0
                points_size_z = 0.6000000000000001
                object_rotation_speed = 1.800000000000001
                object1_rotation_angle = 433.34999999997996
                object1_rotation_x = 0.0
                object1_rotation_y = -0.04
                object1_rotation_z = 0.0
                object2_rotation_angle = 433.34999999997996
                object2_rotation_x = 0.0
                object2_rotation_y = 0.04
                object2_rotation_z = 0.0
                object3_rotation_angle = 433.34999999997996
                object3_rotation_x = 0.01
                object3_rotation_y = 1.0
                object3_rotation_z = 0.0
                object4_rotation_angle = 433.34999999997996
                object4_rotation_x = -0.01
                object4_rotation_y = -1.0
                object4_rotation_z = 0.0
                object1_pos_offset_x = 0.0
                object1_pos_offset_y = -0.04
                object1_pos_offset_z = 0.0
                object2_pos_offset_x = 0.0
                object2_pos_offset_y = 0.04
                object2_pos_offset_z = 0.0
                object3_pos_offset_x = 0.01
                object3_pos_offset_y = 1.0
                object3_pos_offset_z = 0.0
                object4_pos_offset_x = -0.01
                object4_pos_offset_y = -1.0
                object4_pos_offset_z = 0.0
                object1_color = (1.0, 0.0, 0.0, 1.0)
                object2_color = (0.8, 0.4, 0.0, 1.0)
                object3_color = (0.9, 0.1, 0.0, 1.0)
                object4_color = (0.9, 0.9, 0.0, 1.0)
                camera_rot = [-45.99999999999996, -160.0]
                camera_pos = [852327.1227998008, 6826.908915752626, 313009.78254839]
                object_pos = [849000.407779635, 5600.0, 317332.04117208306]
                math_op_x = "tan"
                math_op_z = "tan"
                math_op_theta_x = "cos"
                math_op_theta_z = "sin"
                math_op_radius = ""
                math_op_radius_tweak_x = ""
                math_op_radius_tweak_z = ""
                phi_op = "atan2"
                phi_op_tweak_x = "*"
                phi_op_tweak_z = "*"
                phi_op_tweak_theta = ""
                theta_op = "-"
                theta_x = ""
                theta_z = ""
                math_op_x_func = math_ops[math_op_x]
                math_op_z_func = math_ops[math_op_z]
                math_op_theta_x_func = math_ops[math_op_theta_x]
                math_op_theta_z_func = math_ops[math_op_theta_z]
                if math_op_radius:
                    math_op_radius_func = math_ops[math_op_radius]
                if math_op_radius_tweak_x:
                    math_op_radius_tweak_x_func = math_ops[math_op_radius_tweak_x]
                if math_op_radius_tweak_z:
                    math_op_radius_tweak_z_func = math_ops[math_op_radius_tweak_z]
                if phi_op:
                    phi_op_func = phi_ops[phi_op]
                if phi_op_tweak_theta:
                    phi_op_tweak_theta_func = phi_ops[phi_op_tweak_theta]
                if theta_op:
                    theta_op_func = phi_ops[theta_op]
                theta_value_x = theta_values[theta_x]
                theta_value_z = theta_values[theta_z]
                points_triggered = True
                ##############
                # End Preset #
                ##############
            elif event.key == pg.K_d:
                ############################################
                # Still 93 Points Shape Effect v1.0 Preset #
                ############################################
                num_objects = 4
                num_points = 5900
                point_size = 1.6
                theta_tweak = 3.200000000000002
                radius_tweak = 0.9500000000000001
                phi_tweak = 7.300001999999989
                points_tweak_x = 1.3000000000000005
                points_tweak_y = 1.0
                points_tweak_z = 1.0500000000000003
                points_size_x = 0.9000000000000008
                points_size_y = 2.100000000000001
                points_size_z = 0.8
                object_rotation_speed = 0.9500000000000002
                object1_rotation_angle = -235.0500000000192
                object1_rotation_x = 0.0
                object1_rotation_y = -0.04
                object1_rotation_z = 0.0
                object2_rotation_angle = -235.0500000000192
                object2_rotation_x = 0.0
                object2_rotation_y = 0.04
                object2_rotation_z = 0.0
                object3_rotation_angle = -235.0500000000192
                object3_rotation_x = 0.01
                object3_rotation_y = 1.0
                object3_rotation_z = 0.0
                object4_rotation_angle = -235.0500000000192
                object4_rotation_x = -0.01
                object4_rotation_y = -1.0
                object4_rotation_z = 0.0
                object1_pos_offset_x = 0.0
                object1_pos_offset_y = -0.04
                object1_pos_offset_z = 0.0
                object2_pos_offset_x = 0.0
                object2_pos_offset_y = 0.04
                object2_pos_offset_z = 0.0
                object3_pos_offset_x = 0.01
                object3_pos_offset_y = 1.0
                object3_pos_offset_z = 0.0
                object4_pos_offset_x = -0.01
                object4_pos_offset_y = -1.0
                object4_pos_offset_z = 0.0
                object1_color = (0.0, 0.0, 1.0, 1.0)
                object2_color = (0.2, 0.7, 0.7, 1.0)
                object3_color = (0.6, 0.5, 0.9, 1.0)
                object4_color = (0.9, 0.0, 0.0, 1.0)
                camera_rot = [-7.599999999999962, 107.0]
                camera_pos = [810211.0013052621, 9949.832350290744, 317674.3076638416]
                object_pos = [849000.407779635, 6000.0, 318332.04117208306]
                math_op_x = "sin"
                math_op_z = "atan"
                math_op_theta_x = "erf"
                math_op_theta_z = "sin"
                math_op_radius = "cos"
                math_op_radius_tweak_x = ""
                math_op_radius_tweak_z = ""
                phi_op = "-"
                phi_op_tweak_x = "*"
                phi_op_tweak_z = "*"
                phi_op_tweak_theta = ""
                theta_op = "*"
                theta_x = ""
                theta_z = ""
                math_op_x_func = math_ops[math_op_x]
                math_op_z_func = math_ops[math_op_z]
                math_op_theta_x_func = math_ops[math_op_theta_x]
                math_op_theta_z_func = math_ops[math_op_theta_z]
                if math_op_radius:
                    math_op_radius_func = math_ops[math_op_radius]
                if math_op_radius_tweak_x:
                    math_op_radius_tweak_x_func = math_ops[math_op_radius_tweak_x]
                if math_op_radius_tweak_z:
                    math_op_radius_tweak_z_func = math_ops[math_op_radius_tweak_z]
                if phi_op:
                    phi_op_func = phi_ops[phi_op]
                if phi_op_tweak_theta:
                    phi_op_tweak_theta_func = phi_ops[phi_op_tweak_theta]
                if theta_op:
                    theta_op_func = phi_ops[theta_op]
                theta_value_x = theta_values[theta_x]
                theta_value_z = theta_values[theta_z]
                points_triggered = True
                ##############
                # End Preset #
                ##############
            elif event.key == pg.K_f:
                ############################################
                # Still 93 Points Shape Effect v1.0 Preset #
                ############################################
                num_objects = 4
                num_points = 4000
                point_size = 1.6
                theta_tweak = 3.6000000000000023
                radius_tweak = 1.0
                phi_tweak = 12.99999999999997
                points_tweak_x = 1.5000000000000004
                points_tweak_y = 1.0
                points_tweak_z = 0.9
                points_size_x = 1.0
                points_size_y = 1.3000000000000003
                points_size_z = 1.0
                object_rotation_speed = 1.7000000000000008
                object1_rotation_angle = 204.80000000001232
                object1_rotation_x = 0.0
                object1_rotation_y = -0.04
                object1_rotation_z = 0.0
                object2_rotation_angle = 204.80000000001232
                object2_rotation_x = 0.0
                object2_rotation_y = 0.04
                object2_rotation_z = 0.0
                object3_rotation_angle = 204.80000000001232
                object3_rotation_x = 0.01
                object3_rotation_y = 1.0
                object3_rotation_z = 0.0
                object4_rotation_angle = 204.80000000001232
                object4_rotation_x = -0.01
                object4_rotation_y = -1.0
                object4_rotation_z = 0.0
                object1_pos_offset_x = 0.0
                object1_pos_offset_y = -0.04
                object1_pos_offset_z = 0.0
                object2_pos_offset_x = 0.0
                object2_pos_offset_y = 0.04
                object2_pos_offset_z = 0.0
                object3_pos_offset_x = 0.01
                object3_pos_offset_y = 1.0
                object3_pos_offset_z = 0.0
                object4_pos_offset_x = -0.01
                object4_pos_offset_y = -1.0
                object4_pos_offset_z = 0.0
                object1_color = (0.5058823529411764, 0.3803921568627451, 0.24313725490196078, 1.0)
                object2_color = (0.0, 1.0, 0.0, 0.1)
                object3_color = (0.26666666666666666, 0.4117647058823529, 0.23921568627450981, 1.0)
                object4_color = (0.3058823529411765, 0.17647058823529413, 0.07450980392156863, 1.0)
                camera_rot = [5.599999999999997, -88.0]
                camera_pos = [49279.556211978284, 39589.46383690813, 149656.71133673156]
                object_pos = [27152.257961935342, 17214.828262775503, 141503.18818378414]
                math_op_x = "sin"
                math_op_z = "atan"
                math_op_theta_x = "cos"
                math_op_theta_z = "sin"
                math_op_radius = ""
                math_op_radius_tweak_x = "erfc"
                math_op_radius_tweak_z = "erfc"
                phi_op = "-"
                phi_op_tweak_x = "*"
                phi_op_tweak_z = "*"
                phi_op_tweak_theta = ""
                theta_op = "*"
                theta_x = ""
                theta_z = ""
                math_op_x_func = math_ops[math_op_x]
                math_op_z_func = math_ops[math_op_z]
                math_op_theta_x_func = math_ops[math_op_theta_x]
                math_op_theta_z_func = math_ops[math_op_theta_z]
                if math_op_radius:
                    math_op_radius_func = math_ops[math_op_radius]
                if math_op_radius_tweak_x:
                    math_op_radius_tweak_x_func = math_ops[math_op_radius_tweak_x]
                if math_op_radius_tweak_z:
                    math_op_radius_tweak_z_func = math_ops[math_op_radius_tweak_z]
                if phi_op:
                    phi_op_func = phi_ops[phi_op]
                if phi_op_tweak_theta:
                    phi_op_tweak_theta_func = phi_ops[phi_op_tweak_theta]
                if theta_op:
                    theta_op_func = phi_ops[theta_op]
                theta_value_x = theta_values[theta_x]
                theta_value_z = theta_values[theta_z]
                points_triggered = True
                ##############
                # End Preset #
                ##############
            elif event.key == pg.K_g:
                ############################################
                # Still 93 Points Shape Effect v1.0 Preset #
                ############################################
                num_objects = 4
                num_points = 40000
                point_size = 1.4
                theta_tweak = 7.700417000000048
                radius_tweak = 14.45000000000007
                phi_tweak = 7.000813000000104
                points_tweak_x = 2.5999999999999988
                points_tweak_y = 2.000000000000001
                points_tweak_z = 1.3000000000000003
                points_size_x = 0.6999999999999911
                points_size_y = 2.400000000000004
                points_size_z = 0.30000000000000104
                object_rotation_speed = 1.1500000000000004
                object1_rotation_angle = 43261.25000024805
                object1_rotation_x = 0.0
                object1_rotation_y = -0.04
                object1_rotation_z = 0.0
                object2_rotation_angle = 43261.25000024805
                object2_rotation_x = 0.0
                object2_rotation_y = 0.04
                object2_rotation_z = 0.0
                object3_rotation_angle = 43261.25000024805
                object3_rotation_x = 0.01
                object3_rotation_y = 1.0
                object3_rotation_z = 0.0
                object4_rotation_angle = 43261.25000024805
                object4_rotation_x = -0.01
                object4_rotation_y = -1.0
                object4_rotation_z = 0.0
                object1_pos_offset_x = 0.0
                object1_pos_offset_y = -0.04
                object1_pos_offset_z = 0.0
                object2_pos_offset_x = 0.0
                object2_pos_offset_y = 0.04
                object2_pos_offset_z = 0.0
                object3_pos_offset_x = 0.01
                object3_pos_offset_y = 1.0
                object3_pos_offset_z = 0.0
                object4_pos_offset_x = -0.01
                object4_pos_offset_y = -1.0
                object4_pos_offset_z = 0.0
                object1_color = (1.0, 0.0, 0.0, 1.0)
                object2_color = (1.0, 0.1, 0.0, 1.0)
                object3_color = (0.3, 0.3, 0.7, 1.0)
                object4_color = (1.0, 0.1, 0.5, 1.0)
                camera_rot = [-90.0, 209.0]
                camera_pos = [580759.2842431526, 17376.47018112839, 394608.6278154671]
                object_pos = [582314.4633483291, 92411.09778541568, 394960.3480879411]
                math_op_x = "cos"
                math_op_z = "tan"
                math_op_theta_x = "asinh"
                math_op_theta_z = "atan"
                math_op_radius = "cos"
                math_op_radius_tweak_x = "cos"
                math_op_radius_tweak_z = "log1p"
                phi_op = "pow"
                phi_op_tweak_x = "*"
                phi_op_tweak_z = "*"
                phi_op_tweak_theta = ""
                theta_op = "*"
                theta_x = ""
                theta_z = ""
                math_op_x_func = math_ops[math_op_x]
                math_op_z_func = math_ops[math_op_z]
                math_op_theta_x_func = math_ops[math_op_theta_x]
                math_op_theta_z_func = math_ops[math_op_theta_z]
                if math_op_radius:
                    math_op_radius_func = math_ops[math_op_radius]
                if math_op_radius_tweak_x:
                    math_op_radius_tweak_x_func = math_ops[math_op_radius_tweak_x]
                if math_op_radius_tweak_z:
                    math_op_radius_tweak_z_func = math_ops[math_op_radius_tweak_z]
                if phi_op:
                    phi_op_func = phi_ops[phi_op]
                if phi_op_tweak_theta:
                    phi_op_tweak_theta_func = phi_ops[phi_op_tweak_theta]
                if theta_op:
                    theta_op_func = phi_ops[theta_op]
                theta_value_x = theta_values[theta_x]
                theta_value_z = theta_values[theta_z]
                points_triggered = True
                ##############
                # End Preset #
                ##############
            elif event.key == pg.K_h:
                ############################################
                # Still 93 Points Shape Effect v1.0 Preset #
                ############################################
                num_objects = 4
                num_points = 4000
                point_size = 1.6
                theta_tweak = 253.8000259999898
                radius_tweak = 1.4500000000000004
                phi_tweak = 6.000037999999999
                points_tweak_x = 3.1500000000000004
                points_tweak_y = 1.0
                points_tweak_z = 0.35000000000000014
                points_size_x = 0.6000000000000002
                points_size_y = 3.0000000000000018
                points_size_z = 1.0
                object_rotation_speed = 0.9500000000000002
                object1_rotation_angle = 16606.949999898585
                object1_rotation_x = 0.0
                object1_rotation_y = 1.7600000000000005
                object1_rotation_z = 0.8999999999999999
                object2_rotation_angle = 16606.449999898592
                object2_rotation_x = 0.0
                object2_rotation_y = 0.44000000000000006
                object2_rotation_z = 1.8000000000000005
                object3_rotation_angle = 16606.449999898592
                object3_rotation_x = 0.21000000000000002
                object3_rotation_y = 1.3000000000000003
                object3_rotation_z = 0.30000000000000004
                object4_rotation_angle = 16606.449999898592
                object4_rotation_x = 0.49
                object4_rotation_y = -0.7000000000000001
                object4_rotation_z = 0.30000000000000004
                object1_pos_offset_x = 0.0
                object1_pos_offset_y = 1.7600000000000005
                object1_pos_offset_z = 0.8999999999999999
                object2_pos_offset_x = 0.0
                object2_pos_offset_y = 0.44000000000000006
                object2_pos_offset_z = 1.8000000000000005
                object3_pos_offset_x = 0.21000000000000002
                object3_pos_offset_y = 1.3000000000000003
                object3_pos_offset_z = 0.30000000000000004
                object4_pos_offset_x = 0.49
                object4_pos_offset_y = -0.7000000000000001
                object4_pos_offset_z = 0.30000000000000004
                object1_color = (0.0, 0.0, 1.0, 1.0)
                object2_color = (0.2, 0.7, 0.7, 1.0)
                object3_color = (0.6, 0.5, 0.9, 1.0)
                object4_color = (0.9, 0.0, 0.0, 1.0)
                camera_rot = [-13.599999999999952, -9.0]
                camera_pos = [866705.6666466281, 160696.68393546916, 359868.24050051125]
                object_pos = [845000.407779635, 85000.0, 307332.04117208306]
                math_op_x = "sin"
                math_op_z = "cos"
                math_op_theta_x = "atan"
                math_op_theta_z = "atan"
                math_op_radius = "lgamma"
                math_op_radius_tweak_x = "erf"
                math_op_radius_tweak_z = "tan"
                phi_op = "+"
                phi_op_tweak_x = "*"
                phi_op_tweak_z = "*"
                phi_op_tweak_theta = ""
                theta_op = "*"
                theta_x = ""
                theta_z = ""
                math_op_x_func = math_ops[math_op_x]
                math_op_z_func = math_ops[math_op_z]
                math_op_theta_x_func = math_ops[math_op_theta_x]
                math_op_theta_z_func = math_ops[math_op_theta_z]
                if math_op_radius:
                    math_op_radius_func = math_ops[math_op_radius]
                if math_op_radius_tweak_x:
                    math_op_radius_tweak_x_func = math_ops[math_op_radius_tweak_x]
                if math_op_radius_tweak_z:
                    math_op_radius_tweak_z_func = math_ops[math_op_radius_tweak_z]
                if phi_op:
                    phi_op_func = phi_ops[phi_op]
                if phi_op_tweak_theta:
                    phi_op_tweak_theta_func = phi_ops[phi_op_tweak_theta]
                if theta_op:
                    theta_op_func = phi_ops[theta_op]
                theta_value_x = theta_values[theta_x]
                theta_value_z = theta_values[theta_z]
                points_triggered = True
                ##############
                # End Preset #
                ##############
            elif event.key == pg.K_j:
                ############################################
                # Still 93 Points Shape Effect v1.0 Preset #
                ############################################
                num_objects = 4
                num_points = 5800
                point_size = 1.6
                theta_tweak = 3.2000130000000038
                radius_tweak = 1.3000000000000003
                phi_tweak = 6.800023999999994
                points_tweak_x = 1.2500000000000002
                points_tweak_y = 1.0
                points_tweak_z = 1.6000000000000005
                points_size_x = 1.2500000000000002
                points_size_y = 1.3000000000000003
                points_size_z = 1.3000000000000003
                object_rotation_speed = 1.800000000000001
                object1_rotation_angle = 8302.050000019435
                object1_rotation_x = 0.0
                object1_rotation_y = -0.04
                object1_rotation_z = 0.0
                object2_rotation_angle = 8302.050000019435
                object2_rotation_x = 0.0
                object2_rotation_y = 0.04
                object2_rotation_z = 0.0
                object3_rotation_angle = 8302.050000019435
                object3_rotation_x = 0.01
                object3_rotation_y = 1.0
                object3_rotation_z = 0.0
                object4_rotation_angle = 8302.050000019435
                object4_rotation_x = -0.01
                object4_rotation_y = -1.0
                object4_rotation_z = 0.0
                object1_pos_offset_x = 0.0
                object1_pos_offset_y = -0.04
                object1_pos_offset_z = 0.0
                object2_pos_offset_x = 0.0
                object2_pos_offset_y = 0.04
                object2_pos_offset_z = 0.0
                object3_pos_offset_x = 0.01
                object3_pos_offset_y = 1.0
                object3_pos_offset_z = 0.0
                object4_pos_offset_x = -0.01
                object4_pos_offset_y = -1.0
                object4_pos_offset_z = 0.0
                object1_color = (0.8, 0.2, 0.0, 0.1)
                object2_color = (0.2, 0.0, 0.0, 0.1)
                object3_color = (1.0, 0.0, 0.0, 1.0)
                object4_color = (0.0, 0.0, 1.0, 1.0)
                camera_rot = [-2.3999999999999955, -85.0]
                camera_pos = [2920.038244788946, 42373.32699509485, 856594.3769418744]
                object_pos = [-6738.981330905459, 21000.40320987841, 853047.3816769368]
                math_op_x = "sin"
                math_op_z = "erf"
                math_op_theta_x = "cos"
                math_op_theta_z = "sin"
                math_op_radius = "erf"
                math_op_radius_tweak_x = "erfc"
                math_op_radius_tweak_z = "erfc"
                phi_op = "atan2"
                phi_op_tweak_x = "*"
                phi_op_tweak_z = "*"
                phi_op_tweak_theta = ""
                theta_op = "*"
                theta_x = ""
                theta_z = ""
                math_op_x_func = math_ops[math_op_x]
                math_op_z_func = math_ops[math_op_z]
                math_op_theta_x_func = math_ops[math_op_theta_x]
                math_op_theta_z_func = math_ops[math_op_theta_z]
                if math_op_radius:
                    math_op_radius_func = math_ops[math_op_radius]
                if math_op_radius_tweak_x:
                    math_op_radius_tweak_x_func = math_ops[math_op_radius_tweak_x]
                if math_op_radius_tweak_z:
                    math_op_radius_tweak_z_func = math_ops[math_op_radius_tweak_z]
                if phi_op:
                    phi_op_func = phi_ops[phi_op]
                if phi_op_tweak_theta:
                    phi_op_tweak_theta_func = phi_ops[phi_op_tweak_theta]
                if theta_op:
                    theta_op_func = phi_ops[theta_op]
                theta_value_x = theta_values[theta_x]
                theta_value_z = theta_values[theta_z]
                points_triggered = True
                ##############
                # End Preset #
                ##############
            elif event.key == pg.K_k:
                ############################################
                # Still 93 Points Shape Effect v1.0 Preset #
                ############################################
                num_objects = 4
                num_points = 4000
                point_size = 1.6
                theta_tweak = 1.0000079999999993
                radius_tweak = 1.0
                phi_tweak = 3.0000340000000048
                points_tweak_x = 1.0
                points_tweak_y = 1.0
                points_tweak_z = 1.0
                points_size_x = 1.0
                points_size_y = 1.0
                points_size_z = 1.0
                object_rotation_speed = 0.7500000000000001
                object1_rotation_angle = 13591.299999942466
                object1_rotation_x = 0.0
                object1_rotation_y = -0.04
                object1_rotation_z = 0.0
                object2_rotation_angle = 13591.299999942466
                object2_rotation_x = 0.0
                object2_rotation_y = 0.04
                object2_rotation_z = 0.0
                object3_rotation_angle = 13591.299999942466
                object3_rotation_x = 0.01
                object3_rotation_y = 1.0
                object3_rotation_z = 0.0
                object4_rotation_angle = 13591.299999942466
                object4_rotation_x = -0.01
                object4_rotation_y = -1.0
                object4_rotation_z = 0.0
                object1_pos_offset_x = 0.0
                object1_pos_offset_y = -0.04
                object1_pos_offset_z = 0.0
                object2_pos_offset_x = 0.0
                object2_pos_offset_y = 0.04
                object2_pos_offset_z = 0.0
                object3_pos_offset_x = 0.01
                object3_pos_offset_y = 1.0
                object3_pos_offset_z = 0.0
                object4_pos_offset_x = -0.01
                object4_pos_offset_y = -1.0
                object4_pos_offset_z = 0.0
                object1_color = (1.0, 1.0, 0.0, 0.1)
                object2_color = (0.0, 1.0, 0.0, 0.1)
                object3_color = (1.0, 0.0, 0.0, 1.0)
                object4_color = (0.0, 0.0, 1.0, 1.0)
                camera_rot = [-36.39999999999995, 0.0]
                camera_pos = [512000.0, 9235.236742586498, 520600.0]
                object_pos = [512000, 8000, 509000]
                math_op_x = "erf"
                math_op_z = "sin"
                math_op_theta_x = "cos"
                math_op_theta_z = "sin"
                math_op_radius = "erf"
                math_op_radius_tweak_x = "erfc"
                math_op_radius_tweak_z = "tan"
                phi_op = "*"
                phi_op_tweak_x = "*"
                phi_op_tweak_z = "*"
                phi_op_tweak_theta = ""
                theta_op = "*"
                theta_x = ""
                theta_z = ""
                math_op_x_func = math_ops[math_op_x]
                math_op_z_func = math_ops[math_op_z]
                math_op_theta_x_func = math_ops[math_op_theta_x]
                math_op_theta_z_func = math_ops[math_op_theta_z]
                if math_op_radius:
                    math_op_radius_func = math_ops[math_op_radius]
                if math_op_radius_tweak_x:
                    math_op_radius_tweak_x_func = math_ops[math_op_radius_tweak_x]
                if math_op_radius_tweak_z:
                    math_op_radius_tweak_z_func = math_ops[math_op_radius_tweak_z]
                if phi_op:
                    phi_op_func = phi_ops[phi_op]
                if phi_op_tweak_theta:
                    phi_op_tweak_theta_func = phi_ops[phi_op_tweak_theta]
                if theta_op:
                    theta_op_func = phi_ops[theta_op]
                theta_value_x = theta_values[theta_x]
                theta_value_z = theta_values[theta_z]
                points_triggered = True
                ##############
                # End Preset #
                ##############
            elif event.key == pg.K_l:
                ############################################
                # Still 93 Points Shape Effect v1.0 Preset #
                ############################################
                num_objects = 4
                num_points = 8000
                point_size = 1.5
                theta_tweak = 2.60006000000001
                radius_tweak = 0.8499999999999999
                phi_tweak = 3.8001340000000194
                points_tweak_x = 1.1500000000000001
                points_tweak_y = 1.0
                points_tweak_z = 0.95
                points_size_x = 2.5500000000000016
                points_size_y = 6.799999999999993
                points_size_z = 2.300000000000001
                object_rotation_speed = 1.5500000000000007
                object1_rotation_angle = 47181.1499996554
                object1_rotation_x = 0.0
                object1_rotation_y = -0.05
                object1_rotation_z = 0.01
                object2_rotation_angle = 47181.1499996554
                object2_rotation_x = 0.0
                object2_rotation_y = 0.03
                object2_rotation_z = -0.009999999999999997
                object3_rotation_angle = 47181.0999996554
                object3_rotation_x = -0.020000000000000004
                object3_rotation_y = 1.03
                object3_rotation_z = 0.02
                object4_rotation_angle = 47181.0499996554
                object4_rotation_x = 0.01
                object4_rotation_y = -0.98
                object4_rotation_z = 0.02
                object1_pos_offset_x = 0.0
                object1_pos_offset_y = -0.05
                object1_pos_offset_z = 0.01
                object2_pos_offset_x = 0.0
                object2_pos_offset_y = 0.03
                object2_pos_offset_z = -0.009999999999999997
                object3_pos_offset_x = -0.020000000000000004
                object3_pos_offset_y = 1.03
                object3_pos_offset_z = 0.02
                object4_pos_offset_x = 0.01
                object4_pos_offset_y = -0.98
                object4_pos_offset_z = 0.02
                object1_color = (1.0, 0.1, 0.0, 0.1)
                object2_color = (0.0, 0.5, 0.0, 0.1)
                object3_color = (0.9, 0.1, 0.1, 1.0)
                object4_color = (0.1, 0.1, 1.0, 1.0)
                camera_rot = [0.8000000000000417, 0.0]
                camera_pos = [514528.571181361, 147737.87567425912, 590049.5565482099]
                object_pos = [513000.4902891392, 72887.22299692867, 515800.3232986453]
                math_op_x = "sin"
                math_op_z = "sin"
                math_op_theta_x = "sin"
                math_op_theta_z = "asinh"
                math_op_radius = "cos"
                math_op_radius_tweak_x = "tan"
                math_op_radius_tweak_z = "erfc"
                phi_op = "+"
                phi_op_tweak_x = "*"
                phi_op_tweak_z = "*"
                phi_op_tweak_theta = ""
                theta_op = "*"
                theta_x = ""
                theta_z = ""
                math_op_x_func = math_ops[math_op_x]
                math_op_z_func = math_ops[math_op_z]
                math_op_theta_x_func = math_ops[math_op_theta_x]
                math_op_theta_z_func = math_ops[math_op_theta_z]
                if math_op_radius:
                    math_op_radius_func = math_ops[math_op_radius]
                if math_op_radius_tweak_x:
                    math_op_radius_tweak_x_func = math_ops[math_op_radius_tweak_x]
                if math_op_radius_tweak_z:
                    math_op_radius_tweak_z_func = math_ops[math_op_radius_tweak_z]
                if phi_op:
                    phi_op_func = phi_ops[phi_op]
                if phi_op_tweak_theta:
                    phi_op_tweak_theta_func = phi_ops[phi_op_tweak_theta]
                if theta_op:
                    theta_op_func = phi_ops[theta_op]
                theta_value_x = theta_values[theta_x]
                theta_value_z = theta_values[theta_z]
                points_triggered = True
                ##############
                # End Preset #
                ##############

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fov, (screen_w / screen_h), 0, LANDSCAPE_SIZE + AMPLITUDE * 2)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glRotatef(camera_rot[0], 0.1, 0.0, 0.0)
    glRotatef(camera_rot[1], 0.0, 0.1, 0.0)
    glPushMatrix()
    glEnable(GL_TEXTURE_CUBE_MAP)
    glDepthMask(GL_FALSE)
    glUseProgram(sky_shader)
    glBindTexture(GL_TEXTURE_CUBE_MAP, sky_id)
    glBindBuffer(GL_ARRAY_BUFFER, sky_vbo)
    glVertexPointer(3, GL_FLOAT, 0, None)
    glEnableClientState(GL_VERTEX_ARRAY)
    glDrawArrays(GL_TRIANGLES, 0, sky_verts.size)
    glDisableClientState(GL_VERTEX_ARRAY)
    glBindTexture(GL_TEXTURE_CUBE_MAP, 0)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glUseProgram(0)
    glDepthMask(GL_TRUE)
    glDisable(GL_TEXTURE_CUBE_MAP)
    glPopMatrix()

    glTranslatef(-camera_pos[0], -camera_pos[1], -camera_pos[2])

    glPushMatrix()
    glBindBuffer(GL_ARRAY_BUFFER, verts_vbo)
    glEnableClientState(GL_COLOR_ARRAY)
    glColorPointer(3, GL_FLOAT, 0, c_void_p(landscape.nbytes))
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, None)
    glEnableClientState(GL_NORMAL_ARRAY)
    glBindBuffer(GL_ARRAY_BUFFER, normals_vbo)
    glNormalPointer(GL_FLOAT, 0, None)
    glDrawArrays(GL_TRIANGLES, 0, landscape.size)
    glDisableClientState(GL_COLOR_ARRAY)
    glDisableClientState(GL_VERTEX_ARRAY)
    glDisableClientState(GL_NORMAL_ARRAY)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glPopMatrix()

    object1_rotation_angle_x += object_rotation_speed
    object2_rotation_angle_x += object_rotation_speed
    object3_rotation_angle_x += object_rotation_speed
    object4_rotation_angle_x += object_rotation_speed
    object1_rotation_angle_y += object_rotation_speed
    object2_rotation_angle_y += object_rotation_speed
    object3_rotation_angle_y += object_rotation_speed
    object4_rotation_angle_y += object_rotation_speed
    object1_rotation_angle_z += object_rotation_speed
    object2_rotation_angle_z += object_rotation_speed
    object3_rotation_angle_z += object_rotation_speed
    object4_rotation_angle_z += object_rotation_speed

    if points_triggered:
        glPointSize(point_size)
        points_array = np.zeros((num_points, 3), dtype=np.float32)
        points = generate_points(num_points, points_array)
        positions_array = np.zeros((len(points), 3), dtype=np.float32)
        point_positions = calculate_point_positions(points, points_radius, points_size_x, points_size_y, points_size_z, positions_array)
        objects_vbo = update_vbo(point_positions)
        points_triggered = False

    glBindBuffer(GL_ARRAY_BUFFER, objects_vbo)
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, None)

    if num_objects == 1 or num_objects == 2 or num_objects == 3 or num_objects == 4:
        glPushMatrix()
        glTranslatef(object_pos[0], object_pos[1], object_pos[2])
        glTranslatef(object1_pos_offset_x, object_pos[1] + object1_pos_offset_y, object1_pos_offset_z)
        glRotatef(object1_rotation_angle_x, object1_rotation_x, object1_rotation_y, object1_rotation_z)
        glColor4fv(object1_color)
        glDrawArrays(GL_POINTS, 0, num_points)
        glPopMatrix()
    if num_objects == 2 or num_objects == 3 or num_objects == 4:
        glPushMatrix()
        glTranslatef(object_pos[0], object_pos[1], object_pos[2])
        glTranslatef(object2_pos_offset_x, object_pos[1] + object2_pos_offset_y, object2_pos_offset_z)
        glRotatef(object2_rotation_angle_x, object2_rotation_x, object2_rotation_y, object2_rotation_z)
        glColor4fv(object2_color)
        glDrawArrays(GL_POINTS, 0, num_points)
        glPopMatrix()
    if num_objects == 3 or num_objects == 4:
        glPushMatrix()
        glTranslatef(object_pos[0], object_pos[1], object_pos[2])
        glTranslatef(object3_pos_offset_x, object_pos[1] + object3_pos_offset_y, object3_pos_offset_z)
        glRotatef(object3_rotation_angle_x, object3_rotation_x, object3_rotation_y, object3_rotation_z)
        glColor4fv(object3_color)
        glDrawArrays(GL_POINTS, 0, num_points)
        glPopMatrix()
    if num_objects == 4:
        glPushMatrix()
        glTranslatef(object_pos[0], object_pos[1], object_pos[2])
        glTranslatef(object4_pos_offset_x, object_pos[1] + object4_pos_offset_y, object4_pos_offset_z)
        glRotatef(object4_rotation_angle_x, object4_rotation_x, object4_rotation_y, object4_rotation_z)
        glColor4fv(object4_color)
        glDrawArrays(GL_POINTS, 0, num_points)
        glPopMatrix()
        glDisableClientState(GL_VERTEX_ARRAY)
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    apocalypse_elapsed_time = time() - apocalypse_start_time

    if apocalypse_elapsed_time >= apocalypse_timer_duration:
        break

    pg.display.flip()

pg.mixer.music.stop()
glDeleteBuffers(1, [verts_vbo, normals_vbo, objects_vbo, sky_id])
glDeleteTextures(1, [sky_id])
glUseProgram(0)
glDeleteProgram(sky_shader)
