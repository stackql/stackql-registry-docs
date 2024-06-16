---
title: vnet_peering
hide_title: false
hide_table_of_contents: false
keywords:
  - vnet_peering
  - databricks
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>vnet_peering</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.databricks.vnet_peering" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Name of the virtual network peering resource |
| <CopyableCode code="properties" /> | `object` | Properties of the virtual network peering. |
| <CopyableCode code="type" /> | `string` | type of the virtual network peering resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="peeringName, resourceGroupName, subscriptionId, workspaceName" /> | Gets the workspace vNet Peering. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Lists the workspace vNet Peerings. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="peeringName, resourceGroupName, subscriptionId, workspaceName, data__properties" /> | Creates vNet Peering for workspace. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="peeringName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes the workspace vNetPeering. |
