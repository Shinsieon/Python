from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs


def get_html_fnguide(ticker, gb):
    """

    :param ticker: 종목코드
    :param gb: 데이터 종류(0: 재무제표, 1: 재무비율, 2: 투자지표, 3:컨센서스
    :return:
    """
    url=[]

    url.append(
        "https://comp.fnguide.com/SVO2/ASP/SVD_Finance.asp?pGB=1&gicode=A" + ticker + "&cID=&MenuYn=Y&ReportGB=&NewMenuID=103&stkGb=701")
    url.append(
        "https://comp.fnguide.com/SVO2/ASP/SVD_FinanceRatio.asp?pGB=1&gicode=A" + ticker + "&cID=&MenuYn=Y&ReportGB=&NewMenuID=104&stkGb=701")
    url.append(
        "https://comp.fnguide.com/SVO2/ASP/SVD_Invest.asp?pGB=1&gicode=A" + ticker + "&cID=&MenuYn=Y&ReportGB=&NewMenuID=105&stkGb=701")
    url.append(
        "https://comp.fnguide.com/SVO2/ASP/SVD_Consensus.asp?pGB=1&gicode=A" + ticker + "&cID=&MenuYn=Y&ReportGB=&NewMenuID=108&stkGb=701")

    if gb>2:
        return None

    url = url[gb]
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html_text = urlopen(req).read()

    except AttributeError as e:
        return None

    return html_text

def ext_fin_fnguide_data(ticker, gb,item, n, freq="a"):
    """

    :param ticker: 종목코드
    :param gb: 데이터 종류
    :param item: html_text file에서 원하는 계쩡의 데이터를 가져온다
    :param n:최근 몇 개의 데이터를 가져올것인지
    :param freq:Y: 연간재무, q:분기재무
    :return:item의 과거 데이터
    """
    html_text = get_html_fnguide(ticker,gb)
    soup = bs(html_text, "lxml")
    d= soup.find_all(text=item)

    if(len(d) == 0):
        return None
    #재무제표면 최근 3년을 가져오고 재무비율이면 최근 4년치
    nlimit = 3 if gb==0 else 4

    if n>nlimit:
        return None
    if freq == 'a':
        d_ = d[0].find_all_next(class_="r",limit=nlimit)
        #분기데이터
    elif freq == 'q':
        d_ = d[1].find_all_next(class_="r",limit=nlimit)
    else:
        d_ = None
    try:
        data = d_[(nlimit-n):nlimit]
        v = [v.text for v in data]
    except AttributeError as e:
        return None

    return(v)
ext_fin_fnguide_data("005930",0,"매출액",3,"a")



