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
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
id: sumologic-doc
slug: /providers/sumologic
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Cloud-native, real-time, unified logs and metrics analytics platform.  
    
:::info Provider Summary (v23.04.00143)

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>32</b></span><br />
<span>total methods:&nbsp;<b>267</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>150</b></span><br />
<span>total selectable resources:&nbsp;<b>83</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `sumologic` provider, run the following command:  

```bash
REGISTRY PULL sumologic;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication

The following system environment variables are used for authentication by default:  

- <CopyableCode code="SUMOLOGIC_ACCESSID" /> - SumoLogic Access ID (see <a href="https://help.sumologic.com/docs/manage/security/access-keys/">Generating an Access Key</a>)
- <CopyableCode code="SUMOLOGIC_ACCESSKEY" /> - SumoLogic Access Key (see <a href="https://help.sumologic.com/docs/manage/security/access-keys/">Generating an Access Key</a>)
  
These variables are sourced at runtime (from the local machine or as CI variables/secrets).  

<details>

<summary>Using different environment variables</summary>

To use different environment variables (instead of the defaults), use the `--auth` flag of the `stackql` program.  For example:  

```bash

AUTH='{ "sumologic": { "type": "basic",  "username_var": "YOUR_SUMOLOGIC_ACCESS_ID_VAR", "password_var": "YOUR_SUMOLOGIC_ACCESS_KEY_VAR" }}'
stackql shell --auth="${AUTH}"

```
or using PowerShell:  

```powershell

$Auth = "{ 'sumologic': { 'type': 'basic',  'username_var': 'YOUR_SUMOLOGIC_ACCESS_ID_VAR', 'password_var': 'YOUR_SUMOLOGIC_ACCESS_KEY_VAR' }}"
stackql.exe shell --auth=$Auth

```
</details>


## Server Parameters


The following parameter is required for the `sumologic` provider if you are not using the `us2` region:  

- `region` - The SumoLogic regional endpoint (e.g. `au`, `ca`, `de`, `eu`, `fed`, `in`, `jp`)

This parameter would be supplied to the `WHERE` clause of each `SELECT` statement if you are not usign the `us2` region.
    
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
