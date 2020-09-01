# How to post marcxml record using curl via access token

You can post marcxml record via an access token using the api documents as follows:

assuming that your token is: my_token and the xml record is saved in document.xml

```bash
curl -k -L -H "Authorization: Bearer my_token"  -H 'Content-Type:application/marcxml+xml' --data-binary "@./document.xml" -POST https://~/api/documents/
```

[How to generate an access token](permissions/generate_oauth_token.md)
