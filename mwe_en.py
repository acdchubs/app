# -*- coding: utf-8 -*-
import streamlit as st
import streamlit.components.v1 as cp
from PIL import Image
import base64
from pathlib import Path

import numpy  as np
import pandas as pd
import os
import time


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
    
def render_svg(svg_file,svg_title):
    with open(svg_file, "r") as f:
        lines = f.readlines()
        insvg = "".join(lines)
        decoded = base64.b64encode(insvg.encode("utf-8")).decode("utf-8")
        
        #Method-1
        #html = r'<img src="data:image/svg+xml;base64,%s"/>' % decoded
        
        #Method-2
        #html1="<img src='data:image/svg+xml;base64,{}' class='img-fluid' width='100%'>".format(decoded) 
        #html2="<figcaption>{}</figcaption>".format(svg_title)
        #html = html1 + html2
        
        #Method-3,F-string方式：F"..."，f"..."，F'...'，f'...'四种写法都可以
        html = F"<img src='data:image/svg+xml;base64,{decoded}' class='img-fluid' width='100%'><figcaption><b>{svg_title}</b></figcaption>"
        return html

#================================================================================================================================================
#Configures the default settings of the page
#This must be the first Streamlit command used in your app, and must only be set once.
#================================================================================================================================================
st.set_page_config(page_title="Power Transfer", page_icon="⚙️", layout="wide", initial_sidebar_state="expanded")


#================================================================================================================================================
#Left
#================================================================================================================================================
st.sidebar.markdown("## Topic One：Power Reciprocity")
pic = Image.open('views/DC.jpg')
st.sidebar.image(pic, caption='±800kV JianSu UHVDC',use_column_width=True)


if "counter" not in st.session_state:
    st.session_state.counter = 0
    
def increment():
    st.session_state.counter += 1

with st.sidebar:
    st.subheader(":one: JianSu UHVDC parameters(MW) &#x267A;")
    ptmin = 200  
    ptmax = 4000 
    pt    = st.number_input('UHVDC Delivery Power', ptmin, ptmax, 800, 200, "%d", help="When switched to power reciprocity mode, the sending power is controled less than 4000MW.")
    
    phmin = 100  
    phmax = 2000 
    ph    = st.slider('Power Reciprocity Settings', phmin, phmax, 400, 200, "%d", key='left_slider', on_change=increment)#, on_change = hjdf.addrows([[pt,ph,pt/2,-1*ph,(pc+ph)/2,(pc+ph)/2]]))
    
    pc    =  pt/2         # LCC
    p1    = -1.0 * ph     # VSC1
    p2    = (pc  + ph)/2  # VSC2
    p3    =  p2           # VSC3
    
    '**Power of Each Inverter**'
    '**✅LCC:**' ,  f'**:green[{pc}]**'
    '**✅VSC1:**',  f'**:red[{p1}]**'
    '**✅VSC2:**',  f'**:green[{p2}]**'
    '**✅VSC3:**',  f'**:green[{p3}]**'
   
    st.subheader(":two: Video from real-time system &#x2839;")
    show_video1 = st.sidebar.checkbox("Play power reciprocity video？", True)    
    show_video2 = st.sidebar.checkbox("Play short current test video?", False)
    widthholder = st.empty()
    
    st.markdown("---")
    st.title("About")
    st.warning(
        """
        This app is maintained by Dr. Haifeng LI.
        [AcDcHubs](https://www.github.com/acdchubs).
        """
    )

#================================================================================================================================================
#Right
#================================================================================================================================================
hidesomething = """
            <style>
              #MainMenu {visibility: hidden;}
              footer    {visibility: hidden;}
              header    {visibility: hidden;}
            </style>
            """
st.markdown(hidesomething, unsafe_allow_html=True)

header_html = F"<img src='data:image/png;base64,{img_to_bytes('views/header.png')}' class='img-fluid' width='100%'>"
st.markdown(header_html, unsafe_allow_html=True)

#///////////////////////////////////////////////////////////////////////////////////////////////////
st.subheader('')



import tkinter as tk
from tkinter import filedialog

with st.expander("**Introduction to JianSu UHVDC project**", True):
  introA_text = st.markdown(open("views/introA.md",encoding='utf-8').read(),unsafe_allow_html=True)
  st.image("views/path.jpg",caption = 'JianSu UHVDC passes through 5 provinces and cities of SiChuan, ChongQing, HuBei, AnHui and JiangSu, with a total length of 2,080 km', use_container_width = True)  
  introB_text = st.markdown(open("views/introB.md",encoding='utf-8').read(),unsafe_allow_html=True)
  icon="🔥"

with st.expander("Background of power reciprocity application", True):
  transA_text = st.markdown(open("views/transA.md",encoding='utf-8').read(),unsafe_allow_html=True)
  transA_text = st.markdown(open("views/transB.md",encoding='utf-8').read(),unsafe_allow_html=True)

#///////////////////////////////////////////////////////////////////////////////////////////////////
     
if(show_video1):
  video_filex1 = open('views/2000.mp4', 'rb')
  video_bytes1 = video_filex1.read()
  st.video(video_bytes1)
  
if(show_video2):
  DEFAULT_WIDTH = 80
  video_filex2 = open('views/v.mp4', 'rb')
  video_bytes2 = video_filex2.read()
  
  width = widthholder.slider(label="**Adjust Video Width**", min_value=0, max_value=100, value=DEFAULT_WIDTH, format="%d%%")
  width = max(width, 0.01)
  side  = max((100 - width) / 2, 0.01)
  _, container, _ = st.columns([side, width, side])
  container.video(data=video_bytes2)

