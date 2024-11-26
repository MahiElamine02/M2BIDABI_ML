# Créer une fonction à partir de la cellule d'en haut
def sets_creation(df,first_threshold, ratio):
    
    # Simple
    training_set = df[:first_threshold]
    test_set = df[first_threshold:]
    
    # Dynamical
    training_set_treshold = int(len(df)*ratio)
    training_set = df[:training_set_treshold]
    test_set = df[training_set_treshold:]

    print("training_set size", len(training_set))
    print("test_set size", len(test_set))

    return training_set, test_set
    