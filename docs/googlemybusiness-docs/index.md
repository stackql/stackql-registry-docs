---
title: googlemybusiness
hide_title: false
hide_table_of_contents: false
keywords:
  - googlemybusiness
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googlemybusiness/stackql-googlemybusiness-provider-featured-image.png
id: googlemybusiness-doc
slug: /providers/googlemybusiness

---
Tools for businesses to manage their online presence.  
    
:::info Provider Summary

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>9</b></span><br />
<span>total methods:&nbsp;<b>62</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>31</b></span><br />
<span>total selectable resources:&nbsp;<b>23</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation
```bash
REGISTRY PULL googlemybusiness v23.01.00114;
```

## Authentication
```javascript

{
  "googlemybusiness": {
    "type": string, // authentication type to use, suported values:  service_account
    "credentialsfilepath": string, // path to service account key file
    "scopes": string[], // array of scopes required for API authorization, see [scopes](https://developers.google.com/identity/protocols/oauth2/scopes)
  }
}

```
### Example (Mac/Linux)
```bash

AUTH='{ "googlemybusiness": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json", "scopes": ["https://www.googleapis.com/auth/...", "..."]  }}'
stackql shell --auth="${AUTH}"

```
### Example (PowerShell)
```powershell

$Auth = "{ 'googlemybusiness': { 'type': 'service_account',  'credentialsfilepath': 'creds/sa-key.json', 'scopes': ['https://www.googleapis.com/auth/...', '...'] }}"
stackql.exe shell --auth=$Auth

```
## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/googlemybusiness/businessprofileperformance/">businessprofileperformance</a><br />
<a href="/providers/googlemybusiness/mybusinessaccountmanagement/">mybusinessaccountmanagement</a><br />
<a href="/providers/googlemybusiness/mybusinessbusinesscalls/">mybusinessbusinesscalls</a><br />
<a href="/providers/googlemybusiness/mybusinessbusinessinformation/">mybusinessbusinessinformation</a><br />
<a href="/providers/googlemybusiness/mybusinesslodging/">mybusinesslodging</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/googlemybusiness/mybusinessnotifications/">mybusinessnotifications</a><br />
<a href="/providers/googlemybusiness/mybusinessplaceactions/">mybusinessplaceactions</a><br />
<a href="/providers/googlemybusiness/mybusinessqanda/">mybusinessqanda</a><br />
<a href="/providers/googlemybusiness/mybusinessverifications/">mybusinessverifications</a><br />
</div>
</div>
