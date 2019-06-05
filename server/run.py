from app import create_app
# from app import settings

app = create_app()

if __name__ =='__main__':
    app.run(
        # host=settings.BIND_HOST,
        # port=settings.BIND_PORT,
        # debug=settings.DEBUG,
        host="localhost",
        port=5000,
        debug=True,
    )


