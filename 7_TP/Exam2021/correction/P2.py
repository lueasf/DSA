# C'est un problème du sac a dos !
# En particulier, c'est celui ou les objets on la même valeur que leur poids (la durée de la musique),
# et la capacité du sac est la durée du vol !
# On aura donc le même algorithme que pour le problème du sac a dos, mais
# adapté a la forme de nos données
# Il faudra juste faire attention, car la capacité maximale n'est pas exactement la durée du vol
# mais la durée du vol moins 23 minutes (les 8 au début et les 15 à la fin)

def load_clips_data(clips_database_filename: str) -> tuple[int, list[tuple[int, str]]]:
    duree_vol = 0
    musiques = []

    with open(clips_database_filename, "r") as f:
        duree_vol = int(f.readline().strip())

        for l in f.readlines():
            data = l.split(",")
            duree_musique = int(data[0])
            nom_musique = "".join(data[1:]).strip()
            musiques.append((duree_musique, nom_musique))

    return duree_vol, musiques


def compute_optimal_playlist(flight_duration_in_minutes: int, clips: list[tuple[int, str]]) -> tuple[int, list[tuple[int, str]]]:
    
    # On a plus le temps de mettre des musiques (plus de place dans le sac)
    if flight_duration_in_minutes <= 23:
        return (0, [])

    duree_max, playlist_max = 0, []

    # On essaie toutes les musiques disponibles si on peut les mettre
    for i in range(len(clips)):

        duree, nom = clips[i]

        # Si on peut jouer la musique, on essaie de la prendre
        # Attention, la durée du vol est en minutes et celle de la musique en secondes
        if flight_duration_in_minutes * 60 - duree >= 23 * 60:

            d, p = compute_optimal_playlist(flight_duration_in_minutes - duree / 60, clips[:i] + clips[i+1:])

            if d + duree > duree_max:
                duree_max = d + duree
                playlist_max = [(duree, nom)] + p

    
    return duree_max, playlist_max
