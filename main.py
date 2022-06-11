import subprocess as subp 

from time import sleep

"""
THIS FILE MUST BE IN YOUR ROOT DIRECTORY
FOR EXAMPLE
ALL OF MY PROJECT TYPES (completed_onUpdates, currently_building, and personal)
ARE ALL LOCATED WITHIN MY ROOT DIRECTORY myProjects.

NOTE: IF YOU PLACE THIS FILE ANYWHERE ELSE WITHIN YOUR FILE STRUCTURE,
YOU WILL NEED TO UPDATE THE DIRECTORY PATHS ACCORDINGLY! THIS FILE IS 
SETUP TO BE IN A SPECIFIC FILE STRUCTURE WHICH IS SHOWN BELOW

myProjects/ <- main working directory.
|   -myProjects_completed_onUpdates/ <- where your completed projects will go <- manually move completed projects here
|   |   -project_one/
|   |   -project_two/
|   -myProjects_currently_building/ <- where projects your currently workin on will go <- create projects here. choose option B
|   |   -project_one/
|   |   -project_two/
|   -myProjects_personal/ <- create projects here that are your personal projects i.e. tutorials/examples/etc
|   |   -project_one/
|   |   -project_two/
"""

"""
couldn't figure out what to put in the init method to initialize the init method, so I created a thinker function. 

The thinker function allows only one process to one run at the time as when the script starts, it activates on only one port. 
I don't know how to verify this to you, as I'm not experienced with machine learning, but after 20+ test cases, I can tell you
that they do not all run at the same time.

By putting in return True at the end of each function, the next function call waits for the previous function call to return True before continuing. 
By pythons compiler, if a function is set to return True, once the code inside is completed, and the code errors, it will stop the script and 
display the error to the console.
"""

"""
Future Plans:
- Re-Write For Custom Directory Input
- Incorporate Functions To Allow The User To Move A Completed Project To The Completed Folder
- Create A Working UI Using PySide6 To Allow User-Friendly UI For Easier Access
"""


# initiate the class
# future plans of custom directory input
# future plans of functions to allow moving directories to completed
class CreateReactApp:
    def __init__(self):
        self.start() # start the thinker function

    def start(self):
        # obtain desired path
        path = self.get_path()

        # pass path and get name
        name = self.get_name(path)
        
        # create the app
        self.create_app(name)

        # install necessary dependencies
        self.run_installs(name)

        # open the new project in a vscode workspace
        self.launch_code(name)

        # launch the app using npm start within the new projects directory
        self.launch_app(name)

        # print compelted to the terminal to show class finished
        print("completed")


    # here we obtain the desired path the user wants to create the new
    # project in.
    def get_path(self):
        # initialize options for iteration => less code
        # options are editable to fit your desired root directory.
        # ^^^ See file structure and comments above
        options = ["A) ./myProjects_completed_onUpdates", "B) ./myProjects_currently_building", "C) ./myProjects_personal"]

        # get user input of a, b, or c
        selection_one = input("Select The Directory:\n {}\n".format("\n".join(options)))

        # create a blank path variable
        path = ""

        # depict user input. depending on the letter the user chose,
        # re-write the blank path variable to match the desired path
        if selection_one.lower() == "a":
            path += "./myProjects_completed_onUpdates/"
        elif selection_one.lower() == "b":
            path += "./myProjects_currently_building/"
        elif selection_one.lower() == "c":
            path += "./myProjects_personal/"
        else:
            """
            If for some reason the path chosen does not exist,
            you have/have not created/deleted the inner stuctures,
            or this file is not in the correct root folder. This
            file paths directory is ./Documents/myProjects/main.py
            """
            print("Invalid Operation")

        # if path exists, return it. If no return, next call doesn't happen
        return path

    """
    YOU WILL NOTICE THAT THE VARIABLE X IS USED IN EACH FUNCTION.
    IT IS OK! EACH FUNCTION CALL RESETS THE VARIABLE 'X' TO BE
    EMPTY
    """

    # create the app and use x for the path that was passed
    def create_app(self, x):
        # using subprocess which was imported as subp, we'll call
        # npx to create-react-app with our apps name
        new_app = subp.run(["npx create-react-app {}".format(x)], shell=True)

        # return True to make the next function call wait
        return True


    # here we obtian the desired name for the project
    def get_name(self, x):
        # npx create-react-app has specific instructions
        # as to what the name of the project can contain
        # you're allowed spaces, but no special characters
        # so as a friendly reminder to the user, we print
        # the rules shown below.
        print("Project Names Must Be:")
        print("1) all alphabetical letters")
        print("2) all lowercase letters")
        print("3) No Numbers or Special Characters!")

        # get user input
        name_of_proj = input("Enter Name Of Project:\n")

        # when created a new directory, spaces are considered
        # a new name, thus if we run npx create-react-app new app
        # it will create the app but only under the project name 'new' 
        # so we remove all of the blank spaces in the name. 
        # if you want underscores '_' instead of no spaces, then 
        # change the .replace() method
        fixed_name = name_of_proj.replace(" ","")

        # add the chosen director, and the name of the project together
        # into a new name variable to return back to the thinker
        # function to pass along where needed. If you do not keep the
        # "/" attached to the end of fixed_name, then this program
        # will error out as it no longer recognizes the name of the
        # project as a directory
        new_name = x + fixed_name + "/"

        # again, return the variable new_name so that the next function
        # call can be told to run.
        return new_name
        

    # now we're going to iterate through our dependencies that we know
    # that we will need for our new project. This is editable. To add a
    # new dependency, you just place it in the list. If you don't know
    # how to do that, go back to the basics and learn list comprehension
    def run_installs(self, x):
        # create the first part of the string with the mandatory commands
        # that are initialy typed when creating a new react app via the 
        # terminal and having a prefix of where to create that new react
        # app
        cmd = "npm install --save --prefix " 

        # rename x for readability
        where = x
        
        # create our list of dependencies
        to_install = ["react-router-dom", "styled-components", "express", "mongoose", "axios", "mongodb", "nodemon"]

        # create a new, blank list for later use
        to_execute = []

        # iterate through our list to_install
        for item in to_install:
            # create our new command line entry
            to_push = cmd + " " + where + " " + item

            # append our new command line entry to our new, blank array
            to_execute.append(to_push)

        # iterate through our newly created, previously blank, array
        for item in to_execute:
            # run each newly created command through the terminal
            # to install each dependency. This is the equivalent to
            # opening the terminal and running
            # npm install --save --prefix <path> <library_name> && repeat && repeat
            # as a long long one line command
            subp.run([item], shell=True)

        # again, return so that next function call can go
        return True

    
    # here we just simply tell the terminal to open
    # our newly created project in visual studio code.
    # future updates will show a list of supported 
    # text editors to choose from with their appropriate
    # subprocess calls
    def launch_code(self, x):
        subp.run(["cd {} && code ./".format(x)], shell=True)

        # return True for next function call to execute
        return True


    # here we just simply launch the app. This is the same as
    # opening a new terminal in your vscode workspace and typing
    # npm start. 
    def launch_app(self, x):
        subp.run(["cd {} && npm start".format(x)], shell=True)

        return True


# since it's a class, we use this pretty
# way of running it here instead of having 
# a list of function calls one after another
if __name__ == '__main__':
    CreateReactApp()