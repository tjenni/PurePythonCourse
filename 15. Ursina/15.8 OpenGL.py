# https://metamost.com/post/tech/opengl-with-python/01-opengl-with-python/


import glfw
from OpenGL.GL import *
import numpy as np
import ctypes

# Daten für ein einfaches Dreieck
TRIANGLE_VERTICES = np.array([
    -0.5, -0.5, 0.0,  # Untere linke Ecke
     0.5, -0.5, 0.0,  # Untere rechte Ecke
     0.0,  0.5, 0.0   # Obere Ecke
], dtype=np.float32)

# Shader-Quellcode
VERTEX_SHADER = """
#version 120
attribute vec3 position;

void main() {
    gl_Position = vec4(position, 1.0);
}
"""

FRAGMENT_SHADER = """
#version 120
void main() {
    gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);  // Rot
}
"""

def compile_shader(source, shader_type):
    
    
    buff = ctypes.create_string_buffer(source.encode('utf-8'))
    c_source = ctypes.cast(ctypes.pointer(ctypes.pointer(buff)), ctypes.POINTER(ctypes.POINTER(GLchar)))
    
    
    shader = glCreateShader(shader_type)
    
    
    glShaderSource(shader, 1, c_source, None)
    
    
    
    glCompileShader(shader)
    
    
    if glGetShaderiv(shader, GL_COMPILE_STATUS) != GL_TRUE:
        raise RuntimeError(glGetShaderInfoLog(shader).decode())
    
    
    return shader



def create_shader_program():
    vertex_shader = compile_shader(VERTEX_SHADER, GL_VERTEX_SHADER)
    fragment_shader = compile_shader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
    program = glCreateProgram()
    glAttachShader(program, vertex_shader)
    glAttachShader(program, fragment_shader)
    glLinkProgram(program)
    if glGetProgramiv(program, GL_LINK_STATUS) != GL_TRUE:
        raise RuntimeError(glGetProgramInfoLog(program).decode())
    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)
    return program

def main():
    # GLFW initialisieren
    if not glfw.init():
        raise Exception("GLFW konnte nicht initialisiert werden.")

    # Fenster erstellen
    window = glfw.create_window(800, 600, "GLFW Einfaches Beispiel", None, None)
    if not window:
        glfw.terminate()
        raise Exception("Fenster konnte nicht erstellt werden.")

    glfw.make_context_current(window)

    # Shader erstellen
    shader_program = create_shader_program()

    # VBO erstellen
    VBO = GLuint(0)
    glGenBuffers(1, ctypes.byref(VBO))

    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(
        GL_ARRAY_BUFFER,
        TRIANGLE_VERTICES.nbytes,
        TRIANGLE_VERTICES.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
        GL_STATIC_DRAW
    )

    # Vertex-Attribut festlegen
    position_loc = glGetAttribLocation(shader_program, "position")
    glEnableVertexAttribArray(position_loc)
    glVertexAttribPointer(position_loc, 3, GL_FLOAT, GL_FALSE, 0, None)

    # Hauptschleife
    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClearColor(0.2, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(shader_program)

        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glDrawArrays(GL_TRIANGLES, 0, 3)

        glfw.swap_buffers(window)

    # Ressourcen freigeben
    glDeleteBuffers(1, ctypes.byref(VBO))
    glfw.terminate()

if __name__ == "__main__":
    main()