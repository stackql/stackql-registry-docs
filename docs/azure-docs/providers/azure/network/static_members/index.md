---
title: static_members
hide_title: false
hide_table_of_contents: false
keywords:
  - static_members
  - network
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
<tr><td><b>Name</b></td><td><code>static_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.static_members" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of static member. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` |  | Gets the specified static member. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networkGroupName, networkManagerName, resourceGroupName, subscriptionId" /> | Lists the specified static member. |
| <CopyableCode code="create_or_update" /> | `INSERT` |  | Creates or updates a static member. |
| <CopyableCode code="delete" /> | `DELETE` |  | Deletes a static member. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="networkGroupName, networkManagerName, resourceGroupName, subscriptionId" /> | Lists the specified static member. |
