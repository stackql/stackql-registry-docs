---
title: workspace_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_subscription
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
<tr><td><b>Name</b></td><td><code>workspace_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_subscription" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, sid, subscriptionId, workspaceId" /> | Gets the specified Subscription entity. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Lists all subscriptions of the workspace in an API Management service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, serviceName, sid, subscriptionId, workspaceId" /> | Creates or updates the subscription of specified user to the specified product. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, resourceGroupName, serviceName, sid, subscriptionId, workspaceId" /> | Deletes the specified subscription. |
| <CopyableCode code="regenerate_primary_key" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, sid, subscriptionId, workspaceId" /> | Regenerates primary key of existing subscription of the workspace in an API Management service instance. |
| <CopyableCode code="regenerate_secondary_key" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, sid, subscriptionId, workspaceId" /> | Regenerates secondary key of existing subscription of the workspace in an API Management service instance. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="If-Match, resourceGroupName, serviceName, sid, subscriptionId, workspaceId" /> | Updates the details of a subscription specified by its identifier. |
