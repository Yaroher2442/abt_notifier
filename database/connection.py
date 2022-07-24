from tortoise import Tortoise, run_async

from config.config import DbConfig


async def init(conf: DbConfig):
    # Here we create a SQLite DB using file "db.sqlite3"
    #  also specify the app name of "models"
    #  which contain models from "app.models"
    await Tortoise.init(
        db_url=conf.db_url,
        modules={'models': ['database.models']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()
