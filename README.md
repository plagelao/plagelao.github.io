### How to bump the version

```
cz bump
cz changelog
git add .
git commit --amend
git push origin main
```

Or just run the script

```
./update_versioning.sh
```

### How to populate the categories

```
docker compose run -it --entrypoint='' site bundle exec rake tags:populate
```
