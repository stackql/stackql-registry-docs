---
title: youtube
hide_title: false
hide_table_of_contents: false
keywords:
  - youtube
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/youtube/stackql-youtube-provider-featured-image.png
id: youtube-doc
slug: /providers/youtube

---
Online video sharing and social media platform.  
    
:::info Provider Summary

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>3</b></span><br />
<span>total methods:&nbsp;<b>92</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>38</b></span><br />
<span>total selectable resources:&nbsp;<b>29</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation
```bash
REGISTRY PULL youtube v23.01.00114;
```

## Authentication
```javascript

{
  "youtube": {
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

AUTH='{ "youtube": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json" }}'
stackql shell --auth="${AUTH}"

```
### Example (PowerShell)
```powershell

$Auth = "{ 'youtube': { 'type': 'service_account',  'credentialsfilepath': 'creds/sa-key.json' }}"
stackql.exe shell --auth=$Auth

```
## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/youtube/youtube/">youtube</a><br />
<a href="/providers/youtube/youtubeAnalytics/">youtubeAnalytics</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/youtube/youtubereporting/">youtubereporting</a><br />
</div>
</div>
