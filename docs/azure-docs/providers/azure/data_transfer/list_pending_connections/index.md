---
title: list_pending_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - list_pending_connections
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
<tr><td><b>Name</b></td><td><code>list_pending_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_transfer.list_pending_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="approver" /> | `string` | Approver of this connection request |
| <CopyableCode code="dateSubmitted" /> | `string` | The timestamp that this connection request was submitted at |
| <CopyableCode code="direction" /> | `string` | Direction of data movement |
| <CopyableCode code="flowTypes" /> | `array` | The flow types that are allowed for this resource |
| <CopyableCode code="justification" /> | `string` | Justification for the connection request |
| <CopyableCode code="linkStatus" /> | `string` | Link status of the current connection |
| <CopyableCode code="linkedConnectionId" /> | `string` | Resource ID of the linked connection |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="pin" /> | `string` | PIN to link requests together |
| <CopyableCode code="pipeline" /> | `string` | Pipeline to use to transfer data |
| <CopyableCode code="policies" /> | `array` | The policies for this connection |
| <CopyableCode code="primaryContact" /> | `string` | The primary contact for this connection request |
| <CopyableCode code="provisioningState" /> | `string` | Provisioning state of the connection |
| <CopyableCode code="remoteSubscriptionId" /> | `string` | Subscription ID to link cloud subscriptions together |
| <CopyableCode code="requirementId" /> | `string` | Requirement ID of the connection |
| <CopyableCode code="schemas" /> | `array` | The schemas for this connection |
| <CopyableCode code="secondaryContacts" /> | `array` | The secondary contacts for this connection request |
| <CopyableCode code="status" /> | `string` | Status of the connection |
| <CopyableCode code="statusReason" /> | `string` | Reason for status |
| <CopyableCode code="subscriptionId" /> | `string` | Subscription ID of the pending connection. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="connectionName, resourceGroupName, subscriptionId" /> |
