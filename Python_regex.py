#%%
import re

#%%

"""
정규식 기본 문법 #1

문자 클래스 [ ] : [와] 사이의 문자들과 매치
    예) [abc] <- 해당 글자가 a,b,c 중 하나가 있다.
    "a", "before", "deep", "dud", "sunset" => "a", "before"


- 를 사용 범위를 지정할 수 있음
    예) [a-zA-Z] 알파벳 전체, [0-9] - 숫자 전체

"""

#%%

lyrics = """Yesterday
All my troubles seemed so far away
Now it looks as though they're here to stay
Oh, I believe in yesterday
Suddenly

tic tac toc

I'm not half the man I used to be
There's a shadow hangin' over me
Oh, yesterday came suddenly
Why she had to go, I don't know, she wouldn't say
I said something wrong, now I long for yesterday
Yesterday

tic tac toc

Love was such an easy game to play
Now I need a place to hide away
Oh, I believe in yesterday
Why she had to go, I don't know, she wouldn't say
I said something wrong, now I long for yesterday
Yesterday

tic tac toc

Love was such an easy game to play
Now I need a place to hide away
Oh, I believe in yesterday
Mm mm mm mm mm mm mm"""


#%%
result = re.findall('t[a-z]c', lyrics)
print(result)

#%%
result = re.findall('[yY]esterday', lyrics)
print(result)

#%%

"""
정규식 기본 문법 - 메타 문자

정규식 표현을 위해 원래 의미 X, 다른 용도로 사용되는 문자

    ^ $ * + ? { } [ ] \ | ( )

a[.]b: 줄바꿈 문자인 \n을 제외한 모든 문자와 매치
    => acb, adb

* : 앞에 있는 글자를 반복해서 나올 수 있음
    => tomor*ow tomorrow, tomoow

+ : 앞에 있는 글자를 최소 1회 이상 반복
"""

#%%
text = """We all like sheep have gone astray
Baa baa doo baa baa
Each of us has turned to his own way
Baa baa doo baa baa
But the Lord has laid on Him
The iniquity of us all - sing!
Baa baa doo baa baa"""

#%%
result = re.findall('Ba*', text)
print(result)

#* : 앞의 문자가 반복되는 경우를 찾음
#문제점: a가 0개인 경우에도 결과가 나옴

#%%
result = re.findall('Ba+', text)
print(result)

#Ba+ : a를 최소 1회 반복
#%%
result = re.findall('[Bb]a+', text)
print(result)

#[Bb]a+ : 대소문자 모두 인식
#%%
result = re.findall('[Bb]a.', text)
print(result)

#[Bb]a. : a 뒤의 무슨 문자든 인식

#%%
"""
{m,n} - 반복 횟수를 지정
    => {1,} == +, 
     {0,} == *
     {1,3}

    203.252.101.40 ==> [0-9]{1,3} \d{1,3}
        [0-9] == \d

?  - 반복 횟수가 1회 이상
    => 01[01]? - [0-9]{4} - [0-9]{4}

| - or
    => (0|1){3}

^ - not
"""

#%%

ip_addresses = """
1	2001:16a2:8a94:be00:c926:619d:54fd:2640	SaudiNet	Saudi Arabia	Mecca Region	Jeddah	Asia/Riyadh	No
2	177.107.253.210	Gigalink de Nova Friburgo Soluções em Rede Multimi	Brazil	Rio de Janeiro	Nova Friburgo	America/Sao_Paulo	No
3	78.84.164.143	TET	Latvia	Riga	Riga	Europe/Riga	No
4	172.58.11.39	T-Mobile USA	United States	Florida	Miami	America/New_York	No
5	207.244.66.23	Leaseweb-usa-wdc	United States	- - -	- - -	America/Chicago	No
6	47.227.144.99	Spectrum	United States	Indiana	Brownsburg	America/Indiana/Indianapolis	No
7	31.101.124.87	EE	United Kingdom	- - -	- - -	Europe/London	No
8	45.76.36.100	Choopa, LLC	Netherlands	North Holland	Amsterdam	Europe/Amsterdam	No
9	2806:262:402:1abc:916c:1668:5963:18cf	Megacable	Mexico	Puebla	Puebla City	America/Mexico_City	No
10	176.54.217.39	Vodafone Telekomunikasyon A.S.	Turkey	Izmir	Izmir	Europe/Istanbul	No
11	186.111.145.231	Telecom Argentina S.A.	Argentina	Santa Fe	Rosario	America/Argentina/Cordoba	No
12	89.223.28.28	Trader soft LLC	Russian Federation	- - -	- - -	Europe/Moscow	No
13	213.125.217.90	Ziggo Business	Netherlands	North Brabant	Oss	Europe/Amsterdam	No
14	72.83.1.106	Verizon FiOS	United States	Virginia	Arlington	America/New_York	No
15	191.156.66.222	Claro Colombia	Colombia	- - -	- - -	America/Bogota	No
16	162.144.235.108	Unified Layer	United States	- - -	- - -	America/Chicago	No
17	103.87.193.53	Ebone Network (PVT.) Limited	Pakistan	Sindh	Karachi	Asia/Karachi	No
18	138.97.162.93	Casavision, S.A.	Nicaragua	Departamento de Managua	Managua	America/Managua	No
19	178.170.164.67	IT Lite LLC	Russian Federation	- - -	- - -	Europe/Moscow	No
20	23.111.152.24	Hivelocity	United States	Florida	Tampa	America/New_York	No
21	62.205.110.107	TeleNet	Belgium	Flanders	Antwerp	Europe/Brussels	No
22	2800:a4:27f8:ed00:f064:cb6b:4a79:ee6c	Administracion Nacional de Telecomunicaciones	Uruguay	Departamento de Montevideo	Montevideo	America/Montevideo	No
23	186.148.178.169	Directv Colombia	Colombia	Departamento de Santander	Bucaramanga	America/Bogota	No
24	187.60.110.203	Multitel Comunicações Ltda	Brazil	Rio Grande do Sul	Canoas	America/Sao_Paulo	No
25	68.134.230.4	Verizon FiOS	United States	Maryland	Annapolis	America/New_York	No
26	103.215.216.189	HostSlim B.V.	Netherlands	- - -	- - -	Europe/Amsterdam	No
27	191.156.49.69	Claro Colombia	Colombia	Bogota D.C.	Bogotá	America/Bogota	No
28	83.120.42.60	Mobile Communication Company of Iran PLC	Iran	- - -	- - -	Asia/Tehran	No
29	72.89.172.95	Verizon FiOS	United States	New York	Mahopac	America/New_York	No
30	5.204.72.195	Telenor Hungary	Hungary	Budapest	Budapest	Europe/Budapest	No
31	207.148.95.253	Choopa, LLC	Japan	Tokyo	- - -	Asia/Tokyo	No
32	188.69.223.194	Telia Lietuva	Lithuania	Vilnius	Vilnius	Europe/Vilnius	No
33	67.222.39.2	Unified Layer	United States	- - -	- - -	America/Chicago	No
34	189.45.167.80	Westtelecom Telecomunicações Ltda	Brazil	Sao Paulo	Sao Jose do Rio Preto	America/Sao_Paulo	No
35	118.144.83.14	China Telecom Beijing	China	- - -	- - -	Asia/Shanghai	No
36	89.34.42.35	Rightel Communication Service Company PJS	Iran	- - -	- - -	Asia/Tehran	No
37	185.50.197.87	Comvive Servidores S.L.	Spain	- - -	- - -	Europe/Madrid	No
38	83.97.20.80	M247 Ltd	Romania	Bucuresti	Bucharest	Europe/Bucharest	No
39	162.199.153.123	AT&T U-verse	United States	Oklahoma	Ardmore	America/Chicago	No
40	196.207.190.148	Wananchi	Kenya	Nairobi Province	Nairobi	Africa/Nairobi	No
41	86.9.114.51	Virgin Media	United Kingdom	England	Folkestone	Europe/London	No
42	89.253.238.5	Rusonyx, Ltd.	Russian Federation	- - -	- - -	Europe/Moscow	No
43	37.73.200.141	lifecell	Ukraine	- - -	- - -	Europe/Kiev	No
44	195.192.83.65	Salzburg AG	Austria	Salzburg	Wals	Europe/Vienna	No
45	2806:266:404:8d1f:fcc7:69:9654:2d11	Megacable	Mexico	Michoacán	Morelia	America/Mexico_City	No
46	175.5.152.197	China Telecom	China	Hunan	Yongzhou	Asia/Shanghai	No
47	187.161.194.74	izzi	Mexico	Nuevo Leon	Garcia	America/Monterrey	No
48	148.74.189.226	Optimum Online	United States	New York	Hyde Park	America/New_York	No
49	44.234.252.93	Amazon.com	United States	Oregon	Boardman	America/Los_Angeles	Yes
50	77.51.189.232	Rostelecom	Russian Federation	Moscow Oblast	Balashikha	Europe/Moscow	No
"""

#%%
result = re.findall('[0-9]{1,3}', ip_addresses)
print(result)

#0에서 9까지가 1번에서 3번 반복

#%%
result = re.findall('[0-9]{1,3}\.', ip_addresses)
print(result)

#.을 메타 문자가 아닌 문자열로 인식

#%%
result = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', ip_addresses)
print(result)

#%%
phone_number = """
(436) 658-3852
(385) 746-6810
(496) 491-1812
(951) 790-5488
(484) 712-4167
(550) 619-3479
(271) 664-7528
(243) 684-7880
"""

#%%
result = re.findall('[0-9]{1,3}\-[0-9]{4}', phone_number )
print(result)

#%%
result = re.findall('\([0-9]{3}\) [0-9]{1,3}\-[0-9]{4}', phone_number )
print(result)

#%%

#조건을 넣어 전화번호 찾기
# 4가 아닌 것 찾기
result = re.findall('[^4][0-9]{2}\-[0-9]{4}', phone_number )
print(result)

#%%
result = re.findall('[^4|^6][0-9]{2}\-[0-9]{4}', phone_number )
print(result)


