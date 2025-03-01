#!/bin/bash

echo "Bumping version number"
cz bump
echo "Updating changelog"
cz changelog
git add .
echo "Amending version commit to add changelog"
read -p "Press any key to continue..."
git commit --amend
echo "Pushing code"
git push origin main
