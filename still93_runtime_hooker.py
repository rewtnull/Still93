__name__ = '__main__'
### LIBRARIES
### GLOBAL
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import sys
mega_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(mega_dir)
def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
import importlib.util
import pygame as pg
import numpy as np
from ctypes import c_void_p, c_float
### LOCAL
from math import (pi, sin, cos, radians, atan2, tan, atan, degrees, erf, erfc, exp, expm1, gamma,
    lgamma, sinh, cosh, asinh, acosh, log, log10, log1p, log2, e, pow, sqrt)
from operator import add, sub, mul, truediv, eq, mod
from noise import snoise3
from random import randint
from random import uniform
from time import time
from threading import Timer
### OPEN GL
### GLOBAL
from OpenGL.GL import (glEnable, glDisable, glBlendFunc, glClearDepth, glClearColor,
    glClear, glViewport, glMatrixMode, glLoadIdentity, glGenBuffers,
    glBindBuffer, glBufferData, glBufferSubData, glDeleteBuffers,
    glGenTextures, glBindTexture, glDeleteTextures, glTexImage2D,
    glTexParameteri, glDrawArrays, glPushMatrix, glPopMatrix,
    GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_PROJECTION, GL_MODELVIEW,
    GL_ARRAY_BUFFER, GL_TEXTURE_2D, GL_RGBA, GL_UNSIGNED_BYTE, GL_FLOAT,
    GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
### LOCAL
from OpenGL.GLU import gluPerspective
from OpenGL.GL.shaders import compileProgram, compileShader
from OpenGL.GL import (glColor4fv, glPointSize, glLightModelfv, glColorMaterial, glMaterialfv,
    glCreateShader, glShaderSource, glCompileShader, glGetShaderiv, glCreateProgram,
    glAttachShader, glLinkProgram, glGetProgramiv, glValidateProgram, glDetachShader,
    glActiveTexture, glDepthFunc, glDepthMask, glColorPointer, glNormalPointer, glRotatef, glLightfv,
    glFogfv, glFogf, glFogi, glTranslatef, glVertexPointer, glEnableClientState, glDisableClientState,
    glDeleteProgram, glUseProgram, glUniform3d, glUniform1d, glUniform1i, glScalef, glOrtho,
    glTexCoordPointer, glColor4f, glGetUniformLocation, glGetAttribLocation, glEnableVertexAttribArray,
    glDisableVertexAttribArray, glVertexAttribPointer, glUniform2f, glTranslate, glIndexPointer, glHint,
    glDrawElements, glGenVertexArrays, glBindVertexArray, glUniform1f, glGetUniformLocation, glDeleteProgram,
    glDeleteVertexArrays, glBegin, glEnd, glColor3f, glVertex3f, glVertex2f,
    GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE, GL_FALSE, GL_NEAREST,
    GL_VERTEX_ARRAY, GL_DYNAMIC_DRAW, GL_DEPTH_TEST, GL_LEQUAL, GL_TRUE, GL_COLOR_ARRAY, GL_SRC_ALPHA,
    GL_ONE_MINUS_SRC_ALPHA, GL_BLEND, GL_QUADS, GL_TEXTURE_COORD_ARRAY, GL_RGB, GL_POINTS,
    GL_AMBIENT_AND_DIFFUSE, GL_SPECULAR, GL_EMISSION, GL_SHININESS, GL_COMPILE_STATUS, GL_VALIDATE_STATUS,
    GL_LINK_STATUS, GL_TEXTURE_CUBE_MAP, GL_TEXTURE_CUBE_MAP_POSITIVE_X, GL_TEXTURE_WRAP_R, GL_TEXTURE0,
    GL_VERTEX_SHADER, GL_FRAGMENT_SHADER, GL_NORMAL_ARRAY, GL_TRIANGLES, GL_LIGHTING, GL_LIGHT0, GL_LIGHT1,
    GL_LIGHT2, GL_LIGHT3, GL_POSITION, GL_DIFFUSE, GL_AMBIENT, GL_LIGHT_MODEL_AMBIENT, GL_NORMALIZE,
    GL_COLOR_MATERIAL, GL_FRONT, GL_FOG, GL_FOG_COLOR,  GL_FOG_MODE, GL_FOG_START, GL_FOG_END, GL_REPEAT,
    GL_TRIANGLE_STRIP, GL_INT, GL_UNSIGNED_INT, GL_ELEMENT_ARRAY_BUFFER, GL_INDEX_ARRAY, GL_FOG_HINT, GL_NICEST)

pg.init()

screen_w, screen_h = 640, 480
screen = pg.display.set_mode((screen_w, screen_h), pg.FULLSCREEN | pg.DOUBLEBUF | pg.OPENGL)

icon = pg.image.load(resource_path('resources/amigaicon.png'))
pg.display.set_icon(icon)
pg.mouse.set_visible(False)

class MEGA_Main:
    def __init__(self, screen_w, screen_h, screen, pg, np, os, sys, c_void_p, c_float, resource_path, glEnable, glDisable,
        glBlendFunc, glClearDepth, glClearColor, glClear, glViewport, glMatrixMode, glLoadIdentity,
        glGenBuffers, glBindBuffer, glBufferData, glBufferSubData, glDeleteBuffers, glGenTextures,
        glBindTexture, glDeleteTextures, glTexImage2D, glTexParameteri, glDrawArrays, glPushMatrix,
        glPopMatrix, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_PROJECTION, GL_MODELVIEW,
        GL_ARRAY_BUFFER, GL_TEXTURE_2D, GL_RGBA, GL_UNSIGNED_BYTE, GL_FLOAT, GL_TEXTURE_MIN_FILTER,
        GL_TEXTURE_MAG_FILTER, GL_LINEAR):
        self.os = os
        self.sys = sys
        self.screen = screen
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.pg = pg
        self.np = np
        self.c_void_p = c_void_p
        self.c_float = c_float
        self.resource_path = resource_path
        self.glEnable = glEnable
        self.glDisable = glDisable
        self.glBlendFunc = glBlendFunc
        self.glClearDepth = glClearDepth
        self.glClearColor = glClearColor
        self.glClear = glClear
        self.glViewport = glViewport
        self.glMatrixMode = glMatrixMode
        self.glLoadIdentity = glLoadIdentity
        self.glGenBuffers = glGenBuffers
        self.glBindBuffer = glBindBuffer
        self.glBufferData = glBufferData
        self.glBufferSubData = glBufferSubData
        self.glDeleteBuffers = glDeleteBuffers
        self.glGenTextures = glGenTextures
        self.glBindTexture = glBindTexture
        self.glDeleteTextures = glDeleteTextures
        self.glTexImage2D = glTexImage2D
        self.glTexParameteri = glTexParameteri
        self.glDrawArrays = glDrawArrays
        self.glPushMatrix = glPushMatrix
        self.glPopMatrix = glPopMatrix
        self.GL_COLOR_BUFFER_BIT = GL_COLOR_BUFFER_BIT
        self.GL_DEPTH_BUFFER_BIT = GL_DEPTH_BUFFER_BIT
        self.GL_PROJECTION = GL_PROJECTION
        self.GL_MODELVIEW = GL_MODELVIEW
        self.GL_ARRAY_BUFFER = GL_ARRAY_BUFFER
        self.GL_TEXTURE_2D = GL_TEXTURE_2D
        self.GL_RGBA = GL_RGBA
        self.GL_UNSIGNED_BYTE = GL_UNSIGNED_BYTE
        self.GL_FLOAT = GL_FLOAT
        self.GL_TEXTURE_MIN_FILTER = GL_TEXTURE_MIN_FILTER
        self.GL_TEXTURE_MAG_FILTER = GL_TEXTURE_MAG_FILTER
        self.GL_LINEAR = GL_LINEAR

class MEGA01(MEGA_Main):
    def __init__(self):
        super().__init__(screen_w, screen_h, screen, pg, np, os, sys, c_void_p, c_float, resource_path, glEnable, glDisable,
        glBlendFunc, glClearDepth, glClearColor, glClear, glViewport, glMatrixMode, glLoadIdentity,
        glGenBuffers, glBindBuffer, glBufferData, glBufferSubData, glDeleteBuffers, glGenTextures,
        glBindTexture, glDeleteTextures, glTexImage2D, glTexParameteri, glDrawArrays, glPushMatrix,
        glPopMatrix, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_PROJECTION, GL_MODELVIEW,
        GL_ARRAY_BUFFER, GL_TEXTURE_2D, GL_RGBA, GL_UNSIGNED_BYTE, GL_FLOAT, GL_TEXTURE_MIN_FILTER,
        GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        self.var = "still93_we_still_make_cracktros.py"
        self.randint = randint
        self.time = time
        self.pi = pi
        self.sin = sin
        self.cos = cos
        self.radians = radians
        self.glDepthFunc = glDepthFunc
        self.glDepthMask = glDepthMask
        self.glOrtho = glOrtho
        self.glTexCoordPointer = glTexCoordPointer
        self.glColor4f = glColor4f
        self.glVertexPointer = glVertexPointer
        self.glEnableClientState = glEnableClientState
        self.glDisableClientState = glDisableClientState
        self.glTranslatef = glTranslatef
        self.glGetAttribLocation = glGetAttribLocation
        self.glEnableVertexAttribArray = glEnableVertexAttribArray
        self.glDisableVertexAttribArray = glDisableVertexAttribArray
        self.glVertexAttribPointer = glVertexAttribPointer
        self.glUniform2f = glUniform2f
        self.glColorPointer = glColorPointer
        self.GL_TEXTURE_WRAP_S = GL_TEXTURE_WRAP_S
        self.GL_TEXTURE_WRAP_T = GL_TEXTURE_WRAP_T
        self.GL_CLAMP_TO_EDGE = GL_CLAMP_TO_EDGE
        self.GL_FALSE = GL_FALSE
        self.GL_NEAREST = GL_NEAREST
        self.GL_VERTEX_ARRAY = GL_VERTEX_ARRAY
        self.GL_DYNAMIC_DRAW = GL_DYNAMIC_DRAW
        self.GL_DEPTH_TEST = GL_DEPTH_TEST
        self.GL_LEQUAL = GL_LEQUAL
        self.GL_TRUE = GL_TRUE
        self.GL_COLOR_ARRAY = GL_COLOR_ARRAY
        self.GL_SRC_ALPHA = GL_SRC_ALPHA
        self.GL_ONE_MINUS_SRC_ALPHA = GL_ONE_MINUS_SRC_ALPHA
        self.GL_BLEND = GL_BLEND
        self.GL_QUADS = GL_QUADS
        self.GL_TEXTURE_COORD_ARRAY = GL_TEXTURE_COORD_ARRAY

class MEGA02(MEGA_Main):
    def __init__(self):
        super().__init__(screen_w, screen_h, screen, pg, np, os, sys, c_void_p, c_float, resource_path, glEnable, glDisable,
        glBlendFunc, glClearDepth, glClearColor, glClear, glViewport, glMatrixMode, glLoadIdentity,
        glGenBuffers, glBindBuffer, glBufferData, glBufferSubData, glDeleteBuffers, glGenTextures,
        glBindTexture, glDeleteTextures, glTexImage2D, glTexParameteri, glDrawArrays, glPushMatrix,
        glPopMatrix, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_PROJECTION, GL_MODELVIEW,
        GL_ARRAY_BUFFER, GL_TEXTURE_2D, GL_RGBA, GL_UNSIGNED_BYTE, GL_FLOAT, GL_TEXTURE_MIN_FILTER,
        GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        self.var = "still93_pixel_apocalypse.py"
        self.pi = pi
        self.sin = sin
        self.cos = cos
        self.radians = radians
        self.atan2 = atan2
        self.tan = tan
        self.atan = atan
        self.degrees = degrees
        self.erf = erf
        self.erfc = erfc
        self.exp = exp
        self.expm1 = expm1
        self.gamma = gamma
        self.lgamma = lgamma
        self.sinh = sinh
        self.cosh = cosh
        self.asinh = asinh
        self.acosh = acosh
        self.log = log
        self.log10 = log10
        self.log1p = log1p
        self.log2 = log2
        self.e = e
        self.pow = pow
        self.sqrt = sqrt
        self.add = add
        self.sub = sub
        self.mul = mul
        self.truediv = truediv
        self.eq = eq
        self.mod = mod
        self.snoise3 = snoise3
        self.uniform = uniform
        self.time = time
        self.Timer = Timer
        self.glColor4fv = glColor4fv
        self.glPointSize = glPointSize
        self.glLightModelfv = glLightModelfv
        self.glColorMaterial = glColorMaterial
        self.glMaterialfv = glMaterialfv
        self.glCreateShader = glCreateShader
        self.glShaderSource = glShaderSource
        self.glCompileShader = glCompileShader
        self.glGetShaderiv = glGetShaderiv
        self.glCreateProgram = glCreateProgram
        self.glAttachShader = glAttachShader
        self.glLinkProgram = glLinkProgram
        self.glGetProgramiv = glGetProgramiv
        self.glValidateProgram = glValidateProgram
        self.glDetachShader = glDetachShader
        self.glActiveTexture = glActiveTexture
        self.glTranslatef = glTranslatef
        self.glVertexPointer = glVertexPointer
        self.glEnableClientState = glEnableClientState
        self.glDisableClientState = glDisableClientState
        self.glDeleteProgram = glDeleteProgram
        self.glUseProgram = glUseProgram
        self.compileProgram = compileProgram
        self.compileShader = compileShader
        self.glDepthFunc = glDepthFunc
        self.glDepthMask = glDepthMask
        self.glColorPointer = glColorPointer
        self.glNormalPointer = glNormalPointer
        self.glRotatef = glRotatef
        self.glLightfv = glLightfv
        self.glFogfv = glFogfv
        self.glFogf = glFogf
        self.gluPerspective = gluPerspective
        self.GL_RGB = GL_RGB
        self.GL_POINTS = GL_POINTS
        self.GL_AMBIENT_AND_DIFFUSE = GL_AMBIENT_AND_DIFFUSE
        self.GL_SPECULAR = GL_SPECULAR
        self.GL_EMISSION = GL_EMISSION
        self.GL_SHININESS = GL_SHININESS
        self.GL_COMPILE_STATUS = GL_COMPILE_STATUS
        self.GL_VALIDATE_STATUS = GL_VALIDATE_STATUS
        self.GL_LINK_STATUS = GL_LINK_STATUS
        self.GL_TEXTURE_CUBE_MAP = GL_TEXTURE_CUBE_MAP
        self.GL_TEXTURE_CUBE_MAP_POSITIVE_X = GL_TEXTURE_CUBE_MAP_POSITIVE_X
        self.GL_TEXTURE_WRAP_R = GL_TEXTURE_WRAP_R
        self.GL_TEXTURE0 = GL_TEXTURE0
        self.GL_TEXTURE_WRAP_S = GL_TEXTURE_WRAP_S
        self.GL_TEXTURE_WRAP_T = GL_TEXTURE_WRAP_T
        self.GL_CLAMP_TO_EDGE = GL_CLAMP_TO_EDGE
        self.GL_FALSE = GL_FALSE
        self.GL_VERTEX_SHADER = GL_VERTEX_SHADER
        self.GL_FRAGMENT_SHADER = GL_FRAGMENT_SHADER
        self.GL_NEAREST = GL_NEAREST
        self.GL_VERTEX_ARRAY = GL_VERTEX_ARRAY
        self.GL_DYNAMIC_DRAW = GL_DYNAMIC_DRAW
        self.GL_DEPTH_TEST = GL_DEPTH_TEST
        self.GL_LEQUAL = GL_LEQUAL
        self.GL_TRUE = GL_TRUE
        self.GL_COLOR_ARRAY = GL_COLOR_ARRAY
        self.GL_NORMAL_ARRAY = GL_NORMAL_ARRAY
        self.GL_TRIANGLES = GL_TRIANGLES
        self.GL_LIGHTING = GL_LIGHTING
        self.GL_LIGHT0 = GL_LIGHT0
        self.GL_POSITION = GL_POSITION
        self.GL_DIFFUSE = GL_DIFFUSE
        self.GL_AMBIENT= GL_AMBIENT
        self.GL_LIGHT_MODEL_AMBIENT = GL_LIGHT_MODEL_AMBIENT
        self.GL_NORMALIZE = GL_NORMALIZE
        self.GL_COLOR_MATERIAL = GL_COLOR_MATERIAL
        self.GL_FRONT = GL_FRONT
        self.GL_FOG = GL_FOG
        self.GL_FOG_COLOR = GL_FOG_COLOR
        self.GL_FOG_MODE = GL_FOG_MODE
        self.GL_FOG_START = GL_FOG_START
        self.GL_FOG_END = GL_FOG_END

class MEGA03(MEGA_Main):
    def __init__(self):
        super().__init__(screen_w, screen_h, screen, pg, np, os, sys, c_void_p, c_float, resource_path, glEnable, glDisable,
        glBlendFunc, glClearDepth, glClearColor, glClear, glViewport, glMatrixMode, glLoadIdentity,
        glGenBuffers, glBindBuffer, glBufferData, glBufferSubData, glDeleteBuffers, glGenTextures,
        glBindTexture, glDeleteTextures, glTexImage2D, glTexParameteri, glDrawArrays, glPushMatrix,
        glPopMatrix, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_PROJECTION, GL_MODELVIEW,
        GL_ARRAY_BUFFER, GL_TEXTURE_2D, GL_RGBA, GL_UNSIGNED_BYTE, GL_FLOAT, GL_TEXTURE_MIN_FILTER,
        GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        self.var = "still93_julia_my_love.py"
        self.time = time
        self.sin = sin
        self.cos = cos
        self.radians = radians
        self.glActiveTexture = glActiveTexture
        self.glUniform3d = glUniform3d
        self.glUniform1d = glUniform1d
        self.glUniform1i = glUniform1i
        self.glTranslatef = glTranslatef
        self.glVertexPointer = glVertexPointer
        self.glEnableClientState = glEnableClientState
        self.glDisableClientState = glDisableClientState
        self.glDeleteProgram = glDeleteProgram
        self.glUseProgram = glUseProgram
        self.compileProgram = compileProgram
        self.compileShader = compileShader
        self.glScalef = glScalef
        self.glOrtho = glOrtho
        self.glTexCoordPointer = glTexCoordPointer
        self.glColor4f = glColor4f
        self.glGetUniformLocation = glGetUniformLocation
        self.glGetAttribLocation = glGetAttribLocation
        self.glEnableVertexAttribArray = glEnableVertexAttribArray
        self.glDisableVertexAttribArray = glDisableVertexAttribArray
        self.glVertexAttribPointer = glVertexAttribPointer
        self.glUniform2f = glUniform2f
        self.glTranslate = glTranslate
        self.GL_TEXTURE0 = GL_TEXTURE0
        self.GL_TEXTURE_WRAP_S = GL_TEXTURE_WRAP_S
        self.GL_TEXTURE_WRAP_T = GL_TEXTURE_WRAP_T
        self.GL_CLAMP_TO_EDGE = GL_CLAMP_TO_EDGE
        self.GL_FALSE = GL_FALSE
        self.GL_NEAREST = GL_NEAREST
        self.GL_VERTEX_ARRAY = GL_VERTEX_ARRAY
        self.GL_DYNAMIC_DRAW = GL_DYNAMIC_DRAW
        self.GL_SRC_ALPHA = GL_SRC_ALPHA
        self.GL_ONE_MINUS_SRC_ALPHA = GL_ONE_MINUS_SRC_ALPHA
        self.GL_BLEND = GL_BLEND
        self.GL_QUADS = GL_QUADS
        self.GL_TEXTURE_COORD_ARRAY = GL_TEXTURE_COORD_ARRAY
        self.GL_VERTEX_SHADER = GL_VERTEX_SHADER
        self.GL_FRAGMENT_SHADER = GL_FRAGMENT_SHADER
        self.GL_REPEAT = GL_REPEAT
        self.GL_TRIANGLE_STRIP = GL_TRIANGLE_STRIP

class MEGA04(MEGA_Main):
    def __init__(self):
        super().__init__(screen_w, screen_h, screen, pg, np, os, sys, c_void_p, c_float, resource_path, glEnable, glDisable,
        glBlendFunc, glClearDepth, glClearColor, glClear, glViewport, glMatrixMode, glLoadIdentity,
        glGenBuffers, glBindBuffer, glBufferData, glBufferSubData, glDeleteBuffers, glGenTextures,
        glBindTexture, glDeleteTextures, glTexImage2D, glTexParameteri, glDrawArrays, glPushMatrix,
        glPopMatrix, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_PROJECTION, GL_MODELVIEW,
        GL_ARRAY_BUFFER, GL_TEXTURE_2D, GL_RGBA, GL_UNSIGNED_BYTE, GL_FLOAT, GL_TEXTURE_MIN_FILTER,
        GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        self.var = "still93_golden_god_rays.py"
        self.time = time
        self.Timer = Timer
        self.glDepthFunc = glDepthFunc
        self.glDepthMask = glDepthMask
        self.glColorPointer = glColorPointer
        self.glNormalPointer = glNormalPointer
        self.glRotatef = glRotatef
        self.glLightfv  = glLightfv,
        self.glFogfv = glFogfv
        self.glFogf = glFogf
        self.gluPerspective = gluPerspective
        self.glTranslatef = glTranslatef
        self.glVertexPointer = glVertexPointer
        self.glEnableClientState = glEnableClientState
        self.glDisableClientState = glDisableClientState
        self.glScalef = glScalef
        self.glOrtho = glOrtho
        self.glTexCoordPointer = glTexCoordPointer
        self.glColor4f = glColor4f
        self.glIndexPointer = glIndexPointer
        self.glHint = glHint
        self.glDrawElements = glDrawElements
        self.compileProgram = compileProgram
        self.compileShader = compileShader
        self.glDeleteProgram = glDeleteProgram
        self.glUseProgram = glUseProgram
        self.glGenVertexArrays = glGenVertexArrays
        self.glBindVertexArray = glBindVertexArray
        self.glGetAttribLocation = glGetAttribLocation
        self.glEnableVertexAttribArray = glEnableVertexAttribArray
        self.glDisableVertexAttribArray = glDisableVertexAttribArray
        self.glVertexAttribPointer = glVertexAttribPointer
        self.glDeleteVertexArrays = glDeleteVertexArrays
        self.glGetUniformLocation = glGetUniformLocation
        self.glUniform1f = glUniform1f
        self.glUniform2f = glUniform2f
        self.GL_DYNAMIC_DRAW = GL_DYNAMIC_DRAW
        self.GL_VERTEX_SHADER = GL_VERTEX_SHADER
        self.GL_FRAGMENT_SHADER = GL_FRAGMENT_SHADER
        self.GL_TEXTURE_WRAP_S = GL_TEXTURE_WRAP_S
        self.GL_TEXTURE_WRAP_T = GL_TEXTURE_WRAP_T
        self.GL_CLAMP_TO_EDGE = GL_CLAMP_TO_EDGE
        self.GL_FALSE = GL_FALSE
        self.GL_SRC_ALPHA = GL_SRC_ALPHA
        self.GL_ONE_MINUS_SRC_ALPHA = GL_ONE_MINUS_SRC_ALPHA
        self.GL_BLEND = GL_BLEND
        self.GL_QUADS = GL_QUADS

class MEGA05(MEGA_Main):
    def __init__(self):
        super().__init__(screen_w, screen_h, screen, pg, np, os, sys, c_void_p, c_float, resource_path, glEnable, glDisable,
        glBlendFunc, glClearDepth, glClearColor, glClear, glViewport, glMatrixMode, glLoadIdentity,
        glGenBuffers, glBindBuffer, glBufferData, glBufferSubData, glDeleteBuffers, glGenTextures,
        glBindTexture, glDeleteTextures, glTexImage2D, glTexParameteri, glDrawArrays, glPushMatrix,
        glPopMatrix, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_PROJECTION, GL_MODELVIEW,
        GL_ARRAY_BUFFER, GL_TEXTURE_2D, GL_RGBA, GL_UNSIGNED_BYTE, GL_FLOAT, GL_TEXTURE_MIN_FILTER,
        GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        self.var = "still93_beyond_the_balls.py"
        self.sin = sin
        self.cos = cos
        self.radians = radians
        self.sqrt = sqrt
        self.glBegin = glBegin
        self.glEnd = glEnd
        self.glColor3f = glColor3f
        self.glVertex3f = glVertex3f
        self.glVertex2f = glVertex2f
        self.gluPerspective = gluPerspective
        self.glTranslatef = glTranslatef
        self.glLightfv = glLightfv
        self.glFogfv = glFogfv
        self.glFogf = glFogf
        self.glFogi = glFogi
        self.glHint = glHint
        self.glEnableClientState = glEnableClientState
        self.glDisableClientState = glDisableClientState
        self.glVertexPointer = glVertexPointer
        self.time = time
        self.glOrtho = glOrtho
        self.glColor4f = glColor4f
        self.glScalef = glScalef
        self.glTexCoordPointer = glTexCoordPointer
        self.glRotatef = glRotatef
        self.glIndexPointer = glIndexPointer
        self.glDrawElements = glDrawElements
        self.glDepthFunc = glDepthFunc
        self.glDepthMask = glDepthMask
        self.glColorPointer = glColorPointer
        self.glNormalPointer = glNormalPointer
        self.GL_DYNAMIC_DRAW = GL_DYNAMIC_DRAW
        self.GL_NEAREST = GL_NEAREST
        self.GL_DEPTH_TEST = GL_DEPTH_TEST
        self.GL_LEQUAL = GL_LEQUAL
        self.GL_TRUE = GL_TRUE
        self.GL_COLOR_ARRAY = GL_COLOR_ARRAY
        self.GL_NORMAL_ARRAY = GL_NORMAL_ARRAY
        self.GL_TRIANGLES = GL_TRIANGLES
        self.GL_LIGHTING = GL_LIGHTING
        self.GL_LIGHT0 = GL_LIGHT0
        self.GL_LIGHT1 = GL_LIGHT1
        self.GL_LIGHT2 = GL_LIGHT2
        self.GL_LIGHT3 = GL_LIGHT3
        self.GL_POSITION = GL_POSITION
        self.GL_DIFFUSE = GL_DIFFUSE
        self.GL_AMBIENT = GL_AMBIENT
        self.GL_LIGHT_MODEL_AMBIENT = GL_LIGHT_MODEL_AMBIENT
        self.GL_NORMALIZE = GL_NORMALIZE
        self.GL_COLOR_MATERIAL = GL_COLOR_MATERIAL
        self.GL_FRONT = GL_FRONT
        self.GL_FOG = GL_FOG
        self.GL_FOG_COLOR = GL_FOG_COLOR
        self.GL_FOG_MODE = GL_FOG_MODE
        self.GL_FOG_START = GL_FOG_START
        self.GL_FOG_END = GL_FOG_END
        self.GL_INT = GL_INT
        self.GL_UNSIGNED_INT = GL_UNSIGNED_INT
        self.GL_ELEMENT_ARRAY_BUFFER = GL_ELEMENT_ARRAY_BUFFER
        self.GL_INDEX_ARRAY = GL_INDEX_ARRAY
        self.GL_FOG_HINT = GL_FOG_HINT
        self.GL_NICEST = GL_NICEST
        self.GL_SRC_ALPHA = GL_SRC_ALPHA
        self.GL_VERTEX_ARRAY = GL_VERTEX_ARRAY
        self.GL_ONE_MINUS_SRC_ALPHA = GL_ONE_MINUS_SRC_ALPHA
        self.GL_BLEND = GL_BLEND
        self.GL_QUADS = GL_QUADS
        self.GL_TEXTURE_COORD_ARRAY = GL_TEXTURE_COORD_ARRAY

class MEGA06(MEGA_Main):
    def __init__(self):
        super().__init__(screen_w, screen_h, screen, pg, np, os, sys, c_void_p, c_float, resource_path, glEnable, glDisable,
        glBlendFunc, glClearDepth, glClearColor, glClear, glViewport, glMatrixMode, glLoadIdentity,
        glGenBuffers, glBindBuffer, glBufferData, glBufferSubData, glDeleteBuffers, glGenTextures,
        glBindTexture, glDeleteTextures, glTexImage2D, glTexParameteri, glDrawArrays, glPushMatrix,
        glPopMatrix, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_PROJECTION, GL_MODELVIEW,
        GL_ARRAY_BUFFER, GL_TEXTURE_2D, GL_RGBA, GL_UNSIGNED_BYTE, GL_FLOAT, GL_TEXTURE_MIN_FILTER,
        GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        self.var = "still93_keep_it_cool.py"
        self.compileProgram = compileProgram
        self.compileShader = compileShader
        self.glDeleteProgram = glDeleteProgram
        self.glUseProgram = glUseProgram
        self.glOrtho = glOrtho
        self.glUniform1i = glUniform1i
        self.glUniform1f = glUniform1f
        self.glGetUniformLocation = glGetUniformLocation
        self.glGenVertexArrays = glGenVertexArrays
        self.glBindVertexArray = glBindVertexArray
        self.glDeleteVertexArrays = glDeleteVertexArrays
        self.glGetAttribLocation = glGetAttribLocation
        self.glEnableVertexAttribArray = glEnableVertexAttribArray
        self.glDisableVertexAttribArray = glDisableVertexAttribArray
        self.glVertexAttribPointer = glVertexAttribPointer
        self.glActiveTexture = glActiveTexture
        self.GL_FALSE = GL_FALSE
        self.GL_QUADS = GL_QUADS
        self.GL_SRC_ALPHA = GL_SRC_ALPHA
        self.GL_ONE_MINUS_SRC_ALPHA = GL_ONE_MINUS_SRC_ALPHA
        self.GL_BLEND = GL_BLEND
        self.GL_VERTEX_SHADER = GL_VERTEX_SHADER
        self.GL_FRAGMENT_SHADER = GL_FRAGMENT_SHADER
        self.GL_TEXTURE_WRAP_S = GL_TEXTURE_WRAP_S
        self.GL_TEXTURE_WRAP_T = GL_TEXTURE_WRAP_T
        self.GL_CLAMP_TO_EDGE = GL_CLAMP_TO_EDGE
        self.GL_DYNAMIC_DRAW = GL_DYNAMIC_DRAW
        self.GL_TEXTURE0 = GL_TEXTURE0

class MEGA07(MEGA_Main):
    def __init__(self):
        super().__init__(screen_w, screen_h, screen, pg, np, os, sys, c_void_p, c_float, resource_path, glEnable, glDisable,
        glBlendFunc, glClearDepth, glClearColor, glClear, glViewport, glMatrixMode, glLoadIdentity,
        glGenBuffers, glBindBuffer, glBufferData, glBufferSubData, glDeleteBuffers, glGenTextures,
        glBindTexture, glDeleteTextures, glTexImage2D, glTexParameteri, glDrawArrays, glPushMatrix,
        glPopMatrix, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_PROJECTION, GL_MODELVIEW,
        GL_ARRAY_BUFFER, GL_TEXTURE_2D, GL_RGBA, GL_UNSIGNED_BYTE, GL_FLOAT, GL_TEXTURE_MIN_FILTER,
        GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        self.var = "still93_even_good_things_have_to_end.py"
        self.time = time
        self.sin = sin
        self.cos = cos
        self.radians = radians
        self.glVertexPointer = glVertexPointer
        self.glEnableClientState = glEnableClientState
        self.glDisableClientState = glDisableClientState
        self.glCreateShader = glCreateShader
        self.glShaderSource = glShaderSource
        self.glCompileShader = glCompileShader
        self.glGetShaderiv = glGetShaderiv
        self.glCreateProgram = glCreateProgram
        self.glAttachShader = glAttachShader
        self.glLinkProgram = glLinkProgram
        self.glGetProgramiv = glGetProgramiv
        self.glValidateProgram = glValidateProgram
        self.glDetachShader = glDetachShader
        self.glDeleteProgram = glDeleteProgram
        self.glUseProgram = glUseProgram
        self.compileProgram = compileProgram
        self.compileShader = compileShader
        self.glScalef = glScalef
        self.glOrtho = glOrtho
        self.glTexCoordPointer = glTexCoordPointer
        self.glColor4f = glColor4f
        self.glGetUniformLocation = glGetUniformLocation
        self.glGetAttribLocation = glGetAttribLocation
        self.glEnableVertexAttribArray = glEnableVertexAttribArray
        self.glDisableVertexAttribArray = glDisableVertexAttribArray
        self.glVertexAttribPointer = glVertexAttribPointer
        self.glUniform2f = glUniform2f
        self.glTranslate = glTranslate
        self.glVertexPointer = glVertexPointer
        self.glIndexPointer = glIndexPointer
        self.glHint = glHint
        self.glDrawElements = glDrawElements
        self.glGenVertexArrays = glGenVertexArrays
        self.glBindVertexArray = glBindVertexArray
        self.glDeleteVertexArrays = glDeleteVertexArrays
        self.glUniform1f = glUniform1f
        self.GL_COMPILE_STATUS = GL_COMPILE_STATUS
        self.GL_VALIDATE_STATUS = GL_VALIDATE_STATUS
        self.GL_LINK_STATUS = GL_LINK_STATUS
        self.GL_TEXTURE0 = GL_TEXTURE0
        self.GL_TEXTURE_WRAP_S = GL_TEXTURE_WRAP_S
        self.GL_TEXTURE_WRAP_T = GL_TEXTURE_WRAP_T
        self.GL_CLAMP_TO_EDGE = GL_CLAMP_TO_EDGE
        self.GL_FALSE = GL_FALSE
        self.GL_NEAREST = GL_NEAREST
        self.GL_VERTEX_ARRAY = GL_VERTEX_ARRAY
        self.GL_DYNAMIC_DRAW = GL_DYNAMIC_DRAW
        self.GL_SRC_ALPHA = GL_SRC_ALPHA
        self.GL_ONE_MINUS_SRC_ALPHA = GL_ONE_MINUS_SRC_ALPHA
        self.GL_BLEND = GL_BLEND
        self.GL_QUADS = GL_QUADS
        self.GL_TEXTURE_COORD_ARRAY = GL_TEXTURE_COORD_ARRAY
        self.GL_VERTEX_SHADER = GL_VERTEX_SHADER
        self.GL_FRAGMENT_SHADER = GL_FRAGMENT_SHADER
        self.GL_REPEAT = GL_REPEAT
        self.GL_TRIANGLE_STRIP = GL_TRIANGLE_STRIP

class RuntimeHook:
    def execute_scripts(self, mega_parts):
        for script_path in mega_parts:
            module_name = os.path.splitext(os.path.basename(script_path))[0]
            spec = importlib.util.spec_from_file_location(module_name, script_path)
            module = importlib.util.module_from_spec(spec)
            part_name = os.path.splitext(os.path.basename(script_path))[0]

            print("4 uR viEwiNg pLEAsURe:", part_name)

            if part_name == "still93_we_still_make_cracktros":
                part_instance = MEGA01()
            elif part_name == "still93_pixel_apocalypse":
                part_instance = MEGA02()
            elif part_name == "still93_julia_my_love":
                part_instance = MEGA03()
            elif part_name == "still93_golden_god_rays":
                part_instance = MEGA04()
            elif part_name == "still93_beyond_the_balls":
                part_instance = MEGA05()
            elif part_name == "still93_keep_it_cool":
                part_instance = MEGA06()
            elif part_name == "still93_even_good_things_have_to_end":
                part_instance = MEGA07()
            else:
                raise ValueError(f"'{part_name}' not supported.")

            module.runtime_hook = part_instance
            spec.loader.exec_module(module)

mega_parts = [
    'still93_we_still_make_cracktros.py',
    'still93_pixel_apocalypse.py',
    'still93_julia_my_love.py',
    'still93_golden_god_rays.py',
    'still93_beyond_the_balls.py',
    'still93_keep_it_cool.py',
    'still93_even_good_things_have_to_end.py',
]

runtime_hook = RuntimeHook()
runtime_hook.execute_scripts(mega_parts)
