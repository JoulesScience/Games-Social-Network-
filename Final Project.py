# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #
#

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know 
# what they are doing, having taken our web development class). However, it is 
# up to you to create a data structure that manages the game-network information 
# and to define several procedures that operate on the network. 
#
# In a website, the data is stored in a database. In our case, however, all the 
# information comes in a big string of text. Each pair of sentences in the text 
# is formatted as follows: 
# 
# <user> is connected to <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>.
#
# For example:
# 
# John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
# 
# Note that each sentence will be separated from the next by only a period. There will 
# not be whitespace or new lines between sentences.
# 
# Your friend records the information in that string based on user activity on 
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a user's profile.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two (e.g. lists of dictionaries). Pick one that
# will allow you to manage the data above and implement the procedures below. 
# 
# You may assume that <user> is a unique identifier for a user. For example, there
# can be at most one 'John' in the network. Furthermore, connections are not 
# symmetric - if 'Bob' is connected to 'Alice', it does not mean that 'Alice' is
# connected to 'Bob'.
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
# to define any additional helper procedures that can assist you in accomplishing 
# a task. You are encouraged to test your code by using print statements and the 
# Test Run button. 
# ----------------------------------------------------------------------------- 

# Example string input. Use it to test your code.
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information.
# 
# Arguments: 
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the 
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string 
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not 
#   list B's connections or liked games.
#   
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network with no users.
# 
# Return:
#   The newly created network data structure

def create_data_structure(string_input):
    ## create network Dict = {'user':[['user1','user2'],['game1, 'game2']]}
       
    network = {}

    if string_input == '':
        return network
    
    ## create list_users_connected
    text = sentences(string_input)
    list_users_connected = []
       
    for i in text[1]:
        list_users_connected.append(i.split(', '))

    ## create list_likes_play
    text1 = sentences(string_input)
    list_likes_play = []
       
    for a in text1[2]:
        list_likes_play.append(a.split(', '))
        
    for i in range(len(text[0])):
        network[text[0][i]] = [list_users_connected[i], list_likes_play[i]]
                                             
    return network    
    
   
def sentences(text):

    ##get sentences split '.'
    sentences = []    
    while len(text) > 0:
        point = text.find('.')
        sentences.append(text[:point])
        text = text[point+1:]

    ##get users
    users = []
    for sentence in sentences:
        if 'is connected to' in sentence:
            start = sentence.find('is connected to')
            users.append(sentence[:start-1])

    ##get users_connected
    users_connected = []
    frase = 'is connected to'
    longi = len(frase)

    for sentence in sentences:
        if 'is connected to' in sentence:
            start = sentence.find('is connected to')
            users_connected.append(sentence[start+longi+1:])

    ##get games
    games = []
    frase1 = 'likes to play'
    longi1 = len(frase1)

    for sentence in sentences:
        if 'likes to play' in sentence:
            start = sentence.find('likes to play')
            games.append(sentence[start+longi1+1:])                   

    return users, users_connected, games             


# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections that user has
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.
def get_connections(network, user):
    if user in network:
        if network[user][0] != []:
            return network[user][0]
        else:
            return []
    return None

# ----------------------------------------------------------------------------- 
# get_games_liked(network, user): 
#   Returns a list of all the games a user likes
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.
def get_games_liked(network,user):
    if user in network:
        if network[user][1] != []:
            return network[user][1]
        else:
            return []
    return None

# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: the gamer network data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.
def add_connection(network, user_A, user_B):
    if user_A in network and user_B in network:
        if user_B in network[user_A][0]:
            return network
        else:
            network[user_A][0].append(user_B)
        return network
    return False

# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. The new user 
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)
def add_new_user(network, user, games):
    if user in network:
        return network    
    network[user] = [[], games]      
    return network
		
# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.
# 
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.
def get_secondary_connections(network, user):
    second_connect = []
    if user not in network:
        return None
    if network[user][0]:
        for i in network[user][0]:
            for x in range(len(network[i][0])):
                if network[i][0][x] not in second_connect:
                    second_connect.append(network[i][0][x])      
        return second_connect  
    return []  

