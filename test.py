from vcf_parser import VCFParser

my_parser = VCFParser(infile='00001.vcf', split_variants=True, check_info=True)

for variant in my_parser:
    print(variant)
