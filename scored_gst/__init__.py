def prepare_marks(tokens): # creates array with marked tokens
    tokens_arr = []
    for token in tokens:
        tokens_arr.append([token, False]) # marked as not compared
    return tokens_arr

def compare_words(word1, word2): # compare two words, should return 0 - 1
    return 1 if word1 == word2 else 0

def compare_tokens(n1, n2, tokens1, tokens2, compare_function): # compare two tokens
    try:
        if tokens1[n1][1] == tokens2[n2][1] == False: # both token are unmatched
            return compare_function(tokens1[n1][0], tokens2[n2][0])
    except IndexError: # do not check overflown values
        return False
    return False

def check_matches(matches, n1, n2): # check if matches are not overlaping
    # matches[1,2,3]: 1 pos of X token, 2 pos of Y token, 3 length of the match
    for n3, match in enumerate(matches):
        if (n1 >= match[0] and n1 <= match[0] + match[2] - 1) or (n2 >= match[1] and n2 <= match[1] + match[2] - 1):
            return False
    return True

# tokens1, tokens2 = ['string', .... ]
# minimal match - minimal number of tokens in a match
# treshold (includes) - treshold decides if match should continue
# compare function - def func(value 1, value 2) returns 0-1 (1 - match, 0 - no match)
def token_comparison(tokens1, tokens2, minimal_match = 5, threshold = 1, compare_function = compare_words, score_array = False, use_score = False):
    tiles = []
    switched = False
    tokens1_arr = prepare_marks(tokens1)
    tokens2_arr = prepare_marks(tokens2)
    if len(tokens2_arr) < len(tokens1_arr): # optimalization - shorter array should be base for comparison
        tokens1_arr, tokens2_arr = tokens2_arr, tokens1_arr
        switched = True
    maxMin = True
    while maxMin:
        max_match = minimal_match
        matches = []
        for n1, [token1, match1] in enumerate(tokens1_arr):
            if not match1:
                for n2, [token2, match2] in enumerate(tokens2_arr):
                    if not match2:
                        sim_result = 0
                        com_result = 0
                        if score_array:
                            score_arr = []
                        else:
                            score_arr = None
                        comparison_result = compare_tokens(n1, n2, tokens1_arr, tokens2_arr, compare_function)
                        while comparison_result >= threshold:
                            sim_result += 1
                            com_result += comparison_result
                            if score_array:
                                score_arr.append(comparison_result)
                            comparison_result = compare_tokens(n1 + sim_result, n2 + sim_result, tokens1_arr, tokens2_arr, compare_function)
                        if use_score:
                            if com_result == max_match:
                                if check_matches(matches, n1, n2):
                                    matches.append([n1, n2, sim_result, com_result, score_arr])
                            elif com_result > max_match:
                                max_match = com_result
                                matches = [[n1, n2, sim_result, com_result, score_arr]]
                        else:
                            if sim_result == max_match:
                                if check_matches(matches, n1, n2):
                                    matches.append([n1, n2, sim_result, com_result, score_arr])
                            elif sim_result > max_match:
                                max_match = sim_result
                                matches = [[n1, n2, sim_result, com_result, score_arr]]

        for match in matches: # Match matched tokens
            for token_pos in range(0,match[2]):
                tokens1_arr[match[0] + token_pos][1] = True # marks as compared
                tokens2_arr[match[1] + token_pos][1] = True # marks as compared
            tile = {
                'tok_1_pos': match[0],
                'tok_2_pos': match[1],
                'length': match[2],
                'score': match[3],
            }
            if score_array:
                tile['score_array'] = match[4]
            tiles.append(tile)

        if max_match <= minimal_match:
            maxMin = False

    if switched: # reverse to original order
        for tile in tiles:
            tile['tok_1_pos'], tile['tok_2_pos'] = tile['tok_2_pos'], tile['tok_1_pos']
    return tiles

def test():
    arr1 = [
        'Ahoj', # 0
        'Pepo',
        'Jak', # 2
        'Je',
        'Jak',
        'Je', # 7
    ]

    arr2 = [
        'Ahoj', # 0
        'Hozo',
        'Jak',
        'Je',
        'Ahoj',
        'Pepo',
        'Jak',
        'Je', # 7
        'Auto',
    ]

    def score_comparison(word1, word2):
        if word2 == 'Pepo':
            return 2
        if len(word1) == len(word2) == 4:
            return 1
        return 0

    import json

    # print(token_comparison(arr1, arr2, minimal_match=2))
    # print(json.dumps(token_comparison(arr1, arr2, 2), indent = 2))
    print(json.dumps(token_comparison(arr1, arr2, 2, compare_function=score_comparison, use_score=False), indent = 2))
    print(json.dumps(token_comparison(arr1, arr2, 2, compare_function=score_comparison, use_score=True), indent = 2))
    # print(token_comparison(arr1, arr2, 4))
    # print(token_comparison(arr2, arr1, 4))
