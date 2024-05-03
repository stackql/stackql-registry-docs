---
title: datadog
hide_title: false
hide_table_of_contents: false
keywords:
  - datadog
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
id: datadog-doc
slug: /providers/datadog
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Monitoring, alerting and reporting platform for cloud platforms and applications.  
    
:::info Provider Summary (v23.12.00194)

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>41</b></span><br />
<span>total methods:&nbsp;<b>405</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>96</b></span><br />
<span>total selectable resources:&nbsp;<b>88</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `datadog` provider, run the following command:  

```bash
REGISTRY PULL datadog;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication

The following system environment variables are used for authentication by default:  

- <CopyableCode code="DD_API_KEY" /> - Datadog API key (see <a href="https://docs.datadoghq.com/account_management/api-app-keys/#api-keys">Datadog API Key Documentation</a>)
- <CopyableCode code="DD_APP_KEY" /> - Datadog Application Key (see <a href="https://docs.datadoghq.com/account_management/api-app-keys/#application-keys">Datadog Application Key Documentation</a>)
  
These variables are sourced at runtime (from the local machine or as CI variables/secrets).  

<details>

<summary>Using different environment variables</summary>

To use different environment variables (instead of the defaults), use the `--auth` flag of the `stackql` program.  For example:  

```bash

AUTH='{ "datadog": { "type": "custom", "location": "header", "name": "DD-API-KEY", "credentialsenvvar": "YOUR_DD_API_KEY_VAR", "successor": { "type": "custom", "location": "header", "name": "DD-APPLICATION-KEY", "credentialsenvvar": "YOUR_DD_APP_KEY_VAR" }}}'
stackql shell --auth="${AUTH}"

```
or using PowerShell:  

```powershell

$Auth = "{ 'datadog': { 'type': 'custom', 'location': 'header', 'name': 'DD-API-KEY', 'credentialsenvvar': 'YOUR_DD_API_KEY_VAR', 'successor': { 'type': 'custom', 'location': 'header', 'name': 'DD-APPLICATION-KEY', 'credentialsenvvar': 'YOUR_DD_APP_KEY_VAR' }}}"
stackql.exe shell --auth=$Auth

```
</details>

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/datadog/apm_retention_filters/">apm_retention_filters</a><br />
<a href="/providers/datadog/audit/">audit</a><br />
<a href="/providers/datadog/authn_mappings/">authn_mappings</a><br />
<a href="/providers/datadog/ci_visibility/">ci_visibility</a><br />
<a href="/providers/datadog/cloud_workload_security/">cloud_workload_security</a><br />
<a href="/providers/datadog/cloudflare_integration/">cloudflare_integration</a><br />
<a href="/providers/datadog/confluent_cloud/">confluent_cloud</a><br />
<a href="/providers/datadog/containers/">containers</a><br />
<a href="/providers/datadog/dashboard_lists/">dashboard_lists</a><br />
<a href="/providers/datadog/dora_metrics/">dora_metrics</a><br />
<a href="/providers/datadog/downtimes/">downtimes</a><br />
<a href="/providers/datadog/events/">events</a><br />
<a href="/providers/datadog/fastly_integration/">fastly_integration</a><br />
<a href="/providers/datadog/gcp_integration/">gcp_integration</a><br />
<a href="/providers/datadog/incidents/">incidents</a><br />
<a href="/providers/datadog/ip_allowlist/">ip_allowlist</a><br />
<a href="/providers/datadog/key_management/">key_management</a><br />
<a href="/providers/datadog/log_archives/">log_archives</a><br />
<a href="/providers/datadog/log_metrics/">log_metrics</a><br />
<a href="/providers/datadog/logs/">logs</a><br />
<a href="/providers/datadog/metrics/">metrics</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/datadog/monitors/">monitors</a><br />
<a href="/providers/datadog/okta_integration/">okta_integration</a><br />
<a href="/providers/datadog/opsgenie_integration/">opsgenie_integration</a><br />
<a href="/providers/datadog/organizations/">organizations</a><br />
<a href="/providers/datadog/powerpack/">powerpack</a><br />
<a href="/providers/datadog/processes/">processes</a><br />
<a href="/providers/datadog/restriction_policies/">restriction_policies</a><br />
<a href="/providers/datadog/roles/">roles</a><br />
<a href="/providers/datadog/rum/">rum</a><br />
<a href="/providers/datadog/security_monitoring/">security_monitoring</a><br />
<a href="/providers/datadog/sensitive_data_scanner/">sensitive_data_scanner</a><br />
<a href="/providers/datadog/service_accounts/">service_accounts</a><br />
<a href="/providers/datadog/service_definition/">service_definition</a><br />
<a href="/providers/datadog/service_scorecards/">service_scorecards</a><br />
<a href="/providers/datadog/span_metrics/">span_metrics</a><br />
<a href="/providers/datadog/spans/">spans</a><br />
<a href="/providers/datadog/synthetics/">synthetics</a><br />
<a href="/providers/datadog/teams/">teams</a><br />
<a href="/providers/datadog/usage_metering/">usage_metering</a><br />
<a href="/providers/datadog/users/">users</a><br />
</div>
</div>
