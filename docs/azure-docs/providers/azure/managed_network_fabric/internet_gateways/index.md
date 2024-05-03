---
title: internet_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - internet_gateways
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
<tr><td><b>Name</b></td><td><code>internet_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.internet_gateways" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Internet Gateway Properties defines the properties of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="internetGatewayName, resourceGroupName, subscriptionId" /> | Implements Gateway GET method. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Displays Internet Gateways list by resource group GET method. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Displays Internet Gateways list by subscription GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="internetGatewayName, resourceGroupName, subscriptionId, data__properties" /> | Creates a Network Fabric Service Internet Gateway resource instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="internetGatewayName, resourceGroupName, subscriptionId" /> | Execute a delete on Network Fabric Service Internet Gateway. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Displays Internet Gateways list by resource group GET method. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Displays Internet Gateways list by subscription GET method. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="internetGatewayName, resourceGroupName, subscriptionId" /> | Execute patch on Network Fabric Service Internet Gateway. |
