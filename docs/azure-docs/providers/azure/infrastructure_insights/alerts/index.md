---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - infrastructure_insights
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
<tr><td><b>Id</b></td><td><code>azure.infrastructure_insights.alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The Azure Region where the resource lives |
| `properties` | `object` | Contains alert data. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Alerts_Get` | `SELECT` | `alertName, location, resourceGroupName, subscriptionId` | Returns the requested an alert. |
| `Alerts_List` | `SELECT` | `location, resourceGroupName, subscriptionId` | Returns the list of all alerts in a given region. |
| `Alerts_Close` | `EXEC` | `alertName, location, resourceGroupName, subscriptionId, user` | Closes the given alert. |
| `Alerts_Repair` | `EXEC` | `alertName, location, resourceGroupName, subscriptionId` | Repairs an alert. |
