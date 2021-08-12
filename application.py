from website import create_app

application = create_app()
#app.config["CLIENT_NIRS"] = "/Users/octav/Desktop/work/OliBee/Gestiune/generateNir/website/static"

if __name__ == "__main__":
    application.run(debug=True)