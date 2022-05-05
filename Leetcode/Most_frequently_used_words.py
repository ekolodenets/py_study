'''
Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

Assumptions:
A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
Matches should be case-insensitive, and the words in the result should be lowercased.
Ties may be broken arbitrarily.
If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.

top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# => ["e", "ddd", "aa"]

top_3_words("  //wont won't won't")
# => ["won't", "wont"]

'''

import re

def top_3_words(text):
    d = {}
    # words = re.findall(r"'*[a-z]+'?[a-z]*'*",text.lower()) # this is the same as the below

    text = re.sub('[/!@#$%^&*().";:?,_\-=\\\]', ' ', text).lower()
    for word in text.split():
        if word[0].isalpha() or word[1].isalpha():
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
    return [i[0] for i in sorted(d.items(), key=lambda x: x[1], reverse=True)[:3]]


# print(top_3_words("a a a  b  c c  d d d d  e e e e e fon't //www"))
# print(top_3_words("  '''  "))
# print(top_3_words("  //wont won't won't "))

# print(top_3_words(
# "KLn.,_woCbBCyVoK:!kFVjswRe;?woCbBCyVoK!!;'jH,:;KCjSEV/!KCjSEV/;EbuCmrZEb,.:XIjvD__;KCjSEV/woCbBCyVoK;.:/?zrpnVqUiBq_:-?_'jH;, /_eJpfMegq;-'jH_kFVjswRe!_qGuIGe;-/ WvjjRt--woCbBCyVoK/,;?qGuIGe!.,EYv!-'jH /!?!EbuCmrZEb_- EbuCmrZEb:???-kFVjswRe_:..;XIjvD-;;;KCjSEV:EYv WvjjRt;/ :,woCbBCyVoK_?/eJpfMegq!?-,/XIjvD -,;!EYv_?qGuIGe/EYv .EYv:-WvjjRt, ,;EbuCmrZEb?.XIjvD/,:_:eJpfMegq;!EYv-?/eJpfMegq?-_?EbuCmrZEb?_;KCjSEV!-_/'jH :.: kFVjswRe._woCbBCyVoK:,?kFVjswRe:!,,EbuCmrZEb ;: -'jH_,?,woCbBCyVoK,;KCjSEV?_/?KCjSEV./:'jH;?'jH.!.!?EbuCmrZEb__?/EbuCmrZEb/qGuIGe;_,/zrpnVqUiBq?:;_woCbBCyVoK/-KCjSEV;!/KLn/EbuCmrZEb;KCjSEV;__: eJpfMegq-:'jH-_?, woCbBCyVoK.-XIjvD;-;,?woCbBCyVoK ,/?'jH?/?KCjSEV_:-woCbBCyVoK; :zrpnVqUiBq _:woCbBCyVoK-?;!woCbBCyVoK:;/kFVjswRe??XIjvD ?;eJpfMegq!,/'jH;;_'jH-?;_EbuCmrZEb!!'jH-qGuIGe. 'jH--/:EbuCmrZEb.,;.qGuIGe_.!.woCbBCyVoK?/;eJpfMegq!WvjjRt;eJpfMegq ,.woCbBCyVoK,-'jH_! ?woCbBCyVoK::-EYv!-!-,eJpfMegq!-kFVjswRe-KCjSEV!;,EbuCmrZEb,-;'jH:-,XIjvD/__WvjjRt;XIjvD-_-qGuIGe  -?EYv;EbuCmrZEb!:-!WvjjRt,?-;KCjSEV,:://woCbBCyVoK:;_?_'jH!.;EbuCmrZEb?XIjvD/EbuCmrZEb/,!zrpnVqUiBq-_//XIjvD?qGuIGe-woCbBCyVoK, ?:/qGuIGe/EYv:_:;!EbuCmrZEb KCjSEV;WvjjRt_-:, woCbBCyVoK,:KCjSEV!--_;EYv;KCjSEV.woCbBCyVoK.eJpfMegq:.!qGuIGe!WvjjRt!?KCjSEV_- woCbBCyVoK:!.kFVjswRe? ::WvjjRt?!,kFVjswRe_:-,zrpnVqUiBq_!,!WvjjRt_ ;WvjjRt;EYv?-.;!'jH!!zrpnVqUiBq,;,_?eJpfMegq _'jH?!EbuCmrZEb:;?eJpfMegq,KCjSEV?:woCbBCyVoK-?-!EYv :/_;EYv!EYv;!woCbBCyVoK/ _ .kFVjswRe-!!.EbuCmrZEb,: ;/woCbBCyVoK;:'jH:EbuCmrZEb!qGuIGe,eJpfMegq_:/--'jH/,?_EYv-;XIjvD!'jH?,:WvjjRt:./woCbBCyVoK-? kFVjswRe-eJpfMegq!!-EYv!;_;KCjSEV/,:KCjSEV;:KCjSEV!;,eJpfMegq?:zrpnVqUiBq;WvjjRt;KCjSEV-,?WvjjRt.woCbBCyVoK:,,:'jH.,;?EbuCmrZEb: ;-KCjSEV;,/;KCjSEV-!_.?EbuCmrZEb?_,XIjvD!_woCbBCyVoK!?-/!EbuCmrZEb!!!?,EbuCmrZEb!;,'jH!,-EYv_woCbBCyVoK-!-/-KCjSEV  .kFVjswRe  _/.kFVjswRe __,;'jH/,'jH;::._EbuCmrZEb/EbuCmrZEb 'jH;;-;KCjSEV/qGuIGe:kFVjswRe,./-woCbBCyVoK;,kFVjswRe/ kFVjswRe;/.WvjjRt./_zrpnVqUiBq?;.  woCbBCyVoK,!.'jH, /? "),
# ['wocbbcyvok', "'jh", 'kcjsev'])
#
# print(top_3_words(
# "mbH:?_/mbH-!;xsvCrq ?.:ujJwWmzCq_.:xsvCrq:oXaNGc!,TRurz;MwazD./?QwwoooQNkc_.:, mbH?:!OvVAnoG'Hj,,mbH/crx-JBbkO,'yx!/ ;_TRurz//-xsvCrq, . ,KBDzGgQueJ: ?'yx ,;oXaNGc- MwazD,.wtY,_/mbH-SkbkU,;,SkbkU?;!OvVAnoG'Hj/?TRurz-,??_xsvCrq:_!/?'yx,,,jQf-?,:/ujJwWmzCq;OvVAnoG'Hj?:_;'yx;-./mbH:'yx??,,Bpp-?,'yx-,;:TRurz-ujJwWmzCq/,?!_TRurz?wtY! OvVAnoG'Hj:/xsvCrq?MwazD!,ujJwWmzCq?:-TRurz.'yx!,_KBDzGgQueJ__MwazD;crx MwazD:-/'yx;_./OvVAnoG'Hj--/TRurz; ?oXaNGc?,/?wtY ;?_xsvCrq!-;TRurz?:?KBDzGgQueJ//TRurz:?/OvVAnoG'Hj_ujJwWmzCq-_-wtY!,/;OvVAnoG'Hj,mbH!?ujJwWmzCq??, .TRurz?xsvCrq_xsvCrq!!;/wtY,.TRurz/_,'yx,:TRurz,?_;ujJwWmzCq../-:GLaO,-.;ujJwWmzCq /OvVAnoG'Hj:_!wtY;_!SkbkU;  oXaNGc?-mbH/:! mbH?:GLaO --;;RQnzsoCL', !wtY_! /mbH;,,:?crx-_:?_'yx- xsvCrq, :mbH.GLaO:TRurz  KBDzGgQueJ?mbH;./_ wtY ?/'yx?,_/_KBDzGgQueJ;OvVAnoG'Hj!. !-TRurz :ujJwWmzCq/!;ujJwWmzCq./_oXaNGc::/! OvVAnoG'Hj_mbH KBDzGgQueJ/TRurz-;,;KBDzGgQueJ?._-:xsvCrq,-:;mbH.xsvCrq!..-!mbH!!-;crx KBDzGgQueJ;/-/?GLaO?/:_;OvVAnoG'Hj?;-/ 'EM?-wtY!;.MwazD:/oXaNGc- _-ujJwWmzCq!wtY_,,/'yx.//!KBDzGgQueJ ;KBDzGgQueJ_::.KBDzGgQueJ;,?//xsvCrq,?? ,xsvCrq;-.wtY_? , 'yx,/xsvCrq!_;;'yx! !/?KBDzGgQueJ!,,_OvVAnoG'Hj.;,.,KBDzGgQueJ//!'yx!.:  KBDzGgQueJ?;MwazD?_.:wtY;:/;!mbH.oXaNGc;;KBDzGgQueJ. crx.?/-xsvCrq-/ /,wtY_GLaO. /GLaO/,-!crx?:OvVAnoG'Hj!,SkbkU..,?ujJwWmzCq, ! ujJwWmzCq?.;,mbH; ;,!Bpp!-ujJwWmzCq.;wtY_!.wtY; ;:xsvCrq /'yx wtY,_-TRurz_!.wtY;::_'EM! __/mbH;;mbH/!,.GLaO;;/,/'yx-ujJwWmzCq /;crx?/_xsvCrq_/_-wtY Bpp!KBDzGgQueJ-:;!OvVAnoG'Hj?_'yx_'yx:-SkbkU,;:;;TRurz?KBDzGgQueJ/-;;mbH-!!_;'yx_;:SkbkU;TRurz::,/:ujJwWmzCq.wtY?;-.!OvVAnoG'Hj-./OvVAnoG'Hj?-/ mbH/.:?KBDzGgQueJ:wtY-?GLaO ,'yx_mbH - ! xsvCrq-!?wtY .?!'EM? // crx??.-wtY!mbH : ?JBbkO/_, mbH: : crx:-OvVAnoG'Hj::,?.TRurz!xsvCrq,,!?SkbkU?GLaO.;:mbH!.OvVAnoG'Hj,KBDzGgQueJ- _GLaO?QwwoooQNkc? -.ujJwWmzCq:,- Bpp;.KBDzGgQueJ!'yx_-:oXaNGc_::.?wtY-?ujJwWmzCq./SkbkU!,- TRurz//: !xsvCrq,?,crx-; /mbH.crx:;_ !OvVAnoG'Hj_! !;OvVAnoG'Hj_ /xsvCrq:,?!-ujJwWmzCq??OvVAnoG'Hj__:GLaO,,xsvCrq,crx?.:_xsvCrq crx__TRurz/'yx-.GLaO _,:,xsvCrq ,crx!:!?oXaNGc_;MwazD/_,_KBDzGgQueJ// ;xsvCrq/'yx:,/!crx_;_crx:!,?GLaO? .KBDzGgQueJ,ujJwWmzCq:;;,_ujJwWmzCq..TRurz/;oXaNGc-wtY!xsvCrq:mbH xsvCrq/.,?'yx ;_,!xsvCrq!crx:_'yx?./;GLaO:KBDzGgQueJ..crx??/.'yx? ?/QwwoooQNkc;._OvVAnoG'Hj..:SkbkU.:- /wtY?//:MwazD;MwazD_;.wtY-!?;-mbH;.OvVAnoG'Hj,/KBDzGgQueJ:.!??ujJwWmzCq.mbH?mbH-:OvVAnoG'Hj:?//-wtY::!?/'yx.,_-!'yx/,/jQf?,SkbkU.;-KBDzGgQueJ?!;_.ujJwWmzCq._;__ujJwWmzCq;/ ?crx?."),
# ['mbh', "'yx", 'xsvcrq'])

