Use the pwd and ls commands to browse directories in your Linux file system

You can interact with the Linux shell by entering commands into the Linux terminal

The pwd command prints the path name to the present working directory

The ls command lists the contents of a directory



Tab completion:

In this exercise, you will use tab completion to quickly enter a command to navigate to the Pictures directory.



If you type:



1

\~ $ cd P

Copied!

and press Tab, the shell will autocomplete the command to:



1

\~ $ cd Pictures/

because the Pictures directory is the only directory within your current folder that starts with a "P".



In this exercise, you will explore directories using the cd command.



Recall the symbols used to navigate to special paths:



Symbol	Stands for path to

\~	      Home directory

/	      Root directory

.	      Current directory

..	      Parent directory





1\. List the contents of the root directory.

ls /



2\. Change directories to your default home directory



cd \~



3\. Verify your current working directory is



pwd





Linux terminal tips

Use tab completion to autocomplete pathnames and command names.



Scroll through your command history with the Up Arrow and Down Arrow keys to find and re-run a command you already used.



Getting information

Display the reference manual for the ls command:

1

man ls

Copied!

Browsing and navigating directories

Special paths

Symbol	Represents path to

\~	home directory

/	root directory

.	present working directory

..	parent of present working directory

List files and directories in the current directory:

1

ls

Copied!

List files and directories in a directory:

1

ls path\_to\_directory

Copied!

Return path to present working directory:

1

pwd

Copied!

Change the current directory to a subdirectory:

1

cd child\_directory\_name

Copied!

Tip: Because cd looks in the current directory for child\_directory\_name, you don’t need to type the entire path.



Change the current directory:

Up one level: cd ../



To home: cd \~ or cd



To some other directory: cd path\_to\_directory



Change the current directory to another one at the same level:

Suppose you have two sibling directories within the same directory, dir\_1 and dir\_2, and your present working directory is dir\_1. To switch to dir\_2, enter:



cd ../dir\_2



Tip: Using .., you don't need to know the path to the parent directory to switch to a sibling.



Change the current directory back to the directory you were in previously:

cd -



Upgrading and installing packages

Fetch and display up-to-date information about all upgradable packages:

1

sudo apt update

Copied!

Upgrade to the latest supported version of nano:

1

sudo apt upgrade nano

Copied!

Install Vim:

1

sudo apt install vim

Copied!

Creating and editing files

Create a new text file and open it with nano:

1

nano file\_name.txt

Copied!

Tip: If the file already exists, nano simply opens it for editing.



Key	Sorts by

m	Memory Usage

p	CPU Usage

n	Process ID (PID)

t	Running Time





Special    Character	Effect

\\n	     Start a new line

\\t	     Insert a tab





Specifier	Explanation

%d	Displays the day of the month (01 to 31)

%h	Displays the abbreviated month name (Jan to Dec)

%m	Displays the month of year (01 to 12)

%Y	Displays the four-digit year

%T	Displays the time in 24 hour format as HH:MM:SS

%H	Displays the hour





In this lab, you learned that you can use the commands:



whoami   to return your username

uname    to print the kernel name

id       to display the user and group id

df       to print available disk space

ps       to list running processes and their process id

top      to view a real-time table of processes

echo     to print given text

date     to display the current time and date

man      to get the user manual for a command







In this lab, you learned that you can use the commands:



pwd    to get the location of your present working directory

ls     to list the files and directories within a directory

mkdir  to create a new directory

cd     to change your present working directory

touch  to create a new file

find   to search for and locate files

rm     to remove a file

mv     to rename or move a file

cp     to copy a file









In Linux First you need enter into the directory after that you need to create a txt file using "touch command"

then you need use "nano or vim to edit or modify" the content press "Ctl + X then Y and then Enter "

To print the content in the direc you need to use the "cat command in the Linux"





\--------------------------------------------------------------------------------------------------------------------------------------------------------------------------





**🧭 Linux Learning Roadmap (Beginner → Advanced → Projects)**



**🟢 Phase 1: Linux Basics (Foundation)**



Goal: Become comfortable with terminal and file system

Concepts to learn:



What is Linux? (Kernel, distro, shell)

Directory structure (/, /home, /etc, /var)

Types of users (root vs normal user)



**Must-know commands:**



pwd        # Show current directory

ls         # List files

cd         # Change directory

mkdir      # Create folder

rm         # Remove files/folders

cp         # Copy files

mv         # Move/rename files

cat        # View file

nano       # Edit file

✅ Practice:



Create folders and files

Navigate between directories

Copy and rename files





**🟡 Phase 2: Intermediate Linux (Daily Usage)**



Goal: Work efficiently like a developer/admin

Topics:



File permissions

Searching files

Package installation

Process management



**Important commands:**



chmod      # Change permissions

chown      # Change ownership

grep       # Search text

find       # Find files

apt/yum    # Package manager

ps         # Show running processes

top        # Monitor system

kill       # Stop process✅ Practice:



Change file permissions

Install software (e.g., git, curl)

Monitor CPU and memory usage





**🔵 Phase 3: Advanced Linux (System + Networking)**



Goal: Understand how Linux works behind the scenes



Topics:



Systemctl (services)

Networking basics

Logs and debugging

SSH and remote access



**Important commands:**



systemctl   # Manage services

journalctl  # View logs

ip a        # Show IP address

ping        # Check connectivity

ssh         # Remote login

netstat     # Network stats

``

✅ Practice:



Start/stop services (nginx, ssh)

Connect to remote server

Troubleshoot issues using logs





**🔴 Phase 4: Shell Scripting**



Goal: Automate tasks

Basics:



Variables

Loops

Conditions

Functions



Example:



\#!/bin/bash



for i in {1..5}

do

&#x20; echo "Hello $i"

done

``



✅ Practice:



Script to clean logs

Script to monitor disk usage

Script to automate backups





**🟣 Phase 5: Real-World Projects (VERY IMPORTANT)**



**💻 Project 1: Personal Linux Server**



Install Ubuntu Server

Configure SSH

Create users

Setup firewall





**🌐 Project 2: Web Server (DevOps Starter)**



Install Nginx/Apache

Host a static website

Configure domain (optional)

Setup HTTPS





**📊 Project 3: Monitoring System**



Install htop

Setup logging

Write script for alerts





**☁️ Project 4: Cloud + Linux (Matches your AWS interest)**



Launch EC2 instance

Connect via SSH

Deploy app on server

