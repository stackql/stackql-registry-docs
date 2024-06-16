---
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
  - nexus
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.virtual_machines" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` |  |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineName" /> | Get properties of the provided virtual machine. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of virtual machines in the provided resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of virtual machines in the provided subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineName, data__extendedLocation, data__properties" /> | Create a new virtual machine or update the properties of the existing virtual machine. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineName" /> | Delete the provided virtual machine. |
| <CopyableCode code="power_off" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineName" /> | Power off the provided virtual machine. |
| <CopyableCode code="reimage" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineName" /> | Reimage the provided virtual machine. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineName" /> | Restart the provided virtual machine. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineName" /> | Start the provided virtual machine. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineName" /> | Patch the properties of the provided virtual machine, or update the tags associated with the virtual machine. Properties and tag updates can be done independently. |
