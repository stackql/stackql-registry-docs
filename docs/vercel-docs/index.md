---
title: vercel
hide_title: false
hide_table_of_contents: false
keywords:
  - vercel
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Vercel resources using SQL
custom_edit_url: null
image: /img/providers/vercel/stackql-vercel-provider-featured-image.png
id: vercel-doc
slug: /providers/vercel
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Cloud platform for serverless deployment and hosting of web applications.  
    
:::info Provider Summary (v23.12.00183)

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>19</b></span><br />
<span>total methods:&nbsp;<b>138</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>40</b></span><br />
<span>total selectable resources:&nbsp;<b>36</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `vercel` provider, run the following command:  

```bash
REGISTRY PULL vercel;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication

The following system environment variables are used for authentication by default:  

- <CopyableCode code="VERCEL_API_TOKEN" /> - Vercel API Token (see [Creating a Vercel API Token](https://vercel.com/account/tokens))
  
These variables are sourced at runtime (from the local machine or as CI variables/secrets).  

<details>

<summary>Using different environment variables</summary>

To use different environment variables (instead of the defaults), use the `--auth` flag of the `stackql` program.  For example:  

```bash

AUTH='{ "okta": { "type": "bearer", "credentialsenvvar": "YOUR_VERCEL_API_TOKEN_VAR" }}'
stackql shell --auth="${AUTH}"

```
or using PowerShell:  

```powershell

$Auth = "{ 'okta': { 'type': 'bearer', 'credentialsenvvar': 'YOUR_VERCEL_API_TOKEN_VAR' }}"
stackql.exe shell --auth=$Auth

```
</details>

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/vercel/aliases/">aliases</a><br />
<a href="/providers/vercel/artifacts/">artifacts</a><br />
<a href="/providers/vercel/authentication/">authentication</a><br />
<a href="/providers/vercel/billing_settings/">billing_settings</a><br />
<a href="/providers/vercel/cache/">cache</a><br />
<a href="/providers/vercel/certs/">certs</a><br />
<a href="/providers/vercel/checks/">checks</a><br />
<a href="/providers/vercel/deployments/">deployments</a><br />
<a href="/providers/vercel/dns/">dns</a><br />
<a href="/providers/vercel/domains/">domains</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/vercel/edge_config/">edge_config</a><br />
<a href="/providers/vercel/integrations/">integrations</a><br />
<a href="/providers/vercel/log_drains/">log_drains</a><br />
<a href="/providers/vercel/project_members/">project_members</a><br />
<a href="/providers/vercel/projects/">projects</a><br />
<a href="/providers/vercel/secrets/">secrets</a><br />
<a href="/providers/vercel/teams/">teams</a><br />
<a href="/providers/vercel/user/">user</a><br />
<a href="/providers/vercel/webhooks/">webhooks</a><br />
</div>
</div>
