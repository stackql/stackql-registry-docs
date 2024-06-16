---
title: addons
hide_title: false
hide_table_of_contents: false
keywords:
  - addons
  - data_box_edge
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
<tr><td><b>Name</b></td><td><code>addons</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box_edge.addons" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The object name. |
| <CopyableCode code="kind" /> | `string` | Addon type. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="addonName, deviceName, resourceGroupName, roleName, subscriptionId" /> | Gets a specific addon by name. |
| <CopyableCode code="list_by_role" /> | `SELECT` | <CopyableCode code="deviceName, resourceGroupName, roleName, subscriptionId" /> | Lists all the addons configured in the role. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="addonName, deviceName, resourceGroupName, roleName, subscriptionId, data__kind" /> | Create or update a addon. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="addonName, deviceName, resourceGroupName, roleName, subscriptionId" /> | Deletes the addon on the device. |
