---
title: machines
hide_title: false
hide_table_of_contents: false
keywords:
  - machines
  - hybrid_compute
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
<tr><td><b>Name</b></td><td><code>machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_compute.machines" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="kind" /> | `string` | Indicates which kind of Arc machine placement on-premises, such as HCI, SCVMM or VMware etc. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a hybrid machine. |
| <CopyableCode code="resources" /> | `array` | The list of extensions affiliated to the machine |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="machineName, resourceGroupName, subscriptionId" /> | Retrieves information about the model view or the instance view of a hybrid machine. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the hybrid machines in the specified resource group. Use the nextLink property in the response to get the next page of hybrid machines. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the hybrid machines in the specified subscription. Use the nextLink property in the response to get the next page of hybrid machines. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="machineName, resourceGroupName, subscriptionId" /> | The operation to create or update a hybrid machine. Please note some properties can be set only during machine creation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="machineName, resourceGroupName, subscriptionId" /> | The operation to delete a hybrid machine. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the hybrid machines in the specified resource group. Use the nextLink property in the response to get the next page of hybrid machines. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists all the hybrid machines in the specified subscription. Use the nextLink property in the response to get the next page of hybrid machines. |
| <CopyableCode code="assess_patches" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | The operation to assess patches on a hybrid machine identity in Azure. |
| <CopyableCode code="install_patches" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId, data__maximumDuration, data__rebootSetting" /> | The operation to install patches on a hybrid machine identity in Azure. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="machineName, resourceGroupName, subscriptionId" /> | The operation to update a hybrid machine. |
