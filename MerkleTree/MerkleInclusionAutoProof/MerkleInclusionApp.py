from merkle_utils import *

# 1. 데이터 파일 불러오기
with open("data_sample.txt", "r") as f:
    data = [line.strip() for line in open("data_sample.txt", encoding="utf-8").readlines()]

# 2. Merkle Tree 생성
leaves = [hash_fn(x) for x in data]
tree = build_merkle_tree(leaves)

# 3. 각 항목에 대해 Inclusion Proof 자동 수행
with open("ProofLog.md", "w", encoding="utf-8") as log:
    log.write("# Merkle Inclusion Proof Log\n\n")
    for index, item in enumerate(data):
        leaf_hash = hash_fn(item)
        proof = generate_merkle_proof(tree, index)
        result = verify_merkle_proof(leaf_hash, proof, tree[-1][0])
        log.write(f"✅ {item} (Index {index}): {'✔️ YES' if result else '❌ NO'}\n")



print("[DEBUG] Start Merkle Proof")
for level in tree[:-1]:
    print(level)
    
    
    
