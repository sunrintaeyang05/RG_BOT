import discord
from discord.ext import commands
from discord.ext.commands import bot

bot = commands.Bot(command_prefix = '~', allowed_mentions=discord.AllowedMentions(
        users=True,         # Whether to ping individual user @mentions
    ),)
mem = ['시작 시스템 점검','<@dasd>', '<@1312>', '<@ㅇㄴㄹㄴ>']

@bot.event
async def on_ready():
    print("[!] 봇 이름 : " + bot.user.name)
    print('시스템 부팅에 성공하였습니다.')
    
    await bot.change_presence(activity=discord.Game(name="3월 20일 (일) 16:00..........\n"))
    print('시스템 상태가 온라인 입니다.')

@bot.command()
async def 테스트(ctx):
    embed = discord.Embed(colour = discord.Colour.blue())
    embed.add_field(name="test", value='봇이 정상적으로 작동', inline=False)
    await ctx.send(embed=embed)
    
@bot.command()
async def rg1(ctx, i : int):
    ch_S = bot.get_channel(954302045773504572)
    ch_M = bot.get_channel(954422240265527296)
    ch_R = bot.get_channel(954421508057497611)
    
    await bot.change_presence(activity=discord.Game(name= mem[i] + "님의 면접이 진행 중...." ))
    print('시스템이 ' + mem[i] + "님의 면접 진행을 확인하였습니다." )
    
    embedS = discord.Embed(
        title = '면접 대기실 이동 요청',
        description = "이전 면접자의 면접이 끝나 다음 대기자는 입장해주시기 바랍니다.",
        colour = discord.Colour.blue()
    )
    embedS.add_field(name="대상자", value=mem[i+2], inline=True)
    embedS.add_field(name="위치", value="<#947443088987672606>", inline=True)
    embedS.set_author(name="이태양", icon_url="https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-19/274744041_634230954358609_8606896980741257929_n.jpg?stp=dst-jpg_s320x320&_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=101&_nc_ohc=h41-lAlp5QwAX8WdDNf&edm=ABfd0MgBAAAA&ccb=7-4&oh=00_AT_kmKySJiPKf-8wO-nYv8SKICKtbYi3RKzxZ0tejCbrMw&oe=623BB0F0&_nc_sid=7bff83")
    embedS.set_footer(text='2022학년도 RG 신입생 선발 면접 | SUNRINT')
    embedS.set_image(url="https://i.ibb.co/TPhwH4J/Kakao-Talk-Photo-2022-03-18-09-55-59.jpg")
    
    embedM = discord.Embed(
        title = '면접실 이동 요청',
        description = "이전 면접자의 면접이 끝나 대기 면접자를 면접실로 이동해주시기 바랍니다.",
        colour = discord.Colour.blue()
    )
    embedM.add_field(name="대상자", value=mem[i+1], inline=True)
    embedM.add_field(name="위치", value="<#947443760730611712>", inline=True)
    embedM.add_field(name="책임자", value="<@449864031050661890>", inline=False)
    embedM.set_author(name="이태양", icon_url="https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-19/274744041_634230954358609_8606896980741257929_n.jpg?stp=dst-jpg_s320x320&_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=101&_nc_ohc=h41-lAlp5QwAX8WdDNf&edm=ABfd0MgBAAAA&ccb=7-4&oh=00_AT_kmKySJiPKf-8wO-nYv8SKICKtbYi3RKzxZ0tejCbrMw&oe=623BB0F0&_nc_sid=7bff83")
    embedM.set_footer(text='2022학년도 RG 신입생 선발 면접팀 | SUNRINT')
    embedM.set_image(url="https://i.ibb.co/TPhwH4J/Kakao-Talk-Photo-2022-03-18-09-55-59.jpg")
    
    embedR = discord.Embed(
        title = '면접 완료',
        description = "해당 면접자의 선발 고사가 \n정상적으로 이루어졌습니다. \n참여해주셔서 감사합니다.",
        colour = discord.Colour.blue()
    )
    embedR.add_field(name="대상자", value=mem[i], inline=True)
    embedR.add_field(name="위치", value="<#947443760730611712>", inline=True)
    embedR.add_field(name="책임자", value="<@449864031050661890>", inline=False)
    embedR.set_author(name="이태양", icon_url="https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-19/274744041_634230954358609_8606896980741257929_n.jpg?stp=dst-jpg_s320x320&_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=101&_nc_ohc=h41-lAlp5QwAX8WdDNf&edm=ABfd0MgBAAAA&ccb=7-4&oh=00_AT_kmKySJiPKf-8wO-nYv8SKICKtbYi3RKzxZ0tejCbrMw&oe=623BB0F0&_nc_sid=7bff83")
    embedR.set_footer(text='2022학년도 RG 신입생 선발 면접팀 | SUNRINT')
    embedR.set_image(url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Feedbin-Icon-check.svg/2560px-Feedbin-Icon-check.svg.png")
    
    await ch_S.send(embed=embedS)
    await ch_M.send(embed=embedM)
    await ch_R.send(embed=embedR)


@bot.command(pass_context=True)
async def join(ctx):
    global vc
    vc = await ctx.message.author.voice.channel.connect()

@bot.command()
async def rg_list_1(ctx):
    ch_N = bot.get_channel(954300150946340874)
    
    embedL = discord.Embed(
        title = '면접 1팀 시간표',
        description = "해당 순서를 정확히 기억해주세요. \n향후 데이터를 기반으로 호출됩니다. \n많은 관심 부탁드립니다.",
        colour = discord.Colour.blue()
    )
    embedL.add_field(name="4:00", value="<@681377129514139649>", inline=False)
    embedL.add_field(name="4:10", value="<@478099631365160960>", inline=False)
    embedL.add_field(name="4:20", value="<@643216918609920001>", inline=False)
    embedL.add_field(name="4:30 (10분간)", value="시스템 재정비", inline=False)
    embedL.add_field(name="4:40", value="<@305493950246944769>", inline=False)
    embedL.add_field(name="4:50", value="<@362156760993366025>", inline=False)
    embedL.add_field(name="5:00", value="<@683619475765067781>", inline=False)
    embedL.add_field(name="5:10", value="<@953811601910292540>", inline=False)
    embedL.add_field(name="5:20", value="<@898933530158043207>", inline=False)
    embedL.add_field(name="5:30", value="<@668612763689418773>", inline=False)
    embedL.add_field(name="5:40", value="<@953799164142166046>", inline=False)
    embedL.add_field(name="5:50", value="<@749541049927467009>", inline=False)
    embedL.add_field(name="6:00 ~ 7:00", value="저녁 시간", inline=False)
    embedL.add_field(name="7:10", value="<@741830816962707518>", inline=False)
    embedL.add_field(name="7:20", value="<@769890732290867232>", inline=False)
    embedL.add_field(name="7:30", value="<@769154939313586196>", inline=False)
    embedL.add_field(name="7:40", value="<@557902529757839360>", inline=False)
    embedL.add_field(name="7:50", value="<@612642469640798229>", inline=False)
    embedL.add_field(name="8:00", value="<@454636599213555712>", inline=False)
    embedL.add_field(name="8:10", value="<@954023542058524755>", inline=False)
    embedL.add_field(name="8:20", value="<@614712683022778369>", inline=False)
    embedL.add_field(name="8:30", value="<@930664076344975371>", inline=False)
    embedL.add_field(name="8:40", value="<@866855525774000178>", inline=False)
    embedL.add_field(name="8:50", value="<@302057991539261442>", inline=False)
    embedL.add_field(name="9:00", value="<@695182596161667132>", inline=False)
    embedL.add_field(name="9:10", value="<@569787547220443136>", inline=False)
    embedL.add_field(name="9:20", value="<@487189721496158219>", inline=False)
    embedL.add_field(name="9:30", value="<@605740899334619157>", inline=False)
    embedL.add_field(name="9:40", value="<@512289605169709078>", inline=False)
    embedL.add_field(name="9:50", value="<@528088914435637268>", inline=False)
    
    embedL.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/3/33/SunrinInternetHighSchool.png")
    embedL.set_author(name="이태양", icon_url="https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-19/274744041_634230954358609_8606896980741257929_n.jpg?stp=dst-jpg_s320x320&_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=101&_nc_ohc=h41-lAlp5QwAX8WdDNf&edm=ABfd0MgBAAAA&ccb=7-4&oh=00_AT_kmKySJiPKf-8wO-nYv8SKICKtbYi3RKzxZ0tejCbrMw&oe=623BB0F0&_nc_sid=7bff83")
    embedL.set_footer(text='2022학년도 RG 신입생 선발 면접팀 | SUNRINT')
    embedL.set_image(url="https://i.ibb.co/TPhwH4J/Kakao-Talk-Photo-2022-03-18-09-55-59.jpg")
    
    await ch_N.send(embed=embedL)
    
@bot.command()
async def rg_list_1_text(ctx):
    ch_N = bot.get_channel(954302045773504572)
    
    embedL = discord.Embed(
        title = '면접 1팀 시간표',
        description = "해당 순서를 정확히 기억해주세요. \n향후 데이터를 기반으로 호출됩니다. \n많은 관심 부탁드립니다. \n@everyone",
        colour = discord.Colour.blue()
    )
    embedL.add_field(name="4:00", value="10606 김휘현", inline=False)
    embedL.add_field(name="4:10", value="10616 유현우", inline=False)
    embedL.add_field(name="4:20", value="10421 장태환", inline=False)
    embedL.add_field(name="4:30 (10분간)", value="시스템 재정비", inline=False)
    embedL.add_field(name="4:40", value="10804 김범수", inline=False)
    embedL.add_field(name="4:50", value="10604 김준서", inline=False)
    embedL.add_field(name="5:00", value="11108 문태현", inline=False)
    embedL.add_field(name="5:10", value="11212 윤진형", inline=False)
    embedL.add_field(name="5:20", value="11005 김유빈", inline=False)
    embedL.add_field(name="5:30", value="11213 이경훈", inline=False)
    embedL.add_field(name="5:40", value="11103김수빈", inline=False)
    embedL.add_field(name="5:50", value="10408 석찬우", inline=False)
    embedL.add_field(name="6:00 ~ 7:00", value="저녁 시간", inline=False)
    embedL.add_field(name="7:10", value="10516 조형서", inline=False)
    embedL.add_field(name="7:20", value="10413 유인성", inline=False)
    embedL.add_field(name="7:30", value="10403 김서하", inline=False)
    embedL.add_field(name="7:40", value="11218 주건우", inline=False)
    embedL.add_field(name="7:50", value="10407 방정연", inline=False)
    embedL.add_field(name="8:00", value="11020 조성환", inline=False)
    embedL.add_field(name="8:10", value="11214 이유진", inline=False)
    embedL.add_field(name="8:20", value="11110 박세현", inline=False)
    embedL.add_field(name="8:30", value="10508 배진영", inline=False)
    embedL.add_field(name="8:40", value="11119 유호빈", inline=False)
    embedL.add_field(name="8:50", value="10502 김기훈", inline=False)
    embedL.add_field(name="9:00", value="11008 박세현", inline=False)
    embedL.add_field(name="9:10", value="10520 최진범", inline=False)
    embedL.add_field(name="9:20", value="11019 정지훈", inline=False)
    embedL.add_field(name="9:30", value="10513 이채은", inline=False)
    embedL.add_field(name="9:40", value="10619 정재형", inline=False)
    embedL.add_field(name="9:50", value="10608 마진성", inline=False)
    
    embedL.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/3/33/SunrinInternetHighSchool.png")
    embedL.set_author(name="이태양", icon_url="https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-19/274744041_634230954358609_8606896980741257929_n.jpg?stp=dst-jpg_s320x320&_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=101&_nc_ohc=h41-lAlp5QwAX8WdDNf&edm=ABfd0MgBAAAA&ccb=7-4&oh=00_AT_kmKySJiPKf-8wO-nYv8SKICKtbYi3RKzxZ0tejCbrMw&oe=623BB0F0&_nc_sid=7bff83")
    embedL.set_footer(text='2022학년도 RG 신입생 선발 면접팀 | SUNRINT')
    embedL.set_image(url="https://i.ibb.co/TPhwH4J/Kakao-Talk-Photo-2022-03-18-09-55-59.jpg")
    
    await ch_N.send(embed=embedL)



@bot.command()
async def notice(ctx, title : str, des):
    ch_R = bot.get_channel(947440401994874940)
    
    embedL = discord.Embed(
        title = title,
        description = des,
        colour = discord.Colour.blue()
    )
    embedL.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/3/33/SunrinInternetHighSchool.png")
    embedL.set_author(name="이태양", icon_url="https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-19/274744041_634230954358609_8606896980741257929_n.jpg?stp=dst-jpg_s320x320&_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=101&_nc_ohc=h41-lAlp5QwAX8WdDNf&edm=ABfd0MgBAAAA&ccb=7-4&oh=00_AT_kmKySJiPKf-8wO-nYv8SKICKtbYi3RKzxZ0tejCbrMw&oe=623BB0F0&_nc_sid=7bff83")
    embedL.set_footer(text='2022학년도 RG 신입생 선발 면접팀 | SUNRINT')
    embedL.set_image(url="https://i.ibb.co/TPhwH4J/Kakao-Talk-Photo-2022-03-18-09-55-59.jpg")
    
    await ch_R.send(embed=embedL)

@bot.command()
async def 문의(ctx):
    ch_R = bot.get_channel(954418062872952862)
    
    embedL = discord.Embed(
        title = '문의사항 및 지원 요청',
        description = "학번이름 기재후, \n문의 및 지원 내용 기재 부탁드립니다.",
        colour = discord.Colour.blue()
    )
    embedL.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/3/33/SunrinInternetHighSchool.png")
    embedL.set_author(name="RG 지원팀")
    embedL.set_footer(text='2022학년도 RG 신입생 선발 면접팀 | SUNRINT')
    embedL.set_image(url="https://i.ibb.co/TPhwH4J/Kakao-Talk-Photo-2022-03-18-09-55-59.jpg")
    
    await ch_R.send(embed=embedL)

@bot.command()
async def clear(ctx , amount : int):
  await ctx.channel.purge(limit=amount + 1)
    


bot.run('OTU0MTgwODkzOTY5Mzc5MzY5.YjPYNA.Mu1mn1mUY2iYSsH8EVxjFkfOkTs')
