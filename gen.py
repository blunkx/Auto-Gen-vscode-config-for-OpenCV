import json
import os
import subprocess
import sys


def write_json(file_name, json_file):
    """
    If the file is not exist, throw an exception.
    Args:
        file_name(str): file name to write
    Returns:
        None
    """
    json_path = os.path.join(os.getcwd(), file_name)
    try:
        with open(json_path, "w+") as input_file:
            json.dump(json_file, input_file, indent=4)
            print("Successfully generated ", file_name)
    except Exception:
        print("Failed to open!")
        sys.exit()


def read_json(file_name):
    """
    If the file is not exist, throw an exception.
    Args:
        file_name(str): file name to read
    Returns:
        json.load(input_file)(dict): Data read from json
    """
    json_path = os.path.join(os.getcwd(), file_name)
    try:
        with open(json_path) as input_file:
            return json.load(input_file)
    except Exception:
        print("Failed to open!")
        sys.exit()


"""
def execute_cmd(cmd):
    # subprocess.run(["brew", "install", "opencv"], stdout=subprocess.PIPE)
    process = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    # wait for the process to terminate
    out, err = process.communicate()
    # errcode = process.returncode
    out = out.decode("utf-8")
    err = err.decode("utf-8")
    print("out = ", out)
    print("err = ", err)
"""


def execute_cmd(cmd):
    try:
        output = subprocess.check_output(
            cmd,
            stderr=subprocess.STDOUT,
            shell=True,
            timeout=3,
            universal_newlines=True,
        )
    except subprocess.CalledProcessError as exc:
        print("Status : FAIL %d\n" % exc.returncode)
        l = list(exc.output)
        s = "".join(l)
        print(s)
        sys.exit()
    else:
        return output


def parse_and_add(data, properties, tasks):
    l = data.split(" ")
    a = []
    a.append
    for each in l:
        op = each.replace("\n", "")[:2]
        para = each.replace("\n", "")[2:]
        if op == "-I":
            properties["configurations"][0]["includePath"].append(para)
        tasks["tasks"][0]["args"].append(op)
        tasks["tasks"][0]["args"].append(para)
    # print(tasks["tasks"][0]["args"])


c_cpp_properties = read_json("c_cpp_properties.json")
tasks = read_json("tasks.json")

parse_and_add(
    execute_cmd("pkg-config --cflags --libs opencv4"), c_cpp_properties, tasks
)
write_json("gen_c_cpp_properties.json", c_cpp_properties)
write_json("gen_tasks.json", tasks)
