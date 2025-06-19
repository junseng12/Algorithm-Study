import hashlib

def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

def merkle_tree(leaves):
    # leaf hash
    current_level = [hash_data(leaf) for leaf in leaves]
    tree = [current_level]  # 트리 각 층 저장

    while len(current_level) > 1:
        next_level = []
        for i in range(0, len(current_level), 2):
            left = current_level[i]
            right = current_level[i+1] if i+1 < len(current_level) else left
            print("Left:" + left + " " + "Right:" + right)
            combined = hash_data(left + right)
            next_level.append(combined)
        current_level = next_level
        tree.append(current_level)

    return tree

if __name__ == "__main__":
    tx_list = ["tx1", "tx2", "tx3", "tx4", "tx5"]
    tree = merkle_tree(tx_list)
    print("Merkle Root:", tree[-1][0])
    print("Tree:")
    for level in tree:
        print(level)
