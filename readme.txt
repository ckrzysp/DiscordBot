@client.event
async def on_message(message):
    if message.content.startswith(',SPR'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))

# commands with "," prefix

@client.command(name = 'say')
@commands.has_permissions(manage_messages = True)
async def response(ctx, *, arg):
    
    await ctx.channel.purge(limit = 1)
    await ctx.send(arg)

@client.command(name = 'dm')
async def version(context):
    
    await context.author.send("Hello there!") 

@client.command(name = 'ping')
async def ping(ctx):

    lat = client.latency * 1000
    await ctx.send(f"KrzysioBot has {round(client.latency * 1000)}ms")

@client.command(name = 'time')
async def time(ctx):

    currentTime = datetime.now()
    await ctx.send(currentTime)

@client.command(name = 'chris')
async def version(context, delete = 1):

    await context.channel.purge(limit = delete)
    await context.send('Wake up <@411267683980673035>')

@client.command(name = 'dumb')
async def version(context, delete = 1):

    await context.channel.purge(limit = delete)
    for i in range(2):
        for i in range(25):
        
            await context.send('Hey <@327231810360836098> your stupid :middle_finger:')

@client.command(name = 'pereira')
async def version(context, delete = 1):

    await context.channel.purge(limit = delete)
    await context.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


# possible games and fun stuff

@client.command(name = 'num')
async def num(ctx):

    number = 0
    add = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]

    while 1 == 1:
        ran = random.choice(add)

        await ctx.send(number)
        number += ran

        if number >= 51:

            break

@client.command(name = 'wordA')
async def word(ctx):


    sen = ['Well',
            'hello',
            'there']
    await ctx.send(sen)

    sen.pop(2)
    await ctx.send(sen)
    
    sen.pop(1)
    await ctx.send(sen)

    sen.pop(0)
    await ctx.send(sen)

    sen2 = ['Well',
            'hello',
            'there']    

    sen.append(sen2[0])
    await ctx.send(sen)

    sen.append(sen2[1])
    await ctx.send(sen)

    sen.append(sen2[2])
    await ctx.send(sen)

@client.command(name = 'coinf')
async def coin(ctx):

    coin = ['**heads**',
            '**tails**']
    
    ran = random.choice(coin)

    await ctx.send('The bot chose '+ ran)




@client.command(name = 'cmds')
async def embed(message):

    embedB = discord.Embed(title = "KrzysioBot commands", description = "Here are some commands for the bot and say hello!", color = 0x0efa9c)
    
    embedB.add_field(name = "Fun cmds", value = ",time\n,coinf\n,wordA\n,randW\n,ping\n,dm\n,image\n,num\n\n **Annoy cmds** \n,chris", inline = False)
    embedB.add_field(name = 'Admin cmds', value = ',kick @user \n,ban @user ("reason")', inline = False)
    embedB.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/506958296343904256/779117487391899668/Sharp.png')
    embedB.set_footer(text = "From Krzysio#9449")

    await message.send(embed = embedB)

@client.command(name = 'image')
async def image(ctx):

    images = ['https://cdn.discordapp.com/attachments/778810052702240780/779783795640500224/image1.jpg',
            'https://cdn.discordapp.com/attachments/778810052702240780/779783825520984084/image2.webp',
            'https://cdn.discordapp.com/attachments/778810052702240780/779783846467338240/image3.jpg',
            'https://cdn.discordapp.com/attachments/778810052702240780/779783880043003924/image4.jpg',
            'https://cdn.discordapp.com/attachments/778810052702240780/779783903731908618/image5.jpg']

    randImage = random.choice(images)

    await ctx.send(randImage)


#kick/ban/purge/mute/deafen

@client.command(name = 'mute')
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    
    await member.send("You were muted.")

@client.command(name = 'purge', pass_context = True)
@commands.has_permissions(manage_messages = True)
async def clear(ctx, *, arg):
    
    await ctx.channel.purge(limit = int(arg) + (1))


@client.command(name = 'kick', pass_context = True)
@commands.has_permissions(kick_members = True)
async def kick(context, member: discord.Member):
    
    await member.kick()
    await context.send('User ' + member.display_name + ' has been kicked successfully.')

@client.command(name = 'ban', pass_context = True)
@commands.has_permissions(kick_members = True)
async def ban(context, member: discord.Member, *, reason = None):
    
    await member.ban(reason = reason)
    await context.send('User ' + member.display_name + ' has been banned successfully.')

# Run the client on the server
client.run(token)

# // TO COME //

'''reaction_title = ""
reactions = {}
reactionMessageID = ""

@client.command(name = 'reaction_post')
async def reaction_post(context):

    embedR = discord.Embed(title = reaction_title, color = 0x4cd92c9)
    embed.set_author(name = 'KrzysioBot')
    embed.add_field(name = 'Probably the role part', value = ",reaction_new_title \"New Title\"")
    embed.add_field(name = 'New Role', value = ",reaction_add_role \"@\"")

    await context.send(embed = embed)
    await context.message.delete()

@client.command(name = 'reaction_title')
async def reaction_title(context, new_title):

    global reaction_title
    reaction_title = new_title
    await context.send('Title is: `' + reaction_title + '`')

@client.command(name = 'reaction_role')
async def reaction_role(context, role: discord.Role, reaction):

    if role != None:
        reactions[role.name] = reaction
        await context.send("Role `" + role.name + "` has been added with an emoji" + reaction)
        await context.message.delete()

    else:
        await context.send("Failed, try again")
    
    print(reactions)'''


