import requests
import os


os.system('cls')
# Please place you osu api key.
# Request it here https://osu.ppy.sh/p/api/
apikey = 'apikeyhere'

data = []


def get_top_play(user: str, mode=0, limit=3):
    URL = 'https://osu.ppy.sh/api/get_user_best'
    params = {
        'k': apikey,
        'u': user,
        'm': mode,
        'limit': limit
    }

    if mode == 0:
        mode_str = 'Standard'
        mlink = 'osu'
    elif mode == 1:
        mode_str = 'Taiko'
        mlink = 'taiko'
    elif mode == 2:
        mode_str = 'Catch The Beat'
        mlink = 'catch'
    elif mode == 3:
        mode_str = 'Mania'
        mlink = 'mania'
    else:
        pass

    if mode < 0 or mode > 4 or user is None:
        print('Invalid mode.')
    else:
        resp = requests.get(
            URL,
            params=params,
            verify=True,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44"
            }
        )

        data = resp.json()

        print(f'-------------------- User best of {user} ({mode_str}) --------------------')

        for i in range(0, limit):
            beatmap_id = data[i]['beatmap_id']
            score = data[i]['score']
            maxcombo = data[i]['maxcombo']
            c50 = data[i]['count50']
            c100 = data[i]['count100']
            c300 = data[i]['count300']
            cmiss = data[i]['countmiss']
            ckat = data[i]['countkatu']
            cgek = data[i]['countgeki']
            perfect = data[i]['perfect']
            enabled_mods = data[i]['enabled_mods']
            play_date = data[i]['date']
            rank = data[i]['rank']
            pp = data[i]['pp']
            replay = data[i]['replay_available']

            URL2 = 'https://osu.ppy.sh/api/get_beatmaps'
            params = {
                'k': apikey,
                'b': beatmap_id
            }

            resp2 = requests.get(
                URL2,
                params=params,
                verify=True
            )

            data2 = resp2.json()

            print(f'Array {i+1}')
            print(f"Beatmap Title: {data2[0]['artist']} - {data2[0]['title']}")
            print(f'https://osu.ppy.sh/b/{beatmap_id}')
            print(f"Difficulty: {data2[0]['difficultyrating']} stars ({data2[0]['version']})")
            print(f'Play Date: {play_date}')
            print(f'Rank: {rank}')
            print(f"Score: {score}")
            print(f'Max Combo: {maxcombo}')
            print(f'PP: {pp}')

            if replay == 1:
                repl = 'Yes'
            else:
                repl = 'No'

            if perfect == 1:
                perf = 'Yes'
            else:
                perf = 'No'

            print(f'Is Full Combo?: {perf}')
            print(f'Replay Available?: {repl}')               

            if mode == 0:
                print(f'300/100/50/X: {c300}/{c100}/{c50}/{cmiss}')
            elif mode == 1:
                print(f'300/100/50/X: {c300}/{c100}/{c50}/{cmiss}')
                print(f'Kats/Gekis: {ckat}/{cgek}')
            elif mode == 2:
                print(f'Fruits/Ticks/DMiss/Miss: {c300}/{c100}/{c50}/{cmiss}')
            elif mode == 3:
                print(f'320/300/200/100/50/X: {cgek}/{c300}/{ckat}/{c100}/{c50}/{cmiss}')

            print('--------------------------------------------------')


def main():
    try:
        choice = None
        while choice != 'n':
            username = input("Enter username: ")
            try:
                mode = int(input("Enter mode (leave blanks for standard): "))
            except ValueError:
                mode = 0
            get_top_play(username, mode, 3)
            choice = input("\n\nEnter again? (y/n): ")
            if choice == 'y':
                os.system('cls')
    except KeyboardInterrupt:
        print('\n\n User cancelled operation')
    except IndexError:
        print('You didn\'t supply a username or it does not exist')
        main()


main()
