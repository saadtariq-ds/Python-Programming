from prescription_data import adverse_interactions

meds_to_watch = set()

for interaction in adverse_interactions:
    # meds_to_watch = meds_to_watch.union(interaction)
    meds_to_watch.update(interaction)

print(sorted(meds_to_watch))
