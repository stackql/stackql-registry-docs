---
title: alert_incidents
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_incidents
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
<tr><td><b>Name</b></td><td><code>alert_incidents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.authorization.alert_incidents</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The alert incident ID. |
| `name` | `string` | The alert incident name. |
| `properties` | `object` | Alert incident properties |
| `type` | `string` | The alert incident type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `alertId, alertIncidentId, scope` | Get the specified alert incident. |
| `remediate` | `EXEC` | `alertId, alertIncidentId, scope` | Remediate an alert incident. |
