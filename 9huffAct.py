#1-----Huffman coding--------
import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    frequency = Counter(text)

    heap = [
        HuffmanNode(char, freq)
        for char, freq in frequency.items()
    ]

    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)

    return heap[0] if heap else None


def generate_codes(root, current_code="", codes=None):
    if codes is None:
        codes = {}

    if root is None:
        return codes

    if root.char is not None:
        codes[root.char] = current_code or "0"
        return codes

    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)

    return codes


text_input = "hello huffman"

tree_root = build_huffman_tree(text_input)
huffman_codes = generate_codes(tree_root)

print("Huffman Codes Mapping:")

for character, binary_code in huffman_codes.items():
    print(repr(character) + ":", binary_code)




#2-------Activity Selection------------
def activity_selection(start, finish):
    n = len(start)

    activities = []

    for i in range(n):
        activities.append((start[i], finish[i], i + 1))

    activities.sort(key=lambda x: x[1])

    selected = []

    selected.append(activities[0])

    last_finish = activities[0][1]

    for i in range(1, n):
        if activities[i][0] >= last_finish:
            selected.append(activities[i])
            last_finish = activities[i][1]

    return selected


start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

result = activity_selection(start, finish)

print("Selected Activities:")

for activity in result:
    print("Activity", activity[2],
          "Start:", activity[0],
          "Finish:", activity[1])

print("Maximum Activities:", len(result))
