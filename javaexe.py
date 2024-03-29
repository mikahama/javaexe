# -*- coding: utf-8 -*- 
import subprocess
import os
jar = "program.jar"
execute=  "java.exe -jar &jar&"
import sys


#load settings
try:
        ini_path = os.path.dirname(os.path.abspath(sys.argv[0])) + "\\" + "options.ini"
        ini = open(ini_path, "r")
        correct_group = False
        for line in ini:
                if line.startswith("["):#if it's a group
                        if line.startswith("[javaexe]"):#if it's the correct group
                                correct_group = True
                        else:#if the group is not correct
                                correct_group = False
                elif correct_group:#if it's an item in the correct group
                        line = line.replace("\r","")#remove linebreaks
                        line = line.replace("\n","")
                        if line.startswith("jar="):
                                jar = line[4:]
                        elif line.startswith("execute="):
                                execute= line[8:]

except:#or use the defaults
        pass

#Execute java
if not ":" in jar:#resolve the absolute path
        jar = os.path.dirname(os.path.abspath(sys.argv[0])) + "\\" + jar
        jar = os.path.abspath(jar)
commands = execute.split(" ")
index=0
for command in commands:#replace &jar& with the actual path to the java file
        if command == "&jar&":
                commands[index] = jar
                break
        index = index+1
try:
        commands = commands + sys.argv[1:]
        p=subprocess.Popen(commands)
except:
        import java_window