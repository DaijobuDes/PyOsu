import requests
import os


os.system('cls')
# Please place you osu api key.
# Request it here https://osu.ppy.sh/p/api/
apikey = 'apikeyhere'

data = []


def getuser(user: str, mode=0):
    URL = 'https://osu.ppy.sh/api/get_user'
    params = {
        'k': apikey,
        'u': user,
        'm': mode
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

        username = data[0]['username']
        user_id = data[0]['user_id']
        join_date = data[0]['join_date']
        c300 = data[0]['count300']
        c100 = data[0]['count100']
        c50 = data[0]['count50']
        playcount = data[0]['playcount']
        country = data[0]['country']
        pp_raw = data[0]['pp_raw']
        accuracy = data[0]['accuracy']
        global_rank = data[0]['pp_rank']
        local_rank = data[0]['pp_country_rank']
        ssh = data[0]['count_rank_ssh']
        ss = data[0]['count_rank_ss']
        sh = data[0]['count_rank_sh']
        s = data[0]['count_rank_s']
        a = data[0]['count_rank_a']

        try:
            print(f'-------------------- User details of {username} ({mode_str}) --------------------')
            print(f'{username} ({user_id}) from {country}')
            print(f'Join date: {join_date}')
            print('\n')
            print(f'https://osu.ppy.sh/users/{user_id}/{mlink}')
            print('\n')
            print(f'-------------------- User stats of {username} ({mode_str}) --------------------')
            print(f'   300\'s: **{c300}**')
            print(f'   100\'s: *{c100}*')
            print(f'    50\'s: {c50}')
            print(f'       PP: **{pp_raw}**')
            print(f'Playcount: {playcount}')
            print(f' Accuracy: {accuracy[:5]}%')
            print(f'   Global: {global_rank}')
            print(f'  Country: {local_rank}')

            all_ss = int(ssh)+int(ss)
            all_s = int(sh) + int(s)
            all_a = int(a)
            total_ranks = all_ss+all_s+all_a

            ss_rate = (all_ss/total_ranks)*100
            s_rate = (all_s/total_ranks)*100
            a_rate = all_a/total_ranks*100

            print('\n')
            print(f'-------------------- User ranks of {username} ({mode_str}) --------------------')
            print(f'    SSH/SS: {ssh}/{ss}')
            print(f'      SH/S: {sh}/{s}')
            print(f'         A: {a}')
            print(f'   SS Rate: {str(ss_rate)[:5]}%')
            print(f'    S Rate: {str(s_rate)[:5]}%')
            print(f'    A Rate: {str(a_rate)[:5]}%')
        except ZeroDivisionError:
            print('\n')
            print(f'-------------------- User ranks of {username} ({mode_str}) --------------------')
            print('n division by zero occurred')
            print('Probably user doesn\'t have enough plays or ranks')
        except TypeError:
            print('\n')
            print(f'-------------------- User ranks of {username} ({mode_str}) --------------------')
            print('None')


def main():
    try:
        choice = None
        while choice != 'n':
            username = input("Enter username: ")
            try:
                mode = int(input("Enter mode (leave blank for standard): "))
            except ValueError:
                mode = 0
            getuser(username, mode)
            choice = input("\n\nEnter again? (y/n): ")
            if choice == 'y':
                os.system('cls')
    except KeyboardInterrupt:
        print('\n\nUser cancelled operation')
    except IndexError:
        print('\n\nYou didn\'t supply a username.')
        main()


main()
