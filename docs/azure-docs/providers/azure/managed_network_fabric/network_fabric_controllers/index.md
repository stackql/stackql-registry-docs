---
title: network_fabric_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - network_fabric_controllers
  - managed_network_fabric
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
<tr><td><b>Name</b></td><td><code>network_fabric_controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.network_fabric_controllers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | NetworkFabricControllerProperties defines the resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkFabricControllerName, resourceGroupName, subscriptionId" /> | Shows the provisioning status of Network Fabric Controller. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the NetworkFabricControllers thats available in the resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the NetworkFabricControllers by subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="networkFabricControllerName, resourceGroupName, subscriptionId, data__properties" /> | Creates a Network Fabric Controller. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkFabricControllerName, resourceGroupName, subscriptionId" /> | Deletes the Network Fabric Controller resource. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="networkFabricControllerName, resourceGroupName, subscriptionId" /> | Updates are currently not supported for the Network Fabric Controller resource. |
