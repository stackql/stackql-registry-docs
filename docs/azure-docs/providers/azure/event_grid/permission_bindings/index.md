---
title: permission_bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - permission_bindings
  - event_grid
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
<tr><td><b>Name</b></td><td><code>permission_bindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.permission_bindings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified identifier of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="properties" /> | `object` | The properties of permission binding. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="namespaceName, permissionBindingName, resourceGroupName, subscriptionId" /> | Get properties of a permission binding. |
| <CopyableCode code="list_by_namespace" /> | `SELECT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Get all the permission bindings under a namespace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="namespaceName, permissionBindingName, resourceGroupName, subscriptionId" /> | Create or update a permission binding with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="namespaceName, permissionBindingName, resourceGroupName, subscriptionId" /> | Delete an existing permission binding. |
