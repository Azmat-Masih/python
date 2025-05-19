# Write a python function to remove the word from the list and strip at the same the time.


# this is not working proporly # 


def rem(list_,word_):
    n = []
    for item in list_:
        if not(item == word_):
            n.append(item.strip(word_))
        # list_.remove(word_)
    
    return n
    


list_ = ["hairry", "saim", "David", "brain"]


print(rem(list_, "ai"))