---
title: registered_prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - registered_prefixes
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
<tr><td><b>Name</b></td><td><code>registered_prefixes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.peering.registered_prefixes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` | The properties that define a registered prefix. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="peeringName, registeredPrefixName, resourceGroupName, subscriptionId" /> | Gets an existing registered prefix with the specified name under the given subscription, resource group and peering. |
| <CopyableCode code="list_by_peering" /> | `SELECT` | <CopyableCode code="peeringName, resourceGroupName, subscriptionId" /> | Lists all registered prefixes under the given subscription, resource group and peering. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="peeringName, registeredPrefixName, resourceGroupName, subscriptionId" /> | Creates a new registered prefix with the specified name under the given subscription, resource group and peering. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="peeringName, registeredPrefixName, resourceGroupName, subscriptionId" /> | Deletes an existing registered prefix with the specified name under the given subscription, resource group and peering. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="peeringName, registeredPrefixName, resourceGroupName, subscriptionId" /> | Validates an existing registered prefix with the specified name under the given subscription, resource group and peering. |
