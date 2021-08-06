# Basic-NLP-app
To run the app, you have to clone into this repo and make sure you have all the required packages installed.
To do so, run the following comand in your terminal ```pip install -r requirements.txt ``` (make sure you are in the directory of the repo).

In the terminal execute the following command ```streamlit run app.py```
This will open a localhost webpage in your default browser (google chrome recommended). 
To use the app in the different browser - copy the output of the command in the terminal in a form of a **host:port** (192.168.0.120:8501) and paste it in the search string.

When you have the app up and running, you have to choose the language from the dropdown list. The helping error messages will guide you in case of a problem.
Next you are presented with the following options:
- Extract tokens and lemmas from the given text. To check this out, insert the text in the text area and press the 'Analyze' button.
- Perform the default NER from spaCy library, available in the open source. Insert the desired piece of the text and press the 'Extract Entities' button. You will be given the json file containing all the labled words and phrases.
- Perform the default NER from Flair library, available in the open source. Insert the desired piece of the text and press the 'Extract Entities' button. You will be given the json file containing all the labled words and phrases.
- Perform the custom NER, that detects words and phrases labled with 'LOCATION', 'FRUIT', 'DISEASE' and 'POLLUTION'. 
  To test it you may utilize the following sentence, for instance: **Radioactive bananas are thrown into rubbish bins in Berlin.** 
  Insert the desired piece of the text and press the 'Extract Entities' button. You will be given the json file containing all the labled words and phrases.
- Get the summary of the text using statistical frequencies. To test it -- insert the piece of text into the Text area and press the 'Summarize' button. You will receive the info from the text in a nutshell.
