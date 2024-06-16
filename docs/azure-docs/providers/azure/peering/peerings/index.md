---
title: peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - peerings
  - peering
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
<tr><td><b>Name</b></td><td><code>peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.peering.peerings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="kind" /> | `string` | The kind of the peering. |
| <CopyableCode code="location" /> | `string` | The location of the resource. |
| <CopyableCode code="properties" /> | `object` | The properties that define connectivity to the Microsoft Cloud Edge. |
| <CopyableCode code="sku" /> | `object` | The SKU that defines the tier and kind of the peering. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="peeringName, resourceGroupName, subscriptionId" /> | Gets an existing peering with the specified name under the given subscription and resource group. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the peerings under the given subscription and resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the peerings under the given subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="peeringName, resourceGroupName, subscriptionId, data__kind, data__location, data__sku" /> | Creates a new peering or updates an existing peering with the specified name under the given subscription and resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="peeringName, resourceGroupName, subscriptionId" /> | Deletes an existing peering with the specified name under the given subscription and resource group. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="peeringName, resourceGroupName, subscriptionId" /> | Updates tags for a peering with the specified name under the given subscription and resource group. |
