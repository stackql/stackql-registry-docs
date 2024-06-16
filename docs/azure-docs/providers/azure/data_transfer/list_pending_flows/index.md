---
title: list_pending_flows
hide_title: false
hide_table_of_contents: false
keywords:
  - list_pending_flows
  - data_transfer
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
<tr><td><b>Name</b></td><td><code>list_pending_flows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_transfer.list_pending_flows" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="connection" /> | `object` | A resource selected from ARM |
| <CopyableCode code="connectionId" /> | `string` | Connection ID of the pending flow. |
| <CopyableCode code="dataType" /> | `string` | Transfer Storage Blobs or Tables |
| <CopyableCode code="flowId" /> | `string` | Dataflow GUID associated with this flow |
| <CopyableCode code="flowType" /> | `string` | Flow type for the specified resource |
| <CopyableCode code="keyVaultUri" /> | `string` | AME, PME, or TORUS only! AKV Chain Containing SAS Token |
| <CopyableCode code="linkStatus" /> | `string` | Link status of the current flow |
| <CopyableCode code="linkedFlowId" /> | `string` | Resource ID of the linked flow |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="messagingOptions" /> | `object` | The option associated with messaging flows. |
| <CopyableCode code="policies" /> | `array` | The policies for this flow |
| <CopyableCode code="provisioningState" /> | `string` | Provisioning state of the flow |
| <CopyableCode code="schema" /> | `object` | The schema object. |
| <CopyableCode code="serviceBusQueueId" /> | `string` | Service Bus Queue ID |
| <CopyableCode code="status" /> | `string` | Status of the current flow |
| <CopyableCode code="storageAccountId" /> | `string` | Storage Account ID |
| <CopyableCode code="storageAccountName" /> | `string` | Storage Account |
| <CopyableCode code="storageContainerName" /> | `string` | Storage Container Name |
| <CopyableCode code="subscriptionId" /> | `string` | Subscription ID of the pending flow. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="connectionName, resourceGroupName, subscriptionId" /> |
