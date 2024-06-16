---
title: prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - prefixes
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
<tr><td><b>Name</b></td><td><code>prefixes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.peering.prefixes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` | The peering service prefix properties class. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="peeringServiceName, prefixName, resourceGroupName, subscriptionId" /> | Gets an existing prefix with the specified name under the given subscription, resource group and peering service. |
| <CopyableCode code="list_by_peering_service" /> | `SELECT` | <CopyableCode code="peeringServiceName, resourceGroupName, subscriptionId" /> | Lists all prefixes under the given subscription, resource group and peering service. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="peeringServiceName, prefixName, resourceGroupName, subscriptionId" /> | Creates a new prefix with the specified name under the given subscription, resource group and peering service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="peeringServiceName, prefixName, resourceGroupName, subscriptionId" /> | Deletes an existing prefix with the specified name under the given subscription, resource group and peering service. |
