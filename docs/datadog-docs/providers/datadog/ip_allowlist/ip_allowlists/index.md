---
title: ip_allowlists
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_allowlists
  - ip_allowlist
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_allowlists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.ip_allowlist.ip_allowlists</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique identifier of the org. |
| `attributes` | `object` | Attributes of the IP allowlist. |
| `type` | `string` | IP allowlist type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_ip_allowlist` | `SELECT` | `dd_site` | Returns the IP allowlist and its enabled or disabled state. |
| `_get_ip_allowlist` | `EXEC` | `dd_site` | Returns the IP allowlist and its enabled or disabled state. |
| `update_ip_allowlist` | `EXEC` | `data__data, dd_site` | Edit the entries in the IP allowlist, and enable or disable it. |
