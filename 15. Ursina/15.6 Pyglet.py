'''
# OPENGL Version
import glfw
from pyglet.gl import *
import ctypes

if not glfw.init():
    raise Exception("GLFW konnte nicht initialisiert werden.")

window = glfw.create_window(800, 600, "OpenGL Version Check", None, None)
if not window:
    glfw.terminate()
    raise Exception("Fenster konnte nicht erstellt werden.")

glfw.make_context_current(window)

version = ctypes.cast(gl.glGetString(GL_VERSION), ctypes.c_char_p).value.decode()

print(f"Unterstützte OpenGL-Version: {version}")
glfw.terminate()

'''




import glfw
from pyglet.gl import *
import numpy as np
import glm  # Für Matrizen und Vektorrechnungen
import ctypes
import glm

# Vertex Shader (für Position und Farbe)
VERTEX_SHADER = """
#version 120
attribute vec3 aPos;   // Position des Vertex
attribute vec3 aColor; // Farbe des Vertex

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

varying vec3 ourColor; // Farbe an den Fragment-Shader weitergeben

void main() {
    gl_Position = projection * view * model * vec4(aPos, 1.0);
    ourColor = aColor;
}
"""

# Fragment Shader (für Farbausgabe)
FRAGMENT_SHADER = """
#version 120
varying vec3 ourColor; // Eingabefarbe vom Vertex-Shader

void main() {
    gl_FragColor = vec4(ourColor, 1.0); // Setze die Farbe
}
"""

# Daten für einen Würfel
CUBE_VERTICES = np.array([
    # Position         # Farbe
    -0.5, -0.5, -0.5,  1.0, 0.0, 0.0,
     0.5, -0.5, -0.5,  0.0, 1.0, 0.0,
     0.5,  0.5, -0.5,  0.0, 0.0, 1.0,
    -0.5,  0.5, -0.5,  1.0, 1.0, 0.0,
    -0.5, -0.5,  0.5,  1.0, 0.0, 1.0,
     0.5, -0.5,  0.5,  0.0, 1.0, 1.0,
     0.5,  0.5,  0.5,  1.0, 1.0, 1.0,
    -0.5,  0.5,  0.5,  0.0, 0.0, 0.0
], dtype=np.float32)

CUBE_INDICES = np.array([
    0, 1, 2, 2, 3, 0,  # Back face
    4, 5, 6, 6, 7, 4,  # Front face
    0, 4, 7, 7, 3, 0,  # Left face
    1, 5, 6, 6, 2, 1,  # Right face
    3, 7, 6, 6, 2, 3,  # Top face
    0, 4, 5, 5, 1, 0   # Bottom face
], dtype=np.uint32)


def _shaderSource(text, shader_type=GL_VERTEX_SHADER):
    buff = ctypes.create_string_buffer(text.encode('utf-8'))
    c_text = ctypes.cast(ctypes.pointer(ctypes.pointer(buff)), ctypes.POINTER(ctypes.POINTER(GLchar)))
    shader = glCreateShader(shader_type)
    glShaderSource(shader, 1, c_text, None)
    return shader


def compile_shader(source, shader_type):
    shader = _shaderSource(source, shader_type)
    
    glCompileShader(shader)
    
    status = ctypes.c_int(0)
    glGetShaderiv(shader, GL_COMPILE_STATUS, ctypes.byref(status))

    if status.value != GL_TRUE:
        raise GLException("The shader failed to compile. ",
                                  "\n{0}".format(_get_shader_log(shader)))
    
    return shader

def _get_shader_log(shader_id):
    log_length = ctypes.c_int(0)
    
    glGetShaderiv(shader_id, GL_INFO_LOG_LENGTH, ctypes.byref(log_length))
    
    result_str = ctypes.create_string_buffer(log_length.value)
    
    glGetShaderInfoLog(shader_id, log_length, None, result_str)
    
    if result_str.value:
        return ("OpenGL returned the following message when compiling the shader: "
                "\n{0}".format(result_str.value.decode('utf8')))
    else:
        return "Compiled {0} shader successfully.".format(self.type)

