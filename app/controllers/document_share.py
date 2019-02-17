#!/usr/bin/env python
#coding:utf-8
from flask import Flask, Blueprint, render_template, request, flash, session, redirect, url_for, g

document_share = Blueprint(
    'document_share',
    __name__,
    # template_folder='templates/document_share'
)
@document_share.route('/detailedu', methods=['GET', 'POST'])
def detailedu():
    return render_template('detailedu.html')

@document_share.route('/detailtest', methods=['GET', 'POST'])
def detailtest():
    return render_template('detailtest.html')

@document_share.route('/detailreport', methods=['GET', 'POST'])
def detailreport():
    return render_template('detailreport.html')

@document_share.route('/detailppt', methods=['GET', 'POST'])
def detailppt():
    return render_template('detailppt.html')

@document_share.route('/detaillaw', methods=['GET', 'POST'])
def detaillaw():
    return render_template('detaillaw.html')

@document_share.route('/detailjob', methods=['GET', 'POST'])
def detailjob():
    return render_template('detailjob.html')
