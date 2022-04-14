import reranking
from common import author
from collections import Counter
def reranking_logic(item_attributes,distribution_list,author_count,length_of_qualified_authors,list_of_author_id):
    rerank_indices = reranking.rerank(
            item_attributes,
            distribution_list,
            max_na=None,
            k_max=None,
            algorithm="det_greedy",
            verbose=False,
        )
    item_attribute_reranked = [item_attributes[i] for i in rerank_indices]
    print(f"reranking list of items: {item_attribute_reranked[:author_count]}" )
    before = reranking.ndkl(item_attributes,distribution_list)
    after = reranking.ndkl(item_attribute_reranked, distribution_list)
    before_ndcg = reranking.ndcg_diff(item_attributes)
    after_ndcg = reranking.ndcg_diff(item_attribute_reranked)
    print(f"NDKL before reranking: {before:.3f}, NDKL after reranking: {after:.3f}")
    print(f"NDCG before reranking {before_ndcg:.3f}, NDCG after reranking  {after_ndcg:.3f}")
    print(f"infeasible metric: {reranking.infeasible(item_attributes,distribution_list)}")
    print(f"reranked infeasible metric : {reranking.infeasible(item_attribute_reranked, distribution_list)}")
    for i in item_attributes:
        print(reranking.skew(float((item_attributes.count(i)/author_count)),float((list_of_author_id.count(i)/length_of_qualified_authors))))