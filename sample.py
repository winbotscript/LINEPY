from LINEPY import *
from akad.ttypes import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse

# Untuk Login Via Qr link 
#line = LINE()
#line.log("Auth Token : " + str(line.authToken))
#line.log("Timeline Token : " + str(line.tl.channelAccessToken))

# Untuk Login Via Email & password
#line = LINE('EMAIL', 'PASSWORD')
#line.log("Auth Token : " + str(line.authToken))
#line.log("Timeline Token : " + str(line.tl.channelAccessToken))

line = LINE("Token disini")
line.log("Auth Token : " + str(line.authToken))
line.log("Timeline Token : " + str(line.tl.channelAccessToken))

ki = LINE("Token disini")
ki.log("Auth Token : " + str(ki.authToken))
ki.log("Timeline Token : " + str(ki.tl.channelAccessToken))

kk = LINE("Token disini")
kk.log("Auth Token : " + str(kk.authToken))
kk.log("Timeline Token : " + str(kk.tl.channelAccessToken))

kc = LINE("Token disini")
kc.log("Auth Token : " + str(kc.authToken))
kc.log("Timeline Token : " + str(kc.tl.channelAccessToken))

ks = LINE("Token disini")
ks.log("Auth Token : " + str(ks.authToken))
ks.log("Timeline Token : " + str(ks.tl.channelAccessToken))

cl = line
oepoll = OEPoll(cl)
All = [cl,ki,kk,kc,ks]
mid = cl.profile.mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = ks.getProfile().mid
RABots = [mid,Amid,Bmid,Cmid,Dmid]
RASuper = ["Mid Kamu"]
RAFamily = RASuper + RABots
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

