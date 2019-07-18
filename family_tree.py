ada_family = { 'Judith Blunt-Lytton': ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt'],
              'Ada King-Milbanke': ['Ralph King-Milbanke', 'Fanny Heriot'],
              'Ralph King-Milbanke': ['Augusta Ada King', 'William King-Noel'],
              'Anne Isabella Blunt': ['Augusta Ada King', 'William King-Noel'],
              'Byron King-Noel': ['Augusta Ada King', 'William King-Noel'],
              'Augusta Ada King': ['Anne Isabella Milbanke', 'George Gordon Byron'],
              'George Gordon Byron': ['Catherine Gordon', 'Captain John Byron'],
              'John Byron': ['Vice-Admiral John Byron', 'Sophia Trevannion'] }

def ancestors(genealogy, person):
    L=[]
    if person not in genealogy:
        return []
    else:
        L.append(genealogy[person][0])
        L.append(genealogy[person][1])
        return L+ancestors(genealogy, L[0])+ancestors(genealogy, L[1])



print ancestors(ada_family, 'Augusta Ada King')

print ancestors(ada_family, 'Judith Blunt-Lytton')

print ancestors(ada_family, 'Dave')
