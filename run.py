from main import create_app
from src.config.config import DevelopmentConfig

if __name__ == "__main__":
  create_app(DevelopmentConfig).run()