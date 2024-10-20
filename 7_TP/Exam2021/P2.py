def load_clips_data(clips_database_filename: str) -> tuple[int, list[tuple[int, str]]]:
    f = open(clips_database_filename, "r")
    lines = f.readlines()
    L = []
    a = int(lines[0])
    for i in range(1,len(lines)):
        l = lines[i].split(',')
        x,y = int(l[0]), l[1].lstrip()
        L.append((x,y))
    res = (a,L)
    f.close()
    return res

# (40, [(190,'AC/DC - You shook me all night long'),(220,' Muse - Plug in Baby)])


def compute_optimal_playlist(flight_duration_in_minutes: int, clips: list[tuple[int, str]]) -> tuple[int, list[tuple[int, str]]]:
    if flight_duration_in_minutes <= 23:
        return (flight_duration_in_minutes, [])
    
    duree_max, playlis_max = 0, []

    for i in range(len(clips)):
        duree, nom = clips[i]

        if (duree // 60) <= flight_duration_in_minutes:
            duree_max += duree
            playlis_max.append((int(duree),nom))
            duree_c, playlis_c = compute_optimal_playlist(flight_duration_in_minutes - duree, clips[:i] + clips[i+1:])
            if duree_c > duree_max:
                duree_max, playlis_max = duree_c, playlis_c
            duree_max -= duree
            playlis_max.pop()

    return duree_max, playlis_max



if __name__ == "__main__":
    pass