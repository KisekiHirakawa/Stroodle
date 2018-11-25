from nltk.stem import PorterStemmer
#from nltk.tokenize import sent_tokenize, word_tokenize

# TODO: Word2Vec

# Names
names = ["John", "Donald"]

# colours
colours = ["red", "blue", "green", "yellow", "orange", "pink", "purple"]

# key story phrases
story_phrases = ["Once upon a time", "time"]

# kinematic action words
kinematics = ["walking", "running", "jumping", "skipping"]

# short clip sound effects - dictionary
sound_effects = {"thunder":"Storm_exclamation.mp3", 
                 "roar":"European_Dragon_Roaring_and_breathe_fire-daniel-simon.mp3",
                 "warrior":" ",
                 "fire":" "}

# audio clips
negative_music = 'Beethoven-MoonlightSonata.mp3'    
positive_music = 'SCOTT_JOPLIN_The_Entertainer.mp3'



def remove_unwanted_words(search_term):
    search_list = search_term.split(' ')
    for i in search_list:
        if i in colours or i in names or i in story_phrases:
            search_list.remove(i)
    
    search_term = ' '.join(search_list)
    #print(search_term)
    
    return search_term
    


def which_background_audio(sentiment):
    
    #sentiment - tuple (value, type) - HIGHEST amongst all
    # keywords is a list
    audio_clip = ' '
    try:
        if sentiment[1] == 'Neutral' or 'Mixed':
            return None
        
        elif sentiment[1] == 'Negative':
            audio_clip = negative_music
        elif sentiment[1] == 'Positive':
            audio_clip = positive_music 
            
    except:
        audio_clip = ' '
        
    return audio_clip

def which_sound_effect(search_term):
    
    keywords = search_term.split(' ')
    ps = PorterStemmer()
    
    #print(sound_effects.keys)
    try:
        for word in keywords:
            print(ps.stem(word))
            if ps.stem(word) in sound_effects.keys():
                key = ps.stem(word)
            
        audio_clip = sound_effects[key]
        #print(audio_clip)
    except:
        audio_clip = ' '
    
    return audio_clip
    
#print(which_sound_effect('thunder waits'))
#remove_unwanted_words('red dragon thunder')    
#print(which_background_audio(0.5))