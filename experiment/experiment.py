import reranking
item_attributes = [2,1,2,0]
distribution_list = {1: 0.3,2: 0.5, 0:0.2}
rerank_indices = reranking.rerank(
            item_attributes,
            distribution_list,
            max_na=None,
            k_max=None,
            algorithm="det_greedy",
            verbose=False,
        )

item_attribute_reranked = [item_attributes[i] for i in rerank_indices]
print(item_attribute_reranked)
# before = reranking.ndkl(item_attributes,distribution_list)
# after = reranking.ndkl(item_attribute_reranked, distribution_list)
before_ndcg = reranking.ndcg_diff(item_attributes)
after_ndcg = reranking.ndcg_diff(item_attribute_reranked)
# print(f"{before:.3f}, {after:.3f}")
print(f"{before_ndcg:.3f}, {after_ndcg:.3f}")