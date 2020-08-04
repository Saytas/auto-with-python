#!/usr/bin/env python
# coding: utf-8

# # Final Project - Word Cloud

# For this project, you'll create a "word cloud" from a text by writing a script.  This script needs to process the text, remove punctuation, ignore case and words that do not contain all alphabets, count the frequencies, and ignore uninteresting or irrelevant words.  A dictionary is the output of the `calculate_frequencies` function.  The `wordcloud` module will then generate the image from your dictionary.

# For the input text of your script, you will need to provide a file that contains text only.  For the text itself, you can copy and paste the contents of a website you like.  Or you can use a site like [Project Gutenberg](https://www.gutenberg.org/) to find books that are available online.  You could see what word clouds you can get from famous books, like a Shakespeare play or a novel by Jane Austen. Save this as a .txt file somewhere on your computer.
# <br><br>
# Now you will need to upload your input file here so that your script will be able to process it.  To do the upload, you will need an uploader widget.  Run the following cell to perform all the installs and imports for your word cloud script and uploader widget.  It may take a minute for all of this to run and there will be a lot of output messages. But, be patient. Once you get the following final line of output, the code is done executing. Then you can continue on with the rest of the instructions for this notebook.
# <br><br>
# **Enabling notebook extension fileupload/extension...**
# <br>
# **- Validating: <font color =green>OK</font>**

# In[1]:


# Here are all the installs and imports you will need for your word cloud script and uploader widget

get_ipython().system('pip install wordcloud')
get_ipython().system('pip install fileupload')
get_ipython().system('pip install ipywidgets')
get_ipython().system('jupyter nbextension install --py --user fileupload')
get_ipython().system('jupyter nbextension enable --py fileupload')

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys


# Whew! That was a lot. All of the installs and imports for your word cloud script and uploader widget have been completed. 
# <br><br>
# **IMPORTANT!** If this was your first time running the above cell containing the installs and imports, you will need save this notebook now. Then under the File menu above,  select Close and Halt. When the notebook has completely shut down, reopen it. This is the only way the necessary changes will take affect.
# <br><br>
# To upload your text file, run the following cell that contains all the code for a custom uploader widget. Once you run this cell, a "Browse" button should appear below it. Click this button and navigate the window to locate your saved text file.

# In[2]:


# This is the uploader widget

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()


# The uploader widget saved the contents of your uploaded file into a string object named *file_contents* that your word cloud script can process. This was a lot of preliminary work, but you are now ready to begin your script. 

# Write a function in the cell below that iterates through the words in *file_contents*, removes punctuation, and counts the frequency of each word.  Oh, and be sure to make it ignore word case, words that do not contain all alphabets and boring words like "and" or "the".  Then use it in the `generate_from_frequencies` function to generate your very own word cloud!
# <br><br>
# **Hint:** Try storing the results of your iteration in a dictionary before passing them into wordcloud via the `generate_from_frequencies` function.

# In[3]:


# Working
def lowercase_list(file_contents):
    """Helper method to turn all the words to lowercase."""
    words = file_contents.split()
    lowercase_word_list = []
    for word in words:
        word = word.lower()
        lowercase_word_list.append(word)
    
    return lowercase_word_list



# Working
def remove_before_word_characters(file_contents, punctuations):
    """ Helper method removes the words before character """
    check = True
    words = file_contents
    new_list = []
    #count = 0
    for word_w in words:
        check = True
        #print("word_w:", word_w)
        for character in punctuations:
            #print("character:", character)
            if word_w[0] == character:
                check = False
                #print("word_w: ", word_w)
                #print("word_w[0]: ", word_w[0])
                #print(type(word_w[0]))
                fixed_word = word_w[1:]
                #print("fixed word: ", fixed_word)
                new_list.append(fixed_word)
        
        if check:
            new_list.append(word_w)
    
    return new_list



# Working
def remove_after_word_characters(file_contents, punctuations):
    """ Helper method removes the  words from after characters """
    check = True
    words = file_contents
    new_list = []
    #count = 0
    for word_w in words:
        check = True
        #print("word_w:", word_w)
        for character in punctuations:
            #print("character:", character)
            if word_w[-1] == character:
                check = False
                #print("word_w: ", word_w)
                #print("word_w[0]: ", word_w[0])
                #print(type(word_w[0]))
                fixed_word = word_w[:-1]
                #print("fixed word: ", fixed_word)
                new_list.append(fixed_word)
        
        if check:
            new_list.append(word_w)
    
    return new_list


# Working
def remove_uninteresting_words(file_contents, uninteresting_words):
    """ Helper method removes the uninteresting words from the list """
    new_words_list = file_contents
#     print("Length: ", len(new_words_list))
#     print(new_words_list)
#     print()
#     print("Length:", len(uninteresting_words))
#     print(uninteresting_words)
#     print()
    
    for word in new_words_list:
#         print("WORD IS:" + word)
        for unword in uninteresting_words:
            if word == unword:
#                 print("Word to remove: ", word)
                index = new_words_list.index(word)
#                 print("Word to remove index: ", new_words_list.index(word))
                #del word
                new_words_list.remove(word)
                break
    
#     print()
#     print("Length: ", len(new_words_list))
#     print(new_words_list)
#     print()
    
    return new_words_list



def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",     "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",     "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",     "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",     "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    word_counts = {}
    #words = file_contents.split()
    
    # First, make all the words lower case
    words = lowercase_list(file_contents)
    
    no_of_iteration = 0
    while no_of_iteration <= 10:
        # Second, remove before word characters
        words = remove_before_word_characters(words, punctuations)

        # Third, remove before word characters
        words = remove_after_word_characters(words, punctuations)
        
        no_of_iteration += 1
        
    
    
    # Fourth, remove all the uninteresting words
    iteration = 0
    while iteration <= 3:
        words = remove_uninteresting_words(words, uninteresting_words)
        iteration += 1
    
    #print(words)
    
    #print()
    deneme = words
    deneme.sort()
    #print(deneme)
    
    #print()
    deneme2 = words
    sorted(deneme2)
    #print(deneme2)
    
    #print(len(deneme2))
    for word in deneme:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
        #print(word)
    
    print(word_counts)
        

    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_counts)
    cloud.to_file("myfile.jpg")
    return cloud.to_array()


# In[4]:


calculate_frequencies(file_contents)


# In[5]:


print("Length", len(file_contents.split()))
print(file_contents.split())
print()


# If you have done everything correctly, your word cloud image should appear after running the cell below.  Fingers crossed!

# In[6]:


# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()


# If your word cloud image did not appear, go back and rework your `calculate_frequencies` function until you get the desired output.  Definitely check that you passed your frequecy count dictionary into the `generate_from_frequencies` function of `wordcloud`. Once you have correctly displayed your word cloud image, you are all done with this project. Nice work!

# In[ ]:




