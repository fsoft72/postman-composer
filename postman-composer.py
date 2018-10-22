#!/usr/bin/env python

# =====================================================
# Postman Composer v0.1
#
# Written by Fabio Rotondo (fabio.rotondo@gmail.com)
#
# (C)Copyright 2018 OS3 srl  (https://www.os3.it)
#
# Released under the GNU GPLv2
# =====================================================

"""
Postman Composer 
"""

import json

VERSION = "0.1"

class PostmanComposer ( object ):
	"""
	PostmanComposer class

	The PC merges two or more Postman files into one single Postman collection
	"""
	def __init__ ( self, name ):
		self.data = {
				"info" : { 
					"name" : name,
					"schema" : "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
				},
				"item" : []
		}

	def add ( self, fname ):
		"""
		add ( fname )

		Parses the Postname file specified by ``fname`` and adds the elements to the new file
		"""
		data = json.load ( open ( fname ) )
		
		res = {
			"name" : data [ 'info' ] [ 'name' ],
			"item" : data [ 'item' ]
		}

		self.data [ 'item' ].append ( res )

	def save ( self, fname ):
		"""
		save ( fname )

		Saves the new Postman file into ``fname``.
		If ``fname`` does not contains the ``.json`` suffix, it will be added along with "postman_collection.json"
		"""
		if fname.find ( ".json" ) <= 0:
			fname = "%s.postman_collection.json" % fname

		open ( fname, "w" ).write ( json.dumps ( self.data, indent=4 ) )

if __name__ == '__main__':
	import argparse

	args = argparse.ArgumentParser ( "Postman Composer v%s" % VERSION )
	args.add_argument ( "-n", "--name",   type=str, help = 'the collection name' )
	args.add_argument ( "-o", "--output", type=str, help = 'the output file to be created')
	args.add_argument ( "files", nargs='*', type=str, help= 'Files to be included in the final collection')

	res = args.parse_args ()

	p = PostmanComposer ( res.name )

	for n in res.files:
		p.add ( n )

	p.save ( res.output )