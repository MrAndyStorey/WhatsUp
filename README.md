# WhatsUp
Basic FLASK app that I've put together to demonstrate deploying to [Digital Ocean's App Platform](https://docs.digitalocean.com/products/app-platform/)

## Limitations:
When deploying, you'll need to add your app’s entrypoint to it like so: 

```
gunicorn --worker-tmp-dir /dev/shm app:app.
```
