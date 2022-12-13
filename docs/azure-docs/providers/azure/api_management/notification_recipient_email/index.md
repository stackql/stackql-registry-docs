---
title: notification_recipient_email
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_recipient_email
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
<tr><td><b>Name</b></td><td><code>notification_recipient_email</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.notification_recipient_email</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Recipient Email Contract Properties. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `NotificationRecipientEmail_ListByNotification` | `SELECT` | `notificationName, resourceGroupName, serviceName, subscriptionId` | Gets the list of the Notification Recipient Emails subscribed to a notification. |
| `NotificationRecipientEmail_CreateOrUpdate` | `INSERT` | `email, notificationName, resourceGroupName, serviceName, subscriptionId` | Adds the Email address to the list of Recipients for the Notification. |
| `NotificationRecipientEmail_Delete` | `DELETE` | `email, notificationName, resourceGroupName, serviceName, subscriptionId` | Removes the email from the list of Notification. |
| `NotificationRecipientEmail_CheckEntityExists` | `EXEC` | `email, notificationName, resourceGroupName, serviceName, subscriptionId` | Determine if Notification Recipient Email subscribed to the notification. |
