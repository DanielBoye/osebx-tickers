ticker_count = 0
price_count = 1

# Values
values = [('AGLX', 0.8800),('AIRX', 30.50),('AKAST', 3.7300),('AKBM', 12.00),('AKH', 37.00),('AKOBO', 15.29),('ARCH', 7.52),('ABS', 3.5000),('ARGEO', 11.00),('ASTRO', 1.7000),('AURA', 8.80),('ACR', 73.80),('BGBIO', 5.96),('BFISH', 7.30),('CAPSL', 1.5900),('EAM', 13.46),('ECIT', 5.82),('EWIND', 6.94),('EIOF', 27.00),('EMGS', 11.34),('EFUEL', 2.4100),('EXTX', 48.40),('GEOS', 12.40),('HAVI', 1.6250),('HDLY', 20.15),('HUNT', 3.5600),('HYPRO', 0.1352),('KAHOT', 32.95),('KOMPL', 18.62),('KOA', 13.18),('KYOTO', 2.8420),('LYTIX', 18.15),('MVW', 7.72),('MNTR', 10.00),('NEXT', 4.9400),('NORDH', 4.4900),('NANOV', 21.90),('NUMND', 0.9150),('NODL', 6.17),('NOL', 31.95),('NAS', 10.86),('NOR', 10.61),('NYKD', 414.00),('OBSRV', 32.80),('PEXIP', 2.0000),('PGS', 14.72),('QFUEL', 9.05),('SCANA', 6.79),('SKAND', 1.4100),('TEKNA', 0.3500),('VGM', 7.84),]
old_values = [("AEGA", 1484.0),("AGLX", 31.35),("AIRX", 8.6),("AKAST", 5.96),("AKBM", 47.65),("AKH", 17.49),("AOW", 2561.0),("AKOBO", 6.9),("ARCH", 3.75),("ABS", 15.25),("ARGEO", 6.8),("ASTRO", 33.4),("AURA", 102.0),("ACR", 5.59),("BGBIO", 19.42),("BFISH", 13.3),("CAPSL", 17.5),("EAM", 10.0),("ECIT", 7.35),("EWIND", 30.9),("EIOF", 5.1),("EMGS", 1228.0),("EFUEL", 45.0),("EXTX", 19.0),("GEOS", 0.72),("HAVI", 3.94),("HDLY", 7.87),("HUNT", 2798.0),("HYPRO", 18.28),("KAHOT", 31.96),("KOMPL", 61.5),("KOA", 2.89),("KYOTO", 19.78),("LYTIX", 12.7),("MVW", 10.3),("MNTR", 3.38),("NEXT", 6.58),("NORDH", 32.0),("NANOV", 13.72),("NUMND", 27.17),("NODL", 17.2),("NOL", 6.71),("NAS", 12.86),("NOR", 175.0),("NYKD", 48.85),("OBSRV", 7.6),("PEXIP", 43.12),("PGS", 2.8),("QFUEL", 16.21),("SCANA", 1.2),("SKAND", 6.55),("TEKNA", 18.44),("VGM", 3.104)]

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
