#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 23:00:36 2020

@author: oskars
"""

import pydot
import odoorpc
import os

odoo = odoorpc.ODOO("localhost", port=8069)
dbname = "Test"
odoo.login(dbname,"admin","admin")
#os.chdir() Enter a path to a folder whose contents you want to grep.
# For example, your Odoo addons folder.

one2many_fields = odoo.env["ir.model.fields"].search_read([("ttype","=","one2many")])
many2many_fields = odoo.env["ir.model.fields"].search_read([("ttype","=","many2many")])
many2one_fields = odoo.env["ir.model.fields"].search_read([("ttype","=","many2many")])
relational_fields = one2many_fields + many2many_fields + many2one_fields

graph = pydot.Dot(graph_type="graph")

for field in relational_fields:
    try:
        pattern = "'{}|{}'".format(field["model"], field["relation"])
        subprocess.check_output(["grep", "-rnE", pattern, "--include=*.py"])
        edge = pydot.Edge(field["model"], field["relation"], label=field["name"])
        graph.add_edge(edge)
    except:
        pass

#graph.write_svg() Enter a path to export an svg image to.