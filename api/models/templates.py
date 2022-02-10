#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/7 10:14 下午
# software: PyCharm

from flask import current_app
from . import db
from .base import BaseModel
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import orm
from config.setting import config
import datetime

avatarConfig = config.avatar


class TemplatesModel(BaseModel):
    __tablename__ = 'templates'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(50), nullable=True)
    pageViews = db.Column(db.String(10), default='8888', nullable=False)
    price = db.Column(db.String(25), default='', nullable=True)
    avatar = db.Column(db.String(100), default='', nullable=False)

    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'name', 'description', 'pageViews', 'price', 'avatar']

    def __str__(self):
        return "templates(id='%s')" % self.id

    def paginate(self, page, per_page):
        return self.query.paginate(page=page, per_page=per_page, error_out=False)

    def filter_by_name(self, name):
        return self.query.filter(self.name.like("%" + name + "%")).all()

    def get(self, _id):
        return self.query.filter_by(id=_id).first()

    def add(self, user):
        db.session.add(user)
        return session_commit()

    def update(self):
        return session_commit()

    def delete(self, ids):
        # self.query.filter_by(id=id).delete()
        self.query.filter(self.id.in_(ids)).delete(synchronize_session=False)
        return session_commit()


def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        current_app.logger.info(e)
        return reason
