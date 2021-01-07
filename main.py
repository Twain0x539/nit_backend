from transport.sanic.configure_sanic import configure_app



app = configure_app()



def main():
    app = configure_app()

    app.run(
        host='localhost',
        port=25565,
    )


if __name__ == '__main__':
    main()