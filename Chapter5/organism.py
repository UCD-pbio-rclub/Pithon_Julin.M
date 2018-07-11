# Class definition for organism


class Organism:
    def __init__(self, kingdom, phylum, clss, order, family, genus, species):
        self.kingdom = kingdom
        self.phylum = phylum
        self.clss = clss
        self.order = order
        self.family = family
        self.genus = genus
        self.species = species

    def taxonomy(self):
        return self.kingdom, self.phylum, self.clss, self.order, self.family,\
         self.genus, self.species

    def latin_name(self):
        return self.genus + ' ' + self.species
