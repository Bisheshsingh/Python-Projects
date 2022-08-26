import socket,requests
from bs4 import BeautifulSoup
import fake_useragent
import re
import favicon
import urllib.request
import googlesearch
from bs4 import BeautifulSoup as bs
import pickle,numpy as np

l=[]
loading=['-' for i in range(30)]
done=0
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
link=str(input('Enter URL: '))
def domain(url):
    try:
        r = requests.get('https://www.whois.com/whois/'+url).text
        if r.find('Domain:')!=-1:
            return r[r.find('Domain:')+35:r.find('</div><div class=',r.find('Domain:')+35)].strip().lower()
        else:
            return None
    except:
        return None
     
def ip(url):
    url=domain(url)
    if domain(url)==None:
        return -1
    try:
        socket.inet_aton(url)
        return -1
    except:
        return 1
l.append(ip(link))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def url_length(url):
    url='https://'+url if url[:7]!='http://' and url[:8]!='https://' else url
    try:
       return 1 if len(requests.get(url).url)<=54 else (0 if 54<len(requests.get(url).url)<75 else -1)
    except:
        return -1
l.append(url_length(link))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def url_short(url):
    match=re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                    'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                    'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                    'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                    'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                    'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                    'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|tr\.im|link\.zip\.net',url)
    if match:
        return -1
    else:
        return 1

l.append(url_short(link))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def have_at(url):
    return -1 if "@" in url else 1
l.append(have_at(link))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def dob_slsh(url):
    url='https://'+url if url[:7]!='http://' and url[:8]!='https://' else url
    return -1 if "//" in url[8:] else 1
l.append(dob_slsh(link))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0      
def pref_suff(url):
    try:
        return -1 if '-' in domain(url) else 1
    except:
        return -1
l.append(pref_suff(link))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def sub_domains(l):
    if domain(l)==None:
        return -1
    l=l[l.find('www.')+4:]
    if l.count('.') == 1:
        return 1
    elif l.count('.') == 2:
        return 0
    return -1
l.append(sub_domains(link))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def domain_createdate(domains):
        if domains==None:
           return -1
        user = fake_useragent.UserAgent().random
        headers = {'user-agent': user}
        url = f'https://www.nic.ru/whois/?searchWord={domains}'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        try:
            information = soup.find(class_='_3U-mA _23Irb')
            inf = information.text.splitlines()
            for x in inf:
                if 'created:' in x:
                    creation_date = x.split('created:')[-1].strip()
                    creation_date = creation_date[:4]
                    print(f'{domains}: {creation_date}')
                elif 'Creation Date' in x:
                    creation_date = x.split('Creation Date')[-1].strip()
                    creation_date = 2021-int(creation_date[2:6])
                    return 1 if creation_date>=1 else 0
        except:
            return -1
l.append(domain_createdate(domain(link)))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def is_registered(domain_name):
    r = requests.get('https://www.whois.com/whois/'+domain_name).text
    try:
        if int(r[r.find('Expire')+39:r.find('Expire')+43])-2021>=1 and r.find('Expire')!=-1:
            return 1
        else:
            return -1
    except:
        return -1
l.append(is_registered(link))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def favicon_url(url):
    if domain(url)==None:
           return -1
    try:
        url1='https://'+domain(url)
        if domain(url) in favicon.get(url1)[0][0]:
            return 1
        else:
            return -1
    except:
        return -1
l.append(favicon_url(link))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def port_scan(target_ip,port,output):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    try:
        s.connect((target_ip, port))
        output[port]='t'
    except:
        output[port]='f'
    
def port_valid(url):
    if domain(url)==None:
           return -1
    ip = socket.gethostbyname (domain(url)) 
    output={}
    for i in [21,22,23,80,443,445,1433,1521,3306,3389]:
         port_scan(ip,i,output)
    return 1 if output=={21: 'f', 22: 'f', 23: 'f', 80: 't', 443: 't', 445: 'f', 1433: 'f', 1521: 'f', 3306: 'f', 3389: 'f'} else -1
