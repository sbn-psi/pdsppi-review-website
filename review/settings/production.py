import os

print('load production settings')

DEBUG = False

ALLOWED_HOSTS = ['localhost', 'sbnreviews.psi.edu'] 

# AWS S3, Cloudflare CDN configuration
# stores/serves static and media directories in AWS in production

# Upload media files to S3
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# aws settings
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_DEFAULT_ACL = 'public-read'
# Using S3 as a CDN (via CloudFront), tell storage to serve files from there
AWS_S3_CUSTOM_DOMAIN = 'd3qrohnnpazynl.cloudfront.net'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
# s3 static settings
AWS_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
# Allow `django-admin collectstatic` to automatically put your static files in your bucket
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3ManifestStaticStorage'

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'https://sbnreviews.psi.edu'
print('prod DEBUG: ', DEBUG)