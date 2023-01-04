---
title: netlify
hide_title: false
hide_table_of_contents: false
keywords:
  - netlify
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Netlify resources using SQL
custom_edit_url: null
image: /img/providers/netlify/stackql-netlify-provider-featured-image.png
id: netlify-doc
slug: /providers/netlify
---
Web development and content distribution platform.  
 
See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

:::info Provider Summary

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>30</b></span><br />
<span>total methods:&nbsp;<b>105</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>51</b></span><br />
<span>selectable resources:&nbsp;<b>31</b></span><br />
</div>
</div>

:::

## Installation
```bash
REGISTRY PULL netlify v23.01.00104;
```

## Authentication
```javascript
{
  "netlify": {
    /**
      * Type of authentication to use, suported values include: api_key
      * @type String
      */
    "type": string, 
    /**
      * Environment variable name containing the api key or credentials.
      * @type String
      */
    "credentialsenvvar": string, 
    /**
      * Value prepended to the request header, e.g. "Bearer "
      * Must be set to "Bearer "
      * @type String
      */
    "valuePrefix": string, 
  }
}
```
### Example (Mac/Linux)
```bash

NETLIFY_TOKEN=yourtoken
AUTH='{ "netlify": { "type": "api_key",  "credentialsenvvar": "NETLIFY_TOKEN", "valuePrefix": "Bearer " }}'
stackql shell --auth="${AUTH}"

```
### Example (PowerShell)
```powershell

$env:NETLIFY_TOKEN = "yourtoken"
$Auth = "{ 'netlify': { 'type': 'api_key',  'credentialsenvvar': 'NETLIFY_TOKEN', 'valuePrefix': 'Bearer ' }}"
stackql.exe shell --auth=$Auth

```
## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/netlify/access_token/">access_token</a><br />
<a href="/providers/netlify/account_membership/">account_membership</a><br />
<a href="/providers/netlify/account_type/">account_type</a><br />
<a href="/providers/netlify/asset/">asset</a><br />
<a href="/providers/netlify/asset_public_signature/">asset_public_signature</a><br />
<a href="/providers/netlify/audit_log/">audit_log</a><br />
<a href="/providers/netlify/build/">build</a><br />
<a href="/providers/netlify/build_hook/">build_hook</a><br />
<a href="/providers/netlify/build_log_msg/">build_log_msg</a><br />
<a href="/providers/netlify/deploy/">deploy</a><br />
<a href="/providers/netlify/deploy_key/">deploy_key</a><br />
<a href="/providers/netlify/deployed_branch/">deployed_branch</a><br />
<a href="/providers/netlify/dns_zone/">dns_zone</a><br />
<a href="/providers/netlify/file/">file</a><br />
<a href="/providers/netlify/form/">form</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/netlify/function/">function</a><br />
<a href="/providers/netlify/hook/">hook</a><br />
<a href="/providers/netlify/hook_type/">hook_type</a><br />
<a href="/providers/netlify/member/">member</a><br />
<a href="/providers/netlify/metadata/">metadata</a><br />
<a href="/providers/netlify/payment_method/">payment_method</a><br />
<a href="/providers/netlify/service/">service</a><br />
<a href="/providers/netlify/service_instance/">service_instance</a><br />
<a href="/providers/netlify/site/">site</a><br />
<a href="/providers/netlify/sni_certificate/">sni_certificate</a><br />
<a href="/providers/netlify/snippet/">snippet</a><br />
<a href="/providers/netlify/split_test/">split_test</a><br />
<a href="/providers/netlify/submission/">submission</a><br />
<a href="/providers/netlify/ticket/">ticket</a><br />
<a href="/providers/netlify/user/">user</a><br />
</div>
</div>
