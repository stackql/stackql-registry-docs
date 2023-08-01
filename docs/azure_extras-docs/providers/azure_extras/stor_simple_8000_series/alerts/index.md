---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - stor_simple_8000_series
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.stor_simple_8000_series.alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The name of the object. |
| `properties` | `object` | The properties of alert |
| `type` | `string` | The hierarchical type of the object. |
| `kind` | `string` | The Kind of the object. Currently only Series8000 is supported |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Alerts_ListByManager` | `SELECT` | `managerName, resourceGroupName, subscriptionId` | Retrieves all the alerts in a manager. |
| `Alerts_Clear` | `EXEC` | `managerName, resourceGroupName, subscriptionId, data__alerts` | Clear the alerts. |
| `Alerts_SendTestEmail` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId, data__emailList` | Sends a test alert email. |
