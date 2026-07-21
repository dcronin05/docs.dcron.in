FROM nginx:alpine
# Copy the built site from the GitHub action into the nginx root
COPY ./site /usr/share/nginx/html

# Expose port 80
EXPOSE 80
