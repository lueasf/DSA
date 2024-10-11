from util import *
import sys
sys.path.append("..")
sys.path.append(".")

import P2

print_test_start()

#
#   Test load_clips_data
#

with TestCase("load_clips_data - Exemple du sujet") as t:
    d, m = P2.load_clips_data("../exemple.txt")
    
    if d != 40:
        t.fail(f"Durée du vol invalide ({d} != 40)")
    elif len(m) != 8:
        t.fail(f"Nombre de musiques invalides ({len(m)} != 8)")
    else:
        m_parsed = set(map(lambda mus: (mus[0], mus[1].strip()), m))
        m_true = {(190, 'AC/DC - You shook me all night long'), (220, 'MUSE - Plug in Baby'), (416, 'Iron Maiden - Afraid to shoot strangers'), (235, "Shaka Ponk - I'm Picky"), (221, 'Foo Fighters - Saint Cecila'), (232, 'Imagine Dragons - Walking the wire'), (161, 'Greenday - Boulevard of broken dreams'), (253, 'Rise Against - Hero of war')}
        if m_parsed != m_true:
            t.fail(f"Musiques invalides :\nManquantes : {m_true - m_parsed}\nEn trop : {m_parsed - m_true}")


#
#   Test compute_optimal_playlist
#

duree_ex, musiques_ex = 40, [(190, 'AC/DC - You shook me all night long'), (220, 'MUSE - Plug in Baby'), (416, 'Iron Maiden - Afraid to shoot strangers'), (235, "Shaka Ponk - I'm Picky"), (221, 'Foo Fighters - Saint Cecila'), (232, 'Imagine Dragons - Walking the wire'), (161, 'Greenday - Boulevard of broken dreams'), (253, 'Rise Against - Hero of war')]

with TestCase("compute_optimal_playlist - Capacité pleine", "Vérifie le comportement de la fonction lorsqu'il n'y a plus de musiques assez courtes pour être prise") as t:
    
    d, m = P2.compute_optimal_playlist(0, musiques_ex)

    if d != 0:
        t.fail("La durée de la playlist devrait être 0")
    elif len(m) > 0:
        t.fail(f"La playlist devrait être vide (la fonction a renvoyé {m})")
    else:
        d, m = P2.compute_optimal_playlist(8+15, [(23*60, "Musique"), (1, "Musique2")])
        
        if d != 0 or len(m) > 0:
            t.fail(f"La playlist devrait être vide si le vol ne dure pas plus de 8+15 minutes, le temps avant et après la playlist n'est pas correctement pris en compte.\n\nPlaylist renvoyée : {m}")


with TestCase("compute_optimal_playlist - Pas de musiques") as t:

    d, m = P2.compute_optimal_playlist(0, musiques_ex)

    if d != 0 or len(m) != 0:
        t.fail("La fonction devrait renvoyer une playlist vide s'il n'y a pas de musique à prendre")


with TestCase("compute_optimal_playlist - Durée exacte") as t:

    d, m = P2.compute_optimal_playlist(0, musiques_ex)

    if d != 0 or len(m) != 0:
        t.fail("La fonction devrait renvoyer une playlist vide s'il n'y a pas de musique à prendre")


with TestCase("compute_optimal_playlist - Durée de la playlist", "Vérifie que la durée renvoyée correspond bien à la durée des musiques de la playlist") as t:

    d, m = P2.compute_optimal_playlist(duree_ex, musiques_ex)

    duree_playlist = sum(map(lambda mus: mus[0], m))

    if d != duree_playlist:
        t.fail(f"Mauvaise durée de playlist (renvoyée : {d} | réelle : {duree_playlist})")


with TestCase("compute_optimal_playlist - Playlist valide", "Vérifie que la durée de la playlist ne dépasse pas la capacité") as t:

    d, m = P2.compute_optimal_playlist(duree_ex, musiques_ex)

    if d > (duree_ex - 15 - 8)*60:
        t.fail(f"La playlist dure trop longtemps ({d} > ({duree_ex} - 15 - 8)*60 = {(duree_ex - 15 - 8)*60})")


with TestCase("compute_optimal_playlist - Playlist optimale", "Vérifie que la playlist renvoyée est bien la playlist optimale") as t:

    d, m = P2.compute_optimal_playlist(duree_ex, musiques_ex)

    m_parsed = set(map(lambda mus: (mus[0], mus[1].strip()), m))
    m_true = {(190, 'AC/DC - You shook me all night long'), (416, 'Iron Maiden - Afraid to shoot strangers'), (161, 'Greenday - Boulevard of broken dreams'), (253, 'Rise Against - Hero of war')}
    d_true = 1020

    if m_parsed != m_true:
        t.fail(f"La playlist renvoyée n'est pas optimale :\nPlaylist optimale : {m_true}\nPlaylist renvoyée : {m_parsed}\nMusiques manquantes : {m_true - m_parsed}\nMusiques en trop : {m_parsed - m_true}")


tests_summary()
