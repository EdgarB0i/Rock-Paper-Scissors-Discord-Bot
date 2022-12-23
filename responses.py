#this file is for handling responses to the commands.


def get_response(message: str):
  p_message = message.lower()
  if p_message == 'hello':
    return '```Hey there! Interested in some Rock, Paper and Scissors? Type !help to get started.```'

  if p_message == 'help':
    return '```How to play: \n 1.Type !RPS and mention another user to start playing a game of Rock, Paper and Scissors together. For example, !RPS @user123 \n 2.Rock beats Scissors, Paper beats Rock, Scissors beat Paper. \n 3.After mentioning/getting mentioned, directly message !rock, !paper or !scissors to RPS Gamer. ```'

  if message == "RPS":
    return '```Please mention a user you wanna play with. Try !help if you\'re confused.```'

  if message == "RPS <@1053241903363133531>":
    return '``` Sorry, you cannot play against me! Please mention a user to play with.```'

  if p_message == "self call":
    return "``` You can't play against yourself dummy.```"

  if message[0:5] == 'RPS @':
    return "```User not found.```"
  if message[0:6] == 'RPS <@':
    return "```Choose !rock, !paper or !scissors```"

  if p_message == '!rock':
    return "```You have chosen rock.```"

  if p_message == '!paper':
    return "```You have chosen paper.```"

  if p_message == '!scissors':
    return "```You have chosen scissors.```"

  return None
