---
title: monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors
  - dynatrace
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.dynatrace.monitors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | The properties of the managed service identities assigned to this resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties specific to the monitor resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `monitorName, resourceGroupName, subscriptionId` |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` |
| `list_by_subscription_id` | `SELECT` | `subscriptionId` |
| `create_or_update` | `INSERT` | `monitorName, resourceGroupName, subscriptionId, data__properties` |
| `delete` | `DELETE` | `monitorName, resourceGroupName, subscriptionId` |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` |
| `_list_by_subscription_id` | `EXEC` | `subscriptionId` |
| `update` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
