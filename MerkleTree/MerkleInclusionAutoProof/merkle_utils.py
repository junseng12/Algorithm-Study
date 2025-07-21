import hashlib

def hash_fn(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

def build_merkle_tree(leaves):
    tree = [leaves]
    current_level = leaves
    while len(current_level) > 1:
        next_level = []
        for i in range(0, len(current_level), 2):
            left = current_level[i]
            right = current_level[i + 1] if i + 1 < len(current_level) else left
            next_level.append(hash_fn(left + right))
        tree.append(next_level)
        current_level = next_level
    return tree
  
  
def generate_merkle_proof(tree, index):
    proof = []
    for level in tree[:-1]:
        sibling_index = index ^ 1
        # 🔧 수정: 짝이 없을 경우 자기 자신을 복제한 것으로 처리
        if sibling_index < len(level):
            sibling_hash = level[sibling_index]
        else:
            sibling_hash = level[index]  # 자기 자신 복제

        proof.append({
            "hash": sibling_hash,
            "dir": "left" if index % 2 else "right"
        })

        index //= 2
    return proof
  
def verify_merkle_proof(leaf_hash, proof, root_hash):
    current = leaf_hash
    for step in proof:
        if step["dir"] == "left":
            current = hash_fn(step["hash"] + current)
        else:
            current = hash_fn(current + step["hash"])
    return current == root_hash