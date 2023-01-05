plan_int = int(input("План по ШПД\n"))
plan_tv = int(input("План по ТВ\n"))
fact_int = int(input("Факт ШПД\n"))
fact_tv = int(input("Факт ТВ\n"))
time = int(input("Осталось дней\n"))
need_int = plan_int*0.8 - fact_int + 2
need_tv = plan_tv*0.8 - fact_tv + 2
trand = (need_int + need_tv) / time
print("Осталось: ", need_int, "ШПД ", need_tv, "ТВ\n" )
print("Тренд ", trand, "услуг")
print("Ты чемпион!")