---
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
  - dev_test_labs
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
<tr><td><b>Name</b></td><td><code>virtual_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.virtual_machines" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a virtual machine. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, labName, name, resourceGroupName, subscriptionId" /> | Get virtual machine. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, labName, resourceGroupName, subscriptionId" /> | List virtual machines in a given lab. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, labName, name, resourceGroupName, subscriptionId, data__properties" /> | Create or replace an existing virtual machine. This operation can take a while to complete. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, labName, name, resourceGroupName, subscriptionId" /> | Delete virtual machine. This operation can take a while to complete. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, labName, resourceGroupName, subscriptionId" /> | List virtual machines in a given lab. |
| <CopyableCode code="add_data_disk" /> | `EXEC` | <CopyableCode code="api-version, labName, name, resourceGroupName, subscriptionId" /> | Attach a new or existing data disk to virtual machine. This operation can take a while to complete. |
| <CopyableCode code="apply_artifacts" /> | `EXEC` | <CopyableCode code="api-version, labName, name, resourceGroupName, subscriptionId" /> | Apply artifacts to virtual machine. This operation can take a while to complete. |
| <CopyableCode code="claim" /> | `EXEC` | <CopyableCode code="api-version, labName, name, resourceGroupName, subscriptionId" /> | Take ownership of an existing virtual machine This operation can take a while to complete. |
| <CopyableCode code="detach_data_disk" /> | `EXEC` | <CopyableCode code="api-version, labName, name, resourceGroupName, subscriptionId" /> | Detach the specified disk from the virtual machine. This operation can take a while to complete. |
| <CopyableCode code="redeploy" /> | `EXEC` | <CopyableCode code="api-version, labName, name, resourceGroupName, subscriptionId" /> | Redeploy a virtual machine This operation can take a while to complete. |
| <CopyableCode code="resize" /> | `EXEC` | <CopyableCode code="api-version, labName, name, resourceGroupName, subscriptionId" /> | Resize Virtual Machine. This operation can take a while to complete. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="api-version, labName, name, resourceGroupName, subscriptionId" /> | Restart a virtual machine. This operation can take a while to complete. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="api-version, labName, name, resourceGroupName, subscriptionId" /> | Start a virtual machine. This operation can take a while to complete. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="api-version, labName, name, resourceGroupName, subscriptionId" /> | Stop a virtual machine This operation can take a while to complete. |
| <CopyableCode code="transfer_disks" /> | `EXEC` | <CopyableCode code="api-version, labName, name, resourceGroupName, subscriptionId" /> | Transfers all data disks attached to the virtual machine to be owned by the current user. This operation can take a while to complete. |
| <CopyableCode code="un_claim" /> | `EXEC` | <CopyableCode code="api-version, labName, name, resourceGroupName, subscriptionId" /> | Release ownership of an existing virtual machine This operation can take a while to complete. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, labName, name, resourceGroupName, subscriptionId" /> | Allows modifying tags of virtual machines. All other properties will be ignored. |
