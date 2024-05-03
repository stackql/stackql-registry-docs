---
title: scale_unit_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - scale_unit_nodes
  - fabric_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>scale_unit_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.fabric_admin.scale_unit_nodes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | The region where the resource is located. |
| <CopyableCode code="properties" /> | `object` | Holds all properties related to a scale unit node. |
| <CopyableCode code="tags" /> | `object` | List of key-value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, scaleUnitNode, subscriptionId" /> | Return the requested scale unit node. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns a list of all scale unit nodes in a location. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns a list of all scale unit nodes in a location. |
| <CopyableCode code="power_off" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, scaleUnitNode, subscriptionId" /> | Power off a scale unit node. |
| <CopyableCode code="power_on" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, scaleUnitNode, subscriptionId" /> | Power on a scale unit node. |
| <CopyableCode code="repair" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, scaleUnitNode, subscriptionId" /> | Repairs a node of the cluster. |
| <CopyableCode code="shutdown" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, scaleUnitNode, subscriptionId" /> | Shutdown a scale unit node. |
| <CopyableCode code="start_maintenance_mode" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, scaleUnitNode, subscriptionId" /> | Start maintenance mode for a scale unit node. |
| <CopyableCode code="stop_maintenance_mode" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, scaleUnitNode, subscriptionId" /> | Stop maintenance mode for a scale unit node. |
