---
title: snowflake
hide_title: false
hide_table_of_contents: false
keywords:
  - snowflake
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Snowflake resources using SQL
custom_edit_url: null
image: /img/providers/snowflake/stackql-snowflake-provider-featured-image.png
id: snowflake-doc
slug: /providers/snowflake

---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Snowflake for managing data warehousing, analytics, and secure data sharing with scalable cloud-native architecture and pay-as-you-go pricing.


:::info Provider Summary

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>32</b></span><br />
<span>total resources:&nbsp;<b>79</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `snowflake` provider, run the following command:  

```bash
REGISTRY PULL snowflake;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication

The following system environment variables are used for authentication by default:  

- <CopyableCode code="SNOWFLAKE_PAT" /> - Snowflake Programmatic Access Token (PAT) (see <a href="https://docs.snowflake.com/developer-guide/snowflake-rest-api/authentication#using-a-programmatic-access-token-pat">Using a programmatic access token (PAT)</a>)

These variables are sourced at runtime (from the local machine or as CI variables/secrets).  

<details>

<summary>Using different environment variables</summary>

To use different environment variables (instead of the defaults), use the `--auth` flag of the `stackql` program.  For example:  

```bash

AUTH='{ "snowflake": { "type": "bearer",  "credentialsenvvar": "YOUR_SNOWFLAKE_PAT_VAR" }}'
stackql shell --auth="${AUTH}"

```
or using PowerShell:  

```powershell

$Auth = "{ 'snowflake': { 'type': 'bearer',  'credentialsenvvar': 'YOUR_SNOWFLAKE_PAT_VAR' }}"
stackql.exe shell --auth=$Auth

```
</details>


## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/snowflake/account/">account</a><br />
<a href="/providers/snowflake/alert/">alert</a><br />
<a href="/providers/snowflake/api-integration/">api-integration</a><br />
<a href="/providers/snowflake/catalog-integration/">catalog-integration</a><br />
<a href="/providers/snowflake/compute-pool/">compute-pool</a><br />
<a href="/providers/snowflake/database/">database</a><br />
<a href="/providers/snowflake/database-role/">database-role</a><br />
<a href="/providers/snowflake/dynamic-table/">dynamic-table</a><br />
<a href="/providers/snowflake/event-table/">event-table</a><br />
<a href="/providers/snowflake/external-volume/">external-volume</a><br />
<a href="/providers/snowflake/function/">function</a><br />
<a href="/providers/snowflake/grant/">grant</a><br />
<a href="/providers/snowflake/iceberg-table/">iceberg-table</a><br />
<a href="/providers/snowflake/image-repository/">image-repository</a><br />
<a href="/providers/snowflake/managed-account/">managed-account</a><br />
<a href="/providers/snowflake/network-policy/">network-policy</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/snowflake/notebook/">notebook</a><br />
<a href="/providers/snowflake/notification-integration/">notification-integration</a><br />
<a href="/providers/snowflake/pipe/">pipe</a><br />
<a href="/providers/snowflake/procedure/">procedure</a><br />
<a href="/providers/snowflake/result/">result</a><br />
<a href="/providers/snowflake/role/">role</a><br />
<a href="/providers/snowflake/schema/">schema</a><br />
<a href="/providers/snowflake/sqlapi/">sqlapi</a><br />
<a href="/providers/snowflake/stage/">stage</a><br />
<a href="/providers/snowflake/streams/">streams</a><br />
<a href="/providers/snowflake/table/">table</a><br />
<a href="/providers/snowflake/task/">task</a><br />
<a href="/providers/snowflake/user/">user</a><br />
<a href="/providers/snowflake/user-defined-function/">user-defined-function</a><br />
<a href="/providers/snowflake/view/">view</a><br />
<a href="/providers/snowflake/warehouse/">warehouse</a><br />
</div>
</div>
