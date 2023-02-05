ticker_count = 0
price_count = 1

# Values
values = [("AEGA", 0.90101),("AGLX", 30.0),("AIRX", 3.7),("AKAST", 10.48)]
old_values = [("AEGA", 1484.0),("AGLX", 31.35),("AIRX", 8.6),("AKAST", 5.96),("AKBM", 47.65),("ACH", 4797.0),("AKH", 17.49),("AOW", 2561.0),("AKOBO", 6.9),("ARCH", 3.75),("ABS", 15.25),("ARGEO", 6.8),("ASTRO", 33.4),("AURA", 102.0),("ACR", 5.59),("BGBIO", 19.42),("BFISH", 13.3),("CAPSL", 17.5),("EAM", 10.0),("ECIT", 7.35),("ECO", 17.5),("EWIND", 30.9),("EIOF", 5.1),("EMGS", 1228.0),("EFUEL", 45.0),("EXTX", 19.0),("FKRFT", 37.14),("GEOS", 0.72),("HAVI", 3.94),("HYARD", 6.71),("HDLY", 7.87),("HUNT", 2798.0),("HYPRO", 18.28),("KAHOT", 31.96),("KOMPL", 61.5),("KOA", 2.89),("KYOTO", 19.78),("LYTIX", 12.7),("MVW", 10.3),("MSEIS", 4.35),("MRCEL", 5.2),("MNTR", 3.38),("NOC", 4.8),("NEXT", 6.58),("NORDH", 32.0),("NANOV", 13.72),("NUMND", 27.17),("NODL", 17.2),("NOL", 6.71),("NAS", 12.86),("NOR", 175.0),("NYKD", 48.85),("OBSRV", 7.6),("PEXIP", 43.12),("PGS", 2.8),("QFUEL", 16.21),("SCANA", 1.2),("SKAND", 6.55),("TEKNA", 18.44),("VGM", 3.104)]

# Loop to print out the value with taking away the 30.0 to 30 and saving the 10.48 as 10.48
for value in values:
    ticker = value[0]
    price = float(value[1])
    if price.is_integer():
        print(f"{ticker} = {int(price)} kr")
    else:
        print(f"{ticker} = {price} kr")

print("\n\n\n\n\n\n")
for value in old_values:
    ticker = value[0]
    price = float(value[1])
    if price.is_integer():
        print(f"{ticker} = {int(price)} kr")
    else:
        print(f"{ticker} = {price} kr")

print("\n\n\n")

old_values[0][1] = float(old_values[0][1])


# float number_old_values = old_values[][1]

print(type(old_values[0][1]))
