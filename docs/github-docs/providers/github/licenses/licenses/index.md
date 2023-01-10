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
| `spdx_id` | `string` |
| `limitations` | `array` |
| `body` | `string` |
| `url` | `string` |
| `permissions` | `array` |
| `conditions` | `array` |
| `html_url` | `string` |
| `key` | `string` |
| `node_id` | `string` |
| `implementation` | `string` |
| `featured` | `boolean` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `license` |
