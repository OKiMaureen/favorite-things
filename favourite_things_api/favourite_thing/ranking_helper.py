def reorder_rankings_subtract(instance):
    for item in instance:
        item.ranking -= 1
        item.save()
