# class Salomlashish:
#     def __init__(self, ism, fam):
#         self.__ism = ism
#         self.__fam = fam
#
#     def get_ism(self):
#         return self.__ism
#
#     def get_fam(self):
#         return self.__fam
#
#     def salom(self):
#         print(f"Assalomu alaykum hurmatli {self.ism} {self.fam} jamoamizga hush kelibsiz!")
#
# salom1 = Salomlashish("Ali", "Valiyev")
# salom2 = Salomlashish("G'anijon", "Norimov")
# salom3 = Salomlashish("Bobur", "Jovliyev")
#
#
# print(salom1.get_ism())
# print(salom2.get_fam())






class BankHisobi:
    def __init__(self, egasi, boshlangich_balans=0):
        self.__egasi = egasi
        self.__balans = boshlangich_balans

    def get_egasi(self):
        return self.__egasi

    def get_balans(self):
        return self.__balans

    def pul_qosh(self, miqdor):
        if miqdor <= 0:
            print("Noto'g'ri miqdor")
            return
        self.__balans += miqdor

    def pul_yech(self, miqdor):
        if miqdor <= 0:
            print("Noto'g'ri miqdor")
        elif miqdor> self.__balans:
            print("Mavlag' yetarli emas")
        else:
            self.__balans -= miqdor


hisob = BankHisobi("Ozodbek", 5_000_000)
print(hisob.get_egasi())
print(hisob.get_balans())
hisob.pul_qosh(200_000)
print(hisob.get_balans())
hisob.pul_yech(100_000)
print(hisob.get_balans())
hisob.pul_yech(200_000)
hisob.pul_qosh(-100_000)