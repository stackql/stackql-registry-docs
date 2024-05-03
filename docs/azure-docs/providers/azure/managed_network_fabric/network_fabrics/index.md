---
title: network_fabrics
hide_title: false
hide_table_of_contents: false
keywords:
  - network_fabrics
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
<tr><td><b>Name</b></td><td><code>network_fabrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.network_fabrics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Network Fabric Properties defines the properties of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId" /> | Get Network Fabric resource details. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the Network Fabric resources in the given resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all the Network Fabric resources in the given subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId, data__properties" /> | Create Network Fabric resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId" /> | Delete Network Fabric resource. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the Network Fabric resources in the given resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | List all the Network Fabric resources in the given subscription. |
| <CopyableCode code="commit_configuration" /> | `EXEC` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId" /> | Atomic update of the given Network Fabric instance. Sync update of NFA resources at Fabric level. |
| <CopyableCode code="deprovision" /> | `EXEC` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId" /> | Deprovisions the underlying resources in the given Network Fabric instance. |
| <CopyableCode code="provision" /> | `EXEC` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId" /> | Provisions the underlying resources in the given Network Fabric instance. |
| <CopyableCode code="refresh_configuration" /> | `EXEC` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId" /> | Refreshes the configuration of the underlying resources in the given Network Fabric instance. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId" /> | Update certain properties of the Network Fabric resource. |
| <CopyableCode code="upgrade" /> | `EXEC` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId" /> | Upgrades the version of the underlying resources in the given Network Fabric instance. |
| <CopyableCode code="validate_configuration" /> | `EXEC` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId" /> | Validates the configuration of the underlying resources in the given Network Fabric instance. |
