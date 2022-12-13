---
title: notification_recipient_user
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_recipient_user
  - api_management
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
<tr><td><b>Name</b></td><td><code>notification_recipient_user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.notification_recipient_user</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Recipient User Contract Properties. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `NotificationRecipientUser_ListByNotification` | `SELECT` | `notificationName, resourceGroupName, serviceName, subscriptionId` | Gets the list of the Notification Recipient User subscribed to the notification. |
| `NotificationRecipientUser_CreateOrUpdate` | `INSERT` | `notificationName, resourceGroupName, serviceName, subscriptionId, userId` | Adds the API Management User to the list of Recipients for the Notification. |
| `NotificationRecipientUser_Delete` | `DELETE` | `notificationName, resourceGroupName, serviceName, subscriptionId, userId` | Removes the API Management user from the list of Notification. |
| `NotificationRecipientUser_CheckEntityExists` | `EXEC` | `notificationName, resourceGroupName, serviceName, subscriptionId, userId` | Determine if the Notification Recipient User is subscribed to the notification. |
