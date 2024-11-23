#!/usr/bin/env python3

"""
次のサーバで動いてる前提
./server -c $(( 1024 * 128 )) --port 58080 --model ~/llm-models/Phi-3-mini-128k-instruct-Q4_K_M.gguf
"""
LLM_ADDR = "127.0.0.1"
LLM_PORT = 58080
LLM_URL  = f"http://{LLM_ADDR}:{LLM_PORT}/completion"

from argparse import ArgumentParser

ap = ArgumentParser()
ap.add_argument("-c", "--chat-template", help="chatのテンプレート", required=True)
ap.add_argument("-s", "--system-prompt", help="システムプロンプト", required=True)
ap.add_argument("-u", "--user-prompt", help="ユーザープロンプト, 指定がない場合は標準入力から受け付ける")
ap.add_argument("-v", "--verbose", help="デバッグ出力など", action="store_true")
## TODO: どちらかというと履歴をもたせるほうをフラグ化したほうが..
#ap.add_argument("--oneshot", help="単発の質疑応答フラグ(会話履歴を持たない)", action="store_true")
args = ap.parse_args()

## chat-templateをhuggingfaceから落とす
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained(args.chat_template)

## system_promptがファイルだったらファイルから読み込む
import os
system_prompt = args.system_prompt
if os.path.exists(system_prompt) :
    with open(system_prompt) as fd:
        system_prompt = fd.read()


## リクエスト(method)
import urllib.request
import json
import jinja2
def question(user_prompt):
    global system_prompt
    try :
        messages = [ 
            { "role" : "system", "content" : system_prompt }
        ,   { "role" : "user"  , "content" : user_prompt }
        ]
        prompt    = tokenizer.apply_chat_template(messages, tokenize=False)
    except jinja2.exceptions.TemplateError:
        messages = [ 
            { "role" : "user"  , "content" : f"SYS: {system_prompt} \n USER: {user_prompt}" }
        ]
        prompt    = tokenizer.apply_chat_template(messages, tokenize=False)
 
    hdrs = {"content-type" : "application/json" }
    body = json.dumps({"prompt" : prompt }).encode("utf-8")
    req  = urllib.request.Request(LLM_URL, body, hdrs, method="POST")
    with urllib.request.urlopen(req) as res:
        if res.getcode() < 300 :
            resdata = res.read().decode("utf-8")
            return resdata
        else :
            print(req)
            print(res.getcode())
            print(resdata)
            raise RuntimeError

## user_promptがファイルだったファイルから読み込む
### user_promptがなかったら標準入力から
import sys
import pyclip
user_prompt = args.user_prompt
if user_prompt is None:
    while True:
        print( "User: ", end="", flush=True)
        user_prompt = sys.stdin.read()
        print( "\n----- send server -----\n")
        answer = question(user_prompt)
        print( json.loads(answer)["content"] )
        try :
            pyclip.copy(json.loads(answer)["content"] )
        except:
            ## TODO: WSLだとexceptionが出てしまう
            pass
else:
    if os.path.exists(user_prompt) :
        with open(user_prompt) as fd:
            user_prompt = fd.read()
    answer = question(user_prompt)
    print( json.loads(answer)["content"] )
    if args.verbose :
        print("----------------------------")
        print( answer)
    try :
        pyclip.copy(json.loads(answer)["content"] )
    except:
        ## TODO: WSLだとexceptionが出てしまう
        pass

