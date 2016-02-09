import random
import sys

from ascii_tree import AsciiTreeVisualizer
from bintree import BinTree
from treeverifier import TreeVerifier, VerificationException


numErrors = 0
currLine = 0
lines = None
""":type : list[str]"""
linetok = None
""":type : list[str]"""
curr = None
""":type : BinTree"""
save = None
""":type : BinTree"""
currTest = None
""":type currTest: set"""
saveTest = None
""":type saveTest: set"""
headless = False


def show_tree(bt, message):
    """
    Wrapper function showing a tree on the best display possible.
    :type bt : BinTree
    :type message : str
    """
    print(message)
    AsciiTreeVisualizer(bt).show_tree()


def do_action(method_name, action, bt, test_set, num):
    """
    Does an action and displays what it's doing beforehand.

    :param method_name: valid method name to call on an
    BinTree or set.  For example "add, remove, rotateLeft
    or rotateRight".
    :type method_name: str
    :param action: A string describing what is happening. Can contain one {}
    which is replaced by 'num'.
    :type action: str
    :param bt: The BinTree to do the action on.
    :type bt: BinTree
    :param test_set: The test set to do the same operation on to test if the
    action went ok.
    :type test_set: set
    :param num: The argument to the method.
    :type num: int
    :return: Did a verification error occur?
    :rtype: bool
    """
    print()
    print(action.format(num))
    return do_quiet_action(method_name, action, bt, test_set, num)


def do_quiet_action(method_name, action, bt, test_set, num):
    """
    Does an action.

    :param method_name: valid method name to call on an
    BinTree or set.  For example "add, remove, rotate_left
    or rotate_right".
    :type method_name: str
    :param action: A string describing what is happening. Can contain one {}
    which is replaced by 'num'.
    :type action: str
    :param bt: The BinTree to do the action on.
    :type bt: BinTree
    :param test_set: The test set to do the same operation on to test if the
    action went ok.
    :type test_set: set
    :param num: The argument to the method.
    :type num: int
    :return: Did a verification error occur?
    :rtype: bool
    """
    global numErrors

    veri = TreeVerifier.get_verifier(bt)
    clone = None
    try:
        clone = bt.clone()
        method1 = getattr(bt, method_name)
        method1(num)
        if not method_name.startswith("rotate"):
            # Ugly hack, don't do rotations on SortedSets
            method2 = getattr(test_set, method_name)
            try:
                method2(num)
            except KeyError:
                # Ignore key errors when removing from set
                pass

        veri.verify(action.format(num))
        if test_set != set(bt):
            print(("Error "+action+"\n").format(num))
            print("  Current content: {}\n  Expected content: {}\n".format(bt, test_set))
            numErrors += 1
            show_tree(clone, action.format(num)+": Before")
            show_tree(bt, action.format(num)+": After")
            return True

    except VerificationException as e:
        print("Verification exception: {}\n".format(e))

        numErrors += 1
        show_tree(clone, "Before")
        show_tree(bt, "After")
        return True

    return False


def get_line():
    """
    Gets a line from the input. Returns whether there was a valid line.
    This will initialize the ``curr`` and ``linetok`` attributes.
    """
    global linetok, currLine, curr, currTest

    line = ''

    while line.startswith('#') or len(line) == 0:
        currLine += 1
        try:
            line = lines.pop(0)
        except IndexError:
            return False

        line = line.strip()

    linetok = line.split()
    first = linetok.pop(0)
    if first == "C":
        # Keep current BinTree
        pass
    elif first == "S":
        print("Reading saved tree")
        curr = save.clone()
        currTest = set(saveTest)
    elif first == "B":
        print("Creating BinTree")
        curr = BinTree()
        currTest = set()
    else:
        print("Unidentified token {} on line {}".format(first, currLine))
        exit(1)

    return True


def process():
    """
    Processes the BufferedReader for the testcases.
    """
    global curr, currTest, currLine, save, saveTest, numErrors

    error = False
    while not error and get_line():
        while not error and linetok:
            tok = linetok.pop(0)
            if tok.startswith("#"):
                break
            elif tok.startswith("+"):
                num = int(tok[1:])
                error = do_action("add", "Adding {}", curr, currTest, num)
                print(curr)
            elif tok.startswith("-"):
                num = int(tok[1:])
                error = do_action("remove", "Removing {}", curr, currTest, num)
                print(curr)
            elif tok.startswith("l"):
                num = int(tok[1:])
                error = do_action("rotate_left", "Rotating {} left", curr, currTest, num)
                print(curr)
            elif tok.startswith("r"):
                num = int(tok[1:])
                error = do_action("rotate_right", "Rotating {} right", curr, currTest, num)
                print(curr)
            elif tok == "A":
                AsciiTreeVisualizer(curr).show_tree()
            elif tok.startswith("R"):
                num = 0
                if len(tok) > 1:
                    num = int(tok[1:])

                print("Big random test")
                random_test(curr, num)
            elif tok == "%":
                print("Saving tree")
                save = curr.clone()
                saveTest = set(currTest)
            else:
                print("Unidentified token " + tok + " on line " + currLine)
                exit(1)

        AsciiTreeVisualizer(curr).show_tree()

    print("There were {} errors".format(numErrors))


def random_test(tree, seed):
    """
    :type tree: BinTree
    :type seed: int
    """
    print("Big random op:")

    if seed:
        random.seed(seed)
    else:
        random.seed()

    compare_set = set(tree)
    add_now = True

    for i in range(0, 2000):
        if i % 100 == 0:
            print(".", end='', flush=True)
        n = random.randrange(0, 100)

        if add_now:
            error = do_quiet_action("add", "Adding {}", tree, compare_set, n)
        else:
            error = do_quiet_action("remove", "Removing {}", tree, compare_set, n)

        add_now = not add_now

        if error:
            break

    print()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("Reading data from " + sys.argv[1])
        lines = open(sys.argv[1]).readlines()
    else:
        print("Usage: java adc.trees.TestTree [testfile]")
        print("Reading data from standard input")
        print("> ", end='', flush=True)
        lines = sys.stdin.readlines()

    process()
