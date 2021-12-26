apiVersion: apps/v1
kind: Deployment
metadata:
  name: bridge-flask-app
  labels:
    app: bridge-flask-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: bridge-flask-app
  template:
    metadata:
      labels:
        app: bridge-flask-app
    spec:
      containers:
      - name: bridge-flask-app
        image: us-west2-docker.pkg.dev/GOOGLE_CLOUD_PROJECT/palms-park-bridge-club/bridge-flask-app:COMMIT_SHA
        ports:
        - containerPort: 8080
---
kind: Service
apiVersion: v1
metadata:
  name: bridge-flask-app
spec:
  selector:
    app: bridge-flask-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
  type: LoadBalancer
