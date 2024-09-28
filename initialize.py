def initialize():
    import random
    from jumbled import play
    all_words_collection={
                # List 1: 50 words containing 3 letters
        "list1":['cat', 'dog', 'sun', 'car', 'bat', 'pen', 'fan', 'box', 'hat', 'rat',
                'cow', 'pig', 'map', 'log', 'gem', 'net', 'egg', 'cup', 'pot', 'jet',
                'cut', 'zip', 'fun', 'sit', 'tip', 'top', 'bug', 'pit', 'key', 'gum',
                'hop', 'mix', 'gym', 'dry', 'fig', 'pop', 'ice', 'fix', 'run', 'bid',
                'hit', 'bit', 'mud', 'red', 'sip', 'lip', 'pad', 'nod', 'hen', 'joy'],

        # List 2: Words containing 4 to 5 letters
        "list2":['apple', 'grape', 'stone', 'drink', 'table', 'chair', 'bread', 'cloud', 
                'light', 'music', 'clock', 'plant', 'phone', 'water', 'juice', 'heart',
                'bread', 'flute', 'dance', 'dream', 'pride', 'smile', 'flash', 'space',
                'piano', 'paper', 'robot', 'mount', 'beach', 'shirt', 'badge', 'truck',
                'brain', 'swing', 'shirt', 'drama', 'hotel', 'fight', 'brave', 'lemon',
                'truth', 'chalk', 'write', 'paint', 'fruit', 'laugh', 'pilot', 'pouch',
                'grain', 'straw', 'crown', 'plant'],

        # List 3: Words containing 7 to 8 letters
        "list3": ['picture', 'product', 'machine', 'journey', 'balloon', 'holiday', 'morning', 
                'diamond', 'sunlight', 'training', 'giraffe', 'weather', 'festival', 'factory', 
                'mystery', 'scratch', 'baseball', 'mountain', 'umbrella', 'computer', 'cousins', 
                'traffic', 'blankets', 'explorer', 'together', 'internet', 'sandwich', 'program', 
                'sunshine', 'football', 'airplane', 'freedom', 'butterfly', 'elephant', 'medicine', 
                'skylight', 'hospital', 'strawberry', 'recovery', 'problems', 'birthday', 'designer', 
                'swimming', 'wildlife', 'building', 'delivery', 'backpack', 'wildlife', 'exchange', 
                'bedroom'],

        # List 4: Words containing 9 to 10 letters
        "list4":['television', 'generation', 'instrument', 'literature', 'photograph', 'volleyball',
                'navigation', 'adventure', 'basketball', 'impossible', 'revolution', 'understand', 
                'friendship', 'importance', 'department', 'employment', 'firefighter', 'motivation', 
                'population', 'expression', 'investment', 'leadership', 'protection', 'collection', 
                'chemistry', 'controller', 'foundation', 'reflection', 'conclusion', 'statement', 
                'assignment', 'connection', 'inspection', 'promotion', 'meditation', 'adrenaline', 
                'ingredient', 'prediction', 'tournament', 'journalism', 'entertain', 'celebration', 
                'production', 'population', 'occupation', 'leadership', 'historical', 'management', 
                'foundation', 'definition'],

        # List 5: Words containing more than 10 letters
        "list5" : ['communication', 'architecture', 'transportation', 'responsibility', 'international',
                'environmental', 'comprehension', 'investigation', 'qualification', 'concentration',
                'philosophical', 'appreciation', 'unbelievable', 'misunderstand', 'establishment',
                'documentation', 'administration', 'identification', 'recommendation', 'confrontation',
                'interpretation', 'representation', 'qualification', 'understanding', 'anticipation',
                'collaboration', 'misrepresentation', 'consideration', 'implementation', 'determination',
                'representation', 'responsibility', 'preparation', 'investigation', 'participation',
                'developmental', 'congratulation', 'communication', 'transformation', 'organization',
                'rehabilitation', 'infrastructure', 'exaggeration', 'imagination', 'conservation',
                'simplification', 'collaboration', 'complication', 'determination', 'classification']
    }
   
    print("WELCOME..")
    level = input("Please enter the difficulty level (from 1 to 5) ")
    dict_key = 'list'+level
 
    if dict_key in all_words_collection:
        list = all_words_collection[dict_key]
        random_word = random.choice(list)
        play(random_word)        
    else:
        print("please enter a valid number 1 to 5")
        
            
