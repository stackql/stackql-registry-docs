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
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_by_notification` | `SELECT` | `notificationName, resourceGroupName, serviceName, subscriptionId` | Gets the list of the Notification Recipient Emails subscribed to a notification. |
| `create_or_update` | `INSERT` | `email, notificationName, resourceGroupName, serviceName, subscriptionId` | Adds the Email address to the list of Recipients for the Notification. |
| `delete` | `DELETE` | `email, notificationName, resourceGroupName, serviceName, subscriptionId` | Removes the email from the list of Notification. |
| `_list_by_notification` | `EXEC` | `notificationName, resourceGroupName, serviceName, subscriptionId` | Gets the list of the Notification Recipient Emails subscribed to a notification. |
| `check_entity_exists` | `EXEC` | `email, notificationName, resourceGroupName, serviceName, subscriptionId` | Determine if Notification Recipient Email subscribed to the notification. |
