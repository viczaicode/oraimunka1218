class Renszarvas:

    def __init__(self, nev: str, magassag: str, hely: str, leiras: str):
        self.nev = nev
        nevDarabolt = nev.split(" - ")
        self.nevAngol = nevDarabolt[0]
        self.nevMagyar = nevDarabolt[1]
        self.magassag = int(magassag)
        self.hely = int(hely)
        self.leiras = leiras

    def kiir(self) -> str:
        return f"Rénszarvas neve: {self.nev}, Magassága: {self.magassag}."

    def __str__(self) -> str:
        return f"Rénszarvas adatai: Angolnév {self.nevAngol}, magyar név {self.nevMagyar}, magasság: {self.magassag}, sorban elfoglalt helye: {self.hely}, leírás {self.leiras}"