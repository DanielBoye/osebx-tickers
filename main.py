tickers = ["AEGA", "AGLX", "AIRX", "AKAST", "AKBM", "ACH", "AKH", "AKOBO", "ARCH", "ABS", "ARGEO", "ASTRO", "AURA", "ACR", "BGBIO", "BFISH", "CAPSL", "EAM", "ECIT", "ECO", "EWIND", "EIOF", "EMGS", "EFUEL", "EXTX", "FKRFT", "GEOS", "HAVI", "HYARD", "HDLY", "HUNT", "HYPRO", "KAHOT", "KOMPL", "KOA", "KYOTO", "LYTIX", "MVW", "MSEIS", "MRCEL", "MNTR", "NOC", "NEXT", "NORDH", "NANOV", "NUMND", "NODL", "NOL", "NAS", "NOR", "NYKD", "OBSRV", "PEXIP", "PGS", "QFUEL", "SCANA", "SKAND", "TEKNA", "VGM"]

sentence = "https://finance.yahoo.com/quote/" 
end = ".OL?p=&.tsrc=fin-srch"
n = 0

for word in tickers:
    print(sentence + tickers[n] + end)
    n = n + 1