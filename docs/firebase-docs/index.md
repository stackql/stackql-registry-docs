---
title: firebase
hide_title: false
hide_table_of_contents: false
keywords:
  - firebase
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
Application development platform for creating mobile and web applications.  
    

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation
```bash
REGISTRY PULL firebase v1.0.2;
```

## Authentication
```javascript
{
  "firebase": {
    /**
      * Type of authentication to use, suported values include: service_account, interactive
      * @type String
      */
    "type": string, 
    /**
      * path to service account key file.
      * @type String
      */
    "credentialsfilepath": string, 
  }
}
```
### Example (Mac/Linux)
```bash

AUTH='{ "firebase": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json" }}'
stackql shell --auth="${AUTH}"

```
### Example (PowerShell)
```powershell

$Auth = "{ 'firebase': { 'type': 'service_account',  'credentialsfilepath': 'creds/sa-key.json' }}'
stackql.exe shell --auth=$Auth

```
## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/firebase/fcm/">fcm</a><br />
<a href="/providers/firebase/fcmdata/">fcmdata</a><br />
<a href="/providers/firebase/firebaseappcheck/">firebaseappcheck</a><br />
<a href="/providers/firebase/firebasedatabase/">firebasedatabase</a><br />
<a href="/providers/firebase/firebasedynamiclinks/">firebasedynamiclinks</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/firebase/firebasehosting/">firebasehosting</a><br />
<a href="/providers/firebase/firebaserules/">firebaserules</a><br />
<a href="/providers/firebase/firebasestorage/">firebasestorage</a><br />
<a href="/providers/firebase/toolresults/">toolresults</a><br />
</div>
</div>
