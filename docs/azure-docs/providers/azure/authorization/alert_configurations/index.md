---
title: alert_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_configurations
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
<tr><td><b>Name</b></td><td><code>alert_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.authorization.alert_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The alert configuration ID. |
| `name` | `string` | The alert configuration name. |
| `properties` | `object` | Alert configuration properties. |
| `type` | `string` | The alert configuration type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `alertId, scope` | Get the specified alert configuration. |
| `update` | `EXEC` | `alertId, scope` | Update an alert configuration. |
