---
title: subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription
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
<tr><td><b>Name</b></td><td><code>subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.subscription" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, sid, subscriptionId" /> | Gets the specified Subscription entity. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists all subscriptions of the API Management service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, serviceName, sid, subscriptionId" /> | Creates or updates the subscription of specified user to the specified product. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, resourceGroupName, serviceName, sid, subscriptionId" /> | Deletes the specified subscription. |
| <CopyableCode code="regenerate_primary_key" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, sid, subscriptionId" /> | Regenerates primary key of existing subscription of the API Management service instance. |
| <CopyableCode code="regenerate_secondary_key" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, sid, subscriptionId" /> | Regenerates secondary key of existing subscription of the API Management service instance. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="If-Match, resourceGroupName, serviceName, sid, subscriptionId" /> | Updates the details of a subscription specified by its identifier. |
