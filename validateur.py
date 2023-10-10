import lxml.etree as ET
import click
import sys

@click.command()
@click.argument("rng_file")
@click.argument("xml_file")
def apply_rng(rng_file, xml_file):
	"""Applique le rng sur le XML qui vient d'être ajouté"""
	rng_doc = ET.parse(rng_file)
	rng_schema = ET.RelaxNG(rng_doc)	
	xml_doc = ET.parse(xml_file)	
	validate_bool= rng_schema.validate(xml_doc)
	if validate_bool:
		sys.exit(0)
	else:
		sys.exit(1)
        
        
if __name__=="__main__":
	apply_rng()