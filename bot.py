import discord
import responses
move_list={}
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
rpmChannelCall=""
rpmChannelCall_ID=""
rpmCallers=[]
cnt=0 #cnt acts as a flag. After RPS @user is called, it will be set to 2 allowing users to enter one entry each.

#this function is actually sending the responses either privately or in a channel.
#here user_message is going into get_response function where it's being checked as p_message. Basically it has the message of the user.
async def send_message(message, user_message, is_private,member,moves):
    global rpmCallers
    global move_list
    global rpmChannelCall
    global rpmChannelCall_ID
    try:
        #response variable has the appropiate response for a user_message/command in it.
        response = responses.get_response(user_message)
        if len(moves)==2:
            #storing the moves by the users in variables
            move1=list(moves.values())[0]
            move2=list(moves.values())[1]

            #storing respective keys/userID's in variables.
            key1=list(moves.keys())[0]
            key2=list(moves.keys())[1]

            channel=rpmChannelCall
            
            #-------------------------------------checking who won----------------------------------------------
            #rock wins
            if move1=="rock" and move2=="scissors":
                #user1 with rock wins
                await channel.send("**"+"<@" + key1 + ">"+" chose "+move1+":rock:"+"\n"+"**")
                await channel.send("**"+"<@" + key2 + ">"+" chose "+move2+":scissors:"+"\n"+"**")
                await channel.send("**"+"<@" + key1 + ">"+" wins!!!!! "+":tada:"+":tada:"+":tada:"+"**")
                await channel.send("https://i.gifer.com/uI6.gif")

            elif move1=="scissors" and move2=="rock":   
                #user2 with rock wins
                await channel.send("**"+"<@" + key1 + ">"+" chose "+move1+":scissors:"+"\n"+"**")
                await channel.send("**"+"<@" + key2 + ">"+" chose "+move2+":rock:"+"\n"+"**")
                await channel.send("**"+"<@" + key2 + ">"+" wins!!!!! "+":tada:"+":tada:"+":tada:"+"**")
                await channel.send("https://i.gifer.com/uI6.gif")

            #paper wins
            elif move1=="paper" and move2=="rock":
                await channel.send("**"+"<@" + key1 + ">"+" chose "+move1+":scroll:"+"\n"+"**")
                await channel.send("**"+"<@" + key2 + ">"+" chose "+move2+":rock:"+"\n"+"**")
                await channel.send("**"+"<@" + key1 + ">"+" wins!!!!! "+":tada:"+":tada:"+":tada:"+"**")
                await channel.send("https://i.gifer.com/uI6.gif")
            elif move1=="rock" and move2=="paper":
                await channel.send("**"+"<@" + key1 + ">"+" chose "+move1+":rock:"+"\n"+"**")
                await channel.send("**"+"<@" + key2 + ">"+" chose "+move2+":scroll:"+"\n"+"**")
                await channel.send("**"+"<@" + key2 + ">"+" wins!!!!! "+":tada:"+":tada:"+":tada:"+"**")
                await channel.send("https://i.gifer.com/uI6.gif")
            
            #Scissors wins
            elif move1=="scissors" and move2=="paper":
                await channel.send("**"+"<@" + key1 + ">"+" chose "+move1+":scissors:"+"\n"+"**")
                await channel.send("**"+"<@" + key2 + ">"+" chose "+move2+":scroll:"+"\n"+"**")
                await channel.send("**"+"<@" + key1 + ">"+" wins!!!!! "+":tada:"+":tada:"+":tada:"+"**")
                await channel.send("https://i.gifer.com/uI6.gif")
            elif move1=="paper" and move2=="scissors":
                await channel.send("**"+"<@" + key1 + ">"+" chose "+move1+":scroll:"+"\n"+"**")
                await channel.send("**"+"<@" + key2 + ">"+" chose "+move2+":scissors:"+"\n"+"**")
                await channel.send("**"+"<@" + key2 + ">"+" wins!!!!! "+":tada:"+":tada:"+":tada:"+"**")
                await channel.send("https://i.gifer.com/uI6.gif")

            #Rock Tie
            elif move1=="rock" and move2=="rock":
                await channel.send("**"+"<@" + key1 + ">"+" chose "+move1+":rock:"+"\n"+"**")
                await channel.send("**"+"<@" + key2 + ">"+" chose "+move2+":rock:"+"\n"+"**")
                await channel.send("**"+" It's a tie!!!!! "+":tada:"+":tada:"+":tada:"+"**")
                await channel.send("https://thumbs.gfycat.com/AnnualPinkJavalina-size_restricted.gif")
            #paper tie
            elif move1=="paper" and move2=="paper":
                await channel.send("**"+"<@" + key1 + ">"+" chose "+move1+":scroll:"+"\n"+"**")
                await channel.send("**"+"<@" + key2 + ">"+" chose "+move2+":scroll:"+"\n"+"**")
                await channel.send("**"+" It's a tie!!!!! "+":tada:"+":tada:"+":tada:"+"**")
                await channel.send("https://thumbs.gfycat.com/AnnualPinkJavalina-size_restricted.gif")
            #Scissors tie
            elif move1=="scissors" and move2=="scissors":
                await channel.send("**"+"<@" + key1 + ">"+" chose "+move1+":scissors:"+"\n"+"**")
                await channel.send("**"+"<@" + key2 + ">"+" chose "+move2+":scissors:"+"\n"+"**")
                await channel.send("**"+" It's a tie!!!!! "+":tada:"+":tada:"+":tada:"+"**")
                await channel.send("https://thumbs.gfycat.com/AnnualPinkJavalina-size_restricted.gif")



            #emptying dictionaries for future use.
            moves.clear()
            move_list.clear()
            

            
        #sending out the response in discord channel/dms. is_private has boolean values declared in bot running function.
        if is_private:
            await message.author.send(response)
            
            if member!=None:
                await member.send(response)
              
        else:
            await message.channel.send(response)

    #this is for printing errors in terminal.
    except Exception as e:
        print(e)



