from os import environ

SESSION_CONFIGS = [
    
    dict(
    name='my_session_config',
    display_name='Real Game Enterance',
    num_demo_participants=10,
    app_sequence=['AppGuessNum', 'guess_two_thirds'],
    num_apples=10
	),

    dict(
        name='guess_two_thirds',
        app_sequence=['guess_two_thirds'],
        num_demo_participants=10,
    ),
     dict(
        name='AppGuessNum',
        app_sequence=['AppGuessNum'],
        num_demo_participants=10,
    ),

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '5282913877038'
