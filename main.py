#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2019 zahirjunejo <zahirjunejo@zahirjunejo-Inspiron-1564>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sys
import pandas as pd
from sqlalchemy import create_engine

def main():
	#demoDF = pd.read_csv('demo.csv')
	demoDF = pd.read_csv(str(sys.argv[1]))
	engine = create_engine('sqlite:///demo.db', echo=False)
	demoDF.to_sql('users', con=engine, if_exists = 'replace')
	print str(len(demoDF.index)) + " records inserted successfully."
	return 0

if __name__ == '__main__':
	print "This is the name of the script: ", sys.argv[0]
	print "Number of arguments: ", len(sys.argv)
	print "The arguments are: " , str(sys.argv)
	main()
	

