---
title: pending_flows
hide_title: false
hide_table_of_contents: false
keywords:
  - pending_flows
  - data_transfer
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>pending_flows</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pending_flows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_transfer.pending_flows" /></td></tr>
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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="connectionName, resourceGroupName, subscriptionId" /> | Lists all pending flows for a connection. |

## `SELECT` examples

Lists all pending flows for a connection.


```sql
SELECT
connection,
connectionId,
dataType,
flowId,
flowType,
keyVaultUri,
linkStatus,
linkedFlowId,
location,
messagingOptions,
policies,
provisioningState,
schema,
serviceBusQueueId,
status,
storageAccountId,
storageAccountName,
storageContainerName,
subscriptionId,
tags
FROM azure.data_transfer.pending_flows
WHERE connectionName = '{{ connectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```