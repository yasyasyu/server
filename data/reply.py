#!/usr/local/bin/python
# -*- coding: utf-8 -*-
print("Content-type: text/html; charset=UTF-8\n")
import tweepy
import time,datetime
def main():
    history_url = "/virtual/yasyasyu/public_html/data/history/reply_history_last.txt"
    history_list = "/virtual/yasyasyu/public_html/data/history/reply_history_list.txt"
    #history_url ="./reply_history.txt"
    Twitter_ID = "elements_boron"
    CK="vihy73O6J8NPzot6ecmM3S33p"
    CS="eDzelyLPOGPT8snShGB0MGb7wvILSTJBnbzqfiAyRbYDtUchRT"
    AT="1177243027552604160-O1gVSGIMRKLi0INxPfnfKSUcyU9J8Q"
    AS="rnMNaGk0mPJxNzNIDXo2YHjfA8XPPO2eIMXyjFDjEEDVl"
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)
    api2 = tweepy.API(auth)
    timeline=api2.mentions_timeline(count=1)

    for status in timeline:
        status_id=status.id
        mention=status.author.screen_name.encode("UTF-8")
        tweet_time = str(status.created_at)
        inp = status.text
        strip_text = inp.lstrip("@elements_boron")
        history_tweet = tweet_time+"\n"+"from:"+mention
        rh = open(history_url,"r")
        reply_history = rh.read()
        rh.close
    
    
        if(reply_history==history_tweet):
            print("get the same tweet.")
            exit()
        else:
            tweeted_text = strip_text
            element_number = element_number_gen(tweeted_text)
            tweet_text   = tweeted_text_gen(element_number)
            today = datetime.datetime.fromtimestamp(time.time())
            now_time=today.strftime('%Y/%m/%d %H:%M:%S')
            now_time = str(now_time)
            print(now_time)
            print(mention)
            print(tweet_text)
            reply_text="@"+mention+"\n"+now_time+"\n"+tweet_text

            if str(status.in_reply_to_screen_name)==Twitter_ID and str(status.user.screen_name)!=Twitter_ID:
                print("send to reply for this tweet.")
                rh = open(history_url,"w")
                rh.write(history_tweet)
                rh.close()
                rl = open(history_list,"a")
                rl.write("\n"+history_tweet)
                rl.close
                api2.update_status(status=reply_text,in_reply_to_status_id=status_id)
            else:
                print("err")



def element_number_gen(tweeted_text):
    tweeted_text = tweeted_text
    i = 118
    while all:
        if(i<0):
            element_number = 0
            break
        if(str(i) in tweeted_text):
            element_number = i
            break
        i -= 1

    return element_number
""" if("118"  in tweeted_text):
        element_number = 118
    elif("117"  in tweeted_text):
        element_number = 117
    elif("116"  in tweeted_text):
        element_number = 116
    elif("115" in tweeted_text):
        element_number =115
    elif("114" in tweeted_text):
        element_number =114
    elif("113" in tweeted_text):
        element_number =113
    elif("112" in tweeted_text):
        element_number =112
    elif("111" in tweeted_text):
        element_number =111
    elif("110" in tweeted_text):
        element_number =110
    elif("109" in tweeted_text):
        element_number =109
    elif("108" in tweeted_text):
        element_number =108
    elif("107" in tweeted_text):
        element_number =107
    elif("106" in tweeted_text):
        element_number =106
    elif("105" in tweeted_text):
        element_number =105
    elif("104" in tweeted_text):
        element_number =104
    elif("103" in tweeted_text):
        element_number =103
    elif("102" in tweeted_text):
        element_number =102
    elif("101" in tweeted_text):
        element_number =101
    elif("100" in tweeted_text):
        element_number =100
    elif("99" in tweeted_text):
        element_number =99
    elif("98" in tweeted_text):
        element_number =98
    elif("97" in tweeted_text):
        element_number =97
    elif("96" in tweeted_text):
        element_number =96
    elif("95" in tweeted_text):
        element_number =95
    elif("94" in tweeted_text):
        element_number =94
    elif("93" in tweeted_text):
        element_number =93
    elif("92" in tweeted_text):
        element_number =92
    elif("91" in tweeted_text):
        element_number =91
    elif("90" in tweeted_text):
        element_number =90
    elif("89" in tweeted_text):
        element_number =89
    elif("88" in tweeted_text):
        element_number =88
    elif("87" in tweeted_text):
        element_number =87
    elif("86" in tweeted_text):
        element_number =86
    elif("85" in tweeted_text):
        element_number =85
    elif("84" in tweeted_text):
        element_number =84
    elif("83" in tweeted_text):
        element_number =83
    elif("82" in tweeted_text):
        element_number =82
    elif("81" in tweeted_text):
        element_number =81
    elif("80" in tweeted_text):
        element_number =80
    elif("79" in tweeted_text):
        element_number =79
    elif("78" in tweeted_text):
        element_number =78
    elif("77" in tweeted_text):
        element_number =77
    elif("76" in tweeted_text):
        element_number =76
    elif("75" in tweeted_text):
        element_number =75
    elif("74" in tweeted_text):
        element_number =74
    elif("73" in tweeted_text):
        element_number =73
    elif("72" in tweeted_text):
        element_number =72
    elif("71" in tweeted_text):
        element_number =71
    elif("70" in tweeted_text):
        element_number =70
    elif("69" in tweeted_text):
        element_number =69
    elif("68" in tweeted_text):
        element_number =68
    elif("67" in tweeted_text):
        element_number =67
    elif("66" in tweeted_text):
        element_number =66
    elif("65" in tweeted_text):
        element_number =65
    elif("64" in tweeted_text):
        element_number =64
    elif("63" in tweeted_text):
        element_number =63
    elif("62" in tweeted_text):
        element_number =62
    elif("61" in tweeted_text):
        element_number =61
    elif("60" in tweeted_text):
        element_number =60
    elif("59" in tweeted_text):
        element_number =59
    elif("58" in tweeted_text):
        element_number =58
    elif("57" in tweeted_text):
        element_number =57
    elif("56" in tweeted_text):
        element_number =56
    elif("55" in tweeted_text):
        element_number =55
    elif("54" in tweeted_text):
        element_number =54
    elif("53" in tweeted_text):
        element_number =53
    elif("52" in tweeted_text):
        element_number =52
    elif("51" in tweeted_text):
        element_number =51
    elif("50" in tweeted_text):
        element_number =50
    elif("49" in tweeted_text):
        element_number =49
    elif("48" in tweeted_text):
        element_number =48
    elif("47" in tweeted_text):
        element_number =47
    elif("46" in tweeted_text):
        element_number =46
    elif("45" in tweeted_text):
        element_number =45
    elif("44" in tweeted_text):
        element_number =44
    elif("43" in tweeted_text):
        element_number =43
    elif("42" in tweeted_text):
        element_number =42
    elif("41" in tweeted_text):
        element_number =41
    elif("40" in tweeted_text):
        element_number =40
    elif("39" in tweeted_text):
        element_number =39
    elif("38" in tweeted_text):
        element_number =38
    elif("37" in tweeted_text):
        element_number =37
    elif("36" in tweeted_text):
        element_number =36
    elif("35" in tweeted_text):
        element_number =35
    elif("34" in tweeted_text):
        element_number =34
    elif("33" in tweeted_text):
        element_number =33
    elif("32" in tweeted_text):
        element_number =32
    elif("31" in tweeted_text):
        element_number =31
    elif("30" in tweeted_text):
        element_number =30
    elif("29" in tweeted_text):
        element_number =29
    elif("28" in tweeted_text):
        element_number =28
    elif("27" in tweeted_text):
        element_number =27
    elif("26" in tweeted_text):
        element_number =26
    elif("25" in tweeted_text):
        element_number =25
    elif("24" in tweeted_text):
        element_number =24
    elif("23" in tweeted_text):
        element_number =23
    elif("22" in tweeted_text):
        element_number =22
    elif("21" in tweeted_text):
        element_number =21
    elif("20" in tweeted_text):
        element_number =20
    elif("19" in tweeted_text):
        element_number =19
    elif("18" in tweeted_text):
        element_number =18
    elif("17" in tweeted_text):
        element_number =17
    elif("16" in tweeted_text):
        element_number =16
    elif("15" in tweeted_text):
        element_number =15
    elif("14" in tweeted_text):
        element_number =14
    elif("13" in tweeted_text):
        element_number =13
    elif("12" in tweeted_text):
        element_number =12
    elif("11" in tweeted_text):
        element_number =11
    elif("10" in tweeted_text):
        element_number =10
    elif("9" in tweeted_text):
        element_number =9
    elif("8" in tweeted_text):
        element_number =8
    elif("7" in tweeted_text):
        element_number =7
    elif("6" in tweeted_text):
        element_number =6
    elif("5" in tweeted_text):
        element_number =5
    elif("4" in tweeted_text):
        element_number =4
    elif("3" in tweeted_text):
        element_number =3
    elif("2" in tweeted_text):
        element_number =2
    elif("1" in tweeted_text):
        element_number =1
    elif("0" in tweeted_text):
        element_number =0
 """



