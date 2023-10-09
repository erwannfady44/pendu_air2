import random, mots

def affiche_pendu(erreurs):
    pendu = []

    match erreurs:
        case 1:
            pendu = ["_____"]
        case 2:
            pendu = [
                "  |",
                "  |",
                "  |",
                "  |",
                "  |",
                "__|__"
            ]
        case 3:
            pendu = [
                "   __________",
                "  |",
                "  |",
                "  |",
                "  |",
                "  |",
                "__|__"
            ]
        case 4:
            pendu = [
                "   __________",
                "  | /",
                "  |/",
                "  |",
                "  |",
                "  |",
                "__|__"
            ]
        case 5:
            pendu = [
                "   __________",
                "  | /       |",
                "  |/",
                "  |",
                "  |",
                "  |",
                "__|__"
            ]

        case 6:
            pendu = [
                "   __________",
                "  | /       |",
                "  |/        0",
                "  |",
                "  |",
                "  |",
                "__|__"
            ]

        case 7:
            pendu = [
                "   __________",
                "  | /       |",
                "  |/        0",
                "  |         |",
                "  |         |",
                "  |",
                "__|__"
            ]
        case 8:
            pendu = [
                "   __________",
                "  | /       |",
                "  |/        0",
                "  |        /|",
                "  |         |",
                "  |",
                "__|__"
            ]
        case 9:
            pendu = [
                "   __________",
                "  | /       |",
                "  |/        0",
                "  |        /|\\",
                "  |         |",
                "  |",
                "__|__"
            ]
        case 10:
            pendu = [
                "   __________",
                "  | /       |",
                "  |/        0",
                "  |        /|\\",
                "  |         |",
                "  |        /",
                "__|__"
            ]
        case 11:
            pendu = [
                "   __________",
                "  | /       |",
                "  |/        0",
                "  |        /|\\",
                "  |         |",
                "  |        / \\",
                "__|__"
            ]

    for ligne in pendu:
        print(ligne)
def choix_mot():
    return mots.mots.__getitem__(random.randint(0, len(mots.mots) - 1))
if __name__ == '__main__':
    print(choix_mot())


