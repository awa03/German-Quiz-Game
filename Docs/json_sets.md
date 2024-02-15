# Modifying The Json Set
The purpose of this documentation is to inform the user on how to manually add words and definitions to use to study with. While this project focuses on the german language the applications of this software are endless. This portion serves to act as a digital replacement to flash cards.

### Loading Files
Currently there is no in app way to load files given by the user. For now please navigate to the Windows directory, and then the Study Set directory. This can be done via commands as follows:
```sh
cd Windows/Study_Set
```
Then by modifying the active_set.json you can add words and definitions to study from. More documentation on how to complete the json modification can be found in the documentation folder: [Modifying Json Sets](Docs/json_sets.md)
****
### What You Will See
Once you have navigated the active set file you should see a file that contains something like this. The "Word" keyword represents the german word, while the "Definition" signifys the english translation. 

```json
[
  {
    "Word": "Ich",
    "Definition": "Nomative - I"
  },
  {
    "Word": "Du",
    "Definition": "Nomative - You"
  },
  {
    "Word": "Er",
    "Definition": "Nomative - He"
  },
 ]
```
****
### Adding Words
Adding words to this project is simple, yet it may be tedious. If needed there are many json generator such as [OBJGen](https://www.objgen.com/json/local/design) that may assist you. AI assistance may also be useful for simpler requests. Note that json syntax is extremely important to the function of this program, so ensure that the common issues are resolved before running the program.
Now in order to add a word we need to simply add another set of brackets, followed by a comma. Ensure that the Word and definition are wrapped in quotations. 
```json
[
  {
    "Word": "Ich",
    "Definition": "Nomative - I"
  },
  {
    "Word": "Du",
    "Definition": "Nomative - You"
  },
  {
    "Word": "Er",
    "Definition": "Nomative - He"
  },
  {
    "Word": "Added Word",
    "Definition": "Added Definition"
  },
 ]
```
> [!Note]
> Copy and pasting previously defined words, and editing the input maybe easier (syntactially) to generate new cards.
****
### Deleting Words
In order to delete a word from the active set we simply reverse the process of adding one. Remove the bracketed word of your choosing and youre all set to study!
****
### Common Issues
There are many issues that may arise in the creation of your json file. If this happens ask an ai assistant or json formatter for assistance, and if this doesnt resolve the issue feel free to email awa22@fsu.edu for further help. Additionally ensure all commas are present and the words are wrapped in quotes.
