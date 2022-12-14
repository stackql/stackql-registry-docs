---
title: action_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - action_groups
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
<tr><td><b>Name</b></td><td><code>action_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.action_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource Id |
| `name` | `string` | Azure resource name |
| `properties` | `object` | An Azure action group. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Azure resource type |
| `location` | `string` | Resource location |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ActionGroups_Get` | `SELECT` | `actionGroupName, resourceGroupName, subscriptionId` | Get an action group. |
| `ActionGroups_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Get a list of all action groups in a resource group. |
| `ActionGroups_ListBySubscriptionId` | `SELECT` | `subscriptionId` | Get a list of all action groups in a subscription. |
| `ActionGroups_CreateOrUpdate` | `INSERT` | `actionGroupName, resourceGroupName, subscriptionId` | Create a new action group or update an existing one. |
| `ActionGroups_Delete` | `DELETE` | `actionGroupName, resourceGroupName, subscriptionId` | Delete an action group. |
| `ActionGroups_CreateNotificationsAtActionGroupResourceLevel` | `EXEC` | `actionGroupName, resourceGroupName, subscriptionId, data__alertType` | Send test notifications to a set of provided receivers |
| `ActionGroups_CreateNotificationsAtResourceGroupLevel` | `EXEC` | `resourceGroupName, subscriptionId, data__alertType` | Send test notifications to a set of provided receivers |
| `ActionGroups_EnableReceiver` | `EXEC` | `actionGroupName, resourceGroupName, subscriptionId, data__receiverName` | Enable a receiver in an action group. This changes the receiver's status from Disabled to Enabled. This operation is only supported for Email or SMS receivers. |
| `ActionGroups_GetTestNotifications` | `EXEC` | `notificationId, subscriptionId` | Get the test notifications by the notification id |
| `ActionGroups_GetTestNotificationsAtActionGroupResourceLevel` | `EXEC` | `actionGroupName, notificationId, resourceGroupName, subscriptionId` | Get the test notifications by the notification id |
| `ActionGroups_GetTestNotificationsAtResourceGroupLevel` | `EXEC` | `notificationId, resourceGroupName, subscriptionId` | Get the test notifications by the notification id |
| `ActionGroups_PostTestNotifications` | `EXEC` | `subscriptionId, data__alertType` | Send test notifications to a set of provided receivers |
| `ActionGroups_Update` | `EXEC` | `actionGroupName, resourceGroupName, subscriptionId` | Updates an existing action group's tags. To update other fields use the CreateOrUpdate method. |
