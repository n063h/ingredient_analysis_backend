from ingredient_analysis_backend import app
import ingredient_analysis_backend.setting as Config

if __name__ == '__main__':
    app.run(host=Config.FLASK_HOST,port=Config.FLASK_PORT,debug=True)