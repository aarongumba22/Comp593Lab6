###########################################
# created by : Aaron Gumba
#Lab 7
#date: March 26,2022
#
##################################
#import libraries
from urllib import request
import requests
from sys import argv

#function that checks the other functions below if its access
#takes the given argument of a specific pokemon
#prints out the pokemon details and Url of the pastebin
def main():   
  
  user= argv[1]
  pokemonDict = get_pokemon(user)

  if pokemonDict != None:
   pokemonstring= PasteBinOutput(pokemonDict)
  
   pasteurl=post_to_PasteBin(pokemonstring[0:100],pokemonstring[0:100])
   print(pasteurl)
  
  else:
        print("None")
  
# function that gathers the information of the pokemon such as the name, abilities,weight and height
#a forloop that iterates if it has more than 1 skill and save it 
def PasteBinOutput(pokemonDiction):
  
    print("Pokemon Information")
    pokemon = "Name = " + pokemonDiction['name'] + "\n"
    pokemon += "Weight = " + str(pokemonDiction['weight']) + "\n"
    pokemon += "Height = " + str(pokemonDiction['height']) + "\n"
    pokemon += "Type = -"
    for pokemonType in pokemonDiction['types']:
      pokemon += pokemonType['type']['name'] + "\n       "
      pokemon += "-"
    pokemon = pokemon[:-1]
    print (pokemon)
    return(pokemon)
  
  
#function that uses the api of pokemon character. checks  if it connects successfully   
def get_pokemon(user):
  print("Getting Pokemon info......")
  response = requests.get('https://pokeapi.co/api/v2/'+ user)

  if response.status_code == 200:
      
    print('Response:',response.status_code, '🎉🎉🎉', '\n')
    print("Success")
    return response.json()
  else:
    print('Uh Oh, Unsucessful',response.status_code)
    return 

#function that request an api and paste the info gathered about the pokemon then checks if its a success
def post_to_PasteBin(title,body):
  print("Posting Pokemon info......")
  params = {
    'api_dev_key': "f4R0OTFza_qTQ1NZJYLjoCeLqoHQux4X",
    'api_option': 'paste',
    'api_paste_code': body,
    'api_paste_name': title
}
  resp_mes= requests.post("https://pastebin.com/api/api_post.php", data = params)

  if resp_mes.status_code == 200:
      
    print('Response:',resp_mes.status_code, '🎉🎉🎉', '\n')
    print("Success")
    return resp_mes.text
  else:
    print('Uh Oh, Unsucessful',resp_mes.status_code)
    return resp_mes.status_code

#calls out the main function
main()