from fastapi import FastAPI ,Body, Depends
import schemas
import models
from database import Base, engine,SessionLocal
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)


def get_session():
    session=SessionLocal()
    try:
        yield session
    finally:
        session.close()

app=FastAPI()


@app.get("/")
def getitems(session: Session=Depends(get_session)):
    '''
    args:a local session for database.
    Output: will return back all the items as a JSON list
    '''
    items =session.query(models.Item).all()
    return items


#get route
@app.get("/{id}")
def getItem(id:int ,session: Session=Depends(get_session)):
    '''
    args:a local session for database and unique id.
    Output: will return back the item with a specified id as a JSON list
    '''
    item=session.query(models.Item).get(id)
    return item

#post route
@app.post("/") #adding data to database
def addItem(item:schemas.Item, session: Session=Depends(get_session)):
    '''
    To add item in the database
    '''
    item=models.Item(location=item.location, longitude=item.longitude,latitude=item.latitude)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


#update using id:primary key
@app.put("/{id}")
def updateItem(id:int,item:schemas.Item, session: Session=Depends(get_session)):
    '''
    Update any item with the specified id.
    '''
    itemObject = session.query(models.Item).get(id)
    itemObject.location =item.location
    itemObject.longitude =item.longitude
    itemObject.latitude =item.latitude
    session.commit()
    return itemObject

#delete items using id:primary
@app.delete("/{id}")
def deleteItem(id:int,session: Session=Depends(get_session)):
    '''
    Delete any row with an unique id.
    '''
    itemObject=session.query(models.Item).get(id)
    session.delete(itemObject)
    session.commit()
    session.close()
    return f"Item corresponding to id :{id} is obsoleted"