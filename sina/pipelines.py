# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, create_engine, Text, DateTime, String, Integer
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Data(Base):
    __tablename__ = 'data'
    id = Column(Integer(), primary_key=True)
    times = Column(DateTime)
    title = Column(Text())
    content = Column(Text())
    type = Column(Text())


class SinaPipeline:
    def __init__(self):
        self.engine = create_engine('mysql+pymysql://root:123456@localhost:3306/sina2', encoding='utf-8')
        Base.metadata.create_all(self.engine)
        self.DBSession = sessionmaker(bind=self.engine)

    def process_item(self, item, spider):
        new = Data()
        new.title = item['title']
        new.times = item['times']
        new.content = item['desc']
        new.type = item['type']
        session = self.DBSession()
        session.add(new)
        session.commit()
        return item
