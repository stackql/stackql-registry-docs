---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - storsimple_1200_series
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
<tr><td><b>Id</b></td><td><code>azure_extras.storsimple_1200_series.alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier. |
| `name` | `string` | The name. |
| `properties` | `object` | Properties of alert |
| `type` | `string` | The type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_by_manager` | `SELECT` | `managerName, resourceGroupName, subscriptionId` | Retrieves all the alerts in a manager. |
| `_list_by_manager` | `EXEC` | `managerName, resourceGroupName, subscriptionId` | Retrieves all the alerts in a manager. |
| `clear` | `EXEC` | `managerName, resourceGroupName, subscriptionId, data__alerts` | Clear the alerts. |
| `send_test_email` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId, data__emailList` | Sends a test alert email. |
