---
title: network_functions
hide_title: false
hide_table_of_contents: false
keywords:
  - network_functions
  - mpc_network_function
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
<tr><td><b>Name</b></td><td><code>network_functions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mpc_network_function.network_functions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Network Function Properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkFunctionName, resourceGroupName, subscriptionId" /> | Get a NetworkFunctionResource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List NetworkFunctionResource resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List NetworkFunctionResource resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkFunctionName, resourceGroupName, subscriptionId" /> | Create a NetworkFunctionResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkFunctionName, resourceGroupName, subscriptionId" /> | Delete a NetworkFunctionResource |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List NetworkFunctionResource resources by resource group |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | List NetworkFunctionResource resources by subscription ID |
