# mid_termproject

ReadMe file:
Overview:
We possess a JSON file along with two Python scripts, both of which take the JSON file as input. One script outputs customer details such as names and phone numbers, while the other provides information about menu items, including their prices and the total number of orders received.
Customers.json file is the output of customer.py file and items.json file is output of items.py file.

Required Components:
1.Check Python Installation: 	First, you need to verify whether Python is already installed on your PC. You can do this by opening a command prompt or terminal and typing “python –version” or “python3 –version”. If Python is installed, it will display the version number. If not, you'll need to download and install Python 3.3 from the official Python website.
2. Install GitHub: To install GitHub on your PC, you can visit the GitHub website and download the GitHub Desktop application. Follow the installation instructions provided on the website to complete the installation process.
3.Install VS Code Editor: Visual Studio Code (VS Code) is a popular code editor that supports various programming languages, including Python. You can download the installer for VS Code from the official website and follow the installation instructions provided. Once installed, you can use VS Code to write and execute your Python programs.
4.Create a Repository on GitHub: After installing GitHub Desktop, you can launch the application and sign in with your GitHub account. Then, click on the "New Repository" button to create a new repository. Follow the prompts to set up the repository, including providing a name, description, and selecting options like public or private repository.
5. Add and Collaborate with rxt1077: Once the repository is created, you can add collaborators by navigating to the "Settings" tab of the repository on GitHub. In the "Collaborators" section, you can search for the username "rxt1077" and add them as a collaborator. This will grant them access to the repository, allowing them to view and contribute to the project.
6.Import Libraries: In your Python scripts, you may need to import various libraries or modules to access additional functionality. For example, you might import the “json” module to work with JSON data, or the “requests” module to make HTTP requests. To import a library, you can use the “import” keyword followed by the name of the library. 
For example:
 import json
import argparse
Ensure that any libraries you use are installed on your system using tools like “pip”, the Python package manager. You can install libraries using the command “pip install <library_name>” in your command prompt or terminal.
By following these steps, you can set up your development environment and collaborate on a Python project using GitHub.
Implementation:
1. Customer.py Implementation:
1)The “customers.py” file takes “example_orders.json” as input. In the main method, it calls the “read_object()” function, which opens and returns the JSON file. Then, it invokes “extract_customer_data()” to gather the required customer data, storing it in the variable “customer_data()”. Subsequently, it creates a “customers.json” file and writes the customer names and phone numbers into it.
2. Items.py Implementation:
1)The “Items.py” file also takes “example_orders.json” as input. In the main method, it calls “read_orders()” to open the input JSON file. Then, it proceeds to “process_items()” to extract the     items from the JSON file.
2)For each item in an order, the script checks whether the item already exists in the items dictionary. If not, it adds the item with its price and sets the order count to 1. If the item already exists, it increments the order count for that item by 1.
3)After processing, the main method creates a JSON file that contains the item names, prices, and the number of orders.
3.Execution and Output:
1) Both files should be placed in the same directory. Upon execution, two output files,   “customer.json” and “items.json”, are generated in the same directory.
2) These modifications ensure clarity and conciseness in describing the functionalities and implementation details of the scripts.
