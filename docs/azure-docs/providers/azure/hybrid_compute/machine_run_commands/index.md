---
title: machine_run_commands
hide_title: false
hide_table_of_contents: false
keywords:
  - machine_run_commands
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
<tr><td><b>Name</b></td><td><code>machine_run_commands</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_compute.machine_run_commands" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a run command. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="machineName, resourceGroupName, runCommandName, subscriptionId" /> | The operation to get a run command. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="machineName, resourceGroupName, subscriptionId" /> | The operation to get all the run commands of a non-Azure machine. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="machineName, resourceGroupName, runCommandName, subscriptionId" /> | The operation to create or update a run command. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="machineName, resourceGroupName, runCommandName, subscriptionId" /> | The operation to delete a run command. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="machineName, resourceGroupName, subscriptionId" /> | The operation to get all the run commands of a non-Azure machine. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="machineName, resourceGroupName, runCommandName, subscriptionId" /> | The operation to update the run command. |
