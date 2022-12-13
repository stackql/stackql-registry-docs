---
title: notification_hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_hubs
  - notification_hubs
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
<tr><td><b>Name</b></td><td><code>notification_hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.notification_hubs.notification_hubs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `location` | `string` | Resource location |
| `properties` | `object` | NotificationHub properties. |
| `sku` | `object` | The Sku description for a namespace |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `NotificationHubs_Get` | `SELECT` | `namespaceName, notificationHubName, resourceGroupName, subscriptionId` | Lists the notification hubs associated with a namespace. |
| `NotificationHubs_List` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` | Lists the notification hubs associated with a namespace. |
| `NotificationHubs_CreateOrUpdate` | `INSERT` | `namespaceName, notificationHubName, resourceGroupName, subscriptionId, data__properties` | Creates/Update a NotificationHub in a namespace. |
| `NotificationHubs_Delete` | `DELETE` | `namespaceName, notificationHubName, resourceGroupName, subscriptionId` | Deletes a notification hub associated with a namespace. |
| `NotificationHubs_CheckNotificationHubAvailability` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId, data__name` | Checks the availability of the given notificationHub in a namespace. |
| `NotificationHubs_CreateOrUpdateAuthorizationRule` | `EXEC` | `authorizationRuleName, namespaceName, notificationHubName, resourceGroupName, subscriptionId, data__properties` | Creates/Updates an authorization rule for a NotificationHub |
| `NotificationHubs_DebugSend` | `EXEC` | `namespaceName, notificationHubName, resourceGroupName, subscriptionId` | test send a push notification |
| `NotificationHubs_DeleteAuthorizationRule` | `EXEC` | `authorizationRuleName, namespaceName, notificationHubName, resourceGroupName, subscriptionId` | Deletes a notificationHub authorization rule |
| `NotificationHubs_GetAuthorizationRule` | `EXEC` | `authorizationRuleName, namespaceName, notificationHubName, resourceGroupName, subscriptionId` | Gets an authorization rule for a NotificationHub by name. |
| `NotificationHubs_GetPnsCredentials` | `EXEC` | `namespaceName, notificationHubName, resourceGroupName, subscriptionId` | Lists the PNS Credentials associated with a notification hub . |
| `NotificationHubs_ListAuthorizationRules` | `EXEC` | `namespaceName, notificationHubName, resourceGroupName, subscriptionId` | Gets the authorization rules for a NotificationHub. |
| `NotificationHubs_ListKeys` | `EXEC` | `authorizationRuleName, namespaceName, notificationHubName, resourceGroupName, subscriptionId` | Gets the Primary and Secondary ConnectionStrings to the NotificationHub  |
| `NotificationHubs_Patch` | `EXEC` | `namespaceName, notificationHubName, resourceGroupName, subscriptionId` | Patch a NotificationHub in a namespace. |
| `NotificationHubs_RegenerateKeys` | `EXEC` | `authorizationRuleName, namespaceName, notificationHubName, resourceGroupName, subscriptionId` | Regenerates the Primary/Secondary Keys to the NotificationHub Authorization Rule |
