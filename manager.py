#! /usr/bin/env python2.7

import get5
import flask_script
import flask_migrate


manager = flask_script.Manager(get5.app)


# Database migrations
migrate = flask_migrate.Migrate(get5.app, get5.db)
manager.add_command('db', flask_migrate.MigrateCommand)


if __name__ == '__main__':
    manager.run()