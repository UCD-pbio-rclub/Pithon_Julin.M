# demo organism

from longOrganism import LongOrganism

Arabidopsis = LongOrganism(kingdom='Plantae',
                           phylum='Tracheophyta',
                           clss='Magnoliopsida',
                           order='Brassicales',
                           family='Brassicaceae',
                           genus='Arabidopsis',
                           species='thaliana',
                           ploidy='diploid',
                           genome_size=250,
                           chromosomes=5)

Bnapus = LongOrganism(kingdom='Plantae',
                           phylum='Tracheophyta',
                           clss='Magnoliopsida',
                           order='Brassicales',
                           family='Brassicaceae',
                           genus='Brassica',
                           species='napus',
                           ploidy='tetraploid',
                           genome_size=1200,
                           chromosomes=19)

print('The latin name of Arabidopsis is', Arabidopsis.latin_name())

print(Bnapus.latin_name(), 'has', Bnapus.chromosomes, 'chromosomes')

Arabidopsis.compare(Bnapus)
