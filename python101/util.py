__author__ = 'productiontwic'


def do_guess(guess_lst, ans_lst):
    matched_a = 0
    matched_b = 0
    for gus_key in range(len(guess_lst)):
        for ans_key in range(len(ans_lst)):
            if (guess_lst[gus_key] == ans_lst[ans_key]) & (gus_key == ans_key):
                matched_a += 1
                break
            elif guess_lst[gus_key] == ans_lst[ans_key]:
                matched_b += 1
                break
            else:
                continue
    print('{} A {} B'.format(matched_a, matched_b))
