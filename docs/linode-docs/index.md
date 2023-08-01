---
title: linode
hide_title: false
hide_table_of_contents: false
keywords:
  - linode
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
id: linode-doc
slug: /providers/linode

---
 Cloud Computing Services by Akamai.  
    
:::info Provider Summary (v23.05.00149)

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>17</b></span><br />
<span>total methods:&nbsp;<b>508</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>107</b></span><br />
<span>total selectable resources:&nbsp;<b>92</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `linode` provider, run the following command:  

```bash
REGISTRY PULL linode;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication

The following system environment variables are used for authentication by default:  

- `LINODE_TOKEN` - Linode API token (see [How to Create a Linode API Token](https://www.linode.com/docs/products/tools/api/guides/manage-api-tokens/#create-an-api-token))
  
These variables are sourced at runtime (from the local machine or as CI variables/secrets).  

<details>

<summary>Using different environment variables</summary>

To use different environment variables (instead of the defaults), use the `--auth` flag of the `stackql` program.  For example:  

```bash

AUTH='{ "linode": { "type": "bearer",  "credentialsenvvar": "YOUR_LINODE_TOKEN_VAR" }}'
stackql shell --auth="${AUTH}"

```
or using PowerShell:  

```powershell

$Auth = "{ 'linode': { 'type': 'bearer',  'credentialsenvvar': 'YOUR_LINODE_TOKEN_VAR' }}"
stackql.exe shell --auth=$Auth

```
</details>

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/linode/account/">account</a><br />
<a href="/providers/linode/databases/">databases</a><br />
<a href="/providers/linode/domains/">domains</a><br />
<a href="/providers/linode/images/">images</a><br />
<a href="/providers/linode/instances/">instances</a><br />
<a href="/providers/linode/lke/">lke</a><br />
<a href="/providers/linode/longview/">longview</a><br />
<a href="/providers/linode/managed/">managed</a><br />
<a href="/providers/linode/networking/">networking</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/linode/nodebalancers/">nodebalancers</a><br />
<a href="/providers/linode/object_storage/">object_storage</a><br />
<a href="/providers/linode/profile/">profile</a><br />
<a href="/providers/linode/regions/">regions</a><br />
<a href="/providers/linode/support/">support</a><br />
<a href="/providers/linode/tags/">tags</a><br />
<a href="/providers/linode/view/">view</a><br />
<a href="/providers/linode/volumes/">volumes</a><br />
</div>
</div>
