---
title: licenses
hide_title: false
hide_table_of_contents: false
keywords:
  - licenses
  - licenses
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>licenses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.licenses.licenses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `name` | `string` |
| `description` | `string` |
| `key` | `string` |
| `conditions` | `array` |
| `url` | `string` |
| `body` | `string` |
| `node_id` | `string` |
| `html_url` | `string` |
| `permissions` | `array` |
| `featured` | `boolean` |
| `limitations` | `array` |
| `implementation` | `string` |
| `spdx_id` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `license` | Gets information about a specific license. For more information, see "[Licensing a repository ](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)." |
| `get_all_commonly_used` | `SELECT` |  | Lists the most commonly used licenses on GitHub. For more information, see "[Licensing a repository ](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)." |
