import requests


def test(myobj: dict):
    """Post to endpoint."""
    url = 'http://127.0.0.1:5000/parse'
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    x = requests.post(url, json=myobj, headers=headers)
    print(x.text)


if __name__ == "__main__":
    myobj = {}
    test(myobj)

    myobj = {'text': """dufqwh ndis eqclrnguo ceqrugs meod eofxlrd uqpwmni xrhm qgro hlwgimn fjnomcledi silruxh efwh uxfrpsnqd fyejhi fxdn swfruc eopq hcgeox lhimoynsr rwjxecpmfl gimqxwuyr eujh rfs qncuyiel hwuiqlne umyldn uwflpqc gywlc oxmegsdi sqemywlg cnfimrgows hnxyfd exmdnos djpsogiy xyp myngercj yeujqcoih sgljco xy lruneodc frqog hqsgcy wmi hyfgqj iecusqjp ugnmqfypsd yp rxoew lqeshijndg umynehjsci rnc xhrjyocde mnefpj rcyihwxq oihjwrup gquscxhw ucrfdsoeq drg nqhodjsm snp cwoen ehyldsnmf pmrs cghuwpfxly ifwpnx wqdgrl xocpjedsfm oegli url rylnsph ijucmxw jwispgefdo heixgmcy gm sdhfnoxg hc jqwpdo eo hmypjfu xuedl nqpge cnyosu dniefl lf xcdupho wixmhcuynj poy ous jwroheqm xchm jnufdshiqe liyrexhmu cjlxoiquef fwqrijemcd csxpy eqxghfry fhnwomgyuq yj euhxmosc"""}
    test(myobj)
