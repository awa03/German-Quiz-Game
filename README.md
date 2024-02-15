# German Quiz Game
German Quiz Master is an engaging and educational quiz game designed to test your knowledge of the German language. Whether you're a beginner or an advanced learner, this interactive game offers a fun way to enhance your German vocabulary, grammar, and comprehension skills.

Featuring a sleek and intuitive user interface built with the Dear PyGui library, German Quiz Master provides a seamless gaming experience for players of all levels. The minimalist design ensures easy navigation and focus on the quiz questions, allowing users to immerse themselves in the learning process without distractions.

# Purpose
The purpose of this application is to train german skills, this project randomly generates german words, asking for the translation from the user. This allows users to tests words they may not have seen before. I am currently a student and have had difficulty learning german because of this I created this program to help me study. 

****
# Installation
>[!Note]
>For Windows users, the process may differ. For best results use Linux or Mac.

To install this project, follow these steps:
1. Clone the repository to your local machine:
   - ```
     git clone https://github.com/awa03/German-Quiz-Game.git
     ```
2. Navigate to the project directory:
   - ```sh
     cd German-Quiz-Game
     ```
4. Install the required dependencies:
   - ```sh
     sudo apt-get install pip
     ```
5. Run the setup script:
   - ```sh
     cd Setup
     ./Install.sh
     ```
If you would like to run the precompiled version simply navigate to the dist directory using the command.
```sh
      cd dist # Navigates To Directory
     ./main   # Launches the Program
```
This will allow you to run the program without needing to run any commands! You can also do this by opening the directory from your file browser and launching the application.
For more detailed instructions, refer to the [Installation Guide](Docs/installation.md).
****
# Loading Files
Currently there is no in app way to load files given by the user. For now please navigate to the Windows directory, and then the Study Set directory. This can be done via commands as follows:
```sh
cd Windows/Study_Set
```
Then by modifying the active_set.json you can add words and definitions to study from. More documentation on how to complete the json modification can be found in the documentation folder: [Modifying Json Sets](Docs/json_sets.md)

****
# Stretch Goals
- Card Matching
- Flash Cards ✅
- Load Data Set
  - Json ✅
  - TXT 
- Clean Up UI
  - Color Schemes
  - Light and Dark Mode
- Remake for Dotnet MAUI
  - Since there are many limitations of the GUI library I plan to migrate to dotnet Maui
- Highscore Feature ✅ 
- Game Settings
  - No Repeat Words
  - Multi word
  - Sentences
  - In app settings
- Override button
  - If the user spelled the word incorrectly but feels their answer is correct

