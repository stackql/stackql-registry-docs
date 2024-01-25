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
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_by_notification` | `SELECT` | `notificationName, resourceGroupName, serviceName, subscriptionId` | Gets the list of the Notification Recipient User subscribed to the notification. |
| `create_or_update` | `INSERT` | `notificationName, resourceGroupName, serviceName, subscriptionId, userId` | Adds the API Management User to the list of Recipients for the Notification. |
| `delete` | `DELETE` | `notificationName, resourceGroupName, serviceName, subscriptionId, userId` | Removes the API Management user from the list of Notification. |
| `_list_by_notification` | `EXEC` | `notificationName, resourceGroupName, serviceName, subscriptionId` | Gets the list of the Notification Recipient User subscribed to the notification. |
| `check_entity_exists` | `EXEC` | `notificationName, resourceGroupName, serviceName, subscriptionId, userId` | Determine if the Notification Recipient User is subscribed to the notification. |
