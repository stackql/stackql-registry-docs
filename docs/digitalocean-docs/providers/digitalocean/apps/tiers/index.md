---
title: tiers
hide_title: false
hide_table_of_contents: false
keywords:
  - tiers
  - apps
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tiers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.apps.tiers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `name` | `string` |
| `egress_bandwidth_bytes` | `string` |
| `slug` | `string` |
| `storage_bytes` | `string` |
| `build_seconds` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_tier` | `SELECT` | `slug` | Retrieve information about a specific app tier. |
| `list_tiers` | `SELECT` |  | List all app tiers. |
| `_get_tier` | `EXEC` | `slug` | Retrieve information about a specific app tier. |
| `_list_tiers` | `EXEC` |  | List all app tiers. |
