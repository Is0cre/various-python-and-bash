#!/bin/bash

# Set the URL of the website to download

echo -n "what website do you want to download?: "
read url


# Download the website using curl, with the '-L' option to follow redirects
# and the '-k' option to ignore SSL certificate errors
curl -Lk "$url" > index.html

# Extract the links from the downloaded page
links=$(grep -oP '(?<=href=")[^"]*' index.html)

# Download each link
for link in $links; do
  # Check if the link is a relative path or an absolute URL
  if [[ $link == /* ]]; then
    # If the link is a relative path, add the base URL
    link="$url$link"
  fi
  # Download the resource
  curl -Lk "$link" -o "$link"
done
