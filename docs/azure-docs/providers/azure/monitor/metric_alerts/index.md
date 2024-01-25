---
title: metric_alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - metric_alerts
  - monitor
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
<tr><td><b>Name</b></td><td><code>metric_alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.metric_alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource Id |
| `name` | `string` | Azure resource name |
| `location` | `string` | Resource location |
| `properties` | `object` | An alert rule. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Gets or sets a list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in length than 128 characters and a value no greater in length than 256 characters. |
| `type` | `string` | Azure resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, ruleName, subscriptionId` | Retrieve an alert rule definition. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Retrieve alert rule definitions in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Retrieve alert rule definitions in a subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, ruleName, subscriptionId, data__properties` | Create or update an metric alert definition. |
| `delete` | `DELETE` | `resourceGroupName, ruleName, subscriptionId` | Delete an alert rule definition. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Retrieve alert rule definitions in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Retrieve alert rule definitions in a subscription. |
| `update` | `EXEC` | `resourceGroupName, ruleName, subscriptionId` | Update an metric alert definition. |
