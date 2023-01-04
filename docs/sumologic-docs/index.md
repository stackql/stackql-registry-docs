---
title: sumologic
hide_title: false
hide_table_of_contents: false
keywords:
  - sumologic
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
id: sumologic-doc
slug: /providers/sumologic
---
Cloud-native, real-time, unified logs and metrics analytics platform.  

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

:::info Provider Summary

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;&nbsp;&nbsp;<b>32</b></span><br />
<span>total methods:&nbsp;<b>267</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>150</b></span><br />
<span>total selectable resources:&nbsp;<b>83</b></span><br />
</div>
</div>

:::

## Installation
```bash
REGISTRY PULL sumologic v23.01.00104;
```

## Authentication
```javascript

{
  "sumologic": {
    /**
      * Type of authentication to use, suported values include: basic
      * @type String
      */
    "type": string, 
    /**
      * Environment variable name containing the api key or credentials.
      * Variable value must be a base64 encoded string of the form: username:password
      * @type String
      */
    "credentialsenvvar": string, 
  }
}

```
### Example (Mac/Linux)
```bash

export SUMO_CREDS=$(echo -n 'youraccessid:YOURACCESSTOKEN' | base64 --wrap 0)
AUTH='{ "sumologic": { "type": "basic", "credentialsenvvar": "SUMO_CREDS" } }'
stackql shell --auth="${AUTH}"

```
### Example (PowerShell)
```powershell

$env:SUMO_CREDS = [System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes("youraccessid:YOURACCESSTOKEN"))
$Auth = "{ 'sumologic': { 'type': 'basic', 'credentialsenvvar': 'SUMO_CREDS' } }"
stackql shell --auth=$Auth

```
## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/sumologic/access_keys/">access_keys</a><br />
<a href="/providers/sumologic/account/">account</a><br />
<a href="/providers/sumologic/apps/">apps</a><br />
<a href="/providers/sumologic/archive/">archive</a><br />
<a href="/providers/sumologic/collectors/">collectors</a><br />
<a href="/providers/sumologic/connections/">connections</a><br />
<a href="/providers/sumologic/content/">content</a><br />
<a href="/providers/sumologic/dashboards/">dashboards</a><br />
<a href="/providers/sumologic/dynamic_parsing_rules/">dynamic_parsing_rules</a><br />
<a href="/providers/sumologic/extraction_rules/">extraction_rules</a><br />
<a href="/providers/sumologic/fields/">fields</a><br />
<a href="/providers/sumologic/health_events/">health_events</a><br />
<a href="/providers/sumologic/ingest_budgets/">ingest_budgets</a><br />
<a href="/providers/sumologic/log_searches/">log_searches</a><br />
<a href="/providers/sumologic/logs_data_forwarding/">logs_data_forwarding</a><br />
<a href="/providers/sumologic/lookup_tables/">lookup_tables</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/sumologic/metrics_queries/">metrics_queries</a><br />
<a href="/providers/sumologic/metrics_searches/">metrics_searches</a><br />
<a href="/providers/sumologic/monitors/">monitors</a><br />
<a href="/providers/sumologic/partitions/">partitions</a><br />
<a href="/providers/sumologic/password_policy/">password_policy</a><br />
<a href="/providers/sumologic/plan/">plan</a><br />
<a href="/providers/sumologic/policies/">policies</a><br />
<a href="/providers/sumologic/roles/">roles</a><br />
<a href="/providers/sumologic/saml/">saml</a><br />
<a href="/providers/sumologic/scheduled_views/">scheduled_views</a><br />
<a href="/providers/sumologic/service_allowlist/">service_allowlist</a><br />
<a href="/providers/sumologic/slos/">slos</a><br />
<a href="/providers/sumologic/tokens/">tokens</a><br />
<a href="/providers/sumologic/tracing/">tracing</a><br />
<a href="/providers/sumologic/transformation_rules/">transformation_rules</a><br />
<a href="/providers/sumologic/users/">users</a><br />
</div>
</div>
