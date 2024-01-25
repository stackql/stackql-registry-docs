---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - authorization
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.authorization.alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The alert ID. |
| `name` | `string` | The alert name. |
| `properties` | `object` | Alert properties. |
| `type` | `string` | The alert type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `alertId, scope` | Get the specified alert. |
| `refresh` | `EXEC` | `alertId, scope` | Refresh an alert. |
| `refresh_all` | `EXEC` | `scope` | Refresh all alerts for a resource scope. |
| `update` | `EXEC` | `alertId, scope` | Update an alert. |
