

class Mycar:
    def setName(self, name):
        self.name = name

    def drive(self):
        print(f"{self.name} 이(가) 달려요!")


if __name__ == "__main__":
    c1: Mycar = Mycar()
    c1.setName("소나타")

    c2: Mycar = Mycar()  # MyCar -> Mycar로 수정
    c2.setName("아반떼")

    c1.drive()
    c2.drive()

