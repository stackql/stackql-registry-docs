---
title: alert_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_rules
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
<tr><td><b>Name</b></td><td><code>alert_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.alert_rules</code></td></tr>
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
| `get` | `SELECT` | `resourceGroupName, ruleName, subscriptionId` | Gets a classic metric alert rule |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List the classic metric alert rules within a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List the classic metric alert rules within a subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, ruleName, subscriptionId, data__properties` | Creates or updates a classic metric alert rule. |
| `delete` | `DELETE` | `resourceGroupName, ruleName, subscriptionId` | Deletes a classic metric alert rule |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List the classic metric alert rules within a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List the classic metric alert rules within a subscription. |
| `update` | `EXEC` | `resourceGroupName, ruleName, subscriptionId` | Updates an existing classic metric AlertRuleResource. To update other fields use the CreateOrUpdate method. |
