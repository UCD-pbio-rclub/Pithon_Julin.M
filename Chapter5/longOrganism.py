# Class definition for long organism
import organism


class LongOrganism(organism.Organism):
    def __init__(self, kingdom, phylum, clss, order, family, genus,
                 species, ploidy, genome_size, chromosomes):
        organism.Organism.__init__(self, kingdom, phylum, clss, order,
                               family, genus, species)
        self.ploidy = ploidy
        self.genome_size = genome_size
        self.chromosomes = chromosomes

    def ploidy(self):
        return self.ploidy

    def genome_size(self):
        return self.genome_size

    def chromosomes(self):
        return self.chromosomes

    def compare(self, other):  # compare this organism to another
        if self.chromosomes > other.chromosomes:
            print(self.latin_name(), 'has more chromosomes than',
                  other.latin_name())
        elif self.chromosomes < other.chromosomes:
            print(self.latin_name(), 'has fewer chromosomes than',
                  other.latin_name())
        else:
            print(self.latin_name(), 'and', other.latin_name(),
                  'have the same number of chromosomes')

        if self.genome_size > other.genome_size:
            print(self.latin_name(), 'has a larger genome than',
                  other.latin_name())
        elif self.genome_size < other.genome_size:
            print(self.latin_name(), 'has a smaller genome than',
                  other.latin_name())
        else:
            print(self.latin_name(), 'and', other.latin_name(),
                  'have the same genome size')

        if self.ploidy == other.ploidy:
            print(self.latin_name(), 'and', other.latin_name(),
                  'have the same ploidy')
        else:
            print(self.latin_name(), ' is ', self.ploidy, ', whereas ',
                  other.latin_name(), ' is ', other.ploidy, sep='')
