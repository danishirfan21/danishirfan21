#!/usr/bin/env python3
"""Generate an SVG snapshot of public GitHub telemetry. No third-party image service."""
import json, os, urllib.request, urllib.parse, html
USER='danishirfan21'
TOKEN=os.environ.get('GITHUB_TOKEN','')
ROOT=os.path.dirname(os.path.dirname(__file__))

def get(url):
    headers={'Accept':'application/vnd.github+json','User-Agent':'danish-profile-stats','X-GitHub-Api-Version':'2022-11-28'}
    if TOKEN: headers['Authorization']='Bearer '+TOKEN
    req=urllib.request.Request(url,headers=headers)
    with urllib.request.urlopen(req,timeout=25) as r:return json.load(r)

def search(q):
    return get('https://api.github.com/search/issues?q='+urllib.parse.quote(q))['total_count']

values={'repositories':'—','stars':'—','pull_requests':'—','merged_prs':'—','followers':'—'}
try:
    u=get('https://api.github.com/users/'+USER)
    values['repositories']=u.get('public_repos','—');values['followers']=u.get('followers','—')
except Exception as e:print('User fetch failed:',e)
try:
    repos=[];page=1
    while True:
        batch=get(f'https://api.github.com/users/{USER}/repos?per_page=100&page={page}&type=owner')
        repos.extend(batch)
        if len(batch)<100 or page>=10:break
        page+=1
    values['stars']=sum(x.get('stargazers_count',0) for x in repos if not x.get('fork'))
except Exception as e:print('Repository fetch failed:',e)
for key,query in [('pull_requests',f'type:pr author:{USER}'),('merged_prs',f'type:pr author:{USER} is:merged')]:
    try:values[key]=search(query)
    except Exception as e:print(key,'fetch failed:',e)

items=[('PUBLIC REPOSITORIES','repositories'),('STARS EARNED','stars'),('PRS OPENED','pull_requests'),('PRS MERGED','merged_prs'),('FOLLOWERS','followers')]
svg=['''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="180" viewBox="0 0 960 180"><rect width="960" height="180" rx="6" fill="#06100b"/><rect x="1" y="1" width="958" height="178" rx="6" fill="none" stroke="#265b3c"/><text x="30" y="30" fill="#67b585" font-size="14" font-family="monospace" letter-spacing="3">PUBLIC GITHUB TELEMETRY  /  AUTO-SYNC</text><path d="M30 45h900" stroke="#214830"/>''']
for i,(title,k) in enumerate(items):
    x=30+i*184
    if i:svg.append(f'<path d="M{x-14} 59v96" stroke="#244633"/>')
    val=html.escape(str(values[k]))
    svg.append(f'<text x="{x}" y="105" fill="#c8fadb" font-family="monospace" font-weight="bold" font-size="39">{val}</text><text x="{x}" y="143" fill="#83ba91" font-family="monospace" font-size="12">{title}</text>')
svg.append('</svg>')
path=os.path.join(ROOT,'assets','telemetry.svg')
with open(path,'w') as f:f.write(''.join(svg))
print(values)
