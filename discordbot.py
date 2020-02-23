from discord.ext import commands
import os
import traceback
import discord
import random  # おみくじで使用

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()  # 接続に使用するオブジェクト


@client.event
async def on_ready():
    """起動時に通知してくれる処理"""
    print('ログインしました')
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')

@client.event
async def on_message(message):
    """メッセージを処理"""
    if message.author.bot:  # ボットのメッセージをハネる
        return

    if message.content == "眠たい":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん さっさと寝ましょうねzzz")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "疲れた":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん 身体を休めてくださいね♡")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "おはよう":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん ☆おはようございます☆")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "こんにちは":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん ☆こんにちは！☆")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "こんばんは":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん ㊰こんばんは㊰")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "下手":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん 残念！下手でもいいさ！")  # f文字列（フォーマット済み文字列リテラル）
        

    if message.content == "利食い":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さんと一緒に パーティーしましょう☆")  # f文字列（フォーマット済み文字列リテラル）
        
    elif message.content == "投票":
        # リアクションアイコンを付けたい
        q = await message.channel.send("あなたはデイトレーダーですか？")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記

                
    elif message.content == "質問":
        # リアクションアイコンを付けたい
        q = await message.channel.send("あなたは損益通算で利益ですか？")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記
        

    elif message.content == "おみくじ":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日の運勢は！",
                              color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[投資運勢InvestmentFortune] ",
                        value=random.choice(('☆☆彡超最高☆彡☆【大幅利食い！アルゴに勝つ！】','☆最高☆【日経平均に関係なく材料株の押し目で利幅を出せます☆彡】','やったね☆！【納得出来る日でしょう。想定外であった動きで利益を出せます。】'
                                             ,'大吉【☆☆☆自信もって取り組めば必ず好成果となって返ってきます。♡♡♡株価ボードを眺めたら発想する銘柄が当たり】', '中吉【☆☆好チャンス！買増しで攻めて成果あり。♡♡とりあえず問題なしかな！？】', '小吉【☆☆通常の押し目セオリーを変化させたら好成果となる。♡♡】'
                                             ,  '末吉【☆☆SNSで見た銘柄が当たる！♡少し息抜きも考えて、外出したら吉あり】', '吉【☆現状変化なし♡特に変化なし。コスト抜けはする！】',  '吉【☆まぁ！こんなもんよ。日経読んでみて下さい。発見ある！”】'
                                             , 'ごく普通やね【何それ！？と思うだろうがごく普通だ！棚から牡丹餅はない】', '大凶【▲▲吐き気するわ！駄目だこりゃ】'
                                             , '凶【▲残念！好機はないね。負けも勝ちの内かと思え！見切り千両】', '大凶【▲▲やばい！ロスカットも想定に！駄目だこりゃ】', '凶【▲悲しい幅のリバウンドであってもカットをする事も大切！', '凶【▲次第に貴方の銘柄は見放されている。見直しをすれば吉になるかも！】', '吉【▲待ちスタンスで我慢も大切。翌営業日にかけるしかない！】', '凶【▲焦りは禁物。我慢も大切。しかしロスカットも大切】', '大大凶【▲▲▲言葉に表せない...。終了！】')), inline=False)
        await message.channel.send(embed=embed)

    elif message.content == "!ダイレクトメッセージ":
        # ダイレクトメッセージ送信
        dm = await message.author.create_dm()
        await dm.send(f"{message.author.mention}さんにダイレクトメッセージ")


client.run(token)
