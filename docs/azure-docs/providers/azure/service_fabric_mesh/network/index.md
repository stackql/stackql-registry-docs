---
title: network
hide_title: false
hide_table_of_contents: false
keywords:
  - network
  - service_fabric_mesh
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
<tr><td><b>Name</b></td><td><code>network</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_mesh.network" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Describes properties of a network resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, networkResourceName, resourceGroupName, subscriptionId" /> | Gets the information about the network resource with the given name. The information include the description and other properties of the network. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Gets the information about all network resources in a given resource group. The information include the description and other properties of the Network. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | Gets the information about all network resources in a given resource group. The information include the description and other properties of the network. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, networkResourceName, resourceGroupName, subscriptionId, data__properties" /> | Creates a network resource with the specified name, description and properties. If a network resource with the same name exists, then it is updated with the specified description and properties. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, networkResourceName, resourceGroupName, subscriptionId" /> | Deletes the network resource identified by the name. |
