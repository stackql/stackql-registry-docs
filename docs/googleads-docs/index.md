---
title: googleads
hide_title: false
hide_table_of_contents: false
keywords:
  - googleads
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
id: googleads-doc
slug: /providers/googleads

---
Online advertising platform by Google.  
    
:::info Provider Summary

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>10</b></span><br />
<span>total methods:&nbsp;<b>398</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>139</b></span><br />
<span>total selectable resources:&nbsp;<b>119</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation
```bash
REGISTRY PULL googleads v23.01.00114;
```

## Authentication
```javascript

{
  "googleads": {
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

AUTH='{ "googleads": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json" }}'
stackql shell --auth="${AUTH}"

```
### Example (PowerShell)
```powershell

$Auth = "{ 'googleads': { 'type': 'service_account',  'credentialsfilepath': 'creds/sa-key.json' }}"
stackql.exe shell --auth=$Auth

```
## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/googleads/adexchangebuyer2/">adexchangebuyer2</a><br />
<a href="/providers/googleads/adexperiencereport/">adexperiencereport</a><br />
<a href="/providers/googleads/admob/">admob</a><br />
<a href="/providers/googleads/adsense/">adsense</a><br />
<a href="/providers/googleads/adsensehost/">adsensehost</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/googleads/dfareporting/">dfareporting</a><br />
<a href="/providers/googleads/doubleclickbidmanager/">doubleclickbidmanager</a><br />
<a href="/providers/googleads/doubleclicksearch/">doubleclicksearch</a><br />
<a href="/providers/googleads/localservices/">localservices</a><br />
<a href="/providers/googleads/realtimebidding/">realtimebidding</a><br />
</div>
</div>
