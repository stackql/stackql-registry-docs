---
title: registered_asns
hide_title: false
hide_table_of_contents: false
keywords:
  - registered_asns
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
<tr><td><b>Name</b></td><td><code>registered_asns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.peering.registered_asns" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` | The properties that define a registered ASN. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="peeringName, registeredAsnName, resourceGroupName, subscriptionId" /> | Gets an existing registered ASN with the specified name under the given subscription, resource group and peering. |
| <CopyableCode code="list_by_peering" /> | `SELECT` | <CopyableCode code="peeringName, resourceGroupName, subscriptionId" /> | Lists all registered ASNs under the given subscription, resource group and peering. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="peeringName, registeredAsnName, resourceGroupName, subscriptionId" /> | Creates a new registered ASN with the specified name under the given subscription, resource group and peering. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="peeringName, registeredAsnName, resourceGroupName, subscriptionId" /> | Deletes an existing registered ASN with the specified name under the given subscription, resource group and peering. |