# ----------------------------------------------------------------------------- 	
# count_common_connections(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return: 
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.
def count_common_connections(network, user_A, user_B):
    count = 0
    if user_A in network and user_B in network:
        for i in network[user_A][0]:
            for x in network[user_B][0]:
                if i == x:
                    count += 1 
        return count

    else:
        return False

# ----------------------------------------------------------------------------- 
# find_path_to_friend(network, user_A, user_B): 
#   Finds a connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
#Sample output
#   >>> print find_path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hints: 
# - Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
# - If you are comfortable with default parameters, you might consider using one 
#   in this procedure to keep track of nodes already visited in your search. You 
#   may safely add default parameters since all calls used in the grading script 
#   will only include the arguments network, user_A, and user_B.

def find_path_to_friend(network, user_A, user_B, visited=None):       
    # your RECURSIVE solution here!
    
    if network == {}:
        return None
    if user_A not in network:
       return None
    if user_B not in network:
       return None       

    for i in network:
        if network[i][0] == []:
            return None 
        
    if visited == None:
        visited = {}

    path = None
    
    visited[user_A] = True    
        
    
    if user_A == user_B:
        return [user_B]
        
    for user in network[user_A][0]:        
        if user not in visited:
            path = find_path_to_friend(network, user, user_B, visited)
            if path != None:
                break
     
    if path != None:
        path.reverse()
        path.append(user_A)
        path.reverse()
    return path       


               
def find_path_to_friend2(network, user_A, user_B, visited = None):
	# your RECURSIVE solution here!
	
	if visited is None: visited = {}
	
	path = None
	if user_A not in network or user_B not in network: return None
	
	visited[user_A] = True
	if user_A == user_B: return [user_B]
	
	for friend in network[user_A][0]:
	    if friend not in visited: path = find_path_to_friend(network, friend, user_B, visited)
	    if path is not None: break
	
	if path is not None:
	    path.reverse()
	    path.append(user_A)
	    path.reverse()
	    print visited
	return path

    

##def buscar(x):
##    return [x]

    
      


##    nodes_visited = []
##    path = []
##
##    if network == {}:
##        return None
##    if user_A not in network:
##       return None
##    if user_B not in network:
##       return None       
##
##    for i in network:
##        if network[i][0] == []:
##            return None 
##        
##    if user_B in network[user_A][0]:
##        path.append(user_A)
##        path.append(user_B)
##        nodes_visited.append(user_A)
##
##        return path
##    
##    nodes_visited.append(user_A)
##    path.append(user_A)
##        
##    next_node = network[user_A][0]

##    for node in next_node:
##        if node in nodes_visited:
##            next_node.remove(node)
                       
##    while next_node:
##               
##        for user in next_node:
##            if user_B in network[user][0]:
##                return path + find_path_to_friend(network, user, user_B)
##                break
##
##
##            nodes_visited.append(user)
##            next_node2 = []
##            for user_2 in network[user][0]:
##                if user_2 not in nodes_visited:
##                    if user_2 not in next_node:
##                        next_node2.append(user_2)
##                        print nodes_visited, next_node2
##                        
##        
##        next_node = next_node2             
    

    #return path + find_path_to_friend(network, user, user_B)   

    
    

#GRACIAS DIOS


##def find_path_to_friend(network, user_A, user_B):       
##    # your RECURSIVE solution here!
##
##    nodes_visited = []
##    path = []
##
##    if user_B in network[user_A][0]:
##        path.append(user_A)
##        path.append(user_B)
##        nodes_visited.append(user_A)
##
##        return path, nodes_visited
##
##    for user in network[user_A][0]:
##        if user_B in network[user][0]:
##            path.append(user_A)
##            path.append(user)
##            path.append(user_B)
##            return path
##            
##        funciona pero pierde la ruta:
                    
