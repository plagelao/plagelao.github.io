### How to bump the version

```
cz bump
cz changelog
git add .
git commit --amend
git push origin main
```

### How to populate the categories

```
docker compose run -it --entrypoint='' site bundle exec rake tags:populate
```
