import hashlib

def hash_fn(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

# 1. Merkle Tree 구성 함수
def build_merkle_tree(leaves):
    tree = [leaves]
    current_level = leaves
    while len(current_level) > 1:
        next_level = []
        for i in range(0, len(current_level), 2):
            left = current_level[i]
            right = current_level[i + 1] if i + 1 < len(current_level) else left
            combined = hash_fn(left + right)
            next_level.append(combined)
        tree.append(next_level)
        current_level = next_level
    return tree

# 2. Merkle Proof 생성 함수 (✅ 여기에 집중!)
def generate_merkle_proof(tree, index):
    proof = []
    # 왜 레벨을 기준으로 처리하는가? : 매 층을 “한 번에” 처리해 트리 깊이를 자연스럽게 줄이며 루트까지 상승하기 위해.
    for level in tree[:-1]:  # 루트 제외
        sibling_index = index ^ 1  # 0<->1, 2<->3 ...
        #✔ 핵심
        # sibling_index 가 배열 범위를 벗어나면(== len(level)) → “짝이 없다” → 자기 해시 복제 규칙 적용
        # > 상황은 0-based 인덱스 특성상 실질적으로 발생하지 않음.
        if sibling_index < len(level):
            proof.append({
                "hash": level[sibling_index],
                "dir": "left" if sibling_index < index else "right"
            })
        index //= 2
    return proof

# 3. Merkle Proof 검증 함수
def verify_merkle_proof(leaf_hash, proof, root_hash):
    current = leaf_hash
    for step in proof:
        if step["dir"] == "left":
            current = hash_fn(step["hash"] + current)
        else:
            current = hash_fn(current + step["hash"])
    return current == root_hash

# 💡 실행 테스트
if __name__ == "__main__":
    data = ["a", "b", "c", "d"]
    leaves = [hash_fn(x) for x in data]
    tree = build_merkle_tree(leaves)

    index = 2  # 'c'
    proof = generate_merkle_proof(tree, index)
    result = verify_merkle_proof(leaves[index], proof, tree[-1][0])

    print("Merkle Root:", tree[-1][0])
    print("Proof for index 2:", proof)
    print("Verification result:", result)
