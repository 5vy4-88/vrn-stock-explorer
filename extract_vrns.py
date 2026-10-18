#!/usr/bin/env python3
"""Re-extract the VRN table from stock.pdf (westernreg.co.uk, October 2026).
Usage: python extract_vrns.py ../data/stock.pdf   (needs: pip install pdfplumber pandas openpyxl)
The PDF is a five-column layout, so words are grouped by x-position, then by line.
Part 1 = first 226 priced entries (+ VAT), Part 2 = remaining 53 (no VAT)."""
import sys,re,collections,json,pdfplumber,pandas as pd
pdf=sys.argv[1] if len(sys.argv)>1 else '../data/stock.pdf'
page=pdfplumber.open(pdf).pages[0]; words=page.extract_words()
bounds=[0,105,215,335,445,10000]; pairs=[]
for i in range(5):
    lines=collections.defaultdict(list)
    for w in words:
        if bounds[i]<=w['x0']<bounds[i+1]: lines[round(w['top'])].append(w)
    for k in sorted(lines):
        s=' '.join(z['text'] for z in sorted(lines[k],key=lambda z:z['x0']))
        m=re.match(r'^(.+?),£(\d+)$',s)
        if m: pairs.append((m.group(1),int(m.group(2))))
assert len(pairs)==279, f'expected 279 priced rows, got {len(pairs)}'
def fmt(v):
    if re.fullmatch(r'[A-Z]{2}\d{2} [A-Z]{3}',v): return 'Current'
    if re.fullmatch(r'[A-Z]\d{1,3} [A-Z]{3}',v): return 'Prefix'
    if re.fullmatch(r'[A-Z]{3} \d{1,3}[A-Z]',v): return 'Suffix'
    return 'Dateless'
rows=[(i+1,v,p,'Part 1' if i<226 else 'Part 2','Plus VAT' if i<226 else 'No VAT','Main list',fmt(v)) for i,(v,p) in enumerate(pairs)]
for v in ['E33 HHH','E33 LLL','E33 PPP','E33 VVV','E33 WWW','E33 YYY']: rows.append((len(rows)+1,v,None,'Part 1','Plus VAT','New + VAT Stock banner',fmt(v)))
for v in ['IIG 3','ROI 990']: rows.append((len(rows)+1,v,None,'Part 2','No VAT','New No VAT Stock banner',fmt(v)))
df=pd.DataFrame(rows,columns=['No.','VRN','Price (GBP)','Part','VAT','Source block','Format'])
df.to_csv('stock_vrns_extracted.csv',index=False,encoding='utf-8-sig'); df.to_excel('stock_vrns_extracted.xlsx',index=False)
print(len(df),'rows written')
