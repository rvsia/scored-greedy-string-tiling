# Scored Greedy String Tiling
An enhanced version of Greed String Tiling algorithm which allows using custom scoring functions.

* Allows to use a  custom comparison function :sparkles:
* Allows to use a scoring system to determine the best match :pencil:
* Configurable :hammer:

# Install

- TODO

#  Usage

```python
import scoredgst # TODO

arr1 = [
	'Hello', # 0
	'Jonah', # 1
	'How', # 2
	'Are', # 3
	'You', # 4
	'Today', # 5
]

arr1 = [
	'Hello', # 0
	'Jeremiah', # 1
	'How', # 2
	'Are', # 3
	'You', # 4
	'Tomorrow', # 5
]

scoredgst.token_comparison(arr1, arr2, 2)
# => [{'tok_1_pos': 2, 'tok_2_pos': 2, 'length': 3, 'score': 3}]
```
**tok_1_pos** - a position of token in the first array of the match

**tok_2_pos** - a position of token in the second array of the match

**length** - a length of the match

**score** - a score of the match

**score_array** - see a API

## API

```python
def token_comparison(	tokens1,
			tokens2, 
			minimal_match = 5,
			threshold = 1, 
			compare_function = compare_words, 
			score_array = False, 
			use_score = False)
```

**tokens1, tokens2** [arrays] - array of tokens (please, use custom preproccesing to obtain these arrays!)

**minimal_match** [integer] - minimal length of a match

**threshold** [number] - decides (based on a return of compare_function) if algorithm should continue comparing a sequence (use with custom functions) (includes the threshold value!)

**compare_function** [function] - a function which takes two inputs (token1 and token2) and returns their similiarity in range 0-1 (0 - different, 1 - the same)

**score_array** [boolean] - will append to the result array scores of each pair in the match

```python
[{'tok_1_pos': 2, 'tok_2_pos': 2, 'length': 3, 'score': 3, 'score_array': [1, 1, 1]}]
```

**use_score** [boolean] - will use a score to find higher matches (normally, the algorithm will choose the longest match of all, with this option on, it will choose a match with the highest score)

# Todo
- [X] Algorithm
- [X] Docs
- [ ] Tests
- [ ] PIP release

# Based on

[1] Wise, Michael. (1993). String Similarity via Greedy String Tiling and Running Karp−Rabin Matching. Unpublished Basser Department of Computer Science Report. 

[2] VŠIANSKÝ, Richard. Rozpoznávání podobností zdrojových kódů jazyka PHP v systému Anton [online]. Brno, 2017 [cit. 2019-03-10]. Available from: <https://theses.cz/id/9w9lvn/>. Bachelor's thesis. Mendelova univerzita v Brně, Faculty of Business and Economics. Thesis supervisor Ing. Dita Dlabolová.