def tweeted_text_gen(element_number):
    element_number = element_number
    if(element_number ==0):
        tweet_text = '未定義'
    else:
        if(element_number == 1):
            tweet_text='元素番号:1,元素記号:H'+'\n'+'日本語名:水素,英語名:Hydrogen,ラテン名:Hydrogenium'+'\n'+'周期:1,族:1,原子量:1.00794（7）'+'\n'+'英語名の由来:性質：希: hydro（水）+gennao（生じる）'
        elif(element_number == 2):
            tweet_text='元素番号:2,元素記号:He'+'\n'+'日本語名:ヘリウム,英語名:Helium,ラテン名:Helium'+'\n'+'周期:1,族:18,原子量:4.002602（2）'+'\n'+'英語名の由来:場所：太陽上に発見、希: helios（太陽）'
        elif(element_number == 3):
            tweet_text='元素番号:3,元素記号:Li'+'\n'+'日本語名:リチウム,英語名:Lithium,ラテン名:Lithium'+'\n'+'周期:2,族:1,原子量:6.941（2）'+'\n'+'英語名の由来:他：岩から採取、希: lithos（石）'
        elif(element_number == 4):
            tweet_text='元素番号:4,元素記号:Be'+'\n'+'日本語名:ベリリウム,英語名:Beryllium,ラテン名:Beryllium'+'\n'+'周期:2,族:2,原子量:9.012182（3）'+'\n'+'英語名の由来:鉱物：緑柱石 beryl'
        elif(element_number == 5):
            tweet_text='元素番号:5,元素記号:B'+'\n'+'日本語名:ホウ素,英語名:Boron,ラテン名:Borium'+'\n'+'周期:2,族:13,原子量:10.811（7）'+'\n'+'英語名の由来:鉱物：ホウ砂 buraq[2]、ペルシア語: borax‎'
        elif(element_number == 6):
            tweet_text='元素番号:6,元素記号:C'+'\n'+'日本語名:炭素,英語名:Carbon,ラテン名:Carbonium'+'\n'+'周期:2,族:14,原子量:12.0107（8）'+'\n'+'英語名の由来:性質：可燃物、梵: jval、羅: Carbo[3]'
        elif(element_number == 7):
            tweet_text='元素番号:7,元素記号:N'+'\n'+'日本語名:窒素,英語名:Nitrogen,ラテン名:Nitrogenium'+'\n'+'周期:2,族:15,原子量:14.0067（2）'+'\n'+'英語名の由来:鉱物：硝石 nitrum（希: nitre（硝石）+gennao（生じる）[4]）'
        elif(element_number == 8):
            tweet_text='元素番号:8,元素記号:O'+'\n'+'日本語名:酸素,英語名:Oxygen,ラテン名:Oxygenium'+'\n'+'周期:2,族:16,原子量:15.9994（3）'+'\n'+'英語名の由来:性質：酸の根元、希: oxys（酸味）+gennao（生じる）'
        elif(element_number == 9):
            tweet_text='元素番号:9,元素記号:F'+'\n'+'日本語名:フッ素,英語名:Fluorine,ラテン名:Fluorum'+'\n'+'周期:2,族:17,原子量:18.9984032（5）'+'\n'+'英語名の由来:鉱物：蛍石、羅: fluorite[5]'
        elif(element_number == 10):
            tweet_text='元素番号:10,元素記号:Ne'+'\n'+'日本語名:ネオン,英語名:Neon,ラテン名:Neon'+'\n'+'周期:2,族:18,原子量:20.1797（6）'+'\n'+'英語名の由来:他：「新しい」、希: neos'
        elif(element_number == 11):
            tweet_text='元素番号:11,元素記号:Na'+'\n'+'日本語名:ナトリウム,英語名:Sodium,ラテン名:Natrium'+'\n'+'周期:3,族:1,原子量:22.98976928（2）'+'\n'+'英語名の由来:性質：ヘブライ語: nether‎（洗剤）またはソーダ、亜: suda‎[6]'
        elif(element_number == 12):
            tweet_text='元素番号:12,元素記号:Mg'+'\n'+'日本語名:マグネシウム,英語名:Magnesium,ラテン名:Magnesium'+'\n'+'周期:3,族:2,原子量:24.3050（6）'+'\n'+'英語名の由来:鉱物：マグネシア magnesia alba（ギリシアのマグネシア地区[7]）'
        elif(element_number == 13):
            tweet_text='元素番号:13,元素記号:Al'+'\n'+'日本語名:アルミニウム,英語名:Aluminium[注 1],ラテン名:Aluminium'+'\n'+'周期:3,族:13,原子量:26.9815386（8）'+'\n'+'英語名の由来:鉱物：明礬石 alum、古名：アルメンalimen[7]'
        elif(element_number == 14):
            tweet_text='元素番号:14,元素記号:Si'+'\n'+'日本語名:ケイ素,英語名:Silicon,ラテン名:Silicium'+'\n'+'周期:3,族:14,原子量:28.0855（3）'+'\n'+'英語名の由来:鉱物：珪石、希: silex, silicis（火打石）[9]'
        elif(element_number == 15):
            tweet_text='元素番号:15,元素記号:P'+'\n'+'日本語名:リン,英語名:Phosphorus,ラテン名:Phosphorus'+'\n'+'周期:3,族:15,原子量:30.973762（2）'+'\n'+'英語名の由来:性質：発光、希: phos（光）+phoros（運ぶ者）'
        elif(element_number == 16):
            tweet_text='元素番号:16,元素記号:S'+'\n'+'日本語名:硫黄,英語名:Sulfur,ラテン名:Sulphur'+'\n'+'周期:3,族:16,原子量:32.065（5）'+'\n'+'英語名の由来:他：ラテン語: sulphurは語源不明。希: theion（燻らせる）の説も'
        elif(element_number == 17):
            tweet_text='元素番号:17,元素記号:Cl'+'\n'+'日本語名:塩素,英語名:Chlorine,ラテン名:Chlorum'+'\n'+'周期:3,族:17,原子量:35.453（2）'+'\n'+'英語名の由来:色：単体、希: chloros（黄緑）'
        elif(element_number == 18):
            tweet_text='元素番号:18,元素記号:Ar'+'\n'+'日本語名:アルゴン,英語名:Argon,ラテン名:Argon'+'\n'+'周期:3,族:18,原子量:39.948（1）'+'\n'+'英語名の由来:性質：化合しない、希: an ergon（働かない）'
        elif(element_number == 19):
            tweet_text='元素番号:19,元素記号:K'+'\n'+'日本語名:カリウム,英語名:Potassium,ラテン名:Kalium'+'\n'+'周期:4,族:1,原子量:39.0983（1）'+'\n'+'英語名の由来:他：木灰から取れるため、亜: kaljan‎（灰）'
        elif(element_number == 20):
            tweet_text='元素番号:20,元素記号:Ca'+'\n'+'日本語名:カルシウム,英語名:Calcium,ラテン名:Calcium'+'\n'+'周期:4,族:2,原子量:40.078（4）'+'\n'+'英語名の由来:鉱物：石灰石 calcite'
        elif(element_number == 21):
            tweet_text='元素番号:21,元素記号:Sc'+'\n'+'日本語名:スカンジウム,英語名:Scandium,ラテン名:Scandium'+'\n'+'周期:4,族:3,原子量:44.955912（6）'+'\n'+'英語名の由来:場所：発見者・ニルソンの出身地・スカンジナビア'
        elif(element_number == 22):
            tweet_text='元素番号:22,元素記号:Ti'+'\n'+'日本語名:チタン,英語名:Titanium,ラテン名:Titanium'+'\n'+'周期:4,族:4,原子量:47.867（1）'+'\n'+'英語名の由来:神話：地球最初の息子・ティタン Titans'
        elif(element_number == 23):
            tweet_text='元素番号:23,元素記号:V'+'\n'+'日本語名:バナジウム,英語名:Vanadium,ラテン名:Vanadium'+'\n'+'周期:4,族:5,原子量:50.9415（1）'+'\n'+'英語名の由来:神話：スカンジナビアの神・バナジス Vanadis'
        elif(element_number == 24):
            tweet_text='元素番号:24,元素記号:Cr'+'\n'+'日本語名:クロム,英語名:Chromium,ラテン名:Chromium'+'\n'+'周期:4,族:6,原子量:51.9961（6）'+'\n'+'英語名の由来:色：化合物が多色、希: chroma（色）'
        elif(element_number == 25):
            tweet_text='元素番号:25,元素記号:Mn'+'\n'+'日本語名:マンガン,英語名:Manganese,ラテン名:Manganum'+'\n'+'周期:4,族:7,原子量:54.938045（5）'+'\n'+'英語名の由来:鉱物：マンガン鉱（磁鉄鉱） magnes'
        elif(element_number == 26):
            tweet_text='元素番号:26,元素記号:Fe'+'\n'+'日本語名:鉄,英語名:Iron,ラテン名:Ferrum'+'\n'+'周期:4,族:8,原子量:55.845（2）'+'\n'+'英語名の由来:鉱物：鉱物の一般名詞、希: aes、Feは羅: ferrumといわれる[10]'
        elif(element_number == 27):
            tweet_text='元素番号:27,元素記号:Co'+'\n'+'日本語名:コバルト,英語名:Cobalt,ラテン名:Cobaltum'+'\n'+'周期:4,族:9,原子量:58.933195（5）'+'\n'+'英語名の由来:鉱石：コボルト、山の精・悪霊 Koboldから[11]'
        elif(element_number == 28):
            tweet_text='元素番号:28,元素記号:Ni'+'\n'+'日本語名:ニッケル,英語名:Nickel,ラテン名:Niccolum'+'\n'+'周期:4,族:10,原子量:58.6934（4）'+'\n'+'英語名の由来:性質：鉱石から銅が取れない、独: nickl（取り得がない）、Kupfernickel（銅の悪魔）[12]'
        elif(element_number == 29):
            tweet_text='元素番号:29,元素記号:Cu'+'\n'+'日本語名:銅,英語名:Copper,ラテン名:Cuprum'+'\n'+'周期:4,族:11,原子量:63.546（3）'+'\n'+'英語名の由来:場所：古代の発掘地・キプロス島、羅: Cuprum[13]'
        elif(element_number == 30):
            tweet_text='元素番号:30,元素記号:Zn'+'\n'+'日本語名:亜鉛,英語名:Zinc,ラテン名:Zincum'+'\n'+'周期:4,族:12,原子量:65.38（2）'+'\n'+'英語名の由来:鉱物：亜鉛鉱石 zink、独: zinke（尖ったもの）から'
        elif(element_number == 31):
            tweet_text='元素番号:31,元素記号:Ga'+'\n'+'日本語名:ガリウム,英語名:Gallium,ラテン名:Gallium'+'\n'+'周期:4,族:13,原子量:69.723（1）'+'\n'+'英語名の由来:場所：発見者・ボアボードラン出身国・フランスの古名：gallia'
        elif(element_number == 32):
            tweet_text='元素番号:32,元素記号:Ge'+'\n'+'日本語名:ゲルマニウム,英語名:Germanium,ラテン名:Germanium'+'\n'+'周期:4,族:14,原子量:72.64（1）'+'\n'+'英語名の由来:場所：発見者・ウィンクラー出身国・ドイツの古名：germania'
        elif(element_number == 33):
            tweet_text='元素番号:33,元素記号:As'+'\n'+'日本語名:ヒ素,英語名:Arsenic,ラテン名:Arsenicum'+'\n'+'周期:4,族:15,原子量:74.92160（2）'+'\n'+'英語名の由来:鉱物：雄黄、希: arsenihon'
        elif(element_number == 34):
            tweet_text='元素番号:34,元素記号:Se'+'\n'+'日本語名:セレン,英語名:Selenium,ラテン名:Selenium'+'\n'+'周期:4,族:16,原子量:78.96（3）'+'\n'+'英語名の由来:性質：燃焼時に月のように輝く、希: selene（月）（女神・セレーネーから[14]）'
        elif(element_number == 35):
            tweet_text='元素番号:35,元素記号:Br'+'\n'+'日本語名:臭素,英語名:Bromine,ラテン名:Bromum'+'\n'+'周期:4,族:17,原子量:79.904（1）'+'\n'+'英語名の由来:性質：単体の悪臭、希: bromos（悪臭）'
        elif(element_number == 36):
            tweet_text='元素番号:36,元素記号:Kr'+'\n'+'日本語名:クリプトン,英語名:Krypton,ラテン名:Krypton'+'\n'+'周期:4,族:18,原子量:83.798（2）'+'\n'+'英語名の由来:性質：見つけにくかったこと、希: chryptos（隠者）'
        elif(element_number == 37):
            tweet_text='元素番号:37,元素記号:Rb'+'\n'+'日本語名:ルビジウム,英語名:Rubidium,ラテン名:Rubidium'+'\n'+'周期:5,族:1,原子量:85.4678（3）'+'\n'+'英語名の由来:色：炎色反応が紅い、ルビー'
        elif(element_number == 38):
            tweet_text='元素番号:38,元素記号:Sr'+'\n'+'日本語名:ストロンチウム,英語名:Strontium,ラテン名:Strontium'+'\n'+'周期:5,族:2,原子量:87.62（1）'+'\n'+'英語名の由来:場所：鉱物が採れた鉱山 Strontian（スコットランド）'
        elif(element_number == 39):
            tweet_text='元素番号:39,元素記号:Y'+'\n'+'日本語名:イットリウム,英語名:Yttrium,ラテン名:Yttrium'+'\n'+'周期:5,族:3,原子量:88.90585（2）'+'\n'+'英語名の由来:場所：鉱物が発見されたイッテルビー Yitterby（スウェーデン）'
        elif(element_number == 40):
            tweet_text='元素番号:40,元素記号:Zr'+'\n'+'日本語名:ジルコニウム,英語名:Zirconium,ラテン名:Zirconium'+'\n'+'周期:5,族:4,原子量:91.224（2）'+'\n'+'英語名の由来:鉱物：ジルコン、亜: zarqum‎（宝石の種類）[15]'
        elif(element_number == 41):
            tweet_text='元素番号:41,元素記号:Nb'+'\n'+'日本語名:ニオブ,英語名:Niobium,ラテン名:Niobium'+'\n'+'周期:5,族:5,原子量:92.90638（2）'+'\n'+'英語名の由来:神話：タンタルと共存する（タンタロスの娘・ニオベー Niobe）'
        elif(element_number == 42):
            tweet_text='元素番号:42,元素記号:Mo'+'\n'+'日本語名:モリブデン,英語名:Molybdenum,ラテン名:Molybdenum'+'\n'+'周期:5,族:6,原子量:95.96（2）'+'\n'+'英語名の由来:性質：鉛に似ている、希: molybdos（鉛）'
        elif(element_number == 43):
            tweet_text='元素番号:43,元素記号:Tc'+'\n'+'日本語名:テクネチウム,英語名:Technetium,ラテン名:Technetium'+'\n'+'周期:5,族:7,原子量:[98.9063]'+'\n'+'英語名の由来:性質：不安定な核種で、人工的に作られて発見された元素、希: technikos（人工の）[16]'
        elif(element_number == 44):
            tweet_text='元素番号:44,元素記号:Ru'+'\n'+'日本語名:ルテニウム,英語名:Ruthenium,ラテン名:Ruthenium'+'\n'+'周期:5,族:8,原子量:101.07（2）'+'\n'+'英語名の由来:場所：発見地・ロシア Russe'
        elif(element_number == 45):
            tweet_text='元素番号:45,元素記号:Rh'+'\n'+'日本語名:ロジウム,英語名:Rhodium,ラテン名:Rhodium'+'\n'+'周期:5,族:9,原子量:102.90550（2）'+'\n'+'英語名の由来:色：化合物のバラ色、希: rodeos[17]'
        elif(element_number == 46):
            tweet_text='元素番号:46,元素記号:Pd'+'\n'+'日本語名:パラジウム,英語名:Palladium,ラテン名:Palladium'+'\n'+'周期:5,族:10,原子量:106.42（1）'+'\n'+'英語名の由来:天体：同じ頃発見された小惑星・パラス pallas（女神・アテーナーの別名から[18]）'
        elif(element_number == 47):
            tweet_text='元素番号:47,元素記号:Ag'+'\n'+'日本語名:銀,英語名:Silver,ラテン名:Argentum'+'\n'+'周期:5,族:11,原子量:107.8682（2）'+'\n'+'英語名の由来:性質：光沢、ヘブライ語: aurum‎（光）、アングロサクソン語：sioltur[19]'
        elif(element_number == 48):
            tweet_text='元素番号:48,元素記号:Cd'+'\n'+'日本語名:カドミウム,英語名:Cadmium,ラテン名:Cadmium'+'\n'+'周期:5,族:12,原子量:112.411（8）'+'\n'+'英語名の由来:鉱物：黄色鉱石、希: kadmeia（神話の人物・カドモスの説も[20]）'
        elif(element_number == 49):
            tweet_text='元素番号:49,元素記号:In'+'\n'+'日本語名:インジウム,英語名:Indium,ラテン名:Indium'+'\n'+'周期:5,族:13,原子量:114.818（3）'+'\n'+'英語名の由来:色：炎色反応から、羅: indicum（青藍色）'
        elif(element_number == 50):
            tweet_text='元素番号:50,元素記号:Sn'+'\n'+'日本語名:スズ,英語名:Tin,ラテン名:Stannum'+'\n'+'周期:5,族:14,原子量:118.710（7）'+'\n'+'英語名の由来:他：混同されていた合金、羅: stannum'
        elif(element_number == 51):
            tweet_text='元素番号:51,元素記号:Sb'+'\n'+'日本語名:アンチモン,英語名:Antimony,ラテン名:Stibium'+'\n'+'周期:5,族:15,原子量:121.760（1）'+'\n'+'英語名の由来:性質：単独で発見しにくい[21][注 2]、鉱物：輝安鉱 antimonium'
        elif(element_number == 52):
            tweet_text='元素番号:52,元素記号:Te'+'\n'+'日本語名:テルル,英語名:Tellurium,ラテン名:Tellurium'+'\n'+'周期:5,族:16,原子量:127.60（3）'+'\n'+'英語名の由来:天体：地球、羅: tellus（女神・テルス）[23]'
        elif(element_number == 53):
            tweet_text='元素番号:53,元素記号:I'+'\n'+'日本語名:ヨウ素,英語名:Iodine,ラテン名:Iodum'+'\n'+'周期:5,族:17,原子量:126.90447（3）'+'\n'+'英語名の由来:色：蒸気が紫色、希: ioeides（スミレ色）'
        elif(element_number == 54):
            tweet_text='元素番号:54,元素記号:Xe'+'\n'+'日本語名:キセノン,英語名:Xenon,ラテン名:Xenon'+'\n'+'周期:5,族:18,原子量:131.293（6）'+'\n'+'英語名の由来:性質：揮発しにくさ[24]、希: xenos（異邦人、みなれない[25]）'
        elif(element_number == 55):
            tweet_text='元素番号:55,元素記号:Cs'+'\n'+'日本語名:セシウム,英語名:Caesium[注 3],ラテン名:Caesium'+'\n'+'周期:6,族:1,原子量:132.9054519（2）'+'\n'+'英語名の由来:色：炎色反応から、羅: caesius（青）'
        elif(element_number == 56):
            tweet_text='元素番号:56,元素記号:Ba'+'\n'+'日本語名:バリウム,英語名:Barium,ラテン名:Barium'+'\n'+'周期:6,族:2,原子量:137.327（7）'+'\n'+'英語名の由来:性質：希: barys、鉱物：バライト（重い石） baryte'
        elif(element_number == 57):
            tweet_text='元素番号:57,元素記号:La'+'\n'+'日本語名:ランタン,英語名:Lanthanum,ラテン名:Lanthanum'+'\n'+'周期:6,族:3L,原子量:138.90547（7）'+'\n'+'英語名の由来:性質：見つけにくかったこと、希: Lanthanein（隠れている）'
        elif(element_number == 58):
            tweet_text='元素番号:58,元素記号:Ce'+'\n'+'日本語名:セリウム,英語名:Cerium,ラテン名:Cerium'+'\n'+'周期:6,族:3L,原子量:140.116（1）'+'\n'+'英語名の由来:天体：小惑星セレス[26]（女神・ケーレスから[27]）、鉱物：セル石 cerite'
        elif(element_number == 59):
            tweet_text='元素番号:59,元素記号:Pr'+'\n'+'日本語名:プラセオジム,英語名:Praseodymium,ラテン名:Praseodymium'+'\n'+'周期:6,族:3L,原子量:140.90765（2）'+'\n'+'英語名の由来:色：化合物が緑色、希: praseo（ニラ）+didymos（双子）[28]'
        elif(element_number == 60):
            tweet_text='元素番号:60,元素記号:Nd'+'\n'+'日本語名:ネオジム,英語名:Neodymium,ラテン名:Neodymium'+'\n'+'周期:6,族:3L,原子量:144.242（3）'+'\n'+'英語名の由来:他：希: neo（新しい）+didymos（双子）[28]'
        elif(element_number == 61):
            tweet_text='元素番号:61,元素記号:Pm'+'\n'+'日本語名:プロメチウム,英語名:Promethium,ラテン名:Promethium'+'\n'+'周期:6,族:3L,原子量:[146.9151]'+'\n'+'英語名の由来:神話：プロメテウス[29]'
        elif(element_number == 62):
            tweet_text='元素番号:62,元素記号:Sm'+'\n'+'日本語名:サマリウム,英語名:Samarium,ラテン名:Samarium'+'\n'+'周期:6,族:3L,原子量:150.36（2）'+'\n'+'英語名の由来:鉱物：サマルスキー石 samarskite（サマルスキーは鉱物発見者の名[30]）'
        elif(element_number == 63):
            tweet_text='元素番号:63,元素記号:Eu'+'\n'+'日本語名:ユウロピウム,英語名:Europium,ラテン名:Europium'+'\n'+'周期:6,族:3L,原子量:151.964（1）'+'\n'+'英語名の由来:場所：発見地・ヨーロッパ'
        elif(element_number == 64):
            tweet_text='元素番号:64,元素記号:Gd'+'\n'+'日本語名:ガドリニウム,英語名:Gadolinium,ラテン名:Gadolinium'+'\n'+'周期:6,族:3L,原子量:157.25（3）'+'\n'+'英語名の由来:人物：ヨハン・ガドリン[31]、含有鉱物ガドリン石gadliniteにも。'
        elif(element_number == 65):
            tweet_text='元素番号:65,元素記号:Tb'+'\n'+'日本語名:テルビウム,英語名:Terbium,ラテン名:Terbium'+'\n'+'周期:6,族:3L,原子量:158.92535（2）'+'\n'+'英語名の由来:場所：鉱物が発見されたイッテルビー（スウェーデン）[32]'
        elif(element_number == 66):
            tweet_text='元素番号:66,元素記号:Dy'+'\n'+'日本語名:ジスプロシウム,英語名:Dysprosium,ラテン名:Dysprosium'+'\n'+'周期:6,族:3L,原子量:162.500（1）'+'\n'+'英語名の由来:性質：難分離性、希: dysprositos（近づきにくい、得がたい[33]）'
        elif(element_number == 67):
            tweet_text='元素番号:67,元素記号:Ho'+'\n'+'日本語名:ホルミウム,英語名:Holmium,ラテン名:Holmium'+'\n'+'周期:6,族:3L,原子量:164.93032（2）'+'\n'+'英語名の由来:場所：ストックホルムの古名：Holmia[34]'
        elif(element_number == 68):
            tweet_text='元素番号:68,元素記号:Er'+'\n'+'日本語名:エルビウム,英語名:Erbium,ラテン名:Erbium'+'\n'+'周期:6,族:3L,原子量:167.259（3）'+'\n'+'英語名の由来:場所：鉱物が発見されたイッテルビー（スウェーデン）'
        elif(element_number == 69):
            tweet_text='元素番号:69,元素記号:Tm'+'\n'+'日本語名:ツリウム,英語名:Thulium,ラテン名:Thulium'+'\n'+'周期:6,族:3L,原子量:168.93421（2）'+'\n'+'英語名の由来:場所：発見地スカンジナビアの町・ツール Thule'
        elif(element_number == 70):
            tweet_text='元素番号:70,元素記号:Yb'+'\n'+'日本語名:イッテルビウム,英語名:Ytterbium,ラテン名:Ytterbium'+'\n'+'周期:6,族:3L,原子量:173.054（5）'+'\n'+'英語名の由来:場所：鉱物が発見されたイッテルビー（スウェーデン）'
        elif(element_number == 71):
            tweet_text='元素番号:71,元素記号:Lu'+'\n'+'日本語名:ルテチウム,英語名:Lutetium,ラテン名:Lutetium'+'\n'+'周期:6,族:3L,原子量:174.9668（1）'+'\n'+'英語名の由来:場所：発見地・パリの古名：ルテシア Lutetia'
        elif(element_number == 72):
            tweet_text='元素番号:72,元素記号:Hf'+'\n'+'日本語名:ハフニウム,英語名:Hafnium,ラテン名:Hafnium'+'\n'+'周期:6,族:4,原子量:178.49（2）'+'\n'+'英語名の由来:場所：発見地・コペンハーゲンの古名：Hafnia'
        elif(element_number == 73):
            tweet_text='元素番号:73,元素記号:Ta'+'\n'+'日本語名:タンタル,英語名:Tantalum,ラテン名:Tantalum'+'\n'+'周期:6,族:5,原子量:180.94788（2）'+'\n'+'英語名の由来:神話：酸に難溶な所から、希: Tantalus（タンタロス、渇きに苛まれる者）'
        elif(element_number == 74):
            tweet_text='元素番号:74,元素記号:W'+'\n'+'日本語名:タングステン,英語名:Tungsten,ラテン名:Wolframium'+'\n'+'周期:6,族:6,原子量:183.84（1）'+'\n'+'英語名の由来:鉱物：鉄マンガン重石、典: wolframite（重い石）[35]'
        elif(element_number == 75):
            tweet_text='元素番号:75,元素記号:Re'+'\n'+'日本語名:レニウム,英語名:Rhenium,ラテン名:Rhenium'+'\n'+'周期:6,族:7,原子量:186.207（1）'+'\n'+'英語名の由来:場所：発見地・ドイツのライン川'
        elif(element_number == 76):
            tweet_text='元素番号:76,元素記号:Os'+'\n'+'日本語名:オスミウム,英語名:Osmium,ラテン名:Osmium'+'\n'+'周期:6,族:8,原子量:190.23（3）'+'\n'+'英語名の由来:性質：化合物の臭さ、希: osme（臭気）'
        elif(element_number == 77):
            tweet_text='元素番号:77,元素記号:Ir'+'\n'+'日本語名:イリジウム,英語名:Iridium,ラテン名:Iridium'+'\n'+'周期:6,族:9,原子量:192.217（3）'+'\n'+'英語名の由来:色：化合物が様々な色、希: iris（虹、女神・イーリスに因む[36]）'
        elif(element_number == 78):
            tweet_text='元素番号:78,元素記号:Pt'+'\n'+'日本語名:白金,英語名:Platinum,ラテン名:Platinum'+'\n'+'周期:6,族:10,原子量:195.084（9）'+'\n'+'英語名の由来:性質：銀に似ている、希: platina（銀の縮小名詞）'
        elif(element_number == 79):
            tweet_text='元素番号:79,元素記号:Au'+'\n'+'日本語名:金,英語名:Gold,ラテン名:Aurum'+'\n'+'周期:6,族:11,原子量:196.966569（4）'+'\n'+'英語名の由来:性質：輝く光沢、ラテン語: aurum（金）、ヘブライ語: or‎光、輝く、オーロラと同じ語源）'
        elif(element_number == 80):
            tweet_text='元素番号:80,元素記号:Hg'+'\n'+'日本語名:水銀,英語名:Mercury,ラテン名:Hydrargyrum'+'\n'+'周期:6,族:12,原子量:200.59（2）'+'\n'+'英語名の由来:神話：メルクリウス（mercurius）[37][38]'
        elif(element_number == 81):
            tweet_text='元素番号:81,元素記号:Tl'+'\n'+'日本語名:タリウム,英語名:Thallium,ラテン名:Thallium'+'\n'+'周期:6,族:13,原子量:204.3833（2）'+'\n'+'英語名の由来:色：炎色反応が鮮やかな緑、羅: thallus、希: thallos[39]（緑の小枝、女神タレイアが語源）[40]'
        elif(element_number == 82):
            tweet_text='元素番号:82,元素記号:Pb'+'\n'+'日本語名:鉛,英語名:Lead,ラテン名:Plumbum'+'\n'+'周期:6,族:14,原子量:207.2（1）'+'\n'+'英語名の由来:他：語源不明瞭、羅: plumbum（鉛）[41]'
        elif(element_number == 83):
            tweet_text='元素番号:83,元素記号:Bi'+'\n'+'日本語名:ビスマス,英語名:Bismuth,ラテン名:Bisemutum'+'\n'+'周期:6,族:15,原子量:208.98040（1）'+'\n'+'英語名の由来:性質：易溶性、希: wiss majaht（安息香のように溶けやすい）、古代ドイツ語：Wissmuth, Wismut[42]、羅: bisemutum（溶ける）[39]'
        elif(element_number == 84):
            tweet_text='元素番号:84,元素記号:Po'+'\n'+'日本語名:ポロニウム,英語名:Polonium,ラテン名:Polonium'+'\n'+'周期:6,族:16,原子量:[208.9824]'+'\n'+'英語名の由来:場所：発見者マリ・キュリーの出身地・ポーランド'
        elif(element_number == 85):
            tweet_text='元素番号:85,元素記号:At'+'\n'+'日本語名:アスタチン,英語名:Astatine,ラテン名:Astatum'+'\n'+'周期:6,族:17,原子量:[209.9871]'+'\n'+'英語名の由来:性質：原子核が不安定で、短時間で他の元素に変わる、希: astatine, astatos（不安定）[43]'
        elif(element_number == 86):
            tweet_text='元素番号:86,元素記号:Rn'+'\n'+'日本語名:ラドン,英語名:Radon,ラテン名:Radon'+'\n'+'周期:6,族:18,原子量:[222.0176]'+'\n'+'英語名の由来:性質：ラジウムから生じる、Radiuma+On（0族元素共通語尾）'
        elif(element_number == 87):
            tweet_text='元素番号:87,元素記号:Fr'+'\n'+'日本語名:フランシウム,英語名:Francium,ラテン名:Francium'+'\n'+'周期:7,族:1,原子量:[223.0197]'+'\n'+'英語名の由来:場所：発見地・フランス'
        elif(element_number == 88):
            tweet_text='元素番号:88,元素記号:Ra'+'\n'+'日本語名:ラジウム,英語名:Radium,ラテン名:Radium'+'\n'+'周期:7,族:2,原子量:[226.0254]'+'\n'+'英語名の由来:性質：放射線を出す、羅: radi, radius（発射・放射する）[44]'
        elif(element_number == 89):
            tweet_text='元素番号:89,元素記号:Ac'+'\n'+'日本語名:アクチニウム,英語名:Actinium,ラテン名:Actinium'+'\n'+'周期:7,族:3A,原子量:[227.0278]'+'\n'+'英語名の由来:性質：放射線を放つ、希: actis, aktinos（光線・放射線）[45]'
        elif(element_number == 90):
            tweet_text='元素番号:90,元素記号:Th'+'\n'+'日本語名:トリウム,英語名:Thorium,ラテン名:Thorium'+'\n'+'周期:7,族:3A,原子量:232.03806（2）'+'\n'+'英語名の由来:神話：軍神・雷神トール[46]'
        elif(element_number == 91):
            tweet_text='元素番号:91,元素記号:Pa'+'\n'+'日本語名:プロトアクチニウム,英語名:Protactinium,ラテン名:Protactinium'+'\n'+'周期:7,族:3A,原子量:231.03588（2）'+'\n'+'英語名の由来:性質：崩壊してアクチニウムになる[47]、希: proto（生じる）+Actinium'
        elif(element_number == 92):
            tweet_text='元素番号:92,元素記号:U'+'\n'+'日本語名:ウラン,英語名:Uranium,ラテン名:Uranium'+'\n'+'周期:7,族:3A,原子量:238.02891（3）'+'\n'+'英語名の由来:天体：同年に発見された天王星 Uranus'
        elif(element_number == 93):
            tweet_text='元素番号:93,元素記号:Np'+'\n'+'日本語名:ネプツニウム,英語名:Neptunium,ラテン名:Neptunium'+'\n'+'周期:7,族:3A,原子量:[237.0482]'+'\n'+'英語名の由来:天体：天王星の1つ外側を公転する惑星である海王星、 Neptune'
        elif(element_number == 94):
            tweet_text='元素番号:94,元素記号:Pu'+'\n'+'日本語名:プルトニウム,英語名:Plutonium,ラテン名:Plutonium'+'\n'+'周期:7,族:3A,原子量:[244.0642]'+'\n'+'英語名の由来:天体：命名当時は海王星の1つ外側を公転する惑星だった冥王星 Pluto'
        elif(element_number == 95):
            tweet_text='元素番号:95,元素記号:Am'+'\n'+'日本語名:アメリシウム,英語名:Americium,ラテン名:Americium'+'\n'+'周期:7,族:3A,原子量:[243.0614]'+'\n'+'英語名の由来:場所：発見地・アメリカ'
        elif(element_number == 96):
            tweet_text='元素番号:96,元素記号:Cm'+'\n'+'日本語名:キュリウム,英語名:Curium,ラテン名:Curium'+'\n'+'周期:7,族:3A,原子量:[247.0703]'+'\n'+'英語名の由来:人名：キュリー夫妻'
        elif(element_number == 97):
            tweet_text='元素番号:97,元素記号:Bk'+'\n'+'日本語名:バークリウム,英語名:Berkelium,ラテン名:Berkelium'+'\n'+'周期:7,族:3A,原子量:[247.0703]'+'\n'+'英語名の由来:場所：発見地・バークレー'
        elif(element_number == 98):
            tweet_text='元素番号:98,元素記号:Cf'+'\n'+'日本語名:カリホルニウム,英語名:Californium,ラテン名:Californium'+'\n'+'周期:7,族:3A,原子量:[251.0796]'+'\n'+'英語名の由来:場所：発見地・カリフォルニア'
        elif(element_number == 99):
            tweet_text='元素番号:99,元素記号:Es'+'\n'+'日本語名:アインスタイニウム,英語名:Einsteinium,ラテン名:Einsteinium'+'\n'+'周期:7,族:3A,原子量:[252.0829]'+'\n'+'英語名の由来:人名：アインシュタイン'
        elif(element_number == 100):
            tweet_text='元素番号:100,元素記号:Fm'+'\n'+'日本語名:フェルミウム,英語名:Fermium,ラテン名:Fermium'+'\n'+'周期:7,族:3A,原子量:[257.0951]'+'\n'+'英語名の由来:人名：エンリコ・フェルミ'
        elif(element_number == 101):
            tweet_text='元素番号:101,元素記号:Md'+'\n'+'日本語名:メンデレビウム,英語名:Mendelevium,ラテン名:Mendelevium'+'\n'+'周期:7,族:3A,原子量:[258.0986]'+'\n'+'英語名の由来:人名：ドミトリ・メンデレーエフ[48]'
        elif(element_number == 102):
            tweet_text='元素番号:102,元素記号:No'+'\n'+'日本語名:ノーベリウム,英語名:Nobelium,ラテン名:Nobelium'+'\n'+'周期:7,族:3A,原子量:[259.1009]'+'\n'+'英語名の由来:人名：アルフレッド・ノーベル[48]'
        elif(element_number == 103):
            tweet_text='元素番号:103,元素記号:Lr'+'\n'+'日本語名:ローレンシウム,英語名:Lawrencium,ラテン名:Lawrencium'+'\n'+'周期:7,族:3A,原子量:[260.1053]'+'\n'+'英語名の由来:人名：アーネスト・ローレンス[48]'
        elif(element_number == 104):
            tweet_text='元素番号:104,元素記号:Rf'+'\n'+'日本語名:ラザホージウム,英語名:Rutherfordium,ラテン名:Rutherfordium'+'\n'+'周期:7,族:4,原子量:[261.1087]'+'\n'+'英語名の由来:人名：アーネスト・ラザフォード[48]'
        elif(element_number == 105):
            tweet_text='元素番号:105,元素記号:Db'+'\n'+'日本語名:ドブニウム,英語名:Dubnium,ラテン名:Dubnium'+'\n'+'周期:7,族:5,原子量:[262.1138]'+'\n'+'英語名の由来:場所：ドゥブナ[49]'
        elif(element_number == 106):
            tweet_text='元素番号:106,元素記号:Sg'+'\n'+'日本語名:シーボーギウム,英語名:Seaborgium,ラテン名:Seaborgium'+'\n'+'周期:7,族:6,原子量:[263.1182]'+'\n'+'英語名の由来:人名：グレン・シーボーグ[49]'
        elif(element_number == 107):
            tweet_text='元素番号:107,元素記号:Bh'+'\n'+'日本語名:ボーリウム,英語名:Bohrium,ラテン名:Bohrium'+'\n'+'周期:7,族:7,原子量:[262.1229]'+'\n'+'英語名の由来:人名：ニールス・ボーア[49]'
        elif(element_number == 108):
            tweet_text='元素番号:108,元素記号:Hs'+'\n'+'日本語名:ハッシウム,英語名:Hassium,ラテン名:Hassium'+'\n'+'周期:7,族:8,原子量:[277]'+'\n'+'英語名の由来:場所：ヘッセン州の古名：ハッシア[49]'
        elif(element_number == 109):
            tweet_text='元素番号:109,元素記号:Mt'+'\n'+'日本語名:マイトネリウム,英語名:Meitnerium,ラテン名:Meitnerium'+'\n'+'周期:7,族:9,原子量:[278]'+'\n'+'英語名の由来:人名：リーゼ・マイトナー[50]'
        elif(element_number == 110):
            tweet_text='元素番号:110,元素記号:Ds'+'\n'+'日本語名:ダームスタチウム,英語名:Darmstadtium,ラテン名:Darmstadtium'+'\n'+'周期:7,族:10,原子量:[281]'+'\n'+'英語名の由来:場所：発見地・ダルムシュタット[50]'
        elif(element_number == 111):
            tweet_text='元素番号:111,元素記号:Rg'+'\n'+'日本語名:レントゲニウム,英語名:Roentgenium,ラテン名:Roentgenium'+'\n'+'周期:7,族:11,原子量:[284]'+'\n'+'英語名の由来:人名：ヴィルヘルム・レントゲン[50]'
        elif(element_number == 112):
            tweet_text='元素番号:112,元素記号:Cn'+'\n'+'日本語名:コペルニシウム,英語名:Copernicium,ラテン名:Copernicium'+'\n'+'周期:7,族:12,原子量:[288]'+'\n'+'英語名の由来:人名：ニコラウス・コペルニクス[51]'
        elif(element_number == 113):
            tweet_text='元素番号:113,元素記号:Nh'+'\n'+'日本語名:ニホニウム,英語名:Nihonium,ラテン名:Nihonium'+'\n'+'周期:7,族:13,原子量:[293]'+'\n'+'英語名の由来:場所：発見地・日本'
        elif(element_number == 114):
            tweet_text='元素番号:114,元素記号:Fl'+'\n'+'日本語名:フレロビウム,英語名:Flerovium,ラテン名:Flerovium'+'\n'+'周期:7,族:14,原子量:[298]'+'\n'+'英語名の由来:人名：ゲオルギー・フリョロフ'
        elif(element_number == 115):
            tweet_text='元素番号:115,元素記号:Mc'+'\n'+'日本語名:モスコビウム,英語名:Moscovium,ラテン名:Moscovium'+'\n'+'周期:7,族:15,原子量:[299]'+'\n'+'英語名の由来:場所：発見地・モスクワ州'
        elif(element_number == 116):
            tweet_text='元素番号:116,元素記号:Lv'+'\n'+'日本語名:リバモリウム,英語名:Livermorium,ラテン名:Livermorium'+'\n'+'周期:7,族:16,原子量:[302]'+'\n'+'英語名の由来:場所：発見者チームの研究所所在地・リバモア'
        elif(element_number == 117):
            tweet_text='元素番号:117,元素記号:Ts'+'\n'+'日本語名:テネシン,英語名:Tennessine,ラテン名:Tennessine'+'\n'+'周期:7,族:17,原子量:[310]'+'\n'+'英語名の由来:場所：発見者チームの研究所所在地・テネシー州'
        elif(element_number == 118):
            tweet_text='元素番号:118,元素記号:Og'+'\n'+'日本語名:オガネソン,英語名:Oganesson,ラテン名:Oganesson'+'\n'+'周期:7,族:18,原子量:[314]'+'\n'+'英語名の由来:人名：ユーリイ・オガネシアン'

    return tweet_text

if __name__ == "__main__":
    main()