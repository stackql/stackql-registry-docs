---
title: internet_gateway_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - internet_gateway_rules
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
<tr><td><b>Name</b></td><td><code>internet_gateway_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.internet_gateway_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Internet Gateway Rule Properties defines the resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="internetGatewayRuleName, resourceGroupName, subscriptionId" /> | Gets an Internet Gateway Rule resource. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Implements Internet Gateway Rules list by resource group GET method. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all Internet Gateway rules in the given subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="internetGatewayRuleName, resourceGroupName, subscriptionId, data__properties" /> | Creates an Internet Gateway rule resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="internetGatewayRuleName, resourceGroupName, subscriptionId" /> | Implements Internet Gateway Rules DELETE method. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Implements Internet Gateway Rules list by resource group GET method. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | List all Internet Gateway rules in the given subscription. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="internetGatewayRuleName, resourceGroupName, subscriptionId" /> | API to update certain properties of the Internet Gateway Rule resource. |