l.append(port_valid(link))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def port_scan1(target_ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    try:
        s.connect((target_ip, port))
        return 1
    except:
        return -1
        
def http(url):
    if domain(url)==None:
           return -1
    return port_scan1(socket.gethostbyname(domain(url)),443)
l.append(http(link))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def soup(url):
    try:
       if 'https://' not in url:
           url='https://'+url
       page_response= requests.get(url)
       return BeautifulSoup(page_response.content, 'html.parser')
    except:
        return None

def request_url(soup, domain):
    i = 0
    success = 0
    if domain==None:
        return -1
    if soup==None:
        return -1
    for img in soup.find_all('img', src=True):
        dots = [x.start(0) for x in re.finditer('\.', img['src'])]
        if domain not in img['src']:
            success = success + 1
        i = i + 1

    for audio in soup.find_all('audio', src=True):
        dots = [x.start(0) for x in re.finditer('\.', audio['src'])]
        if domain not in audio['src']:
            success = success + 1
        i = i + 1

    for embed in soup.find_all('embed', src=True):
        dots = [x.start(0) for x in re.finditer('\.', embed['src'])]
        if domain not in embed['src']:
            success = success + 1
        i = i + 1

    for i_frame in soup.find_all('i_frame', src=True):
        dots = [x.start(0) for x in re.finditer('\.', i_frame['src'])]
        if domain not in i_frame['src']:
            success = success + 1
        i = i + 1

    try:
        percentage = (success / float(i))*100
        return 1 if round(percentage, 2)<=22 else(-1 if  round(percentage, 2)>61 else 0)
    except:
        return -1
l.append(request_url(soup(link),domain(link)))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def url_of_anchor(soup, domain):
    i = 0
    unsafe = 0
    if domain==None:
        return -1
    if soup==None:
        return -1
    for a in soup.find_all('a', href=True):
        if "#" in a['href'] or "javascript" in a['href'].lower() or "mailto" in a['href'].lower() or not (
                domain in a['href']):
            unsafe = unsafe + 1
        i = i + 1
    try:
        percentage = (unsafe / float(i))*100
        return 1 if round(percentage, 2)<=31 else(-1 if  round(percentage, 2)>67 else 0)
    except:
        return 0
l.append(url_of_anchor(soup(link), domain(link)))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def links_in_tags(soup, domain):
    i=0
    success =0
    if domain==None:
           return -1
    if soup==None:
        return -1
    for link in soup.find_all('link', href= True):
        dots=[x.start(0) for x in re.finditer('\.',link['href'])]
        if domain not in link['href']:
            success = success + 1
        i=i+1

    for script in soup.find_all('script', src= True):
        dots=[x.start(0) for x in re.finditer('\.',script['src'])]
        if domain not in script['src']:
           success = success + 1
        i=i+1
    try:
        percentage = (success / float(i))*100
        return 1 if round(percentage, 2)<=17 else(-1 if  round(percentage, 2)>81 else 0)
    except:
        return 0

l.append(links_in_tags(soup(link), domain(link)))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def sfh(soup, domain):
    if domain==None:
           return -1
    if soup==None:
        return -1
    for form in soup.find_all('form', action= True):
        if form['action'] =="" or form['action'] == "about:blank" :
            return 1
        elif domain not in form['action']:
            return 1
        else:
            return -1
    return 
l.append(sfh(soup(link), domain(link)))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def submitting_to_email(soup):
    if soup==None:
        return -1
    for form in soup.find_all('form', action= True):
        if "mailto:" in form['action']:
            return -1
        else:
            return 1
    return -1
l.append(submitting_to_email(soup(link)))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def abnormal(url):
    try:
        r = requests.get('https://www.whois.com/whois/'+url).text
        if r[r.find('Domain:')+35:r.find('<',r.find('Domain:')+35)] in url:
            return 1
        else:
            return -1
    except:
        return -1
l.append(abnormal(link))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def redirect(url):
    count = 0
    url='https://'+url if url[:7]!='http://' and url[:8]!='https://' else url
    while True:
        try:
           r = requests.head(url)
        except:
            return -1
        if 300 < r.status_code < 400:
            url = r.headers['location']
            count=count+1
        else:
            return 1 if count<=1 else (-1 if count>3 else 0)
l.append(redirect(link))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def status_bar_custom(url):
    url='https://'+url if url[:7]!='http://' and url[:8]!='https://' else url
    try:
       return -1 if 'onMouseOver' in requests.get(url).text else 1
    except:
       return -1
l.append(status_bar_custom(link))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def disablerigclk(url):
    url='https://'+url if url[:7]!='http://' and url[:8]!='https://' else url
    try:
       return -1 if 'event.button==2' in requests.get(url).text else 1
    except:
        return -1
l.append(disablerigclk(link))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def popup(url):
    url='https://'+url if url[:7]!='http://' and url[:8]!='https://' else url
    try:
        return -1 if 'prompt(' in requests.get(url).text else 1
    except:
        return -1
l.append(popup(link))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def iframe(soup):
    if soup==None:
        return -1
    for iframe in soup.find_all('iframe', width=True, height=True, frameBorder=True):
        if iframe['width']=="0" and iframe['height']=="0" and iframe['frameBorder']=="0":
            return -1
        else:
            return 1
    return 1

l.append(iframe(soup(link)))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def age_of_domain(url):
    if domain(url)==None:
           return -1
    r = requests.get('https://www.whois.com/whois/'+domain(url)).text
    try:
        if r.find('Expire')!=-1 and r.find('Registered')!=-1:
            s=int(r[r.find('Expire')+39:r.find('Expire')+43])*12-int(r[r.find('Registered')+42:r.find('Registered')+46])*12
            s1=int(r[r.find('Expire')+44:r.find('Expire')+46])-int(r[r.find('Registered')+47:r.find('Registered')+49])
            if s+s1>=6:
                return 1
            else:
                return -1
    except:
        return -1
    
l.append(age_of_domain(link))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def dns(url):
    if domain(url)==None:
           return -1
    r = requests.get('https://www.whois.com/whois/'+domain(url)).text
    return -1 if 'Looks like this domain has not been registered yet' in r else 1  
l.append(dns(link))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def web_traffic(url):
    try:
        rank = BeautifulSoup(urllib.request.urlopen("http://data.alexa.com/data?cli=10&dat=s&url=" + url).read(), "xml").find("REACH")['RANK']
    except TypeError:
        return -1
    rank= int(rank)
    if (rank<100000):
        return 1
    else:
        return 0
l.append(web_traffic(link))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def pagerank(url):
    return web_traffic(url)
    s='https://checkpagerank.net/index.php'
    para={'name':domain(url)}
    r=requests.post(s,data=para).text
    try:
        if eval(r[r.find('>',r.find('Google PageRank:'))+1:r.find('<',r.find('>',r.find('Google PageRank:')))])==0:
            return -1
        else:
            return 1
    except:
        return -1
l.append(pagerank(link))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def google_index(url):
    try:
       site=googlesearch.search(url,5)
    except:
        return -1
    if site:
        return 1
    else:
        return -1
l.append(google_index(link))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def task(url):
    if domain(url)==None:
           return -1
    dmn=domain(url)
    if 'https://' not in url:
        url='https://'+url
    try:
       resp=requests.get(url)
    except:
        return -1
    soup=bs(resp.text,'html.parser')
    r=0
    for link in soup.find_all('a'):
        temp=link.get('href')
        if temp is not None and dmn in temp:
            r=r+1
    return -1 if r==0 else (1 if r>2 else 0)
l.append(task(link))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done)
loading[done]=0   
def statistical_report(url):
    hostname = url
    h = [(x.start(0), x.end(0)) for x in re.finditer('https://|http://|www.|https://www.|http://www.', hostname)]
    z = int(len(h))
    if z != 0:
        y = h[0][1]
        hostname = hostname[y:]
        h = [(x.start(0), x.end(0)) for x in re.finditer('/', hostname)]
        z = int(len(h))
        if z != 0:
            hostname = hostname[:h[0][0]]
    url_match=re.search('at\.ua|usa\.cc|baltazarpresentes\.com\.br|pe\.hu|esy\.es|hol\.es|sweddy\.com|myjino\.ru|96\.lt|ow\.ly',url)
    try:
        ip_address = socket.gethostbyname(hostname)
        ip_match=re.search('146\.112\.61\.108|213\.174\.157\.151|121\.50\.168\.88|192\.185\.217\.116|78\.46\.211\.158|181\.174\.165\.13|46\.242\.145\.103|121\.50\.168\.40|83\.125\.22\.219|46\.242\.145\.98|107\.151\.148\.44|107\.151\.148\.107|64\.70\.19\.203|199\.184\.144\.27|107\.151\.148\.108|107\.151\.148\.109|119\.28\.52\.61|54\.83\.43\.69|52\.69\.166\.231|216\.58\.192\.225|118\.184\.25\.86|67\.208\.74\.71|23\.253\.126\.58|104\.239\.157\.210|175\.126\.123\.219|141\.8\.224\.221|10\.10\.10\.10|43\.229\.108\.32|103\.232\.215\.140|69\.172\.201\.153|216\.218\.185\.162|54\.225\.104\.146|103\.243\.24\.98|199\.59\.243\.120|31\.170\.160\.61|213\.19\.128\.77|62\.113\.226\.131|208\.100\.26\.234|195\.16\.127\.102|195\.16\.127\.157|34\.196\.13\.28|103\.224\.212\.222|172\.217\.4\.225|54\.72\.9\.51|192\.64\.147\.141|198\.200\.56\.183|23\.253\.164\.103|52\.48\.191\.26|52\.214\.197\.72|87\.98\.255\.18|209\.99\.17\.27|216\.38\.62\.18|104\.130\.124\.96|47\.89\.58\.141|78\.46\.211\.158|54\.86\.225\.156|54\.82\.156\.19|37\.157\.192\.102|204\.11\.56\.48|110\.34\.231\.42',ip_address)  
    except:
        return -1

    if url_match:
        return -1
    else:
        return 1
l.append(statistical_report(link))
done+=1
print('\nLoading:',int((done/30)*100),'%'+' Process: ',done) 
for i in range(len(l)):
    if l[i]==None:
        l[i]=-1

result='Legitimate' if pickle.load(open('model.txt','rb')).predict(np.array([l]))==1 else 'Pishing'
print('\nRESULT: '+result)
