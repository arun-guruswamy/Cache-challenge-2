druggability_scores = []
druggability = 0.00

with open('fpocket/data/sample/5rmm_out/5rmm_info.txt', 'rt') as fin:
    for i, line in enumerate(fin):
        if "Druggability" in line:
            for s in line.split():
                if s[0].isdigit():
                    druggability = float(s)
            druggability_scores.append(druggability)

print(druggability_scores)

mean_score = (sum(druggability_scores))/len(druggability_scores)

print(mean_score)

# 5rlh 0.024823529411764685
# 5rlz 0.042092592592592584
# 5rml 0.028157894736842087
# 5rmm 0.05464705882352941



