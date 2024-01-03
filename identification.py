from scipy.spatial import distance


def identification(numframe1, numligneorigine):
    numframe2 = numframe1 + 1
    with open(f"train/labels/frame_0{numframe1}.txt", "r") as file1:
        with open(f"train/labels/frame_0{numframe2}.txt", "r") as file2:
            frame1 = file1.read()
            frame2 = file2.read()
            ligneframe1 = frame1.split("\n")
            ligneorigine = ligneframe1[numligneorigine]
            ligneoriginesplit = ligneorigine.split(" ")

            vect1 = (float(ligneoriginesplit[1]), float(ligneoriginesplit[2]), float(ligneoriginesplit[3]),
                     float(ligneoriginesplit[4]))
            ligneframe2 = frame2.split("\n")
            distances = []
            ligneframe2.pop()
            for ligne in ligneframe2:
                lignesplit = ligne.split(" ")

                vect2 = (float(lignesplit[1]), float(lignesplit[2]), float(lignesplit[3]), float(lignesplit[4]))
                distances.append(distance.euclidean(vect1, vect2))
            prochaineligne = indicemin(distances)
            return (prochaineligne)


def indicemin(L):
    min = L[0]
    im = 0
    for i in range(1, len(L)):
        if L[i] < min:
            min = L[i]
            im = i
    return im


print(identification(100, 6))
