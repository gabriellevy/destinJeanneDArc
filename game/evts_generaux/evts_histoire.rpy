init -5 python:
    import random
    from abs.religions import religion
    from spe import dec_jea
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import metier

    def AjouterEvtsHistoire():
        global selecteur_
        # Concile d'Orléans
        #concileOrleans = dec_jea.DecJeanneU(proba.Proba(0.03, True), "concileOrleans", 511)
        #selecteur_.ajouterDeclencheur(concileOrleans)

#label concileOrleans:
#    "Vous organisez le premier concile qui ait eu lieu en Gaule. Il aura lieu à Orléans."
#    jump fin_cycle
