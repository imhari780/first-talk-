# from datetime import timedelta
# from pathlib import Path

# # ===============================
# # BASE DIR
# # ===============================
# BASE_DIR = Path(__file__).resolve().parent.parent


# # ===============================
# # SECURITY
# # ===============================
# SECRET_KEY = "django-insecure-@jmu0vu7k@e&+)+lfn_^v_axl09u(q*lkcnt=%jb7-(asc3@2k"
# DEBUG = True
# ALLOWED_HOSTS = []


# # ===============================
# # APPLICATIONS
# # ===============================
# INSTALLED_APPS = [
#     "django.contrib.admin",
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.sessions",
#     "django.contrib.messages",
#     "django.contrib.staticfiles",
#     "rest_framework_simplejwt",
#     # DRF
#     "rest_framework",
#     # YOUR SERVICES
#     "auth_service",
#     "room_gateway",
#     "chat_service",
#     "moderation_service",
#     "dialogue_service",
#     "memory_service",
#     "audio_broadcast",
#     "response_engine",
# ]


# # ===============================
# # MIDDLEWARE
# # ===============================
# MIDDLEWARE = [
#     "django.middleware.security.SecurityMiddleware",
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
# ]


# # ===============================
# # URL & WSGI
# # ===============================
# ROOT_URLCONF = "core.urls"

# WSGI_APPLICATION = "core.wsgi.application"


# # ===============================
# # TEMPLATES
# # ===============================
# TEMPLATES = [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         "DIRS": [],
#         "APP_DIRS": True,
#         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#             ],
#         },
#     },
# ]


# # ===============================
# # DATABASE
# # ===============================
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }


# # ===============================
# # PASSWORD VALIDATION
# # ===============================
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
#     },
#     {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
#     {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
#     {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
# ]


# # ===============================
# # INTERNATIONALIZATION
# # ===============================
# LANGUAGE_CODE = "en-us"
# TIME_ZONE = "UTC"
# USE_I18N = True
# USE_TZ = True


# # ===============================
# # STATIC FILES
# # ===============================
# STATIC_URL = "/static/"


# # ===============================
# # DEFAULT AUTO FIELD
# # ===============================
# DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# AUTH_USER_MODEL = "auth_service.User"


# # ===============================
# # 🔐 DJANGO REST FRAMEWORK (JWT CONFIG)
# # ===============================
# REST_FRAMEWORK = {
#     "DEFAULT_AUTHENTICATION_CLASSES": [
#         "rest_framework_simplejwt.authentication.JWTAuthentication",
#     ],
#     "DEFAULT_PERMISSION_CLASSES": [
#         "rest_framework.permissions.IsAuthenticated",
#     ],
# }


# # ===============================
# # 🔐 SIMPLE JWT SETTINGS
# # ===============================
# SIMPLE_JWT = {
#     "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
#     "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
#     "AUTH_HEADER_TYPES": ("Bearer",),
#     "USER_ID_FIELD": "user_id",
#     "USER_ID_CLAIM": "user_id",
# }

# ASGI_APPLICATION = "core.asgi.application"

# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels.layers.InMemoryChannelLayer",
#     }
# }
from datetime import timedelta
from pathlib import Path


# ===============================
# BASE DIR
# ===============================
BASE_DIR = Path(__file__).resolve().parent.parent


# ===============================
# SECURITY
# ===============================
SECRET_KEY = "django-insecure-@jmu0vu7k@e&+)+lfn_^v_axl09u" "(q*lkcnt=%jb7-(asc3@2k"
DEBUG = True
ALLOWED_HOSTS = []


# ===============================
# APPLICATIONS
# ===============================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework_simplejwt",
    # DRF
    "rest_framework",
    # YOUR SERVICES
    "auth_service",
    "room_gateway",
    "chat_service",
    "moderation_service",
    "dialogue_service",
    "memory_service",
    "audio_broadcast",
    "response_engine",
]


# ===============================
# MIDDLEWARE
# ===============================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ===============================
# URL & WSGI / ASGI
# ===============================
ROOT_URLCONF = "core.urls"
WSGI_APPLICATION = "core.wsgi.application"
ASGI_APPLICATION = "core.asgi.application"


# ===============================
# TEMPLATES
# ===============================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# ===============================
# DATABASE
# ===============================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ===============================
# PASSWORD VALIDATION
# ===============================
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": ("django.contrib.auth.password_validation." "MinimumLengthValidator"),
    },
    {
        "NAME": ("django.contrib.auth.password_validation." "CommonPasswordValidator"),
    },
    {
        "NAME": ("django.contrib.auth.password_validation." "NumericPasswordValidator"),
    },
]


# ===============================
# INTERNATIONALIZATION
# ===============================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# ===============================
# STATIC FILES
# ===============================
STATIC_URL = "/static/"


# ===============================
# DEFAULT AUTO FIELD
# ===============================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ===============================
# CUSTOM USER MODEL
# ===============================
AUTH_USER_MODEL = "auth_service.User"


# ===============================
# 🔐 DJANGO REST FRAMEWORK (JWT)
# ===============================
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}


# ===============================
# 🔐 SIMPLE JWT SETTINGS
# ===============================
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "user_id",
    "USER_ID_CLAIM": "user_id",
}


# ===============================
# CHANNELS
# ===============================
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    }
}
