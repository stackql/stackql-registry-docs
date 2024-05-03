---
title: l2_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - l2_networks
  - nexus
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
<tr><td><b>Name</b></td><td><code>l2_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.l2_networks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` |  |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="l2NetworkName, resourceGroupName, subscriptionId" /> | Get properties of the provided layer 2 (L2) network. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of layer 2 (L2) networks in the provided resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of layer 2 (L2) networks in the provided subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="l2NetworkName, resourceGroupName, subscriptionId, data__extendedLocation, data__properties" /> | Create a new layer 2 (L2) network or update the properties of the existing network. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="l2NetworkName, resourceGroupName, subscriptionId" /> | Delete the provided layer 2 (L2) network. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of layer 2 (L2) networks in the provided resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Get a list of layer 2 (L2) networks in the provided subscription. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="l2NetworkName, resourceGroupName, subscriptionId" /> | Update tags associated with the provided layer 2 (L2) network. |
