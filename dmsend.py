OTM1Mzk2MTc0MDYyNTc5ODA0.Ye-Bkg.tbrVVKVwctQnW8XaASzo1KSBkaI﻿
# 아람쓰#5050 또는 아람#5920 : 전체디엠봇 소스
# 영상보고 모르는점 있을시 유튜브 댓글또는 디엠주세요


import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("봇실행이 시작되었습니다(24시간 온라인).")
    게임   =   불화 . GAE  M문
     클라이언트  를  기다  립니다 . change_presence ( 상태  =  discord . 상태 . 온라인 , 리시  =  게 '임문
</s></s>
#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id == 디스코드ID를 적기!!:
                        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="최상단 제목")
                        embed.add_field(name="제목", value=msg, inline=True)
                        embed.set_footer(text=f"서버초대코드")
                        await i.send(embed=embed)
                except:
                    pass


client.run('OTM1Mzk2MTc0MDYyNTc5ODA0.Ye-Bkg.tbrVVKVwctQnW8XaASzo1KSBkaI')
