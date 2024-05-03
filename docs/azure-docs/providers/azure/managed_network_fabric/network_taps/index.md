---
title: network_taps
hide_title: false
hide_table_of_contents: false
keywords:
  - network_taps
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
<tr><td><b>Name</b></td><td><code>network_taps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.network_taps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Network Tap Properties defines the properties of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkTapName, resourceGroupName, subscriptionId" /> | Retrieves details of this Network Tap. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Displays Network Taps list by resource group GET method. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Displays Network Taps list by subscription GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="networkTapName, resourceGroupName, subscriptionId, data__properties" /> | Creates a Network Tap. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkTapName, resourceGroupName, subscriptionId" /> | Deletes Network Tap. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Displays Network Taps list by resource group GET method. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Displays Network Taps list by subscription GET method. |
| <CopyableCode code="resync" /> | `EXEC` | <CopyableCode code="networkTapName, resourceGroupName, subscriptionId" /> | Implements the operation to the underlying resources. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="networkTapName, resourceGroupName, subscriptionId" /> | API to update certain properties of the Network Tap resource. |
