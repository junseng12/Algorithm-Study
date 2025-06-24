from merkle_utils import *

# 1. 원본 데이터 파일 불러오기
with open("original_data.txt", "r") as f:
   data = [line.strip() for line in f.readlines()]

# 2. Merkle Tree 생성
leaves = [hash_fn(x) for x in data]
tree = build_merkle_tree(leaves)

# 3. 업데이트 명령어 로드
with open("update_instructions.txt", "r", encoding="utf-8") as f:
    updates = [line.strip() for line in f.readlines()]

# 4. Update된 데이터에 대해 Merkle Tree 생성 및 기존 Merkle Root 와 비교
# 새로운 Proof 생성, 검증 결과 기록 자동 수행
with open("UpdateLog.md", "w", encoding="utf-8") as log:
    log.write("# Merkle State Update Log\n")
    log.write("## 각 업데이트마다 Merkle Root 변경 여부, Inclusion Proof 로그 기록\n")
    
    #i는 반복 인덱스 (0부터 시작)
    # update는 "2 melon" 같은 한 줄짜리 문자열
    for i, update in enumerate(updates):
        index, new_value = update.split(maxsplit=1)
        index = int(index) - 1

        #과거 값
        old_value = data[index]
        old_root = tree[-1][0]
        
        # 데이터 변경 및 새로운 트리 계산
        data[index] = new_value  # ✅ 업데이트 반영

        new_leaves = [hash_fn(x) for x in data]
        new_tree = build_merkle_tree(new_leaves)
        new_root = new_tree[-1][0]
        
        log.write(f"## 🔄 Update #1: Index {index} → '{new_value}'\n")
        log.write(f"- Old Value: {old_value}\n")
        log.write(f"- New Value: {new_value}\n")
        log.write(f"- Merkle Root Before (기존 루트): {old_root}\n")
        ## 새로운 Merkle 트리 계산
        log.write(f"- Merkle Root After (새 루트):  {new_root}\n")        
        log.write(f"- Root Changed: {'✅ YES' if old_root != new_root else '❌ NO'}\n\n")


    
    
