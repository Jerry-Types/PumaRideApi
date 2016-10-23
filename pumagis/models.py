from django.db import models
import sys
from qgis.core import *
from qgis.networkanalysis import *
import os

import sys
import socket

import path_server

def sendRequest(a_x, a_y, b_x, b_y):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 8011))

    message = "%s %s %s %s" % (a_x, a_y, b_x, b_y)

    path_server.replyWith(sock, message)
    reply = path_server.recieveMessage(sock)

    return(reply)


class Point(models.Model):
	name= models.CharField(max_length=500)
	lon=models.FloatField(default=0.0)
	lat=models.FloatField(default=0.0)

	class Meta:
		verbose_name = "Point"
        verbose_name_plural = "Points"
        
	def __str__(self):
		return self.name


class Line(models.Model):
	name= models.CharField(max_length=500)
	p_origen=models.CharField(max_length=50,default="(0.0,0.0)")
	p_destino=models.CharField(max_length=50,default="(0.0,0.0)")

	class Meta:
		verbose_name = "Line"
        verbose_name_plural = "Lines"
        
	def __str__(self):
		return self.name

	
	@property
	def shortest_path(self):
		a_lat=float(self.p_origen.split(",")[0].split("(")[1])
		a_lon=float(self.p_origen.split(",")[1].split(")")[0])
		b_lat=float(self.p_destino.split(",")[0].split("(")[1])
		b_lon=float(self.p_destino.split(",")[1].split(")")[0])
		#print a_lat,a_lon,b_lat,b_lon
		poly_line=sendRequest(a_lat,a_lon,b_lat,b_lon)
		return poly_line		