##        for user in next_node:
##        if user_B in network[user][0]:
##            return path + find_path_to_friend(network, user, user_B)        
##
##
##        nodes_visited.append(user)
##        for user_2 in network[user][0]:
##            if user_2 not in nodes_visited:
##                if user_2 not in next_node:
##                    next_node.append(user_2)
##                    print nodes_visited
##

                    
##    
##    
##    
##
##    if user_B not in network[user_A][0]:
##        for node in network[user_A][0]:
##            if find_path_to_friend(network, network[node], user_B):
##                path.append(network[node])
##                path.append(user_B)
##                nodes_visited.append(network[node])
##            return path
##               
##            
##    
##
##    return None
##
##             
##        
##
##    
##
##
##def find_path_to_friend2(network, user_A, user_B):       
##    # your RECURSIVE solution here!
##
##
   
##
##    path = []
##    nodes_visited = []        
##    
##    if network == {}:
##        return None
##    if user_A or user_B not in network:
##        return None
##    if network[user_A][0] == []:
##        return None
##    
##    if user_A in network and user_B in network:
##        path.append(user_A)
##        if user_B in network[user_A][0]:
##            path.append(user_B)            
##    
##        
##        else:
##            for i in network[user_A][0]:
##                find_path_to_friend(network, i, user_B)
##                return path     
##                                
##                  
##    return None                    


##    path = []
##    nodes_visited = []        
##    
##    if network == {}:
##        return None
##    if user_A not in network:
##        return None
##    if network[user_A][0] == []:
##        return None
##    if user_B in network[user_A][0]:
##            path.append(user_A)
##            path.append(user_B)
##            return path
##            
##    
##    if user_A in network and user_B in network:
##        path.append(user_A)
##        if user_B in network[user_A][0]:
##            path.append(user_B)            
##    
##        
##        else:
##            for i in network[user_A][0]:                
##                if user_B in network[i][0]:
##                    path.append(i)
##                    path.append(user_B)
##                                
##
##            
##        return path
##               
##    return None   
                               
##        
##        path.append(user_A)
##        users = network[user_A][0]
##
##        for user in users:
##            if user_A in user:
##                path.append(user)
##            else:
##                return
##                  
##    return None 


        
##        if user_B in users:
##            #path.append(user_B)
##            return user_B 
##        else:
##            return None

        
##    for user in users:
##        if find_path_to_friend(network, user_A, user)  





##    if user_A in network and user_B in network:
##        path.append(user_A)
##        users = network[user_A][0]
##        if user_B in users:
##            path.append(user_B)
##            return path
##        else:
##            return None
##
##
##    nodes_visited = []
##  
##    for user in users:
##        if find_path_to_friend(network, user, user_B) == None:
##            nodes_visited.append(user)
##            
##         
     
##    path = []
##    
##        
##    if user_A in network and user_B in network:
##        path.append(user_A)
##        users = network[user_A][0]
##        if user_B in users:
##            path.append(user_B)
##            return path
##
##
##        else:
##            for user in users:
##                path1 = find_path_to_friend(network, user, user_B)
##                if path1 != None:
##                    return path.append(path1)
##                else:
##                    nodes_visited.append(user)
##                    for a in nodes_visited:
##                        return find_path_to_friend(network, a, user_B) 
##                    
##            
##    return None


# Make-Your-Own-Procedure (MYOP)
##recommend games based on the preferences of other users liked a same game

def recomend_game(network, game):
    user_liked = []
    for i in network:
        if game in network[i][1]:
            user_liked.append(i)

    games_recomended = []
    for x in user_liked:
        for y in network[x][1]:
            if game != y and y not in games_recomended:
                games_recomended.append(y)

    return games_recomended  
        

# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.

# Replace this with your own procedure! You can also uncomment the lines below
# to see how your code behaves. Have fun!

network = create_data_structure(example_input)
##print network
##print get_connections(net, "Debra")
##print get_connections(net, "Mercedes")
##print get_games_liked(net, "John")
##print add_connection(net, "John", "Freda")
##print add_new_user(net, "Debra", []) 
##print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
##print get_secondary_connections(net, "Mercedes")
##print count_common_connections(net, "Mercedes", "John")
##print find_path_to_friend(net, "John", "Ollie")
