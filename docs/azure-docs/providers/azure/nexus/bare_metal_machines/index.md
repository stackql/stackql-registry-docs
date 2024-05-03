---
title: bare_metal_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - bare_metal_machines
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
<tr><td><b>Name</b></td><td><code>bare_metal_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.bare_metal_machines" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId" /> | Get properties of the provided bare metal machine. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of bare metal machines in the provided resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of bare metal machines in the provided subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId, data__extendedLocation, data__properties" /> | Create a new bare metal machine or update the properties of the existing one.<br />All customer initiated requests will be rejected as the life cycle of this resource is managed by the system. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId" /> | Delete the provided bare metal machine.<br />All customer initiated requests will be rejected as the life cycle of this resource is managed by the system. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of bare metal machines in the provided resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Get a list of bare metal machines in the provided subscription. |
| <CopyableCode code="cordon" /> | `EXEC` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId" /> | Cordon the provided bare metal machine's Kubernetes node. |
| <CopyableCode code="power_off" /> | `EXEC` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId" /> | Power off the provided bare metal machine. |
| <CopyableCode code="reimage" /> | `EXEC` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId" /> | Reimage the provided bare metal machine. |
| <CopyableCode code="replace" /> | `EXEC` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId" /> | Replace the provided bare metal machine. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId" /> | Restart the provided bare metal machine. |
| <CopyableCode code="run_command" /> | `EXEC` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId, data__limitTimeSeconds, data__script" /> | Run the command or the script on the provided bare metal machine. The URL to storage account with the command execution results and the command exit code can be retrieved from the operation status API once available. |
| <CopyableCode code="run_data_extracts" /> | `EXEC` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId, data__commands, data__limitTimeSeconds" /> | Run one or more data extractions on the provided bare metal machine. The URL to storage account with the command execution results and the command exit code can be retrieved from the operation status API once available. |
| <CopyableCode code="run_read_commands" /> | `EXEC` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId, data__commands, data__limitTimeSeconds" /> | Run one or more read-only commands on the provided bare metal machine. The URL to storage account with the command execution results and the command exit code can be retrieved from the operation status API once available. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId" /> | Start the provided bare metal machine. |
| <CopyableCode code="uncordon" /> | `EXEC` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId" /> | Uncordon the provided bare metal machine's Kubernetes node. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId" /> | Patch properties of the provided bare metal machine, or update tags associated with the bare metal machine. Properties and tag updates can be done independently. |
