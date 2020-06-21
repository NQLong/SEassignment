from app import app, Base,engine

Base.metadata.create_all(engine)
app.run(debug = True)
