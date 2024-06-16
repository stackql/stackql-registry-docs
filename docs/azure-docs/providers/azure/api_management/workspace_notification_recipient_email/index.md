---
title: workspace_notification_recipient_email
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_notification_recipient_email
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_notification_recipient_email</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_notification_recipient_email" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_notification" /> | `SELECT` | <CopyableCode code="notificationName, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Gets the list of the Notification Recipient Emails subscribed to a notification. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="email, notificationName, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Adds the Email address to the list of Recipients for the Notification. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="email, notificationName, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Removes the email from the list of Notification. |
