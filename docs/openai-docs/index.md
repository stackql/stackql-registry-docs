---
title: openai
hide_title: false
hide_table_of_contents: false
keywords:
  - openai
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage OpenAI and ChatGPT resources using SQL.
custom_edit_url: null
image: /img/providers/openai/stackql-openai-provider-featured-image.png
id: openai-doc
slug: /providers/openai
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

AI models for natural language processing and content generation.


:::info Provider Summary

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>17</b></span><br />
<span>total resources:&nbsp;<b>52</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `openai` provider, run the following command:  

```bash
REGISTRY PULL openai;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication

The following system environment variables are used for authentication by default:  

- <CopyableCode code="OPENAI_API_KEY" /> - OpenAI API key (see <a href="https://platform.openai.com/account/api-keys">How to Create an OpenAI API Key</a>)
        
These variables are sourced at runtime (from the local machine or as CI variables/secrets).  

<details>

<summary>Using different environment variables</summary>

To use different environment variables (instead of the defaults), use the `--auth` flag of the `stackql` program.  For example:  

```bash

AUTH='{ "openai": { "type": "bearer", "credentialsenvvar": "OPENAI_API_KEY" }}'
stackql shell --auth="${AUTH}"
        
```
or using PowerShell:  

```powershell

$Auth = "{ 'openai': { 'type': 'bearer', 'credentialsenvvar': 'OPENAI_API_KEY' }}"
stackql.exe shell --auth=$Auth
        
```
</details>


## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/openai/assistants/">assistants</a><br />
<a href="/providers/openai/audio/">audio</a><br />
<a href="/providers/openai/audit_logs/">audit_logs</a><br />
<a href="/providers/openai/batch/">batch</a><br />
<a href="/providers/openai/chat/">chat</a><br />
<a href="/providers/openai/completions/">completions</a><br />
<a href="/providers/openai/embeddings/">embeddings</a><br />
<a href="/providers/openai/files/">files</a><br />
<a href="/providers/openai/fine_tuning/">fine_tuning</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/openai/images/">images</a><br />
<a href="/providers/openai/invites/">invites</a><br />
<a href="/providers/openai/models/">models</a><br />
<a href="/providers/openai/moderations/">moderations</a><br />
<a href="/providers/openai/projects/">projects</a><br />
<a href="/providers/openai/uploads/">uploads</a><br />
<a href="/providers/openai/users/">users</a><br />
<a href="/providers/openai/vector_stores/">vector_stores</a><br />
</div>
</div>
