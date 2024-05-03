---
title: machine_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - machine_groups
  - service_map
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
<tr><td><b>Name</b></td><td><code>machine_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_map.machine_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Resource ETAG. |
| <CopyableCode code="kind" /> | `string` | Additional resource type qualifier. |
| <CopyableCode code="properties" /> | `object` | Resource properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="machineGroupName, resourceGroupName, subscriptionId, workspaceName" /> | Returns the specified machine group as it existed during the specified time interval. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Returns all machine groups during the specified time interval. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Creates a new machine group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="machineGroupName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes the specified Machine Group. |
| <CopyableCode code="_list_by_workspace" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Returns all machine groups during the specified time interval. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="machineGroupName, resourceGroupName, subscriptionId, workspaceName" /> | Updates a machine group. |
