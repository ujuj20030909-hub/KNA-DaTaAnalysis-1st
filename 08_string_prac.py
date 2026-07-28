# 실습

# code = "PUMP_A"
# state = "정상"
# hour = 1200
# date = "2026-07-16"
# card = "설비: " + code + "\n상태: " + state + "\n가동: " + str(hour) + "\n점검: " + date
# print(card)

# word = "temp_sensor"
# print(word[:4])

# word = "temp_sensor"
# print(word[5:])

# word = "sensor_01"
# print(word[-2:])

# word = "PYTHON"
# print(word[::2])

# word = "PYTHON"
# print(word[::-1])

# ph = "01012345678"
# print(len(ph))

# print("a,b,c,d".count(",")) # 3
# print("a,b,c,d".count(", ")) #0

# word = "sensor_log.csv"
# print(word.startswith("sensor"))
# print(word.endswith(".csv"))

# word = "ready"
# b = word.upper()
# print(b)

# l = "WARNING"
# s = l.lower()
# print(s)

# print("ABC".isupper())
# print("abc".islower())
# print("Abc".islower())

# a = "Sensor_LOG.CSV"
# b = a.lower()
# print(b.startswith("sensor"))
# print(b.endswith(".csv"))

# str = "  Warning  "
# str = str.strip()
# str = str.strip().lower()
# print("[" + str + "]")
# print("[" + str + "]")


# s = "a,b,c,d"
# print(s.split(","))

# n = ["2025", "01", "15"]
# print("-".join(n))

# a = "python"
# print(a[:2] + a[2:].capitalize())

# a = "2025/01/15"
# b = a.split("/")
# c = "-".join(b)
# print(c)

# a = "1, NORMAL ,25.3"
# b = a.split(",")
# c = b[1].strip().lower()
# print(c)

code = "PUMP_A"
temp = 87
print(f"설비{code}, 온도{temp}도")
