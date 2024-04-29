children = {
    "child1": {
        "name": 
            {
                "firstname" : "Emil",
                "lastname" : "Refrence",
            }
            ,"year": 2004
        },
    "child2": {
        "name": {
            "firstname": "Tobias",
            "lastname": "Refrence",
    }
        , "year": 2007
        },  
    "child3": {
        "name": {
            "firstname": "Linus",
            "lastname": "Refrence"
        }
        , "year": 2011
    }
}

print(children["child1"]["name"]["firstname"])
print(children["child2"]["year"])
children.popitem()
print(children.items())