#running discord bot.
def run_discord_bot():
    TOKEN = 'MTA1MzI0MTkwMzM2MzEzMzUzMQ.GJS3br.x32xEtbpeNC7wduRQ_V_QGdMPeSq8vTYVrYp3Y'
    #declaring intents as true, using default intents and calling the discord Client. client.user is the bot itself.
    

    #prints BOT is running in terminal, if the bot is active on discord. Bots react to events.
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')


    #if the event has a message by a author that provokes a response, the bot functions from here.
    @client.event
    
    async def on_message(message):
        global rpmCallers
        global rpmChannelCall
        global rpmChannelCall_ID
        global move_list
        global cnt
        #checking if the message is by the bot itself. Then it's doing nothing.
        if message.author == client.user:
            return

        #storing username, the message that provoked the bot, the channel where the message was given in variables.
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        userID=str(message.author.id)
        selfIDCheck="!RPS <@"+userID+">"
    
        
        #Printing the event.
        print(f'{username} said: "{user_message}" in ({channel})')

        #------If the message starts with ?, response is sent privately cause is_private is set to True.
        #calling send_message function to send proper responses in proper channels--------
        if user_message[0:6] == '!RPS @':
            user_message=user_message[1:]
            await send_message(message, user_message, is_private=False,member=None,moves=move_list)
        
        elif user_message == '!RPS <@1053241903363133531>':
            user_message=user_message[1:]
            await send_message(message, user_message, is_private=False,member=None,moves=move_list)
        
        elif user_message == selfIDCheck:
            user_message="self call"
            await send_message(message, user_message, is_private=False,member=None,moves=move_list)
        
        
        elif user_message[0:7] == '!RPS <@':
            cnt=cnt+2 #flag
            #rpmCallers is a list that stores the ID's of the person who called RPS and the user who was mentioned.
            rpmCallers.append(userID)
            rpmCallers.append(user_message[7:-1])

            #storing the channel ID and name where RPS was called.
            rpmChannelCall_ID= message.channel.id
            rpmChannelCall=client.get_channel(rpmChannelCall_ID)


            user_message=user_message[1:]
            #Getting the ID of the mentioned user and sending same response to that member.
            user = await client.fetch_user(user_message[6:-1] )
            await send_message(message, user_message, is_private=True,member=user,moves=move_list)
            
        
        elif channel=="Direct Message with Unknown User":
            if userID in rpmCallers:
                if cnt!=0:
                    if user_message=="!rock" or user_message=="!paper" or user_message=="!scissors":
                        cnt-=1
                    
                        if user_message=="!rock":
                            move_list[userID]="rock"
                        elif user_message=="!paper":
                            move_list[userID]="paper"
                        elif user_message=="!scissors":
                            move_list[userID]="scissors"
                        rpmCallers.remove(userID)
                        await send_message(message, user_message, is_private=True,member=None,moves=move_list)
    
        
        
        
        elif user_message[0] =="!":
            user_message=user_message[1:]
            
            await send_message(message, user_message, is_private=False,member=None,moves=move_list)

    client.run(TOKEN)