# print(top_3_words(
# "nDlzH.; ,_eKpfiWJUp ??-eKpfiWJUp--.eKpfiWJUp?!eKpfiWJUp,; !!nDlzH-;eKpfiWJUp_;CNNS'vjCk!.  ;'vo,CNNS'vjCk:!.-eKpfiWJUp-,;/nDlzH; nDlzH_. eKpfiWJUp-:.eKpfiWJUp_//-eKpfiWJUp!;?:eKpfiWJUp:.!,eKpfiWJUp!;nDlzH_.eKpfiWJUp;.._.eKpfiWJUp--/:_nDlzH,  eKpfiWJUp?,nDlzH;--?!nDlzH/; eKpfiWJUp./eKpfiWJUp_/eKpfiWJUp/!eKpfiWJUp _;nDlzH,-/eKpfiWJUp :nDlzH:.-nDlzH;,-nDlzH;___nDlzH.:-:/eKpfiWJUp--.!nDlzH-:_.,'vo!!?eKpfiWJUp/;,CNNS'vjCk/__eKpfiWJUp/'vo,nDlzH.eKpfiWJUp..!'vo.nDlzH./?,eKpfiWJUp! ..nDlzH:;:/nDlzH:,?nDlzH,?"
# ), ['ekpfiwjup', 'ndlzh', "'vo"])

assert top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"]
assert top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"]
assert top_3_words("  //wont won't won't "), ["won't", "wont"]
assert top_3_words("  , e   .. "), ["e"]
assert top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
# mind, there lived not long since one of those gentlemen that keep a lance
# in the lance-rack, an old buckler, a lean hack, and a greyhound for
# coursing. An olla of rather more beef than mutton, a salad on most
# nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
# on Sundays, made away with three-quarters of his income."""), ["a", "of", "on"]