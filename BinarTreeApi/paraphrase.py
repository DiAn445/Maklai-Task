import random
from nltk.tree import Tree


def paraphrase(tree: Tree, limit=20) -> Tree:

    # Validate Tree obj, looking for "NP" tags
    if isinstance(tree, Tree):
        result = []
        if "NP" in str(tree).split()[0]:
            shuffler(tree)

        # Recursively reducing the obj to its minimum structure
        for chunk in tree:
            result.append(paraphrase(chunk))
        return Tree(tree.label(), result)

    # If object is string, not Tree object - appends it to tree structure as value
    else:
        return tree


def shuffler(tree: Tree) -> Tree:

    result = []
    # Iterate through each element in the tree to get a list of "NP" labels
    for i in tree:
        # First argument in tree is part of speech abbreviation
        if "NP" in str(i).split()[0]:
            result.append(i)

    # Shuffle the "NP" labels inside this tree to "paraphrase" it
    random.shuffle(result)

    # Replacing old labels with new (shuffled) ones
    for i in range(len(tree)):
        if "NP" in str(tree[i]).split()[0]:
            # So we replace chunk (by index) received it the beginning Tree by last shuffled chunk
            tree[i] = result[-1]
            result.pop(-1)
    return tree








