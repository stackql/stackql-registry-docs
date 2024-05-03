---
title: hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - hubs
  - customer_insights
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.customer_insights.hubs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of hub. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Gets information about the specified hub. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all hubs in the specified subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the hubs in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Creates a hub, or updates an existing hub. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Deletes the specified hub. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Gets all hubs in the specified subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the hubs in a resource group. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Updates a Hub. |
