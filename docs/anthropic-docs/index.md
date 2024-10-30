---
title: anthropic
hide_title: false
hide_table_of_contents: false
keywords:
  - anthropic
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Anthropic resources using SQL.
custom_edit_url: null
image: /img/providers/anthropic/stackql-anthropic-provider-featured-image.png
id: anthropic-doc
slug: /providers/anthropic
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

AI models including Claude for advanced language understanding and generation.  
    
:::info Provider Summary (v24.10.00267)

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>1</b></span><br />
<span>total methods:&nbsp;<b>2</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>2</b></span><br />
<span>total selectable resources:&nbsp;<b>2</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `anthropic` provider, run the following command:  

```bash
REGISTRY PULL anthropic;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication

The following system environment variables are used for authentication by default:  

- <CopyableCode code="ANTHROPIC_API_KEY" /> - Anthropic API key (see <a href="https://docs.anthropic.com/claude/reference/getting-started-with-the-api">How to Create an Anthropic API Key</a>)
    
These variables are sourced at runtime (from the local machine or as CI variables/secrets).  

<details>

<summary>Using different environment variables</summary>

To use different environment variables (instead of the defaults), use the `--auth` flag of the `stackql` program.  For example:  

```bash

AUTH='{ "anthropic": { "type": "bearer", "credentialsenvvar": "MY_ANTHROPIC_API_KEY" }}'
stackql shell --auth="${AUTH}"
    
```
or using PowerShell:  

```powershell

$Auth = "{ 'anthropic': { 'type': 'bearer', 'credentialsenvvar': 'MY_ANTHROPIC_API_KEY' }}"
stackql.exe shell --auth=$Auth
    
```
</details>

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/anthropic/messages/">messages</a><br />
</div>
<div class="providerDocColumn">
</div>
</div>