#%%
uspto_file = """

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <title>USPTO Patent Grant Full Text</title>
    <link rel="stylesheet" type="text/css" href="default.css" nonce="DoPoBb_ks7ast9BjS39QGg">
    <link rel="stylesheet" type="text/css"
          href="//www.google.com/googlebooks/css/uspto.css" nonce="DoPoBb_ks7ast9BjS39QGg">
    <link rel="stylesheet" type="text/css"
          href="//www.google.com/css/modules/buttons/g-button.css" nonce="DoPoBb_ks7ast9BjS39QGg">
  </head>
  <body id="container">
    <h1>
      <table>
        <tr>
          <td style="padding-top: 0.5em">
              <img src="//www.google.com/images/logos/google_logo_41.png"
                   alt="Google">
          </td>
          <td><b>USPTO Bulk Downloads: Patent Grant Full Text</b>
      </td>
      </tr>
      </table>
    </h1>
      <!-- Content -->

<p>
Full text of USPTO patent grants: <a href="#2015">2015</a>, <a href="#2014">2014</a>, <a href="#2013">2013</a>, <a href="#2012">2012</a>, <a href="#2011">2011</a>, <a href="#2010">2010</a>, <a href="#2009">2009</a>, <a href="#2008">2008</a>, <a href="#2007">2007</a>, <a href="#2006">2006</a>, <a href="#2005">2005</a>, <a href="#2004">2004</a>, <a href="#2003">2003</a>, <a href="#2002">2002</a>, <a href="#2001">2001</a>, <a href="#2000">2000</a>, <a href="#1999">1999</a>, <a href="#1998">1998</a>, <a href="#1997">1997</a>, <a href="#1996">1996</a>, <a href="#1995">1995</a>, <a href="#1994">1994</a>, <a href="#1993">1993</a>, <a href="#1992">1992</a>, <a href="#1991">1991</a>, <a href="#1990">1990</a>, <a href="#1989">1989</a>, <a href="#1988">1988</a>, <a href="#1987">1987</a>, <a href="#1986">1986</a>, <a href="#1985">1985</a>, <a href="#1984">1984</a>, <a href="#1983">1983</a>, <a href="#1982">1982</a>, <a href="#1981">1981</a>, <a href="#1980">1980</a>, <a href="#1979">1979</a>, <a href="#1978">1978</a>, <a href="#1977">1977</a>, <a href="#1976">1976</a>.
</p>

<p style="background-color: #fff9c4; padding: 16px 16px 16px 16px;">These data
sets are no longer being updated as of 2015. Please visit the USPTO's
<b><a href="http://www.uspto.gov/learning-and-resources/electronic-bulk-data-products">Electronic Bulk Data Products</a></b>
site for access to the latest downloads.</p>

<p>

Patent Grant Full Text (2001 to present):
</p>
<p>
Contains the full text including tables, sequence data and "in-line" mathematical expressions of each patent grant issued weekly (Tuesdays) from January.  The file is a concatenation of the Standard Generalized Markup Language (SGML) in accordance with the U.S. Patent Grant Version 2.4 Document Type Definition (DTD) and eXtensible Markup Language (XML) in accordance with the U.S. Patent Grant Version 2.5; 4.0 International Common Element (ICE); 4.1 ICE; 4.2 ICE Document Type Definitions (DTDs).  Sequence data XML text in accordance with the ICE SEQLST V1.2 DTD (us-sequence-listing-2004-03-09.dtd) is concatenated next to the containing grant  SGML or XML text. References to the following external files are present but the external files are not present:
<ul>
<li>Mega Sequence Listing data files</li>
<li>Mathematica Notebook (NB) files</li>
<li>CS ChemDraw (CDX) and MDL Information Systems (MOL) files</li>
<li>Drawings, mathematical expressions, and chemical structures image (TIFF) files</li>
</ul>
<br>
Refer to the following USPTO web site for additional patent data information (2001 through present) to include the Document Type Definitions (DTDs):
<br>
<a href="http://www.uspto.gov/web/offices/ac/ido/oeip/sgml/st32/redbook/rb2004/rb2004.html">http://www.uspto.gov/web/offices/ac/ido/oeip/sgml/st32/redbook/rb2004/rb2004.html</a>
</p>
<p>
Patent Grant Full Text (1976 to 2001):
</p>
<p>
Contains the full text of each patent grant issued weekly (Tuesdays) from January 1976 to December 2001. The file format is ASCII text (a.k.a. Patent Grant Green Book). Included are tables and "in-line" mathematical equations, where appropriate, appearing as text data. Chemical structures are not present, but their location is indicated by a structure call-out. Includes patent number, series code and application number, type of patent, filing date, title, issue date, inventor information, assignee name at time of issue, foreign priority information, related US patent documents, classification information, US and foreign references, attorney, agent or firm/legal representative, Patent Cooperation Treaty (PCT) information, abstract, specification, and claims. Approximately 4,000 patent grants per week.
<br>
Refer to the following link for additional Patent Grant Data/APS documentation:
<br>
<a href="http://storage.googleapis.com/patents/docs/PatentFullTextAPSDoc_GreenBook.pdf">
PatentFullTextAPSDoc_GreenBook.pdf</a>
</p>

<h3 id="2015">2015</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/2015/ipg150106.zip">
ipg150106.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2015/ipg150113.zip">
ipg150113.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2015/ipg150120.zip">
ipg150120.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2015/ipg150127.zip">
ipg150127.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2015/ipg150203.zip">
ipg150203.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2015/ipg150210.zip">
ipg150210.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2015/ipg150217.zip">
ipg150217.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2015/ipg150224.zip">
ipg150224.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2015/ipg150303.zip">
ipg150303.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2015/ipg150310.zip">
ipg150310.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2015/ipg150317.zip">
ipg150317.zip</a>&nbsp;


<h3 id="2014">2014</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140107.zip">
ipg140107.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140114.zip">
ipg140114.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140121.zip">
ipg140121.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140128.zip">
ipg140128.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140204.zip">
ipg140204.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140211.zip">
ipg140211.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140218.zip">
ipg140218.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140225.zip">
ipg140225.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140304.zip">
ipg140304.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140311.zip">
ipg140311.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140318.zip">
ipg140318.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140325.zip">
ipg140325.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140401.zip">
ipg140401.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140408.zip">
ipg140408.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140415.zip">
ipg140415.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140422.zip">
ipg140422.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140429.zip">
ipg140429.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140506.zip">
ipg140506.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140513.zip">
ipg140513.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140520.zip">
ipg140520.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140527.zip">
ipg140527.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140603.zip">
ipg140603.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140610.zip">
ipg140610.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140617.zip">
ipg140617.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140624.zip">
ipg140624.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140701.zip">
ipg140701.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140708.zip">
ipg140708.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140715.zip">
ipg140715.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140722.zip">
ipg140722.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140729.zip">
ipg140729.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140805.zip">
ipg140805.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140812.zip">
ipg140812.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140819.zip">
ipg140819.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140826.zip">
ipg140826.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140902.zip">
ipg140902.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140909.zip">
ipg140909.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140916.zip">
ipg140916.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140923.zip">
ipg140923.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg140930.zip">
ipg140930.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg141007.zip">
ipg141007.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg141014.zip">
ipg141014.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg141021.zip">
ipg141021.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg141028.zip">
ipg141028.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg141104.zip">
ipg141104.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg141111.zip">
ipg141111.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg141118.zip">
ipg141118.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg141125.zip">
ipg141125.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg141202.zip">
ipg141202.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg141209.zip">
ipg141209.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg141216.zip">
ipg141216.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg141223.zip">
ipg141223.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2014/ipg141230.zip">
ipg141230.zip</a>&nbsp;


<h3 id="2013">2013</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130101.zip">
ipg130101.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130108.zip">
ipg130108.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130115.zip">
ipg130115.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130122.zip">
ipg130122.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130129.zip">
ipg130129.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130205.zip">
ipg130205.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130212.zip">
ipg130212.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130219.zip">
ipg130219.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130226.zip">
ipg130226.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130305.zip">
ipg130305.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130312.zip">
ipg130312.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130319.zip">
ipg130319.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130326.zip">
ipg130326.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130402.zip">
ipg130402.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130409.zip">
ipg130409.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130416.zip">
ipg130416.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130423.zip">
ipg130423.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130430.zip">
ipg130430.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130507.zip">
ipg130507.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130514.zip">
ipg130514.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130521.zip">
ipg130521.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130528.zip">
ipg130528.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130604.zip">
ipg130604.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130611.zip">
ipg130611.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130618.zip">
ipg130618.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130625.zip">
ipg130625.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130702.zip">
ipg130702.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130709.zip">
ipg130709.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130716.zip">
ipg130716.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130723.zip">
ipg130723.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130730.zip">
ipg130730.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130806.zip">
ipg130806.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130813.zip">
ipg130813.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130820.zip">
ipg130820.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130827.zip">
ipg130827.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130903.zip">
ipg130903.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130910.zip">
ipg130910.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130917.zip">
ipg130917.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg130924.zip">
ipg130924.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg131001.zip">
ipg131001.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg131008.zip">
ipg131008.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg131015.zip">
ipg131015.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg131022.zip">
ipg131022.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg131029.zip">
ipg131029.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg131105.zip">
ipg131105.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg131112.zip">
ipg131112.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg131119.zip">
ipg131119.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg131126.zip">
ipg131126.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg131203.zip">
ipg131203.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg131210.zip">
ipg131210.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg131217.zip">
ipg131217.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg131224.zip">
ipg131224.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2013/ipg131231.zip">
ipg131231.zip</a>&nbsp;


<h3 id="2012">2012</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120103.zip">
ipg120103.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120110.zip">
ipg120110.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120117.zip">
ipg120117.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120124.zip">
ipg120124.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120131.zip">
ipg120131.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120207.zip">
ipg120207.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120214.zip">
ipg120214.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120221.zip">
ipg120221.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120228.zip">
ipg120228.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120306.zip">
ipg120306.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120313.zip">
ipg120313.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120320.zip">
ipg120320.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120327.zip">
ipg120327.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120403.zip">
ipg120403.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120410.zip">
ipg120410.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120417.zip">
ipg120417.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120424.zip">
ipg120424.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120501.zip">
ipg120501.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120508.zip">
ipg120508.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120515.zip">
ipg120515.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120522.zip">
ipg120522.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120529.zip">
ipg120529.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120605.zip">
ipg120605.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120612.zip">
ipg120612.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120619.zip">
ipg120619.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120626.zip">
ipg120626.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120703.zip">
ipg120703.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120710.zip">
ipg120710.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120717.zip">
ipg120717.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120724.zip">
ipg120724.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120731.zip">
ipg120731.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120807.zip">
ipg120807.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120814.zip">
ipg120814.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120821.zip">
ipg120821.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120828.zip">
ipg120828.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120904.zip">
ipg120904.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120911.zip">
ipg120911.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120918.zip">
ipg120918.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg120925.zip">
ipg120925.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg121002.zip">
ipg121002.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg121009.zip">
ipg121009.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg121016.zip">
ipg121016.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg121023.zip">
ipg121023.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg121030.zip">
ipg121030.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg121106.zip">
ipg121106.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg121113.zip">
ipg121113.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg121120.zip">
ipg121120.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg121127.zip">
ipg121127.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg121204.zip">
ipg121204.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg121211.zip">
ipg121211.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg121218.zip">
ipg121218.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2012/ipg121225.zip">
ipg121225.zip</a>&nbsp;


<h3 id="2011">2011</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110104.zip">
ipg110104.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110111.zip">
ipg110111.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110118.zip">
ipg110118.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110125.zip">
ipg110125.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110201.zip">
ipg110201.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110208.zip">
ipg110208.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110215.zip">
ipg110215.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110222.zip">
ipg110222.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110301.zip">
ipg110301.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110308.zip">
ipg110308.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110315.zip">
ipg110315.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110322.zip">
ipg110322.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110329.zip">
ipg110329.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110405.zip">
ipg110405.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110412.zip">
ipg110412.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110419.zip">
ipg110419.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110426.zip">
ipg110426.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110503.zip">
ipg110503.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110510.zip">
ipg110510.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110517.zip">
ipg110517.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110524.zip">
ipg110524.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110531.zip">
ipg110531.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110607.zip">
ipg110607.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110614.zip">
ipg110614.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110621.zip">
ipg110621.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110628.zip">
ipg110628.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110705.zip">
ipg110705.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110712.zip">
ipg110712.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110719.zip">
ipg110719.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110726.zip">
ipg110726.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110802.zip">
ipg110802.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110809.zip">
ipg110809.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110816.zip">
ipg110816.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110823.zip">
ipg110823.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110830.zip">
ipg110830.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110906.zip">
ipg110906.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110913.zip">
ipg110913.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110920.zip">
ipg110920.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg110927.zip">
ipg110927.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg111004.zip">
ipg111004.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg111011.zip">
ipg111011.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg111018.zip">
ipg111018.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg111025.zip">
ipg111025.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg111101.zip">
ipg111101.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg111108.zip">
ipg111108.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg111115.zip">
ipg111115.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg111122.zip">
ipg111122.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg111129.zip">
ipg111129.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg111206.zip">
ipg111206.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg111213.zip">
ipg111213.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg111220.zip">
ipg111220.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2011/ipg111227.zip">
ipg111227.zip</a>&nbsp;


<h3 id="2010">2010</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100105.zip">
ipg100105.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100112.zip">
ipg100112.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100119.zip">
ipg100119.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100126.zip">
ipg100126.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100202.zip">
ipg100202.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100209.zip">
ipg100209.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100216.zip">
ipg100216.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100223.zip">
ipg100223.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100302.zip">
ipg100302.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100309.zip">
ipg100309.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100316.zip">
ipg100316.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100323.zip">
ipg100323.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100330.zip">
ipg100330.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100406.zip">
ipg100406.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100413.zip">
ipg100413.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100420.zip">
ipg100420.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100427.zip">
ipg100427.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100504.zip">
ipg100504.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100511.zip">
ipg100511.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100518.zip">
ipg100518.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100525.zip">
ipg100525.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100601.zip">
ipg100601.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100608.zip">
ipg100608.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100615.zip">
ipg100615.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100622.zip">
ipg100622.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100629.zip">
ipg100629.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100706.zip">
ipg100706.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100713.zip">
ipg100713.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100720.zip">
ipg100720.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100727.zip">
ipg100727.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100803.zip">
ipg100803.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100810.zip">
ipg100810.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100817.zip">
ipg100817.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100824.zip">
ipg100824.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100831.zip">
ipg100831.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100907.zip">
ipg100907.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100914.zip">
ipg100914.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100921.zip">
ipg100921.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg100928.zip">
ipg100928.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg101005.zip">
ipg101005.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg101012.zip">
ipg101012.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg101019.zip">
ipg101019.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg101026.zip">
ipg101026.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg101102.zip">
ipg101102.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg101109.zip">
ipg101109.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg101116.zip">
ipg101116.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg101123.zip">
ipg101123.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg101130.zip">
ipg101130.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg101207.zip">
ipg101207.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg101214.zip">
ipg101214.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg101221.zip">
ipg101221.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2010/ipg101228.zip">
ipg101228.zip</a>&nbsp;


<h3 id="2009">2009</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090106.zip">
ipg090106.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090113.zip">
ipg090113.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090120.zip">
ipg090120.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090127.zip">
ipg090127.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090203.zip">
ipg090203.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090210.zip">
ipg090210.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090217.zip">
ipg090217.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090224.zip">
ipg090224.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090303.zip">
ipg090303.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090310.zip">
ipg090310.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090317.zip">
ipg090317.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090324.zip">
ipg090324.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090331.zip">
ipg090331.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090407.zip">
ipg090407.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090414.zip">
ipg090414.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090421.zip">
ipg090421.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090428.zip">
ipg090428.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090505.zip">
ipg090505.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090512.zip">
ipg090512.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090519.zip">
ipg090519.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090526.zip">
ipg090526.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090602.zip">
ipg090602.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090609.zip">
ipg090609.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090616.zip">
ipg090616.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090623.zip">
ipg090623.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090630.zip">
ipg090630.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090707.zip">
ipg090707.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090714.zip">
ipg090714.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090721.zip">
ipg090721.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090728.zip">
ipg090728.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090804.zip">
ipg090804.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090811.zip">
ipg090811.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090818.zip">
ipg090818.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090825.zip">
ipg090825.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090901.zip">
ipg090901.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090908.zip">
ipg090908.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090915.zip">
ipg090915.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090922.zip">
ipg090922.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg090929.zip">
ipg090929.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg091006.zip">
ipg091006.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg091013.zip">
ipg091013.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg091020.zip">
ipg091020.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg091027.zip">
ipg091027.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg091103.zip">
ipg091103.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg091110.zip">
ipg091110.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg091117.zip">
ipg091117.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg091124.zip">
ipg091124.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg091201.zip">
ipg091201.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg091208.zip">
ipg091208.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg091215.zip">
ipg091215.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg091222.zip">
ipg091222.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2009/ipg091229.zip">
ipg091229.zip</a>&nbsp;


<h3 id="2008">2008</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080101.zip">
ipg080101.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080108.zip">
ipg080108.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080115.zip">
ipg080115.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080122.zip">
ipg080122.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080129.zip">
ipg080129.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080205.zip">
ipg080205.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080212.zip">
ipg080212.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080219.zip">
ipg080219.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080226.zip">
ipg080226.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080304.zip">
ipg080304.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080311.zip">
ipg080311.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080318.zip">
ipg080318.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080325.zip">
ipg080325.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080401.zip">
ipg080401.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080408.zip">
ipg080408.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080415.zip">
ipg080415.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080422.zip">
ipg080422.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080429.zip">
ipg080429.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080506.zip">
ipg080506.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080513.zip">
ipg080513.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080520.zip">
ipg080520.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080527.zip">
ipg080527.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080603.zip">
ipg080603.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080610.zip">
ipg080610.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080617.zip">
ipg080617.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080624.zip">
ipg080624.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080701.zip">
ipg080701.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080708.zip">
ipg080708.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080715.zip">
ipg080715.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080722.zip">
ipg080722.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080729.zip">
ipg080729.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080805.zip">
ipg080805.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080812.zip">
ipg080812.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080819.zip">
ipg080819.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080826.zip">
ipg080826.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080902.zip">
ipg080902.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080909.zip">
ipg080909.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080916.zip">
ipg080916.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080923.zip">
ipg080923.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg080930.zip">
ipg080930.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg081007.zip">
ipg081007.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg081014.zip">
ipg081014.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg081021.zip">
ipg081021.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg081028.zip">
ipg081028.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg081104.zip">
ipg081104.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg081111.zip">
ipg081111.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg081118.zip">
ipg081118.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg081125.zip">
ipg081125.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg081202.zip">
ipg081202.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg081209.zip">
ipg081209.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg081216.zip">
ipg081216.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg081223.zip">
ipg081223.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2008/ipg081230.zip">
ipg081230.zip</a>&nbsp;


<h3 id="2007">2007</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070102.zip">
ipg070102.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070109.zip">
ipg070109.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070116.zip">
ipg070116.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070123.zip">
ipg070123.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070130.zip">
ipg070130.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070206.zip">
ipg070206.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070213.zip">
ipg070213.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070220.zip">
ipg070220.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070227.zip">
ipg070227.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070306.zip">
ipg070306.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070313.zip">
ipg070313.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070320.zip">
ipg070320.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070327.zip">
ipg070327.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070403.zip">
ipg070403.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070410.zip">
ipg070410.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070417.zip">
ipg070417.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070424.zip">
ipg070424.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070501.zip">
ipg070501.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070508.zip">
ipg070508.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070515.zip">
ipg070515.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070522.zip">
ipg070522.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070529.zip">
ipg070529.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070605.zip">
ipg070605.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070612.zip">
ipg070612.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070619.zip">
ipg070619.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070626.zip">
ipg070626.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070703.zip">
ipg070703.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070710.zip">
ipg070710.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070717.zip">
ipg070717.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070724.zip">
ipg070724.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070731.zip">
ipg070731.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070807.zip">
ipg070807.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070814.zip">
ipg070814.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070821.zip">
ipg070821.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070828.zip">
ipg070828.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070904.zip">
ipg070904.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070911.zip">
ipg070911.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070918.zip">
ipg070918.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg070925.zip">
ipg070925.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg071002.zip">
ipg071002.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg071009.zip">
ipg071009.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg071016.zip">
ipg071016.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg071023.zip">
ipg071023.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg071030.zip">
ipg071030.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg071106.zip">
ipg071106.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg071113.zip">
ipg071113.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg071120.zip">
ipg071120.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg071127.zip">
ipg071127.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg071204.zip">
ipg071204.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg071211.zip">
ipg071211.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg071218.zip">
ipg071218.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2007/ipg071225.zip">
ipg071225.zip</a>&nbsp;


<h3 id="2006">2006</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060103.zip">
ipg060103.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060110.zip">
ipg060110.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060117.zip">
ipg060117.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060124.zip">
ipg060124.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060131.zip">
ipg060131.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060207.zip">
ipg060207.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060214.zip">
ipg060214.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060221.zip">
ipg060221.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060228.zip">
ipg060228.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060307.zip">
ipg060307.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060314.zip">
ipg060314.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060321.zip">
ipg060321.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060328.zip">
ipg060328.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060404.zip">
ipg060404.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060411.zip">
ipg060411.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060418.zip">
ipg060418.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060425.zip">
ipg060425.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060502.zip">
ipg060502.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060509.zip">
ipg060509.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060516.zip">
ipg060516.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060523.zip">
ipg060523.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060530.zip">
ipg060530.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060606.zip">
ipg060606.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060613.zip">
ipg060613.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060620.zip">
ipg060620.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060627.zip">
ipg060627.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060704.zip">
ipg060704.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060711.zip">
ipg060711.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060718.zip">
ipg060718.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060725.zip">
ipg060725.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060801.zip">
ipg060801.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060808.zip">
ipg060808.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060815.zip">
ipg060815.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060822.zip">
ipg060822.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060829.zip">
ipg060829.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060905.zip">
ipg060905.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060912.zip">
ipg060912.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060919.zip">
ipg060919.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg060926.zip">
ipg060926.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg061003.zip">
ipg061003.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg061010.zip">
ipg061010.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg061017.zip">
ipg061017.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg061024.zip">
ipg061024.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg061031.zip">
ipg061031.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg061107.zip">
ipg061107.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg061114.zip">
ipg061114.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg061121.zip">
ipg061121.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg061128.zip">
ipg061128.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg061205.zip">
ipg061205.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg061212.zip">
ipg061212.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg061219.zip">
ipg061219.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2006/ipg061226.zip">
ipg061226.zip</a>&nbsp;


<h3 id="2005">2005</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050104.zip">
ipg050104.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050111.zip">
ipg050111.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050118.zip">
ipg050118.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050125.zip">
ipg050125.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050201.zip">
ipg050201.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050208.zip">
ipg050208.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050215.zip">
ipg050215.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050222.zip">
ipg050222.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050301.zip">
ipg050301.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050308.zip">
ipg050308.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050315.zip">
ipg050315.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050322.zip">
ipg050322.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050329.zip">
ipg050329.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050405.zip">
ipg050405.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050412.zip">
ipg050412.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050419.zip">
ipg050419.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050426.zip">
ipg050426.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050503.zip">
ipg050503.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050510.zip">
ipg050510.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050517.zip">
ipg050517.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050524.zip">
ipg050524.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050531.zip">
ipg050531.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050607.zip">
ipg050607.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050614.zip">
ipg050614.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050621.zip">
ipg050621.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050628.zip">
ipg050628.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050705.zip">
ipg050705.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050712.zip">
ipg050712.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050719.zip">
ipg050719.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050726.zip">
ipg050726.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050802.zip">
ipg050802.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050809.zip">
ipg050809.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050816.zip">
ipg050816.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050823.zip">
ipg050823.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050830.zip">
ipg050830.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050906.zip">
ipg050906.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050913.zip">
ipg050913.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050920.zip">
ipg050920.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg050927.zip">
ipg050927.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg051004.zip">
ipg051004.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg051011.zip">
ipg051011.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg051018.zip">
ipg051018.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg051025.zip">
ipg051025.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg051101.zip">
ipg051101.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg051108.zip">
ipg051108.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg051115.zip">
ipg051115.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg051122.zip">
ipg051122.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg051129.zip">
ipg051129.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg051206.zip">
ipg051206.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg051213.zip">
ipg051213.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg051220.zip">
ipg051220.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2005/ipg051227.zip">
ipg051227.zip</a>&nbsp;


<h3 id="2004">2004</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040106.zip">
pg040106.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040113.zip">
pg040113.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040120.zip">
pg040120.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040127.zip">
pg040127.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040203.zip">
pg040203.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040210.zip">
pg040210.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040217.zip">
pg040217.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040224.zip">
pg040224.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040302.zip">
pg040302.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040309.zip">
pg040309.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040316.zip">
pg040316.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040323.zip">
pg040323.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040330.zip">
pg040330.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040406.zip">
pg040406.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040413.zip">
pg040413.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040420.zip">
pg040420.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040427.zip">
pg040427.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040504.zip">
pg040504.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040511.zip">
pg040511.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040518.zip">
pg040518.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040525.zip">
pg040525.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040601.zip">
pg040601.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040608.zip">
pg040608.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040615.zip">
pg040615.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040622.zip">
pg040622.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040629.zip">
pg040629.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040706.zip">
pg040706.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040713.zip">
pg040713.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040720.zip">
pg040720.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040727.zip">
pg040727.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040803.zip">
pg040803.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040810.zip">
pg040810.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040817.zip">
pg040817.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040824.zip">
pg040824.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040831.zip">
pg040831.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040907.zip">
pg040907.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040914.zip">
pg040914.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040921.zip">
pg040921.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg040928.zip">
pg040928.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg041005.zip">
pg041005.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg041012.zip">
pg041012.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg041019.zip">
pg041019.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg041026.zip">
pg041026.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg041102.zip">
pg041102.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg041109.zip">
pg041109.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg041116.zip">
pg041116.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg041123.zip">
pg041123.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg041130.zip">
pg041130.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg041207.zip">
pg041207.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg041214.zip">
pg041214.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg041221.zip">
pg041221.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2004/pg041228.zip">
pg041228.zip</a>&nbsp;


<h3 id="2003">2003</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030107.zip">
pg030107.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030114.zip">
pg030114.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030121.zip">
pg030121.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030128.zip">
pg030128.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030204.zip">
pg030204.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030211.zip">
pg030211.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030218.zip">
pg030218.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030225.zip">
pg030225.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030304.zip">
pg030304.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030311.zip">
pg030311.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030318.zip">
pg030318.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030325.zip">
pg030325.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030401.zip">
pg030401.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030408.zip">
pg030408.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030415.zip">
pg030415.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030422.zip">
pg030422.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030429.zip">
pg030429.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030506.zip">
pg030506.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030513.zip">
pg030513.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030520.zip">
pg030520.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030527.zip">
pg030527.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030603.zip">
pg030603.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030610.zip">
pg030610.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030617.zip">
pg030617.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030624.zip">
pg030624.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030701.zip">
pg030701.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030708.zip">
pg030708.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030715.zip">
pg030715.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030722.zip">
pg030722.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030729.zip">
pg030729.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030805.zip">
pg030805.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030812.zip">
pg030812.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030819.zip">
pg030819.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030826.zip">
pg030826.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030902.zip">
pg030902.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030909.zip">
pg030909.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030916.zip">
pg030916.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030923.zip">
pg030923.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg030930.zip">
pg030930.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg031007.zip">
pg031007.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg031014.zip">
pg031014.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg031021.zip">
pg031021.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg031028.zip">
pg031028.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg031104.zip">
pg031104.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg031111.zip">
pg031111.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg031118.zip">
pg031118.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg031125.zip">
pg031125.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg031202.zip">
pg031202.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg031209.zip">
pg031209.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg031216.zip">
pg031216.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg031223.zip">
pg031223.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2003/pg031230.zip">
pg031230.zip</a>&nbsp;


<h3 id="2002">2002</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020101.zip">
pg020101.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020108.zip">
pg020108.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020115.zip">
pg020115.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020122.zip">
pg020122.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020129.zip">
pg020129.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020205.zip">
pg020205.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020212.zip">
pg020212.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020219.zip">
pg020219.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020226.zip">
pg020226.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020305.zip">
pg020305.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020312.zip">
pg020312.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020319.zip">
pg020319.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020326.zip">
pg020326.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020402.zip">
pg020402.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020409.zip">
pg020409.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020416.zip">
pg020416.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020423.zip">
pg020423.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020430.zip">
pg020430.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020507.zip">
pg020507.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020514.zip">
pg020514.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020521.zip">
pg020521.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020528.zip">
pg020528.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020604.zip">
pg020604.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020611.zip">
pg020611.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020618.zip">
pg020618.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020625.zip">
pg020625.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020702.zip">
pg020702.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020709.zip">
pg020709.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020716.zip">
pg020716.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020723.zip">
pg020723.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020730.zip">
pg020730.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020806.zip">
pg020806.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020813.zip">
pg020813.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020820.zip">
pg020820.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020827.zip">
pg020827.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020903.zip">
pg020903.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020910.zip">
pg020910.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020917.zip">
pg020917.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg020924.zip">
pg020924.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg021001.zip">
pg021001.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg021008.zip">
pg021008.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg021015.zip">
pg021015.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg021022.zip">
pg021022.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg021029.zip">
pg021029.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg021105.zip">
pg021105.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg021112.zip">
pg021112.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg021119.zip">
pg021119.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg021126.zip">
pg021126.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg021203.zip">
pg021203.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg021210.zip">
pg021210.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg021217.zip">
pg021217.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg021224.zip">
pg021224.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2002/pg021231.zip">
pg021231.zip</a>&nbsp;


<h3 id="2001">2001</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010102_wk01.zip">
pftaps20010102_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010109_wk02.zip">
pftaps20010109_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010116_wk03.zip">
pftaps20010116_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010123_wk04.zip">
pftaps20010123_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010130_wk05.zip">
pftaps20010130_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010206_wk06.zip">
pftaps20010206_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010213_wk07.zip">
pftaps20010213_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010220_wk08.zip">
pftaps20010220_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010227_wk09.zip">
pftaps20010227_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010306_wk10.zip">
pftaps20010306_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010313_wk11.zip">
pftaps20010313_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010320_wk12.zip">
pftaps20010320_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010327_wk13.zip">
pftaps20010327_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010403_wk14.zip">
pftaps20010403_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010410_wk15.zip">
pftaps20010410_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010417_wk16.zip">
pftaps20010417_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010424_wk17.zip">
pftaps20010424_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010501_wk18.zip">
pftaps20010501_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010508_wk19.zip">
pftaps20010508_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010515_wk20.zip">
pftaps20010515_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010522_wk21.zip">
pftaps20010522_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010529_wk22.zip">
pftaps20010529_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010605_wk23.zip">
pftaps20010605_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010612_wk24.zip">
pftaps20010612_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010619_wk25.zip">
pftaps20010619_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010626_wk26.zip">
pftaps20010626_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010703_wk27.zip">
pftaps20010703_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010710_wk28.zip">
pftaps20010710_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010717_wk29.zip">
pftaps20010717_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010724_wk30.zip">
pftaps20010724_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010731_wk31.zip">
pftaps20010731_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010807_wk32.zip">
pftaps20010807_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010814_wk33.zip">
pftaps20010814_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010821_wk34.zip">
pftaps20010821_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010828_wk35.zip">
pftaps20010828_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010904_wk36.zip">
pftaps20010904_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010911_wk37.zip">
pftaps20010911_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010918_wk38.zip">
pftaps20010918_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20010925_wk39.zip">
pftaps20010925_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20011002_wk40.zip">
pftaps20011002_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20011009_wk41.zip">
pftaps20011009_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20011016_wk42.zip">
pftaps20011016_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20011023_wk43.zip">
pftaps20011023_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20011030_wk44.zip">
pftaps20011030_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20011106_wk45.zip">
pftaps20011106_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20011113_wk46.zip">
pftaps20011113_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20011120_wk47.zip">
pftaps20011120_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20011127_wk48.zip">
pftaps20011127_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20011204_wk49.zip">
pftaps20011204_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20011211_wk50.zip">
pftaps20011211_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20011218_wk51.zip">
pftaps20011218_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pftaps20011225_wk52.zip">
pftaps20011225_wk52.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010102.zip">
pg010102.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010109.zip">
pg010109.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010116.zip">
pg010116.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010123.zip">
pg010123.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010130.zip">
pg010130.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010206.zip">
pg010206.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010213.zip">
pg010213.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010220.zip">
pg010220.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010227.zip">
pg010227.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010306.zip">
pg010306.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010313.zip">
pg010313.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010320.zip">
pg010320.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010327.zip">
pg010327.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010403.zip">
pg010403.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010410.zip">
pg010410.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010417.zip">
pg010417.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010424.zip">
pg010424.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010501.zip">
pg010501.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010508.zip">
pg010508.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010515.zip">
pg010515.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010522.zip">
pg010522.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010529.zip">
pg010529.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010605.zip">
pg010605.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010612.zip">
pg010612.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010619.zip">
pg010619.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010626.zip">
pg010626.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010703.zip">
pg010703.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010710.zip">
pg010710.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010717.zip">
pg010717.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010724.zip">
pg010724.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010731.zip">
pg010731.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010807.zip">
pg010807.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010814.zip">
pg010814.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010821.zip">
pg010821.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010828.zip">
pg010828.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010904.zip">
pg010904.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010911.zip">
pg010911.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010918.zip">
pg010918.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg010925.zip">
pg010925.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg011002.zip">
pg011002.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg011009.zip">
pg011009.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg011016.zip">
pg011016.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg011023.zip">
pg011023.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg011030.zip">
pg011030.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg011106.zip">
pg011106.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg011113.zip">
pg011113.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg011120.zip">
pg011120.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg011127.zip">
pg011127.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg011204.zip">
pg011204.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg011211.zip">
pg011211.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg011218.zip">
pg011218.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2001/pg011225.zip">
pg011225.zip</a>&nbsp;


<h3 id="2000">2000</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000104_wk01.zip">
pftaps20000104_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000111_wk02.zip">
pftaps20000111_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000118_wk03.zip">
pftaps20000118_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000125_wk04.zip">
pftaps20000125_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000201_wk05.zip">
pftaps20000201_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000208_wk06.zip">
pftaps20000208_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000215_wk07.zip">
pftaps20000215_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000222_wk08.zip">
pftaps20000222_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000229_wk09.zip">
pftaps20000229_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000307_wk10.zip">
pftaps20000307_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000314_wk11.zip">
pftaps20000314_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000321_wk12.zip">
pftaps20000321_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000328_wk13.zip">
pftaps20000328_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000404_wk14.zip">
pftaps20000404_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000411_wk15.zip">
pftaps20000411_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000418_wk16.zip">
pftaps20000418_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000425_wk17.zip">
pftaps20000425_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000502_wk18.zip">
pftaps20000502_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000509_wk19.zip">
pftaps20000509_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000516_wk20.zip">
pftaps20000516_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000523_wk21.zip">
pftaps20000523_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000530_wk22.zip">
pftaps20000530_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000606_wk23.zip">
pftaps20000606_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000613_wk24.zip">
pftaps20000613_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000620_wk25.zip">
pftaps20000620_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000627_wk26.zip">
pftaps20000627_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000704_wk27.zip">
pftaps20000704_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000711_wk28.zip">
pftaps20000711_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000718_wk29.zip">
pftaps20000718_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000725_wk30.zip">
pftaps20000725_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000801_wk31.zip">
pftaps20000801_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000808_wk32.zip">
pftaps20000808_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000815_wk33.zip">
pftaps20000815_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000822_wk34.zip">
pftaps20000822_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000829_wk35.zip">
pftaps20000829_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000905_wk36.zip">
pftaps20000905_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000912_wk37.zip">
pftaps20000912_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000919_wk38.zip">
pftaps20000919_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20000926_wk39.zip">
pftaps20000926_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20001003_wk40.zip">
pftaps20001003_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20001010_wk41.zip">
pftaps20001010_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20001017_wk42.zip">
pftaps20001017_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20001024_wk43.zip">
pftaps20001024_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20001031_wk44.zip">
pftaps20001031_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20001107_wk45.zip">
pftaps20001107_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20001114_wk46.zip">
pftaps20001114_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20001121_wk47.zip">
pftaps20001121_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20001128_wk48.zip">
pftaps20001128_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20001205_wk49.zip">
pftaps20001205_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20001212_wk50.zip">
pftaps20001212_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20001219_wk51.zip">
pftaps20001219_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/2000/pftaps20001226_wk52.zip">
pftaps20001226_wk52.zip</a>&nbsp;


<h3 id="1999">1999</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990105_wk01.zip">
pftaps19990105_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990112_wk02.zip">
pftaps19990112_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990119_wk03.zip">
pftaps19990119_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990126_wk04.zip">
pftaps19990126_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990202_wk05.zip">
pftaps19990202_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990209_wk06.zip">
pftaps19990209_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990216_wk07.zip">
pftaps19990216_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990223_wk08.zip">
pftaps19990223_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990302_wk09.zip">
pftaps19990302_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990309_wk10.zip">
pftaps19990309_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990316_wk11.zip">
pftaps19990316_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990323_wk12.zip">
pftaps19990323_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990330_wk13.zip">
pftaps19990330_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990406_wk14.zip">
pftaps19990406_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990413_wk15.zip">
pftaps19990413_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990420_wk16.zip">
pftaps19990420_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990427_wk17.zip">
pftaps19990427_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990504_wk18.zip">
pftaps19990504_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990511_wk19.zip">
pftaps19990511_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990518_wk20.zip">
pftaps19990518_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990525_wk21.zip">
pftaps19990525_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990601_wk22.zip">
pftaps19990601_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990608_wk23.zip">
pftaps19990608_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990615_wk24.zip">
pftaps19990615_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990622_wk25.zip">
pftaps19990622_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990629_wk26.zip">
pftaps19990629_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990706_wk27.zip">
pftaps19990706_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990713_wk28.zip">
pftaps19990713_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990720_wk29.zip">
pftaps19990720_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990727_wk30.zip">
pftaps19990727_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990803_wk31.zip">
pftaps19990803_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990810_wk32.zip">
pftaps19990810_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990817_wk33.zip">
pftaps19990817_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990824_wk34.zip">
pftaps19990824_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990831_wk35.zip">
pftaps19990831_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990907_wk36.zip">
pftaps19990907_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990914_wk37.zip">
pftaps19990914_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990921_wk38.zip">
pftaps19990921_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19990928_wk39.zip">
pftaps19990928_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19991005_wk40.zip">
pftaps19991005_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19991012_wk41.zip">
pftaps19991012_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19991019_wk42.zip">
pftaps19991019_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19991026_wk43.zip">
pftaps19991026_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19991102_wk44.zip">
pftaps19991102_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19991109_wk45.zip">
pftaps19991109_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19991116_wk46.zip">
pftaps19991116_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19991123_wk47.zip">
pftaps19991123_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19991130_wk48.zip">
pftaps19991130_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19991207_wk49.zip">
pftaps19991207_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19991214_wk50.zip">
pftaps19991214_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19991221_wk51.zip">
pftaps19991221_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1999/pftaps19991228_wk52.zip">
pftaps19991228_wk52.zip</a>&nbsp;


<h3 id="1998">1998</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980106_wk01.zip">
pftaps19980106_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980113_wk02.zip">
pftaps19980113_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980120_wk03.zip">
pftaps19980120_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980127_wk04.zip">
pftaps19980127_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980203_wk05.zip">
pftaps19980203_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980210_wk06.zip">
pftaps19980210_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980217_wk07.zip">
pftaps19980217_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980224_wk08.zip">
pftaps19980224_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980303_wk09.zip">
pftaps19980303_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980310_wk10.zip">
pftaps19980310_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980317_wk11.zip">
pftaps19980317_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980324_wk12.zip">
pftaps19980324_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980331_wk13.zip">
pftaps19980331_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980407_wk14.zip">
pftaps19980407_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980414_wk15.zip">
pftaps19980414_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980421_wk16.zip">
pftaps19980421_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980428_wk17.zip">
pftaps19980428_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980505_wk18.zip">
pftaps19980505_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980512_wk19.zip">
pftaps19980512_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980519_wk20.zip">
pftaps19980519_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980526_wk21.zip">
pftaps19980526_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980602_wk22.zip">
pftaps19980602_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980609_wk23.zip">
pftaps19980609_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980616_wk24.zip">
pftaps19980616_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980623_wk25.zip">
pftaps19980623_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980630_wk26.zip">
pftaps19980630_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980707_wk27.zip">
pftaps19980707_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980714_wk28.zip">
pftaps19980714_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980721_wk29.zip">
pftaps19980721_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980728_wk30.zip">
pftaps19980728_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980804_wk31.zip">
pftaps19980804_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980811_wk32.zip">
pftaps19980811_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980818_wk33.zip">
pftaps19980818_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980825_wk34.zip">
pftaps19980825_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980901_wk35.zip">
pftaps19980901_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980908_wk36.zip">
pftaps19980908_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980915_wk37.zip">
pftaps19980915_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980922_wk38.zip">
pftaps19980922_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19980929_wk39.zip">
pftaps19980929_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19981006_wk40.zip">
pftaps19981006_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19981013_wk41.zip">
pftaps19981013_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19981020_wk42.zip">
pftaps19981020_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19981027_wk43.zip">
pftaps19981027_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19981103_wk44.zip">
pftaps19981103_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19981110_wk45.zip">
pftaps19981110_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19981117_wk46.zip">
pftaps19981117_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19981124_wk47.zip">
pftaps19981124_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19981201_wk48.zip">
pftaps19981201_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19981208_wk49.zip">
pftaps19981208_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19981215_wk50.zip">
pftaps19981215_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19981222_wk51.zip">
pftaps19981222_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1998/pftaps19981229_wk52.zip">
pftaps19981229_wk52.zip</a>&nbsp;


<h3 id="1997">1997</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970107_wk01.zip">
pftaps19970107_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970114_wk02.zip">
pftaps19970114_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970121_wk03.zip">
pftaps19970121_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970128_wk04.zip">
pftaps19970128_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970204_wk05.zip">
pftaps19970204_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970211_wk06.zip">
pftaps19970211_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970218_wk07.zip">
pftaps19970218_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970225_wk08.zip">
pftaps19970225_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970304_wk09.zip">
pftaps19970304_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970311_wk10.zip">
pftaps19970311_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970318_wk11.zip">
pftaps19970318_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970325_wk12.zip">
pftaps19970325_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970401_wk13.zip">
pftaps19970401_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970408_wk14.zip">
pftaps19970408_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970415_wk15.zip">
pftaps19970415_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970422_wk16.zip">
pftaps19970422_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970429_wk17.zip">
pftaps19970429_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970506_wk18.zip">
pftaps19970506_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970513_wk19.zip">
pftaps19970513_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970520_wk20.zip">
pftaps19970520_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970527_wk21.zip">
pftaps19970527_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970603_wk22.zip">
pftaps19970603_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970610_wk23.zip">
pftaps19970610_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970617_wk24.zip">
pftaps19970617_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970624_wk25.zip">
pftaps19970624_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970701_wk26.zip">
pftaps19970701_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970708_wk27.zip">
pftaps19970708_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970715_wk28.zip">
pftaps19970715_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970722_wk29.zip">
pftaps19970722_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970729_wk30.zip">
pftaps19970729_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970805_wk31.zip">
pftaps19970805_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970812_wk32.zip">
pftaps19970812_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970819_wk33.zip">
pftaps19970819_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970826_wk34.zip">
pftaps19970826_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970902_wk35.zip">
pftaps19970902_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970909_wk36.zip">
pftaps19970909_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970916_wk37.zip">
pftaps19970916_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970923_wk38.zip">
pftaps19970923_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19970930_wk39.zip">
pftaps19970930_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19971007_wk40.zip">
pftaps19971007_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19971014_wk41.zip">
pftaps19971014_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19971021_wk42.zip">
pftaps19971021_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19971028_wk43.zip">
pftaps19971028_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19971104_wk44.zip">
pftaps19971104_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19971111_wk45.zip">
pftaps19971111_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19971118_wk46.zip">
pftaps19971118_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19971125_wk47.zip">
pftaps19971125_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19971202_wk48.zip">
pftaps19971202_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19971209_wk49.zip">
pftaps19971209_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19971216_wk50.zip">
pftaps19971216_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19971223_wk51.zip">
pftaps19971223_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1997/pftaps19971230_wk52.zip">
pftaps19971230_wk52.zip</a>&nbsp;


<h3 id="1996">1996</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960102_wk01.zip">
pftaps19960102_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960109_wk02.zip">
pftaps19960109_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960116_wk03.zip">
pftaps19960116_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960123_wk04.zip">
pftaps19960123_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960130_wk05.zip">
pftaps19960130_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960206_wk06.zip">
pftaps19960206_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960213_wk07.zip">
pftaps19960213_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960220_wk08.zip">
pftaps19960220_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960227_wk09.zip">
pftaps19960227_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960305_wk10.zip">
pftaps19960305_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960312_wk11.zip">
pftaps19960312_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960319_wk12.zip">
pftaps19960319_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960326_wk13.zip">
pftaps19960326_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960402_wk14.zip">
pftaps19960402_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960409_wk15.zip">
pftaps19960409_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960416_wk16.zip">
pftaps19960416_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960423_wk17.zip">
pftaps19960423_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960430_wk18.zip">
pftaps19960430_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960507_wk19.zip">
pftaps19960507_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960514_wk20.zip">
pftaps19960514_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960521_wk21.zip">
pftaps19960521_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960528_wk22.zip">
pftaps19960528_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960604_wk23.zip">
pftaps19960604_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960611_wk24.zip">
pftaps19960611_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960618_wk25.zip">
pftaps19960618_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960625_wk26.zip">
pftaps19960625_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960702_wk27.zip">
pftaps19960702_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960709_wk28.zip">
pftaps19960709_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960716_wk29.zip">
pftaps19960716_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960723_wk30.zip">
pftaps19960723_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960730_wk31.zip">
pftaps19960730_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960806_wk32.zip">
pftaps19960806_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960813_wk33.zip">
pftaps19960813_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960820_wk34.zip">
pftaps19960820_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960827_wk35.zip">
pftaps19960827_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960903_wk36.zip">
pftaps19960903_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960910_wk37.zip">
pftaps19960910_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960917_wk38.zip">
pftaps19960917_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19960924_wk39.zip">
pftaps19960924_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19961001_wk40.zip">
pftaps19961001_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19961008_wk41.zip">
pftaps19961008_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19961015_wk42.zip">
pftaps19961015_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19961022_wk43.zip">
pftaps19961022_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19961029_wk44.zip">
pftaps19961029_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19961105_wk45.zip">
pftaps19961105_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19961112_wk46.zip">
pftaps19961112_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19961119_wk47.zip">
pftaps19961119_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19961126_wk48.zip">
pftaps19961126_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19961203_wk49.zip">
pftaps19961203_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19961210_wk50.zip">
pftaps19961210_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19961217_wk51.zip">
pftaps19961217_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19961224_wk52.zip">
pftaps19961224_wk52.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1996/pftaps19961231_wk53.zip">
pftaps19961231_wk53.zip</a>&nbsp;


<h3 id="1995">1995</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950103_wk01.zip">
pftaps19950103_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950110_wk02.zip">
pftaps19950110_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950117_wk03.zip">
pftaps19950117_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950124_wk04.zip">
pftaps19950124_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950131_wk05.zip">
pftaps19950131_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950207_wk06.zip">
pftaps19950207_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950214_wk07.zip">
pftaps19950214_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950221_wk08.zip">
pftaps19950221_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950228_wk09.zip">
pftaps19950228_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950307_wk10.zip">
pftaps19950307_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950314_wk11.zip">
pftaps19950314_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950321_wk12.zip">
pftaps19950321_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950328_wk13.zip">
pftaps19950328_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950404_wk14.zip">
pftaps19950404_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950411_wk15.zip">
pftaps19950411_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950418_wk16.zip">
pftaps19950418_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950425_wk17.zip">
pftaps19950425_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950502_wk18.zip">
pftaps19950502_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950509_wk19.zip">
pftaps19950509_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950516_wk20.zip">
pftaps19950516_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950523_wk21.zip">
pftaps19950523_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950530_wk22.zip">
pftaps19950530_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950606_wk23.zip">
pftaps19950606_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950613_wk24.zip">
pftaps19950613_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950620_wk25.zip">
pftaps19950620_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950627_wk26.zip">
pftaps19950627_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950704_wk27.zip">
pftaps19950704_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950711_wk28.zip">
pftaps19950711_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950718_wk29.zip">
pftaps19950718_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950725_wk30.zip">
pftaps19950725_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950801_wk31.zip">
pftaps19950801_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950808_wk32.zip">
pftaps19950808_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950815_wk33.zip">
pftaps19950815_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950822_wk34.zip">
pftaps19950822_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950829_wk35.zip">
pftaps19950829_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950905_wk36.zip">
pftaps19950905_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950912_wk37.zip">
pftaps19950912_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950919_wk38.zip">
pftaps19950919_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19950926_wk39.zip">
pftaps19950926_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19951003_wk40.zip">
pftaps19951003_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19951010_wk41.zip">
pftaps19951010_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19951017_wk42.zip">
pftaps19951017_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19951024_wk43.zip">
pftaps19951024_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19951031_wk44.zip">
pftaps19951031_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19951107_wk45.zip">
pftaps19951107_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19951114_wk46.zip">
pftaps19951114_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19951121_wk47.zip">
pftaps19951121_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19951128_wk48.zip">
pftaps19951128_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19951205_wk49.zip">
pftaps19951205_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19951212_wk50.zip">
pftaps19951212_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19951219_wk51.zip">
pftaps19951219_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1995/pftaps19951226_wk52.zip">
pftaps19951226_wk52.zip</a>&nbsp;


<h3 id="1994">1994</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940104_wk01.zip">
pftaps19940104_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940111_wk02.zip">
pftaps19940111_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940118_wk03.zip">
pftaps19940118_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940125_wk04.zip">
pftaps19940125_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940201_wk05.zip">
pftaps19940201_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940208_wk06.zip">
pftaps19940208_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940215_wk07.zip">
pftaps19940215_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940222_wk08.zip">
pftaps19940222_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940301_wk09.zip">
pftaps19940301_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940308_wk10.zip">
pftaps19940308_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940315_wk11.zip">
pftaps19940315_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940322_wk12.zip">
pftaps19940322_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940329_wk13.zip">
pftaps19940329_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940405_wk14.zip">
pftaps19940405_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940412_wk15.zip">
pftaps19940412_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940419_wk16.zip">
pftaps19940419_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940426_wk17.zip">
pftaps19940426_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940503_wk18.zip">
pftaps19940503_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940510_wk19.zip">
pftaps19940510_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940517_wk20.zip">
pftaps19940517_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940524_wk21.zip">
pftaps19940524_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940531_wk22.zip">
pftaps19940531_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940607_wk23.zip">
pftaps19940607_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940614_wk24.zip">
pftaps19940614_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940621_wk25.zip">
pftaps19940621_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940628_wk26.zip">
pftaps19940628_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940705_wk27.zip">
pftaps19940705_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940712_wk28.zip">
pftaps19940712_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940719_wk29.zip">
pftaps19940719_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940726_wk30.zip">
pftaps19940726_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940802_wk31.zip">
pftaps19940802_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940809_wk32.zip">
pftaps19940809_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940816_wk33.zip">
pftaps19940816_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940823_wk34.zip">
pftaps19940823_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940830_wk35.zip">
pftaps19940830_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940906_wk36.zip">
pftaps19940906_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940913_wk37.zip">
pftaps19940913_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940920_wk38.zip">
pftaps19940920_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19940927_wk39.zip">
pftaps19940927_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19941004_wk40.zip">
pftaps19941004_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19941011_wk41.zip">
pftaps19941011_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19941018_wk42.zip">
pftaps19941018_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19941025_wk43.zip">
pftaps19941025_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19941101_wk44.zip">
pftaps19941101_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19941108_wk45.zip">
pftaps19941108_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19941115_wk46.zip">
pftaps19941115_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19941122_wk47.zip">
pftaps19941122_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19941129_wk48.zip">
pftaps19941129_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19941206_wk49.zip">
pftaps19941206_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19941213_wk50.zip">
pftaps19941213_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19941220_wk51.zip">
pftaps19941220_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1994/pftaps19941227_wk52.zip">
pftaps19941227_wk52.zip</a>&nbsp;


<h3 id="1993">1993</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930105_wk01.zip">
pftaps19930105_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930112_wk02.zip">
pftaps19930112_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930119_wk03.zip">
pftaps19930119_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930126_wk04.zip">
pftaps19930126_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930202_wk05.zip">
pftaps19930202_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930209_wk06.zip">
pftaps19930209_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930216_wk07.zip">
pftaps19930216_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930223_wk08.zip">
pftaps19930223_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930302_wk09.zip">
pftaps19930302_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930309_wk10.zip">
pftaps19930309_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930316_wk11.zip">
pftaps19930316_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930323_wk12.zip">
pftaps19930323_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930330_wk13.zip">
pftaps19930330_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930406_wk14.zip">
pftaps19930406_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930413_wk15.zip">
pftaps19930413_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930420_wk16.zip">
pftaps19930420_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930427_wk17.zip">
pftaps19930427_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930504_wk18.zip">
pftaps19930504_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930511_wk19.zip">
pftaps19930511_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930518_wk20.zip">
pftaps19930518_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930525_wk21.zip">
pftaps19930525_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930601_wk22.zip">
pftaps19930601_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930608_wk23.zip">
pftaps19930608_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930615_wk24.zip">
pftaps19930615_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930622_wk25.zip">
pftaps19930622_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930629_wk26.zip">
pftaps19930629_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930706_wk27.zip">
pftaps19930706_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930713_wk28.zip">
pftaps19930713_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930720_wk29.zip">
pftaps19930720_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930727_wk30.zip">
pftaps19930727_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930803_wk31.zip">
pftaps19930803_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930810_wk32.zip">
pftaps19930810_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930817_wk33.zip">
pftaps19930817_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930824_wk34.zip">
pftaps19930824_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930831_wk35.zip">
pftaps19930831_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930907_wk36.zip">
pftaps19930907_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930914_wk37.zip">
pftaps19930914_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930921_wk38.zip">
pftaps19930921_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19930928_wk39.zip">
pftaps19930928_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19931005_wk40.zip">
pftaps19931005_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19931012_wk41.zip">
pftaps19931012_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19931019_wk42.zip">
pftaps19931019_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19931026_wk43.zip">
pftaps19931026_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19931102_wk44.zip">
pftaps19931102_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19931109_wk45.zip">
pftaps19931109_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19931116_wk46.zip">
pftaps19931116_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19931123_wk47.zip">
pftaps19931123_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19931130_wk48.zip">
pftaps19931130_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19931207_wk49.zip">
pftaps19931207_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19931214_wk50.zip">
pftaps19931214_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19931221_wk51.zip">
pftaps19931221_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1993/pftaps19931228_wk52.zip">
pftaps19931228_wk52.zip</a>&nbsp;


<h3 id="1992">1992</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920107_wk01.zip">
pftaps19920107_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920114_wk02.zip">
pftaps19920114_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920121_wk03.zip">
pftaps19920121_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920128_wk04.zip">
pftaps19920128_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920204_wk05.zip">
pftaps19920204_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920211_wk06.zip">
pftaps19920211_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920218_wk07.zip">
pftaps19920218_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920225_wk08.zip">
pftaps19920225_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920303_wk09.zip">
pftaps19920303_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920310_wk10.zip">
pftaps19920310_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920317_wk11.zip">
pftaps19920317_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920324_wk12.zip">
pftaps19920324_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920331_wk13.zip">
pftaps19920331_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920407_wk14.zip">
pftaps19920407_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920414_wk15.zip">
pftaps19920414_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920421_wk16.zip">
pftaps19920421_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920428_wk17.zip">
pftaps19920428_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920505_wk18.zip">
pftaps19920505_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920512_wk19.zip">
pftaps19920512_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920519_wk20.zip">
pftaps19920519_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920526_wk21.zip">
pftaps19920526_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920602_wk22.zip">
pftaps19920602_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920609_wk23.zip">
pftaps19920609_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920616_wk24.zip">
pftaps19920616_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920623_wk25.zip">
pftaps19920623_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920630_wk26.zip">
pftaps19920630_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920707_wk27.zip">
pftaps19920707_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920714_wk28.zip">
pftaps19920714_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920721_wk29.zip">
pftaps19920721_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920728_wk30.zip">
pftaps19920728_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920804_wk31.zip">
pftaps19920804_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920811_wk32.zip">
pftaps19920811_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920818_wk33.zip">
pftaps19920818_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920825_wk34.zip">
pftaps19920825_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920901_wk35.zip">
pftaps19920901_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920908_wk36.zip">
pftaps19920908_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920915_wk37.zip">
pftaps19920915_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920922_wk38.zip">
pftaps19920922_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19920929_wk39.zip">
pftaps19920929_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19921006_wk40.zip">
pftaps19921006_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19921013_wk41.zip">
pftaps19921013_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19921020_wk42.zip">
pftaps19921020_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19921027_wk43.zip">
pftaps19921027_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19921103_wk44.zip">
pftaps19921103_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19921110_wk45.zip">
pftaps19921110_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19921117_wk46.zip">
pftaps19921117_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19921124_wk47.zip">
pftaps19921124_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19921201_wk48.zip">
pftaps19921201_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19921208_wk49.zip">
pftaps19921208_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19921215_wk50.zip">
pftaps19921215_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19921222_wk51.zip">
pftaps19921222_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1992/pftaps19921229_wk52.zip">
pftaps19921229_wk52.zip</a>&nbsp;


<h3 id="1991">1991</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910101_wk01.zip">
pftaps19910101_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910108_wk02.zip">
pftaps19910108_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910115_wk03.zip">
pftaps19910115_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910122_wk04.zip">
pftaps19910122_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910129_wk05.zip">
pftaps19910129_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910205_wk06.zip">
pftaps19910205_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910212_wk07.zip">
pftaps19910212_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910219_wk08.zip">
pftaps19910219_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910226_wk09.zip">
pftaps19910226_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910305_wk10.zip">
pftaps19910305_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910312_wk11.zip">
pftaps19910312_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910319_wk12.zip">
pftaps19910319_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910326_wk13.zip">
pftaps19910326_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910402_wk14.zip">
pftaps19910402_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910409_wk15.zip">
pftaps19910409_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910416_wk16.zip">
pftaps19910416_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910423_wk17.zip">
pftaps19910423_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910430_wk18.zip">
pftaps19910430_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910507_wk19.zip">
pftaps19910507_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910514_wk20.zip">
pftaps19910514_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910521_wk21.zip">
pftaps19910521_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910528_wk22.zip">
pftaps19910528_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910604_wk23.zip">
pftaps19910604_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910611_wk24.zip">
pftaps19910611_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910618_wk25.zip">
pftaps19910618_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910625_wk26.zip">
pftaps19910625_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910702_wk27.zip">
pftaps19910702_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910709_wk28.zip">
pftaps19910709_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910716_wk29.zip">
pftaps19910716_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910723_wk30.zip">
pftaps19910723_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910730_wk31.zip">
pftaps19910730_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910806_wk32.zip">
pftaps19910806_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910813_wk33.zip">
pftaps19910813_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910820_wk34.zip">
pftaps19910820_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910827_wk35.zip">
pftaps19910827_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910903_wk36.zip">
pftaps19910903_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910910_wk37.zip">
pftaps19910910_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910917_wk38.zip">
pftaps19910917_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19910924_wk39.zip">
pftaps19910924_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19911001_wk40.zip">
pftaps19911001_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19911008_wk41.zip">
pftaps19911008_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19911015_wk42.zip">
pftaps19911015_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19911022_wk43.zip">
pftaps19911022_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19911029_wk44.zip">
pftaps19911029_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19911105_wk45.zip">
pftaps19911105_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19911112_wk46.zip">
pftaps19911112_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19911119_wk47.zip">
pftaps19911119_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19911126_wk48.zip">
pftaps19911126_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19911203_wk49.zip">
pftaps19911203_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19911210_wk50.zip">
pftaps19911210_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19911217_wk51.zip">
pftaps19911217_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19911224_wk52.zip">
pftaps19911224_wk52.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1991/pftaps19911231_wk53.zip">
pftaps19911231_wk53.zip</a>&nbsp;


<h3 id="1990">1990</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900102_wk01.zip">
pftaps19900102_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900109_wk02.zip">
pftaps19900109_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900116_wk03.zip">
pftaps19900116_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900123_wk04.zip">
pftaps19900123_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900130_wk05.zip">
pftaps19900130_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900206_wk06.zip">
pftaps19900206_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900213_wk07.zip">
pftaps19900213_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900220_wk08.zip">
pftaps19900220_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900227_wk09.zip">
pftaps19900227_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900306_wk10.zip">
pftaps19900306_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900313_wk11.zip">
pftaps19900313_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900320_wk12.zip">
pftaps19900320_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900327_wk13.zip">
pftaps19900327_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900403_wk14.zip">
pftaps19900403_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900410_wk15.zip">
pftaps19900410_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900417_wk16.zip">
pftaps19900417_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900424_wk17.zip">
pftaps19900424_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900501_wk18.zip">
pftaps19900501_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900508_wk19.zip">
pftaps19900508_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900515_wk20.zip">
pftaps19900515_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900522_wk21.zip">
pftaps19900522_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900529_wk22.zip">
pftaps19900529_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900605_wk23.zip">
pftaps19900605_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900612_wk24.zip">
pftaps19900612_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900619_wk25.zip">
pftaps19900619_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900626_wk26.zip">
pftaps19900626_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900703_wk27.zip">
pftaps19900703_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900710_wk28.zip">
pftaps19900710_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900717_wk29.zip">
pftaps19900717_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900724_wk30.zip">
pftaps19900724_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900731_wk31.zip">
pftaps19900731_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900807_wk32.zip">
pftaps19900807_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900814_wk33.zip">
pftaps19900814_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900821_wk34.zip">
pftaps19900821_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900828_wk35.zip">
pftaps19900828_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900904_wk36.zip">
pftaps19900904_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900911_wk37.zip">
pftaps19900911_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900918_wk38.zip">
pftaps19900918_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19900925_wk39.zip">
pftaps19900925_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19901002_wk40.zip">
pftaps19901002_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19901009_wk41.zip">
pftaps19901009_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19901016_wk42.zip">
pftaps19901016_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19901023_wk43.zip">
pftaps19901023_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19901030_wk44.zip">
pftaps19901030_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19901106_wk45.zip">
pftaps19901106_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19901113_wk46.zip">
pftaps19901113_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19901120_wk47.zip">
pftaps19901120_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19901127_wk48.zip">
pftaps19901127_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19901204_wk49.zip">
pftaps19901204_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19901211_wk50.zip">
pftaps19901211_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19901218_wk51.zip">
pftaps19901218_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1990/pftaps19901225_wk52.zip">
pftaps19901225_wk52.zip</a>&nbsp;


<h3 id="1989">1989</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890103_wk01.zip">
pftaps19890103_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890110_wk02.zip">
pftaps19890110_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890117_wk03.zip">
pftaps19890117_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890124_wk04.zip">
pftaps19890124_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890131_wk05.zip">
pftaps19890131_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890207_wk06.zip">
pftaps19890207_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890214_wk07.zip">
pftaps19890214_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890221_wk08.zip">
pftaps19890221_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890228_wk09.zip">
pftaps19890228_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890307_wk10.zip">
pftaps19890307_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890314_wk11.zip">
pftaps19890314_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890321_wk12.zip">
pftaps19890321_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890328_wk13.zip">
pftaps19890328_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890404_wk14.zip">
pftaps19890404_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890411_wk15.zip">
pftaps19890411_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890418_wk16.zip">
pftaps19890418_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890425_wk17.zip">
pftaps19890425_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890502_wk18.zip">
pftaps19890502_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890509_wk19.zip">
pftaps19890509_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890516_wk20.zip">
pftaps19890516_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890523_wk21.zip">
pftaps19890523_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890530_wk22.zip">
pftaps19890530_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890606_wk23.zip">
pftaps19890606_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890613_wk24.zip">
pftaps19890613_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890620_wk25.zip">
pftaps19890620_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890627_wk26.zip">
pftaps19890627_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890704_wk27.zip">
pftaps19890704_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890711_wk28.zip">
pftaps19890711_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890718_wk29.zip">
pftaps19890718_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890725_wk30.zip">
pftaps19890725_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890801_wk31.zip">
pftaps19890801_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890808_wk32.zip">
pftaps19890808_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890815_wk33.zip">
pftaps19890815_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890822_wk34.zip">
pftaps19890822_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890829_wk35.zip">
pftaps19890829_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890905_wk36.zip">
pftaps19890905_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890912_wk37.zip">
pftaps19890912_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890919_wk38.zip">
pftaps19890919_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19890926_wk39.zip">
pftaps19890926_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19891003_wk40.zip">
pftaps19891003_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19891010_wk41.zip">
pftaps19891010_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19891017_wk42.zip">
pftaps19891017_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19891024_wk43.zip">
pftaps19891024_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19891031_wk44.zip">
pftaps19891031_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19891107_wk45.zip">
pftaps19891107_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19891114_wk46.zip">
pftaps19891114_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19891121_wk47.zip">
pftaps19891121_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19891128_wk48.zip">
pftaps19891128_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19891205_wk49.zip">
pftaps19891205_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19891212_wk50.zip">
pftaps19891212_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19891219_wk51.zip">
pftaps19891219_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1989/pftaps19891226_wk52.zip">
pftaps19891226_wk52.zip</a>&nbsp;


<h3 id="1988">1988</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880105_wk01.zip">
pftaps19880105_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880112_wk02.zip">
pftaps19880112_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880119_wk03.zip">
pftaps19880119_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880126_wk04.zip">
pftaps19880126_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880202_wk05.zip">
pftaps19880202_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880209_wk06.zip">
pftaps19880209_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880216_wk07.zip">
pftaps19880216_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880223_wk08.zip">
pftaps19880223_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880301_wk09.zip">
pftaps19880301_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880308_wk10.zip">
pftaps19880308_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880315_wk11.zip">
pftaps19880315_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880322_wk12.zip">
pftaps19880322_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880329_wk13.zip">
pftaps19880329_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880405_wk14.zip">
pftaps19880405_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880412_wk15.zip">
pftaps19880412_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880419_wk16.zip">
pftaps19880419_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880426_wk17.zip">
pftaps19880426_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880503_wk18.zip">
pftaps19880503_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880510_wk19.zip">
pftaps19880510_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880517_wk20.zip">
pftaps19880517_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880524_wk21.zip">
pftaps19880524_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880531_wk22.zip">
pftaps19880531_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880607_wk23.zip">
pftaps19880607_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880614_wk24.zip">
pftaps19880614_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880621_wk25.zip">
pftaps19880621_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880628_wk26.zip">
pftaps19880628_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880705_wk27.zip">
pftaps19880705_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880712_wk28.zip">
pftaps19880712_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880719_wk29.zip">
pftaps19880719_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880726_wk30.zip">
pftaps19880726_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880802_wk31.zip">
pftaps19880802_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880809_wk32.zip">
pftaps19880809_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880816_wk33.zip">
pftaps19880816_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880823_wk34.zip">
pftaps19880823_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880830_wk35.zip">
pftaps19880830_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880906_wk36.zip">
pftaps19880906_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880913_wk37.zip">
pftaps19880913_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880920_wk38.zip">
pftaps19880920_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19880927_wk39.zip">
pftaps19880927_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19881004_wk40.zip">
pftaps19881004_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19881011_wk41.zip">
pftaps19881011_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19881018_wk42.zip">
pftaps19881018_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19881025_wk43.zip">
pftaps19881025_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19881101_wk44.zip">
pftaps19881101_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19881108_wk45.zip">
pftaps19881108_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19881115_wk46.zip">
pftaps19881115_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19881122_wk47.zip">
pftaps19881122_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19881129_wk48.zip">
pftaps19881129_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19881206_wk49.zip">
pftaps19881206_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19881213_wk50.zip">
pftaps19881213_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19881220_wk51.zip">
pftaps19881220_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1988/pftaps19881227_wk52.zip">
pftaps19881227_wk52.zip</a>&nbsp;


<h3 id="1987">1987</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870106_wk01.zip">
pftaps19870106_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870113_wk02.zip">
pftaps19870113_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870120_wk03.zip">
pftaps19870120_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870127_wk04.zip">
pftaps19870127_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870203_wk05.zip">
pftaps19870203_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870210_wk06.zip">
pftaps19870210_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870217_wk07.zip">
pftaps19870217_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870224_wk08.zip">
pftaps19870224_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870303_wk09.zip">
pftaps19870303_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870310_wk10.zip">
pftaps19870310_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870317_wk11.zip">
pftaps19870317_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870324_wk12.zip">
pftaps19870324_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870331_wk13.zip">
pftaps19870331_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870407_wk14.zip">
pftaps19870407_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870414_wk15.zip">
pftaps19870414_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870421_wk16.zip">
pftaps19870421_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870428_wk17.zip">
pftaps19870428_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870505_wk18.zip">
pftaps19870505_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870512_wk19.zip">
pftaps19870512_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870519_wk20.zip">
pftaps19870519_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870526_wk21.zip">
pftaps19870526_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870602_wk22.zip">
pftaps19870602_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870609_wk23.zip">
pftaps19870609_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870616_wk24.zip">
pftaps19870616_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870623_wk25.zip">
pftaps19870623_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870630_wk26.zip">
pftaps19870630_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870707_wk27.zip">
pftaps19870707_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870714_wk28.zip">
pftaps19870714_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870721_wk29.zip">
pftaps19870721_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870728_wk30.zip">
pftaps19870728_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870804_wk31.zip">
pftaps19870804_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870811_wk32.zip">
pftaps19870811_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870818_wk33.zip">
pftaps19870818_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870825_wk34.zip">
pftaps19870825_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870901_wk35.zip">
pftaps19870901_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870908_wk36.zip">
pftaps19870908_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870915_wk37.zip">
pftaps19870915_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870922_wk38.zip">
pftaps19870922_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19870929_wk39.zip">
pftaps19870929_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19871006_wk40.zip">
pftaps19871006_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19871013_wk41.zip">
pftaps19871013_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19871020_wk42.zip">
pftaps19871020_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19871027_wk43.zip">
pftaps19871027_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19871103_wk44.zip">
pftaps19871103_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19871110_wk45.zip">
pftaps19871110_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19871117_wk46.zip">
pftaps19871117_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19871124_wk47.zip">
pftaps19871124_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19871201_wk48.zip">
pftaps19871201_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19871208_wk49.zip">
pftaps19871208_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19871215_wk50.zip">
pftaps19871215_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19871222_wk51.zip">
pftaps19871222_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1987/pftaps19871229_wk52.zip">
pftaps19871229_wk52.zip</a>&nbsp;


<h3 id="1986">1986</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860107_wk01.zip">
pftaps19860107_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860114_wk02.zip">
pftaps19860114_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860121_wk03.zip">
pftaps19860121_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860128_wk04.zip">
pftaps19860128_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860204_wk05.zip">
pftaps19860204_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860211_wk06.zip">
pftaps19860211_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860218_wk07.zip">
pftaps19860218_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860225_wk08.zip">
pftaps19860225_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860304_wk09.zip">
pftaps19860304_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860311_wk10.zip">
pftaps19860311_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860318_wk11.zip">
pftaps19860318_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860325_wk12.zip">
pftaps19860325_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860401_wk13.zip">
pftaps19860401_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860408_wk14.zip">
pftaps19860408_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860415_wk15.zip">
pftaps19860415_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860422_wk16.zip">
pftaps19860422_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860429_wk17.zip">
pftaps19860429_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860506_wk18.zip">
pftaps19860506_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860513_wk19.zip">
pftaps19860513_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860520_wk20.zip">
pftaps19860520_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860527_wk21.zip">
pftaps19860527_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860603_wk22.zip">
pftaps19860603_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860610_wk23.zip">
pftaps19860610_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860617_wk24.zip">
pftaps19860617_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860624_wk25.zip">
pftaps19860624_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860701_wk26.zip">
pftaps19860701_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860708_wk27.zip">
pftaps19860708_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860715_wk28.zip">
pftaps19860715_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860722_wk29.zip">
pftaps19860722_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860729_wk30.zip">
pftaps19860729_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860805_wk31.zip">
pftaps19860805_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860812_wk32.zip">
pftaps19860812_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860819_wk33.zip">
pftaps19860819_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860826_wk34.zip">
pftaps19860826_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860902_wk35.zip">
pftaps19860902_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860909_wk36.zip">
pftaps19860909_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860916_wk37.zip">
pftaps19860916_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860923_wk38.zip">
pftaps19860923_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19860930_wk39.zip">
pftaps19860930_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19861007_wk40.zip">
pftaps19861007_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19861014_wk41.zip">
pftaps19861014_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19861021_wk42.zip">
pftaps19861021_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19861028_wk43.zip">
pftaps19861028_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19861104_wk44.zip">
pftaps19861104_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19861111_wk45.zip">
pftaps19861111_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19861118_wk46.zip">
pftaps19861118_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19861125_wk47.zip">
pftaps19861125_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19861202_wk48.zip">
pftaps19861202_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19861209_wk49.zip">
pftaps19861209_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19861216_wk50.zip">
pftaps19861216_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19861223_wk51.zip">
pftaps19861223_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1986/pftaps19861230_wk52.zip">
pftaps19861230_wk52.zip</a>&nbsp;


<h3 id="1985">1985</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850101_wk01.zip">
pftaps19850101_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850108_wk02.zip">
pftaps19850108_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850115_wk03.zip">
pftaps19850115_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850122_wk04.zip">
pftaps19850122_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850129_wk05.zip">
pftaps19850129_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850205_wk06.zip">
pftaps19850205_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850212_wk07.zip">
pftaps19850212_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850219_wk08.zip">
pftaps19850219_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850226_wk09.zip">
pftaps19850226_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850305_wk10.zip">
pftaps19850305_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850312_wk11.zip">
pftaps19850312_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850319_wk12.zip">
pftaps19850319_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850326_wk13.zip">
pftaps19850326_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850402_wk14.zip">
pftaps19850402_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850409_wk15.zip">
pftaps19850409_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850416_wk16.zip">
pftaps19850416_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850423_wk17.zip">
pftaps19850423_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850430_wk18.zip">
pftaps19850430_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850507_wk19.zip">
pftaps19850507_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850514_wk20.zip">
pftaps19850514_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850521_wk21.zip">
pftaps19850521_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850528_wk22.zip">
pftaps19850528_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850604_wk23.zip">
pftaps19850604_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850611_wk24.zip">
pftaps19850611_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850618_wk25.zip">
pftaps19850618_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850625_wk26.zip">
pftaps19850625_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850702_wk27.zip">
pftaps19850702_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850709_wk28.zip">
pftaps19850709_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850716_wk29.zip">
pftaps19850716_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850723_wk30.zip">
pftaps19850723_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850730_wk31.zip">
pftaps19850730_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850806_wk32.zip">
pftaps19850806_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850813_wk33.zip">
pftaps19850813_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850820_wk34.zip">
pftaps19850820_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850827_wk35.zip">
pftaps19850827_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850903_wk36.zip">
pftaps19850903_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850910_wk37.zip">
pftaps19850910_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850917_wk38.zip">
pftaps19850917_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19850924_wk39.zip">
pftaps19850924_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19851001_wk40.zip">
pftaps19851001_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19851008_wk41.zip">
pftaps19851008_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19851015_wk42.zip">
pftaps19851015_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19851022_wk43.zip">
pftaps19851022_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19851029_wk44.zip">
pftaps19851029_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19851105_wk45.zip">
pftaps19851105_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19851112_wk46.zip">
pftaps19851112_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19851119_wk47.zip">
pftaps19851119_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19851126_wk48.zip">
pftaps19851126_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19851203_wk49.zip">
pftaps19851203_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19851210_wk50.zip">
pftaps19851210_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19851217_wk51.zip">
pftaps19851217_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19851224_wk52.zip">
pftaps19851224_wk52.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1985/pftaps19851231_wk53.zip">
pftaps19851231_wk53.zip</a>&nbsp;


<h3 id="1984">1984</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840103_wk01.zip">
pftaps19840103_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840110_wk02.zip">
pftaps19840110_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840117_wk03.zip">
pftaps19840117_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840124_wk04.zip">
pftaps19840124_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840131_wk05.zip">
pftaps19840131_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840207_wk06.zip">
pftaps19840207_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840214_wk07.zip">
pftaps19840214_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840221_wk08.zip">
pftaps19840221_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840228_wk09.zip">
pftaps19840228_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840306_wk10.zip">
pftaps19840306_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840313_wk11.zip">
pftaps19840313_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840320_wk12.zip">
pftaps19840320_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840327_wk13.zip">
pftaps19840327_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840403_wk14.zip">
pftaps19840403_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840410_wk15.zip">
pftaps19840410_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840417_wk16.zip">
pftaps19840417_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840424_wk17.zip">
pftaps19840424_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840501_wk18.zip">
pftaps19840501_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840508_wk19.zip">
pftaps19840508_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840515_wk20.zip">
pftaps19840515_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840522_wk21.zip">
pftaps19840522_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840529_wk22.zip">
pftaps19840529_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840605_wk23.zip">
pftaps19840605_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840612_wk24.zip">
pftaps19840612_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840619_wk25.zip">
pftaps19840619_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840626_wk26.zip">
pftaps19840626_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840703_wk27.zip">
pftaps19840703_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840710_wk28.zip">
pftaps19840710_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840717_wk29.zip">
pftaps19840717_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840724_wk30.zip">
pftaps19840724_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840731_wk31.zip">
pftaps19840731_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840807_wk32.zip">
pftaps19840807_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840814_wk33.zip">
pftaps19840814_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840821_wk34.zip">
pftaps19840821_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840828_wk35.zip">
pftaps19840828_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840904_wk36.zip">
pftaps19840904_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840911_wk37.zip">
pftaps19840911_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840918_wk38.zip">
pftaps19840918_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19840925_wk39.zip">
pftaps19840925_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19841002_wk40.zip">
pftaps19841002_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19841009_wk41.zip">
pftaps19841009_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19841016_wk42.zip">
pftaps19841016_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19841023_wk43.zip">
pftaps19841023_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19841030_wk44.zip">
pftaps19841030_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19841106_wk45.zip">
pftaps19841106_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19841113_wk46.zip">
pftaps19841113_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19841120_wk47.zip">
pftaps19841120_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19841127_wk48.zip">
pftaps19841127_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19841204_wk49.zip">
pftaps19841204_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19841211_wk50.zip">
pftaps19841211_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19841218_wk51.zip">
pftaps19841218_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1984/pftaps19841225_wk52.zip">
pftaps19841225_wk52.zip</a>&nbsp;


<h3 id="1983">1983</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830104_wk01.zip">
pftaps19830104_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830111_wk02.zip">
pftaps19830111_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830118_wk03.zip">
pftaps19830118_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830125_wk04.zip">
pftaps19830125_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830201_wk05.zip">
pftaps19830201_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830208_wk06.zip">
pftaps19830208_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830215_wk07.zip">
pftaps19830215_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830222_wk08.zip">
pftaps19830222_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830301_wk09.zip">
pftaps19830301_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830308_wk10.zip">
pftaps19830308_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830315_wk11.zip">
pftaps19830315_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830322_wk12.zip">
pftaps19830322_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830329_wk13.zip">
pftaps19830329_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830405_wk14.zip">
pftaps19830405_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830412_wk15.zip">
pftaps19830412_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830419_wk16.zip">
pftaps19830419_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830426_wk17.zip">
pftaps19830426_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830503_wk18.zip">
pftaps19830503_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830510_wk19.zip">
pftaps19830510_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830517_wk20.zip">
pftaps19830517_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830524_wk21.zip">
pftaps19830524_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830531_wk22.zip">
pftaps19830531_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830607_wk23.zip">
pftaps19830607_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830614_wk24.zip">
pftaps19830614_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830621_wk25.zip">
pftaps19830621_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830628_wk26.zip">
pftaps19830628_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830705_wk27.zip">
pftaps19830705_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830712_wk28.zip">
pftaps19830712_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830719_wk29.zip">
pftaps19830719_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830726_wk30.zip">
pftaps19830726_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830802_wk31.zip">
pftaps19830802_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830809_wk32.zip">
pftaps19830809_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830816_wk33.zip">
pftaps19830816_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830823_wk34.zip">
pftaps19830823_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830830_wk35.zip">
pftaps19830830_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830906_wk36.zip">
pftaps19830906_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830913_wk37.zip">
pftaps19830913_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830920_wk38.zip">
pftaps19830920_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19830927_wk39.zip">
pftaps19830927_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19831004_wk40.zip">
pftaps19831004_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19831011_wk41.zip">
pftaps19831011_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19831018_wk42.zip">
pftaps19831018_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19831025_wk43.zip">
pftaps19831025_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19831101_wk44.zip">
pftaps19831101_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19831108_wk45.zip">
pftaps19831108_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19831115_wk46.zip">
pftaps19831115_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19831122_wk47.zip">
pftaps19831122_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19831129_wk48.zip">
pftaps19831129_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19831206_wk49.zip">
pftaps19831206_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19831213_wk50.zip">
pftaps19831213_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19831220_wk51.zip">
pftaps19831220_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1983/pftaps19831227_wk52.zip">
pftaps19831227_wk52.zip</a>&nbsp;


<h3 id="1982">1982</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820105_wk01.zip">
pftaps19820105_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820112_wk02.zip">
pftaps19820112_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820119_wk03.zip">
pftaps19820119_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820126_wk04.zip">
pftaps19820126_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820202_wk05.zip">
pftaps19820202_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820209_wk06.zip">
pftaps19820209_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820216_wk07.zip">
pftaps19820216_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820223_wk08.zip">
pftaps19820223_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820302_wk09.zip">
pftaps19820302_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820309_wk10.zip">
pftaps19820309_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820316_wk11.zip">
pftaps19820316_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820323_wk12.zip">
pftaps19820323_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820330_wk13.zip">
pftaps19820330_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820406_wk14.zip">
pftaps19820406_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820413_wk15.zip">
pftaps19820413_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820420_wk16.zip">
pftaps19820420_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820427_wk17.zip">
pftaps19820427_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820504_wk18.zip">
pftaps19820504_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820511_wk19.zip">
pftaps19820511_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820518_wk20.zip">
pftaps19820518_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820525_wk21.zip">
pftaps19820525_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820601_wk22.zip">
pftaps19820601_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820608_wk23.zip">
pftaps19820608_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820615_wk24.zip">
pftaps19820615_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820622_wk25.zip">
pftaps19820622_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820629_wk26.zip">
pftaps19820629_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820706_wk27.zip">
pftaps19820706_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820713_wk28.zip">
pftaps19820713_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820720_wk29.zip">
pftaps19820720_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820727_wk30.zip">
pftaps19820727_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820803_wk31.zip">
pftaps19820803_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820810_wk32.zip">
pftaps19820810_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820817_wk33.zip">
pftaps19820817_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820824_wk34.zip">
pftaps19820824_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820831_wk35.zip">
pftaps19820831_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820907_wk36.zip">
pftaps19820907_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820914_wk37.zip">
pftaps19820914_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820921_wk38.zip">
pftaps19820921_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19820928_wk39.zip">
pftaps19820928_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19821005_wk40.zip">
pftaps19821005_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19821012_wk41.zip">
pftaps19821012_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19821019_wk42.zip">
pftaps19821019_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19821026_wk43.zip">
pftaps19821026_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19821102_wk44.zip">
pftaps19821102_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19821109_wk45.zip">
pftaps19821109_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19821116_wk46.zip">
pftaps19821116_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19821123_wk47.zip">
pftaps19821123_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19821130_wk48.zip">
pftaps19821130_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19821207_wk49.zip">
pftaps19821207_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19821214_wk50.zip">
pftaps19821214_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19821221_wk51.zip">
pftaps19821221_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1982/pftaps19821228_wk52.zip">
pftaps19821228_wk52.zip</a>&nbsp;


<h3 id="1981">1981</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810106_wk01.zip">
pftaps19810106_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810113_wk02.zip">
pftaps19810113_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810120_wk03.zip">
pftaps19810120_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810127_wk04.zip">
pftaps19810127_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810203_wk05.zip">
pftaps19810203_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810210_wk06.zip">
pftaps19810210_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810217_wk07.zip">
pftaps19810217_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810224_wk08.zip">
pftaps19810224_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810303_wk09.zip">
pftaps19810303_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810310_wk10.zip">
pftaps19810310_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810317_wk11.zip">
pftaps19810317_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810324_wk12.zip">
pftaps19810324_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810331_wk13.zip">
pftaps19810331_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810407_wk14.zip">
pftaps19810407_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810414_wk15.zip">
pftaps19810414_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810421_wk16.zip">
pftaps19810421_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810428_wk17.zip">
pftaps19810428_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810505_wk18.zip">
pftaps19810505_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810512_wk19.zip">
pftaps19810512_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810519_wk20.zip">
pftaps19810519_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810526_wk21.zip">
pftaps19810526_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810602_wk22.zip">
pftaps19810602_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810609_wk23.zip">
pftaps19810609_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810616_wk24.zip">
pftaps19810616_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810623_wk25.zip">
pftaps19810623_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810630_wk26.zip">
pftaps19810630_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810707_wk27.zip">
pftaps19810707_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810714_wk28.zip">
pftaps19810714_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810721_wk29.zip">
pftaps19810721_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810728_wk30.zip">
pftaps19810728_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810804_wk31.zip">
pftaps19810804_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810811_wk32.zip">
pftaps19810811_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810818_wk33.zip">
pftaps19810818_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810825_wk34.zip">
pftaps19810825_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810901_wk35.zip">
pftaps19810901_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810908_wk36.zip">
pftaps19810908_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810915_wk37.zip">
pftaps19810915_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810922_wk38.zip">
pftaps19810922_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19810929_wk39.zip">
pftaps19810929_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19811006_wk40.zip">
pftaps19811006_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19811013_wk41.zip">
pftaps19811013_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19811020_wk42.zip">
pftaps19811020_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19811027_wk43.zip">
pftaps19811027_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19811103_wk44.zip">
pftaps19811103_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19811110_wk45.zip">
pftaps19811110_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19811117_wk46.zip">
pftaps19811117_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19811124_wk47.zip">
pftaps19811124_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19811201_wk48.zip">
pftaps19811201_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19811208_wk49.zip">
pftaps19811208_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19811215_wk50.zip">
pftaps19811215_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19811222_wk51.zip">
pftaps19811222_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1981/pftaps19811229_wk52.zip">
pftaps19811229_wk52.zip</a>&nbsp;


<h3 id="1980">1980</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800101_wk01.zip">
pftaps19800101_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800108_wk02.zip">
pftaps19800108_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800115_wk03.zip">
pftaps19800115_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800122_wk04.zip">
pftaps19800122_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800129_wk05.zip">
pftaps19800129_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800205_wk06.zip">
pftaps19800205_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800212_wk07.zip">
pftaps19800212_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800219_wk08.zip">
pftaps19800219_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800226_wk09.zip">
pftaps19800226_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800304_wk10.zip">
pftaps19800304_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800311_wk11.zip">
pftaps19800311_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800318_wk12.zip">
pftaps19800318_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800325_wk13.zip">
pftaps19800325_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800401_wk14.zip">
pftaps19800401_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800408_wk15.zip">
pftaps19800408_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800415_wk16.zip">
pftaps19800415_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800422_wk17.zip">
pftaps19800422_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800429_wk18.zip">
pftaps19800429_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800506_wk19.zip">
pftaps19800506_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800513_wk20.zip">
pftaps19800513_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800520_wk21.zip">
pftaps19800520_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800527_wk22.zip">
pftaps19800527_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800603_wk23.zip">
pftaps19800603_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800610_wk24.zip">
pftaps19800610_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800617_wk25.zip">
pftaps19800617_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800624_wk26.zip">
pftaps19800624_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800701_wk27.zip">
pftaps19800701_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800708_wk28.zip">
pftaps19800708_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800715_wk29.zip">
pftaps19800715_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800722_wk30.zip">
pftaps19800722_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800729_wk31.zip">
pftaps19800729_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800805_wk32.zip">
pftaps19800805_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800812_wk33.zip">
pftaps19800812_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800819_wk34.zip">
pftaps19800819_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800826_wk35.zip">
pftaps19800826_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800902_wk36.zip">
pftaps19800902_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800909_wk37.zip">
pftaps19800909_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800916_wk38.zip">
pftaps19800916_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800923_wk39.zip">
pftaps19800923_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19800930_wk40.zip">
pftaps19800930_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19801007_wk41.zip">
pftaps19801007_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19801014_wk42.zip">
pftaps19801014_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19801021_wk43.zip">
pftaps19801021_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19801028_wk44.zip">
pftaps19801028_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19801104_wk45.zip">
pftaps19801104_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19801111_wk46.zip">
pftaps19801111_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19801118_wk47.zip">
pftaps19801118_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19801125_wk48.zip">
pftaps19801125_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19801202_wk49.zip">
pftaps19801202_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19801209_wk50.zip">
pftaps19801209_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19801216_wk51.zip">
pftaps19801216_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19801223_wk52.zip">
pftaps19801223_wk52.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1980/pftaps19801230_wk53.zip">
pftaps19801230_wk53.zip</a>&nbsp;


<h3 id="1979">1979</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790102_wk01.zip">
pftaps19790102_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790109_wk02.zip">
pftaps19790109_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790116_wk03.zip">
pftaps19790116_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790123_wk04.zip">
pftaps19790123_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790130_wk05.zip">
pftaps19790130_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790206_wk06.zip">
pftaps19790206_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790213_wk07.zip">
pftaps19790213_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790220_wk08.zip">
pftaps19790220_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790227_wk09.zip">
pftaps19790227_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790306_wk10.zip">
pftaps19790306_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790313_wk11.zip">
pftaps19790313_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790320_wk12.zip">
pftaps19790320_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790327_wk13.zip">
pftaps19790327_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790403_wk14.zip">
pftaps19790403_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790410_wk15.zip">
pftaps19790410_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790417_wk16.zip">
pftaps19790417_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790424_wk17.zip">
pftaps19790424_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790501_wk18.zip">
pftaps19790501_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790508_wk19.zip">
pftaps19790508_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790515_wk20.zip">
pftaps19790515_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790522_wk21.zip">
pftaps19790522_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790529_wk22.zip">
pftaps19790529_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790605_wk23.zip">
pftaps19790605_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790612_wk24.zip">
pftaps19790612_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790619_wk25.zip">
pftaps19790619_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790626_wk26.zip">
pftaps19790626_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790703_wk27.zip">
pftaps19790703_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790710_wk28.zip">
pftaps19790710_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790717_wk29.zip">
pftaps19790717_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790724_wk30.zip">
pftaps19790724_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790731_wk31.zip">
pftaps19790731_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790807_wk32.zip">
pftaps19790807_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790814_wk33.zip">
pftaps19790814_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790821_wk34.zip">
pftaps19790821_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790828_wk35.zip">
pftaps19790828_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790904_wk36.zip">
pftaps19790904_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790911_wk37.zip">
pftaps19790911_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790918_wk38.zip">
pftaps19790918_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19790925_wk39.zip">
pftaps19790925_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19791002_wk40.zip">
pftaps19791002_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19791009_wk41.zip">
pftaps19791009_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19791016_wk42.zip">
pftaps19791016_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19791023_wk43.zip">
pftaps19791023_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19791030_wk44.zip">
pftaps19791030_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19791106_wk45.zip">
pftaps19791106_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19791113_wk46.zip">
pftaps19791113_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19791120_wk47.zip">
pftaps19791120_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19791127_wk48.zip">
pftaps19791127_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19791204_wk49.zip">
pftaps19791204_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19791211_wk50.zip">
pftaps19791211_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19791218_wk51.zip">
pftaps19791218_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1979/pftaps19791225_wk52.zip">
pftaps19791225_wk52.zip</a>&nbsp;


<h3 id="1978">1978</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780103_wk01.zip">
pftaps19780103_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780110_wk02.zip">
pftaps19780110_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780117_wk03.zip">
pftaps19780117_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780124_wk04.zip">
pftaps19780124_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780131_wk05.zip">
pftaps19780131_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780207_wk06.zip">
pftaps19780207_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780214_wk07.zip">
pftaps19780214_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780221_wk08.zip">
pftaps19780221_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780228_wk09.zip">
pftaps19780228_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780307_wk10.zip">
pftaps19780307_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780314_wk11.zip">
pftaps19780314_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780321_wk12.zip">
pftaps19780321_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780328_wk13.zip">
pftaps19780328_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780404_wk14.zip">
pftaps19780404_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780411_wk15.zip">
pftaps19780411_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780418_wk16.zip">
pftaps19780418_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780425_wk17.zip">
pftaps19780425_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780502_wk18.zip">
pftaps19780502_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780509_wk19.zip">
pftaps19780509_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780516_wk20.zip">
pftaps19780516_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780523_wk21.zip">
pftaps19780523_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780530_wk22.zip">
pftaps19780530_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780606_wk23.zip">
pftaps19780606_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780613_wk24.zip">
pftaps19780613_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780620_wk25.zip">
pftaps19780620_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780627_wk26.zip">
pftaps19780627_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780704_wk27.zip">
pftaps19780704_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780711_wk28.zip">
pftaps19780711_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780718_wk29.zip">
pftaps19780718_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780725_wk30.zip">
pftaps19780725_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780801_wk31.zip">
pftaps19780801_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780808_wk32.zip">
pftaps19780808_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780815_wk33.zip">
pftaps19780815_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780822_wk34.zip">
pftaps19780822_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780829_wk35.zip">
pftaps19780829_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780905_wk36.zip">
pftaps19780905_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780912_wk37.zip">
pftaps19780912_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780919_wk38.zip">
pftaps19780919_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19780926_wk39.zip">
pftaps19780926_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19781003_wk40.zip">
pftaps19781003_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19781010_wk41.zip">
pftaps19781010_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19781017_wk42.zip">
pftaps19781017_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19781024_wk43.zip">
pftaps19781024_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19781031_wk44.zip">
pftaps19781031_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19781107_wk45.zip">
pftaps19781107_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19781114_wk46.zip">
pftaps19781114_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19781121_wk47.zip">
pftaps19781121_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19781128_wk48.zip">
pftaps19781128_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19781205_wk49.zip">
pftaps19781205_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19781212_wk50.zip">
pftaps19781212_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19781219_wk51.zip">
pftaps19781219_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1978/pftaps19781226_wk52.zip">
pftaps19781226_wk52.zip</a>&nbsp;


<h3 id="1977">1977</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770104_wk01.zip">
pftaps19770104_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770111_wk02.zip">
pftaps19770111_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770118_wk03.zip">
pftaps19770118_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770125_wk04.zip">
pftaps19770125_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770201_wk05.zip">
pftaps19770201_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770208_wk06.zip">
pftaps19770208_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770215_wk07.zip">
pftaps19770215_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770222_wk08.zip">
pftaps19770222_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770301_wk09.zip">
pftaps19770301_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770308_wk10.zip">
pftaps19770308_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770315_wk11.zip">
pftaps19770315_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770322_wk12.zip">
pftaps19770322_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770329_wk13.zip">
pftaps19770329_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770405_wk14.zip">
pftaps19770405_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770412_wk15.zip">
pftaps19770412_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770419_wk16.zip">
pftaps19770419_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770426_wk17.zip">
pftaps19770426_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770503_wk18.zip">
pftaps19770503_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770510_wk19.zip">
pftaps19770510_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770517_wk20.zip">
pftaps19770517_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770524_wk21.zip">
pftaps19770524_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770531_wk22.zip">
pftaps19770531_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770607_wk23.zip">
pftaps19770607_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770614_wk24.zip">
pftaps19770614_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770621_wk25.zip">
pftaps19770621_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770628_wk26.zip">
pftaps19770628_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770705_wk27.zip">
pftaps19770705_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770712_wk28.zip">
pftaps19770712_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770719_wk29.zip">
pftaps19770719_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770726_wk30.zip">
pftaps19770726_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770802_wk31.zip">
pftaps19770802_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770809_wk32.zip">
pftaps19770809_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770816_wk33.zip">
pftaps19770816_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770823_wk34.zip">
pftaps19770823_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770830_wk35.zip">
pftaps19770830_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770906_wk36.zip">
pftaps19770906_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770913_wk37.zip">
pftaps19770913_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770920_wk38.zip">
pftaps19770920_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19770927_wk39.zip">
pftaps19770927_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19771004_wk40.zip">
pftaps19771004_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19771011_wk41.zip">
pftaps19771011_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19771018_wk42.zip">
pftaps19771018_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19771025_wk43.zip">
pftaps19771025_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19771101_wk44.zip">
pftaps19771101_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19771108_wk45.zip">
pftaps19771108_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19771115_wk46.zip">
pftaps19771115_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19771122_wk47.zip">
pftaps19771122_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19771129_wk48.zip">
pftaps19771129_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19771206_wk49.zip">
pftaps19771206_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19771213_wk50.zip">
pftaps19771213_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19771220_wk51.zip">
pftaps19771220_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1977/pftaps19771227_wk52.zip">
pftaps19771227_wk52.zip</a>&nbsp;


<h3 id="1976">1976</h3>

<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760106_wk01.zip">
pftaps19760106_wk01.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760113_wk02.zip">
pftaps19760113_wk02.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760120_wk03.zip">
pftaps19760120_wk03.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760127_wk04.zip">
pftaps19760127_wk04.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760203_wk05.zip">
pftaps19760203_wk05.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760210_wk06.zip">
pftaps19760210_wk06.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760217_wk07.zip">
pftaps19760217_wk07.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760224_wk08.zip">
pftaps19760224_wk08.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760302_wk09.zip">
pftaps19760302_wk09.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760309_wk10.zip">
pftaps19760309_wk10.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760316_wk11.zip">
pftaps19760316_wk11.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760323_wk12.zip">
pftaps19760323_wk12.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760330_wk13.zip">
pftaps19760330_wk13.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760406_wk14.zip">
pftaps19760406_wk14.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760413_wk15.zip">
pftaps19760413_wk15.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760420_wk16.zip">
pftaps19760420_wk16.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760427_wk17.zip">
pftaps19760427_wk17.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760504_wk18.zip">
pftaps19760504_wk18.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760511_wk19.zip">
pftaps19760511_wk19.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760518_wk20.zip">
pftaps19760518_wk20.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760525_wk21.zip">
pftaps19760525_wk21.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760601_wk22.zip">
pftaps19760601_wk22.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760608_wk23.zip">
pftaps19760608_wk23.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760615_wk24.zip">
pftaps19760615_wk24.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760622_wk25.zip">
pftaps19760622_wk25.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760629_wk26.zip">
pftaps19760629_wk26.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760706_wk27.zip">
pftaps19760706_wk27.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760713_wk28.zip">
pftaps19760713_wk28.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760720_wk29.zip">
pftaps19760720_wk29.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760727_wk30.zip">
pftaps19760727_wk30.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760803_wk31.zip">
pftaps19760803_wk31.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760810_wk32.zip">
pftaps19760810_wk32.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760817_wk33.zip">
pftaps19760817_wk33.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760824_wk34.zip">
pftaps19760824_wk34.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760831_wk35.zip">
pftaps19760831_wk35.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760907_wk36.zip">
pftaps19760907_wk36.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760914_wk37.zip">
pftaps19760914_wk37.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760921_wk38.zip">
pftaps19760921_wk38.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19760928_wk39.zip">
pftaps19760928_wk39.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19761005_wk40.zip">
pftaps19761005_wk40.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19761012_wk41.zip">
pftaps19761012_wk41.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19761019_wk42.zip">
pftaps19761019_wk42.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19761026_wk43.zip">
pftaps19761026_wk43.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19761102_wk44.zip">
pftaps19761102_wk44.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19761109_wk45.zip">
pftaps19761109_wk45.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19761116_wk46.zip">
pftaps19761116_wk46.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19761123_wk47.zip">
pftaps19761123_wk47.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19761130_wk48.zip">
pftaps19761130_wk48.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19761207_wk49.zip">
pftaps19761207_wk49.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19761214_wk50.zip">
pftaps19761214_wk50.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19761221_wk51.zip">
pftaps19761221_wk51.zip</a>&nbsp;
<a href="http://storage.googleapis.com/patents/grant_full_text/1976/pftaps19761228_wk52.zip">
pftaps19761228_wk52.zip</a>&nbsp;

      <div id="about" style="border-top: 1px solid #ccc;">
        <a  href="http://www.google.com/">Google Home</a> -
        <a  href="//www.google.com/patents/sitemap/">Sitemap</a> -
        <a  href="http://www.google.com/googlebooks/uspto.html">USPTO Bulk Downloads</a> -
        <a  href="https://www.google.com/intl/en/privacy/">Privacy Policy</a> -
        <a  href="https://www.google.com/accounts/TOS">Terms of Service</a> -
        <a  href="https://support.google.com/faqs/answer/2539193">About Google Patents</a> -
        <script type="text/javascript" src="//www.gstatic.com/feedback/api.js" nonce="DoPoBb_ks7ast9BjS39QGg"></script>
        <a  href="http://www.google.com/tools/feedback/intl/en/error.html" onclick="
                 try{
                 userfeedback.api.startFeedback({
                 productId: '72792',
                 locale: 'en',
                 bucket: 'bulkdata'
                 });
                 return false;
                 }catch(e){}">
          Send Feedback</a>
        <p> ©2012 Google
      </div>
    <!-- Analytics -->
    <script src="//www.google-analytics.com/ga.js"
            type="text/javascript" nonce="DoPoBb_ks7ast9BjS39QGg"></script>
    <script type="text/javascript" nonce="DoPoBb_ks7ast9BjS39QGg">
      try {
        var pageTracker = _gat._getTracker('UA-4953670-4');
        pageTracker._setCookiePath('/intl/');
        pageTracker._initData();
        pageTracker._trackPageview();
      } catch(err) {}
    </script>
    <script type="text/javascript" nonce="DoPoBb_ks7ast9BjS39QGg">
      var container = document.getElementById("container");
      var bg = "off";
      function toggleBg() {
        if (bg=="off"){
         container.style.background = "url(specs.png)";
          bg="on";
        } else {
          container.style.background = "none";
          bg="off"
        }
      }

      var footer = document.getElementById("about");
      function toggleLine() {
        if (footer.style.borderTop == "1px solid #ccc") {
          footer.style.borderTop = "1px solid #fff";
        } else {
          footer.style.borderTop = "1px solid #ccc"
        }
      }
    </script>
  </body>
</html>

"""

#%%
result = re.findall('(http)(.+)(zip)', uspto_file)
print(result)

#http...zip 형식 추출

#%%
#2000년도 이후 파일만 찾기

result = re.findall('(http)(.+)20[1-9]{2}(.+)(zip)', uspto_file)
print(result)

#%%

result = re.findall('(http)(.+)20[0-9]{1}1(.+)(zip)', uspto_file)
print(result)

#%%
