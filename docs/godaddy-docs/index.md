---
title: godaddy
hide_title: false
hide_table_of_contents: false
keywords:
  - godaddy
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GoDaddy resources using SQL
custom_edit_url: null
image: /img/providers/godaddy/stackql-godaddy-provider-featured-image.png
id: godaddy-doc
slug: /providers/godaddy

---
Domain registration and web hosting services.  
    
:::info Provider Summary (v23.12.00185)

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>9</b></span><br />
<span>total methods:&nbsp;<b>60</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>39</b></span><br />
<span>total selectable resources:&nbsp;<b>19</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `godaddy` provider, run the following command:  

```bash
REGISTRY PULL godaddy;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication

The following system environment variables are used for authentication by default:  

- `GODADDY_API_KEY` - Godaddy API key (see [Creating a Godaddy API Key](https://developer.godaddy.com/keys))
  
These variables are sourced at runtime (from the local machine or as CI variables/secrets).  

<details>

<summary>Using different environment variables</summary>

To use different environment variables (instead of the defaults), use the `--auth` flag of the `stackql` program.  For example:  

```bash

AUTH='{ "okta": { "type": "bearer", "credentialsenvvar": "YOUR_GODADDY_API_KEY_VAR" }}'
stackql shell --auth="${AUTH}"

```
or using PowerShell:  

```powershell

$Auth = "{ 'okta': { 'type': 'bearer', 'credentialsenvvar': 'YOUR_GODADDY_API_KEY_VAR' }}"
stackql.exe shell --auth=$Auth

```
</details>

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/godaddy/abuse/">abuse</a><br />
<a href="/providers/godaddy/aftermarket/">aftermarket</a><br />
<a href="/providers/godaddy/agreements/">agreements</a><br />
<a href="/providers/godaddy/certificates/">certificates</a><br />
<a href="/providers/godaddy/countries/">countries</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/godaddy/domains/">domains</a><br />
<a href="/providers/godaddy/orders/">orders</a><br />
<a href="/providers/godaddy/shoppers/">shoppers</a><br />
<a href="/providers/godaddy/subscriptions/">subscriptions</a><br />
</div>
</div>
