---
title: virtual_network_gateway_nat_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_gateway_nat_rules
  - network
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
<tr><td><b>Name</b></td><td><code>virtual_network_gateway_nat_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_network_gateway_nat_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Parameters for VirtualNetworkGatewayNatRule. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="natRuleName, resourceGroupName, subscriptionId, virtualNetworkGatewayName" /> | Retrieves the details of a nat rule. |
| <CopyableCode code="list_by_virtual_network_gateway" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayName" /> | Retrieves all nat rules for a particular virtual network gateway. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="natRuleName, resourceGroupName, subscriptionId, virtualNetworkGatewayName" /> | Creates a nat rule to a scalable virtual network gateway if it doesn't exist else updates the existing nat rules. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="natRuleName, resourceGroupName, subscriptionId, virtualNetworkGatewayName" /> | Deletes a nat rule. |
