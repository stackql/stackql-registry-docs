---
title: googleworkspace
hide_title: false
hide_table_of_contents: false
keywords:
  - google workspace
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
id: googleworkspace-doc
slug: /providers/googleworkspace

---
Productivity and collaboration tools for businesses.  
    
:::info Provider Summary

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>25</b></span><br />
<span>total methods:&nbsp;<b>433</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>138</b></span><br />
<span>total selectable resources:&nbsp;<b>100</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation
```bash
REGISTRY PULL googleworkspace v23.01.00114;
```

## Authentication
```javascript

{
  "googleworkspace": {
    "type": string, // authentication type to use, suported values:  service_account
    "credentialsfilepath": string, // path to service account key file
    "scopes": string[], // array of scopes required for API authorization, see [scopes](https://developers.google.com/identity/protocols/oauth2/scopes)
  }
}

```
### Example (Mac/Linux)
```bash

AUTH='{ "googleworkspace": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json", "scopes": ["https://www.googleapis.com/auth/drive", "..."]  }}'
stackql shell --auth="${AUTH}"

```
### Example (PowerShell)
```powershell

$Auth = "{ 'googleworkspace': { 'type': 'service_account',  'credentialsfilepath': 'creds/sa-key.json', 'scopes': ['https://www.googleapis.com/auth/drive', '...'] }}"
stackql.exe shell --auth=$Auth

```
## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/googleworkspace/admin/">admin</a><br />
<a href="/providers/googleworkspace/alertcenter/">alertcenter</a><br />
<a href="/providers/googleworkspace/calendar/">calendar</a><br />
<a href="/providers/googleworkspace/chat/">chat</a><br />
<a href="/providers/googleworkspace/chromemanagement/">chromemanagement</a><br />
<a href="/providers/googleworkspace/chromepolicy/">chromepolicy</a><br />
<a href="/providers/googleworkspace/chromeuxreport/">chromeuxreport</a><br />
<a href="/providers/googleworkspace/classroom/">classroom</a><br />
<a href="/providers/googleworkspace/docs/">docs</a><br />
<a href="/providers/googleworkspace/drive/">drive</a><br />
<a href="/providers/googleworkspace/driveactivity/">driveactivity</a><br />
<a href="/providers/googleworkspace/drivelabels/">drivelabels</a><br />
<a href="/providers/googleworkspace/forms/">forms</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/googleworkspace/gmail/">gmail</a><br />
<a href="/providers/googleworkspace/gmailpostmastertools/">gmailpostmastertools</a><br />
<a href="/providers/googleworkspace/groupssettings/">groupssettings</a><br />
<a href="/providers/googleworkspace/keep/">keep</a><br />
<a href="/providers/googleworkspace/licensing/">licensing</a><br />
<a href="/providers/googleworkspace/reseller/">reseller</a><br />
<a href="/providers/googleworkspace/script/">script</a><br />
<a href="/providers/googleworkspace/sheets/">sheets</a><br />
<a href="/providers/googleworkspace/siteVerification/">siteVerification</a><br />
<a href="/providers/googleworkspace/slides/">slides</a><br />
<a href="/providers/googleworkspace/tasks/">tasks</a><br />
<a href="/providers/googleworkspace/vault/">vault</a><br />
</div>
</div>
