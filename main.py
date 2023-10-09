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
    mot = choix_mot()
    trouve = ""
    lettres = []
    perdu = False

    for l in mot:
        if (l == " "):
            trouve += ' '
        else:
            trouve += '_'
    print(trouve)

    while mot != trouve and not perdu:
        l = input("Entrer une lettre \n")

        if (l in mot):
            indices = []
            n = 0
            for m in mot:
                if m == l:
                    indices.append(n)
                n += 1
            for i in indices:
                trouve = trouve[:i] + l + trouve[i + 1:]
            print(trouve)
        else:
            if l not in lettres or len(lettres) == 0:
                lettres.append(l)
                print(trouve)
                print(lettres)
                print("\n\n")
                affiche_pendu(len(lettres))

                if (len(lettres) >= 11):
                    print("PERDU !!!")
            else:
                print("déjà entré")

    print("GAGNE !!!")