def _get_program_info_log(program_id):
    log_length = ctypes.c_int(0)
    result_str = ctypes.create_string_buffer(log_length.value)
    
    glGetProgramInfoLog(program_id, log_length, None, result_str)
    
    if result_str.value:
        return ("OpenGL returned the following message when compiling the shader: "
                "\n{0}".format(result_str.value.decode('utf8')))
    else:
        return "Compiled shader successfully."


def create_shader_program(vertex_source, fragment_source):
    vertex_shader = compile_shader(vertex_source, GL_VERTEX_SHADER)
    fragment_shader = compile_shader(fragment_source, GL_FRAGMENT_SHADER)
    program = glCreateProgram()
    glAttachShader(program, vertex_shader)
    glAttachShader(program, fragment_shader)
    glLinkProgram(program)
    
    status = ctypes.c_int(0)
    glGetProgramiv(program, GL_LINK_STATUS, ctypes.byref(status))
    
    if status == GL_TRUE:
        raise RuntimeError(_get_program_info_log(program))
    
    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)
    return program

def main():
    # Initialisierung von GLFW
    if not glfw.init():
        raise Exception("GLFW konnte nicht initialisiert werden.")

    window = glfw.create_window(800, 600, "OpenGL 3.3 Würfel", None, None)
    if not window:
        glfw.terminate()
        raise Exception("Fenster konnte nicht erstellt werden.")
    
    glfw.make_context_current(window)
    glEnable(GL_DEPTH_TEST)

    # Shader erstellen
    shader_program = create_shader_program(VERTEX_SHADER, FRAGMENT_SHADER)

    # VBO und EBO erstellen
    VBO = GLuint(0)
    EBO = GLuint(0)
    glGenBuffers(1, ctypes.byref(VBO))
    glGenBuffers(1, ctypes.byref(EBO))

    # Vertex-Daten in den VBO laden
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(
        GL_ARRAY_BUFFER, 
        CUBE_VERTICES.nbytes, 
        CUBE_VERTICES.ctypes.data_as(ctypes.POINTER(ctypes.c_float)), 
        GL_STATIC_DRAW
    )

    # Indizes in den EBO laden
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    glBufferData(
        GL_ELEMENT_ARRAY_BUFFER, 
        CUBE_INDICES.nbytes, 
        CUBE_INDICES.ctypes.data_as(ctypes.POINTER(ctypes.c_uint)), 
        GL_STATIC_DRAW
    )
    
    # Vertex-Attribut 0: Position
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * CUBE_VERTICES.itemsize, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    # Vertex-Attribut 1: Farbe
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * CUBE_VERTICES.itemsize, ctypes.c_void_p(3 * CUBE_VERTICES.itemsize))
    glEnableVertexAttribArray(1)

    #glBindVertexArray(0)

    # Matrizen erstellen
    model = glm.mat4()
    view = glm.translate(glm.mat4(1.0), glm.vec3(0, 0, -5))
    projection = glm.perspective(glm.radians(45.0), 800 / 600, 0.1, 100.0)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClearColor(0.2, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glUseProgram(shader_program)

        # Uniforms setzen
        model_loc = glGetUniformLocation(shader_program, "model")
        view_loc = glGetUniformLocation(shader_program, "view")
        proj_loc = glGetUniformLocation(shader_program, "projection")

        glUniformMatrix4fv(model_loc, 1, GL_FALSE, glm.value_ptr(model))
        glUniformMatrix4fv(view_loc, 1, GL_FALSE, glm.value_ptr(view))
        glUniformMatrix4fv(proj_loc, 1, GL_FALSE, glm.value_ptr(projection))

        glBindVertexArray(VAO)
        glDrawElements(GL_TRIANGLES, len(CUBE_INDICES), GL_UNSIGNED_INT, None)
        glBindVertexArray(0)

        glfw.swap_buffers(window)

    # Ressourcen freigeben
    glDeleteVertexArrays(1, VAO)
    glDeleteBuffers(1, VBO)
    glDeleteBuffers(1, EBO)
    glfw.terminate()

if __name__ == "__main__":
    main()