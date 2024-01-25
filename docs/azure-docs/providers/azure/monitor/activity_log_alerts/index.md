---
title: activity_log_alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - activity_log_alerts
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
<tr><td><b>Name</b></td><td><code>activity_log_alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.activity_log_alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource Id. |
| `name` | `string` | The name of the resource. |
| `location` | `string` | The location of the resource. Since Azure Activity Log Alerts is a global service, the location of the rules should always be 'global'. |
| `properties` | `object` | An Azure Activity Log Alert rule. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `activityLogAlertName, resourceGroupName, subscriptionId` | Get an Activity Log Alert rule. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get a list of all Activity Log Alert rules in a resource group. |
| `list_by_subscription_id` | `SELECT` | `subscriptionId` | Get a list of all Activity Log Alert rules in a subscription. |
| `create_or_update` | `INSERT` | `activityLogAlertName, resourceGroupName, subscriptionId` | Create a new Activity Log Alert rule or update an existing one. |
| `delete` | `DELETE` | `activityLogAlertName, resourceGroupName, subscriptionId` | Delete an Activity Log Alert rule. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get a list of all Activity Log Alert rules in a resource group. |
| `_list_by_subscription_id` | `EXEC` | `subscriptionId` | Get a list of all Activity Log Alert rules in a subscription. |
| `update` | `EXEC` | `activityLogAlertName, resourceGroupName, subscriptionId` | Updates 'tags' and 'enabled' fields in an existing Alert rule. This method is used to update the Alert rule tags, and to enable or disable the Alert rule. To update other fields use CreateOrUpdate operation. |
