#!/usr/bin/python

import os
import csv
import sys

# Keys are the standardized field name to be used in consolidated inventory
# Values are the various field names found in the different inventory CSV provided by the acquired banks
standardized_header_mapping = {'Host Name':['Host Name','hostname','Name','Host'],
                               'IP Address': ['IP Address', 'IP', 'IPAddress'],
                               'Department': ['Department','Dept'],
                               'OS' : ['OS', 'Operating System'],
                               'Function' : ['Function']}

consolidated_records= []
# Read Inventory Files
parent_dir= "D:\\Lightsail AWS\\Python For Automation\\Python Mod 2\\Module 2 Supplemental Lab 2\\Inventories"
for filename in os.listdir(parent_dir):
    print(filename)
    with open(parent_dir + '/' + filename, 'r') as csv_file:
        csv_reader= csv.DictReader(csv_file)
        for row in csv_reader:
            print(row)
            modified_record={}
            for standard_key, standard_val in standardized_header_mapping.items():
                for rec_key, rec_val in row.items():
                    if rec_key in standard_val:
                        modified_record[standard_key] = rec_val
                        print(modified_record)
            consolidated_records.append(modified_record)

# Write modified and consolidated records into new file
with open('D:\\Lightsail AWS\\Python For Automation\\Python Mod 2\\Module 2 Supplemental Lab 2\\consolidated_inventory.csv','w') as csv_file:
    header_names=standardized_header_mapping.keys()
    writer =csv.DictWriter(csv_file, fieldnames = header_names)
    writer.writeheader()

    for rec in consolidated_records:
        writer.writerow(rec)
