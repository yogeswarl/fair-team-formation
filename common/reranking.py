import reranking

def reranking_logic(item_attributes,distribution_list,author_count):
    rerank_indices = reranking.rerank(
            item_attributes,  # attributes of the ranked items
            distribution_list,  # desired item distribution
            max_na=None,  # controls the max number of attribute categories applied
            k_max=None,  # length of output, if None, k_max is the length of `item_attribute`
            algorithm="det_cons",  # "det_greedy", "det_cons", "det_relaxed", "det_const_sort"
            verbose=False,
        )
    print(rerank_indices[:author_count])
    item_attribute_reranked = [item_attributes[i] for i in rerank_indices]
    before = reranking.ndkl(item_attributes,distribution_list)
    after = reranking.ndkl(item_attribute_reranked, distribution_list)
    print(f"{before:.3f}, {after:.3f}")