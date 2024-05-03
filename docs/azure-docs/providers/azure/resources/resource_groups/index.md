---
title: resource_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_groups
  - resources
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
<tr><td><b>Name</b></td><td><code>resource_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resources.resource_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource group. |
| <CopyableCode code="name" /> | `string` | The name of the resource group. |
| <CopyableCode code="location" /> | `string` | The location of the resource group. It cannot be changed after the resource group has been created. It must be one of the supported Azure locations. |
| <CopyableCode code="managedBy" /> | `string` | The ID of the resource that manages this resource group. |
| <CopyableCode code="properties" /> | `object` | The resource group properties. |
| <CopyableCode code="tags" /> | `object` | The tags attached to the resource group. |
| <CopyableCode code="type" /> | `string` | The type of the resource group. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all the resource groups for a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, data__location" /> | Creates or updates a resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId" /> | When you delete a resource group, all of its resources are also deleted. Deleting a resource group deletes all of its template deployments and currently stored operations. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Gets all the resource groups for a subscription. |
| <CopyableCode code="check_existence" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Checks whether a resource group exists. |
| <CopyableCode code="export_template" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Captures the specified resource group as a template. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Resource groups can be updated through a simple PATCH operation to a group address. The format of the request is the same as that for creating a resource group. If a field is unspecified, the current value is retained. |
