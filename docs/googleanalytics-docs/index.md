---
title: googleanalytics
hide_title: false
hide_table_of_contents: false
keywords:
  - googleanalytics
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleanalytics/stackql-googleanalytics-provider-featured-image.png
id: googleanalytics-doc
slug: /providers/googleanalytics

---
Web tracking and analytics service.  
    
:::info Provider Summary

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>5</b></span><br />
<span>total methods:&nbsp;<b>242</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>63</b></span><br />
<span>total selectable resources:&nbsp;<b>54</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation
```bash
REGISTRY PULL googleanalytics v23.01.00116;
```

## Authentication
```javascript

{
  "googleanalytics": {
    "type": string, // authentication type to use, suported values:  service_account
    "credentialsfilepath": string, // path to service account key file
    "scopes": string[], // array of scopes required for API authorization, see [scopes](https://developers.google.com/identity/protocols/oauth2/scopes)
  }
}

```
### Example (Mac/Linux)
```bash

AUTH='{ "googleanalytics": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json", "scopes": ["https://www.googleapis.com/auth/...", "..."]  }}'
stackql shell --auth="${AUTH}"

```
### Example (PowerShell)
```powershell

$Auth = "{ 'googleanalytics': { 'type': 'service_account',  'credentialsfilepath': 'creds/sa-key.json', 'scopes': ['https://www.googleapis.com/auth/...', '...'] }}"
stackql.exe shell --auth=$Auth

```
## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/googleanalytics/analytics/">analytics</a><br />
<a href="/providers/googleanalytics/analyticsadmin/">analyticsadmin</a><br />
<a href="/providers/googleanalytics/analyticsdata/">analyticsdata</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/googleanalytics/analyticsreporting/">analyticsreporting</a><br />
<a href="/providers/googleanalytics/tagmanager/">tagmanager</a><br />
</div>
</div>
