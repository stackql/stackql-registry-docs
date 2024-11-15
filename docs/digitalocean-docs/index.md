---
title: digitalocean
hide_title: false
hide_table_of_contents: false
keywords:
  - digitalocean
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Digital Ocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
id: digitalocean-doc
slug: /providers/digitalocean

---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

DigitalOcean for managing cloud servers, databases, networking, and storage in a simplified, developer-friendly environment.


:::info Provider Summary

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>29</b></span><br />
<span>total resources:&nbsp;<b>179</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `digitalocean` provider, run the following command:  

```bash
REGISTRY PULL digitalocean;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication

The following system environment variables are used for authentication by default:  

- <CopyableCode code="DIGITALOCEAN_ACCESS_TOKEN" /> - DigitalOcean API token (see <a href="https://docs.digitalocean.com/reference/api/create-personal-access-token/">How to Create a Personal Access Token</a>)
  
These variables are sourced at runtime (from the local machine or as CI variables/secrets).  

<details>

<summary>Using different environment variables</summary>

To use different environment variables (instead of the defaults), use the `--auth` flag of the `stackql` program.  For example:  

```bash

AUTH='{ "digitalocean": { "type": "bearer",  "credentialsenvvar": "YOUR_DIGITALOCEAN_TOKEN_VAR" }}'
stackql shell --auth="${AUTH}"

```
or using PowerShell:  

```powershell

$Auth = "{ 'digitalocean': { 'type': 'bearer',  'credentialsenvvar': 'YOUR_DIGITALOCEAN_TOKEN_VAR' }}"
stackql.exe shell --auth=$Auth

```
</details>


## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/digitalocean/account/">account</a><br />
<a href="/providers/digitalocean/actions/">actions</a><br />
<a href="/providers/digitalocean/apps/">apps</a><br />
<a href="/providers/digitalocean/billing/">billing</a><br />
<a href="/providers/digitalocean/block_storage/">block_storage</a><br />
<a href="/providers/digitalocean/cdn/">cdn</a><br />
<a href="/providers/digitalocean/certificates/">certificates</a><br />
<a href="/providers/digitalocean/container_registry/">container_registry</a><br />
<a href="/providers/digitalocean/databases/">databases</a><br />
<a href="/providers/digitalocean/domains/">domains</a><br />
<a href="/providers/digitalocean/droplets/">droplets</a><br />
<a href="/providers/digitalocean/firewalls/">firewalls</a><br />
<a href="/providers/digitalocean/floating_ips/">floating_ips</a><br />
<a href="/providers/digitalocean/functions/">functions</a><br />
<a href="/providers/digitalocean/images/">images</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/digitalocean/kubernetes/">kubernetes</a><br />
<a href="/providers/digitalocean/load_balancers/">load_balancers</a><br />
<a href="/providers/digitalocean/monitoring/">monitoring</a><br />
<a href="/providers/digitalocean/one_click_applications/">one_click_applications</a><br />
<a href="/providers/digitalocean/projects/">projects</a><br />
<a href="/providers/digitalocean/regions/">regions</a><br />
<a href="/providers/digitalocean/reserved_ips/">reserved_ips</a><br />
<a href="/providers/digitalocean/sizes/">sizes</a><br />
<a href="/providers/digitalocean/snapshots/">snapshots</a><br />
<a href="/providers/digitalocean/ssh_keys/">ssh_keys</a><br />
<a href="/providers/digitalocean/tags/">tags</a><br />
<a href="/providers/digitalocean/uptime/">uptime</a><br />
<a href="/providers/digitalocean/vpc_peerings/">vpc_peerings</a><br />
<a href="/providers/digitalocean/vpcs/">vpcs</a><br />
</div>
</div>
