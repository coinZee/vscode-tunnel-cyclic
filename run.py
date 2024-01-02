import subprocess

#gr = "python gr.py"
main = "python app.py"

#grpr = subprocess.Popen(gr, shell=True)
mainpr = subprocess.Popen(main, shell=True)

#grpr.wait()
mainpr.wait()
