#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:52:24 2019

@author: yotroz
"""
#%%%
import requests
import json
import seaborn as sns
import pandas as pd
from flask import Flask, render_template, jsonify, request
from jinja2 import Template


app = Flask("index", template_folder='templates')


@app.route("/", methods=["GET","POST"])
def root(): 

        
    return render_template("index.html")



@app.route("/get-score", methods =["GET","POST"])
def gettext(): 
    
    text = request.form["text"]
    print(text)
    
    return getscore(text)

@app.route("/get-chart", methods =["GET","POST"])
def getscore(text): 
    
#    text = request.form["text"]
#    
#    print(text)
    text = text
#    text ="In general, be courteous to others. Attack ideas, not users. Personal insults, shill or troll accusations, hate speech, any advocating or wishing death/physical harm, and other rule violations can result in a permanent ban. If you see comments in violation of our rules, please report them"

#    text = "The Middle par Jimmy Eat World Hey, don't write yourself off yet It's only in your head you feel left out or looked down on. Just TRY your best, TRY everything you can. And don't you worry what they tell themselves when you're away. Chorus It just takes some time, little girl you're in the middle of the ride. Everything, everything will be just fine, everything, everything will be alright, alright. Hey, you know they're all the same. You know you're doing better on your own, so don't buy in. Live right now. Yeah, just be yourself. It doesn't matter if it's good enough for someone else. Chorus It just takes some time, little girl you're in the middle of the ride. Everything, everything will be just fine, everything, everything will be alright, alright. It just takes some time, little girl you're in the middle of the ride. Everything, everything will be just fine, everything, everything will be alright, alright. Hey, don't write yourself off yet. It's only in your head you feel left out or looked down on. Just do your best (just do your best), do everything you can (do everything you can). And don't you worry what their bitter hearts (bitter hearts) are gonna say. Chorus It just takes some time, little girl you're in the middle of the ride. Everything, everything will be just fine, everything, everything will be alright, alright. It just takes some time, little girl you're in the middle of the ride. Everything, everything will be just fine, everything, everything will be alright."
    params = (
        ('version', '2017-09-21\n'),
        ('text', text),
    )
    
    response = requests.get('https://gateway-syd.watsonplatform.net/tone-analyzer/api/v3/tone', params=params, auth=('apikey', 'wkYB8AVtw5zI-hn0KZqRZJb_lUBr4kdq3SwSGb8S3iQH'))
    response = response.json()
    
    tones = []
    scores = []
    
    for tone in response['document_tone']['tones']:
        tones.append(tone['tone_id'])
        scores.append(tone['score'])
        
         
        print("the writer is feeling a " + str(tone["score"]) + " degree of " + tone['tone_id'])
    
    
    data = list(zip(tones, scores))
    df = pd.DataFrame(data, columns=["tone", "score"])
    df = df.to_json()
    
    data = json.dumps(dict(data))
    data = json.loads(data)

#    data = {"scores" : data}
    
    print(df)
    
#    g = sns.catplot(x=df.tone, y=df.score, data=df,
#                    height=6, kind="bar", palette="RdBu")
    
    print(data)
#    return render_template("score.html", df=df, tones=tones, scores=scores)
    return render_template("score.html", data=data)



#%%





#text ="In general, be courteous to others. Attack ideas, not users. Personal insults, shill or troll accusations, hate speech, any advocating or wishing death/physical harm, and other rule violations can result in a permanent ban. If you see comments in violation of our rules, please report them"

#text = "Someway, baby, it's part of me, apart from me You're laying waste to Halloween You fucked it friend, it's on its head, it struck the street You're in Milwaukee, off your feet And at once I knew I was not magnificent Strayed above the highway aisle (Jagged vacance, thick with ice) I could see for miles, miles, miles 3rd and Lake it burnt away, the hallway Was where we learned to celebrate Automatic bought the years you'd talk for me That night you played me 'Lip Parade' Not the needle, nor the thread, the lost decree Saying nothing, that's enough for me And at once I knew I was not magnificent Hulled far from the highway aisle (Jagged vacance, thick with ice)I could…"

 




app.run()