def bot(op):
    try:
        if op.type == 5:
            if Setmain["RAautoadd"] == True:
                ra = cl.getContact(op.param1)
                cl.findAndAddContactsByMid(ra.mid)
                cl.sendMessageWithMention(op.param1, op.param1,"Hai","\nsudah ku addback ya\n\n{}".format(str(Setmain["RAmessage"])))
                
        if op.type == 22:
            if mid in op.param3:
                if Setmain["RAautojoin"] == True:
                    cl.leaveRoom(op.param1)        
                
        if op.type == 13:
            if mid in op.param3:
                if Setmain["RAautojoin"] == True:
                    if Setmain["RAbatas"]["on"] == True:
                        G = cl.getGroup(op.param1)
                        if len(G.members) > Setmain["RAbatas"]["members"]:
                            cl.acceptGroupInvitation(op.param1)
                            ra = cl.getGroup(op.param1)
                            cl.sendText(op.param1,"Maaf jumlah member\n " + str(ra.name) + " lebih dari " + str(Setmain["RAbatas"]["members"]))
                            cl.leaveGroup(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            ra = cl.getGroup(op.param1)
                            cl.sendMessageWithMention(msg.to, ra.creator.mid,"hallo","\nsalken group creator...")
                            
            if Amid in op.param3:
                if Setmain["RAautojoin"] == True:
                    if Setmain["RAbatas"]["on"] == True:
                        G = ki.getGroup(op.param1)
                        if len(G.members) > Setmain["RAbatas"]["members"]:
                            ki.acceptGroupInvitation(op.param1)
                            ra = ki.getGroup(op.param1)
                            ki.sendText(op.param1,"Maaf jumlah member\n " + str(ra.name) + " lebih dari " + str(Setmain["RAbatas"]["members"]))
                            ki.leaveGroup(op.param1)
                        else:
                            ki.acceptGroupInvitation(op.param1)
                            ra = ki.getGroup(op.param1)
                            ki.sendMessageWithMention(msg.to, ra.creator.mid,"hallo","\nsalken group creator...")
                            
            if Bmid in op.param3:
                if Setmain["RAautojoin"] == True:
                    if Setmain["RAbatas"]["on"] == True:
                        G = kk.getGroup(op.param1)
                        if len(G.members) > Setmain["RAbatas"]["members"]:
                            kk.acceptGroupInvitation(op.param1)
                            ra = kk.getGroup(op.param1)
                            kk.sendText(op.param1,"Maaf jumlah member\n " + str(ra.name) + " lebih dari " + str(Setmain["RAbatas"]["members"]))
                            kk.leaveGroup(op.param1)
                        else:
                            kk.acceptGroupInvitation(op.param1)
                            ra = kk.getGroup(op.param1)
                            kk.sendMessageWithMention(msg.to, ra.creator.mid,"hallo","\nsalken group creator...")
                            
            if Cmid in op.param3:
                if Setmain["RAautojoin"] == True:
                    if Setmain["RAbatas"]["on"] == True:
                        G = kc.getGroup(op.param1)
                        if len(G.members) > Setmain["RAbatas"]["members"]:
                            kc.acceptGroupInvitation(op.param1)
                            ra = kc.getGroup(op.param1)
                            kc.sendText(op.param1,"Maaf jumlah member\n " + str(ra.name) + " lebih dari " + str(Setmain["RAbatas"]["members"]))
                            kc.leaveGroup(op.param1)
                        else:
                            kc.acceptGroupInvitation(op.param1)
                            ra = kc.getGroup(op.param1)
                            kc.sendMessageWithMention(msg.to, ra.creator.mid,"hallo","\nsalken group creator...")
                            
            if Dmid in op.param3:
                if Setmain["RAautojoin"] == True:
                    if Setmain["RAbatas"]["on"] == True:
                        G = ks.getGroup(op.param1)
                        if len(G.members) > Setmain["RAbatas"]["members"]:
                            ks.acceptGroupInvitation(op.param1)
                            ra = ks.getGroup(op.param1)
                            ks.sendText(op.param1,"Maaf jumlah member\n " + str(ra.name) + " lebih dari " + str(Setmain["RAbatas"]["members"]))
                            ks.leaveGroup(op.param1)
                        else:
                            ks.acceptGroupInvitation(op.param1)
                            ra = ks.getGroup(op.param1)
                            ks.sendMessageWithMention(msg.to, ra.creator.mid,"hallo","\nsalken group creator...")                
                
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = sender
                elif msg.toType == 2:
                    to = receiver
                    
                if msg.contentType == 13:
                    if Setmain["RAautoscan"] == True:
                        msg.contentType = 0
                        cl.sendText(msg.to,msg.contentMetadata["mid"])
                        
                elif msg.contentType == 0:
                    if Setmain["RAautoread"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                        ki.sendChatChecked(msg.to, msg_id)
                        kk.sendChatChecked(msg.to, msg_id)
                        kc.sendChatChecked(msg.to, msg_id)
                        ks.sendChatChecked(msg.to, msg_id)
                    if text is None:    
                        return
                    else:
                        
        #---------------------- Start Command ------------------------#
                        
                        if text.lower() == "menu":
                            md = "🔰|RA| Family github version\n\n"
                            md += ".cek「@」\n"
                            md += ".gid\n"
                            md += ".yid\n"
                            md += ".me\n"
                            md += ".spbot\n"
                            md += ".bye\n"
                            cl.sendText(msg.to, md)
                            
            #---------------- Fungsi Command ------------------#
            
                        elif ".cek" in text.lower():
                            key = eval(msg.contentMetadata["MENTION"])
                            keys = key["MENTIONEES"][0]["M"]
                            ra = cl.getContact(keys)
                            try:
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/{}".format(str(ra.pictureStatus)))
                                cl.sendMessageWithMention(msg.to,ra.mid,"[Nama]\n","\n\n[Bio]\n{}".format(str(ra.statusMessage)))
                            except:
                                pass
                            
                        elif text.lower() == ".gid":
                            cl.sendMessageWithMention(msg.to, msg._from,"","\nMemproses..")
                            cl.sendText(msg.to,msg.to)
                            
                        elif text.lower() == ".yid":
                            cl.sendMessageWithMention(msg.to, msg._from,"","\nMemproses..")
                            cl.sendText(msg.to,msg._from)
                        
                        elif text.lower() == ".me":
                            cl.sendMessageWithMention(msg.to,msg._from,"Hay","\nada apa?")
                            
                        elif text.lower() == ".spbot":
                            start = time.time()
                            cl.sendText("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start
                            cl.sendText(msg.to, "%s " % (elapsed_time))
                            
                            start2 = time.time()
                            ki.sendText("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start2
                            ki.sendText(msg.to, "%s" % (elapsed_time))
                                
                            start3 = time.time()
                            kk.sendText("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start3
                            kk.sendText(msg.to, "%s" % (elapsed_time))
                                
                            start4 = time.time()
                            kc.sendMessage("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start4
                            kc.sendText(msg.to, "%s" % (elapsed_time))
                                
                            start5 = time.time()
                            ks.sendText("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start5
                            ks.sendText(msg.to, "%s" % (elapsed_time))
                            
                        elif text.lower() == ".bye":
                            if msg._from in RASuper:
                                ra = cl.getGroup(msg.to)
                                cl.sendMessageWithMention(msg.to,ra.creator.mid,"Maaf","\n aku keluar dulu ya..")
                                cl.leaveGroup(msg.to)
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                ks.leaveGroup(msg.to)
                                
                        elif '/ti/g/' in msg.text.lower():
                            if msg._from in RASuper:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(msg.text)
                                n_links=[]
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    if Setmain["RAautojoin"] == True:
                                        ra = cl.findGroupByTicket(ticket_id)
                                        cl.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        ki.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        kk.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        kc.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        ks.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        
                                    else:    
                                        cl.sendMessageWithMention(msg.to,msg._from,"Maaf","\naktifkan auotojoin dulu")

    except Exception as error:
        print (error)
        
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                oepoll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))
                thread1.start()
                thread1.join()
    except Exception as e:
        print(e)