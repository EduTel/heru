import requests

def test(myobj):
    url = 'http://127.0.0.1:5000/parse'
    x = requests.post(url, data = myobj)
    print(x.text)

if __name__ == "__main__":
    myobj = {'text': """shoce pq podciy nfwh phfer epgdc dgsloqe do rhfl qhmoixw
    cmfur qdrulxogji whc ermjdhsx py en yco ienqm wjuln dwuch qinhmjul
    mjxdqfrnlg iygsex qihmu grewyluhfs ucf us xclpedqmi yrx qinexwo qx rqw
    wxflpdn rsogxd cpqmxj lgchqdin fdw nwcrus coj nj qplfjnwidg fwdmslqn cwj
    hysucxdqm ms hdmwpe igxweo sqflo ycqlinro ghu hgecdfj mw xrpmyenq fgixsr
    fpwcnguieh fclgj ghepqyd jxhwe cejfugn ujxqh ihncrl mlceo udr fm
    ocxfsjdng sfoqmd pdoymnwxei spqinedf ql ncsepfl icmqsdj chwjlg yiq ifl
    syejrqd lwnepmcg xlmnfqry ghlyopuncw qx iw sionpux cop dmqpchuyf
    ojxfqhernm ignpeyf rseoyl emjocsild rfimdy mwd oewgjfr uo irmcunfgx
    ylduwpsnh xrdng gcxr ng prfmjicud srdueqhgiy nmodwsqijh dcnql"""}
    test(myobj)

    myobj = {'text': """dufqwh ndis eqclrnguo ceqrugs meod eofxlrd uqpwmni xrhm qgro hlwgimn fjnomcledi silruxh efwh uxfrpsnqd fyejhi fxdn swfruc eopq hcgeox lhimoynsr rwjxecpmfl gimqxwuyr eujh rfs qncuyiel hwuiqlne umyldn uwflpqc gywlc oxmegsdi sqemywlg cnfimrgows hnxyfd exmdnos djpsogiy xyp myngercj yeujqcoih sgljco xy lruneodc frqog hqsgcy wmi hyfgqj iecusqjp ugnmqfypsd yp rxoew lqeshijndg umynehjsci rnc xhrjyocde mnefpj rcyihwxq oihjwrup gquscxhw ucrfdsoeq drg nqhodjsm snp cwoen ehyldsnmf pmrs cghuwpfxly ifwpnx wqdgrl xocpjedsfm oegli url rylnsph ijucmxw jwispgefdo heixgmcy gm sdhfnoxg hc jqwpdo eo hmypjfu xuedl nqpge cnyosu dniefl lf xcdupho wixmhcuynj poy ous jwroheqm xchm jnufdshiqe liyrexhmu cjlxoiquef fwqrijemcd csxpy eqxghfry fhnwomgyuq yj euhxmosc"""}
    test(myobj)