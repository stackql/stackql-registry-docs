---
title: move_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - move_resources
  - resource_mover
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
<tr><td><b>Name</b></td><td><code>move_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_mover.move_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource Id for the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Defines the move resource properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, moveCollectionName, moveResourceName, resourceGroupName, subscriptionId" /> | Gets the Move Resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, moveCollectionName, resourceGroupName, subscriptionId" /> | Lists the Move Resources in the move collection. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, moveCollectionName, moveResourceName, resourceGroupName, subscriptionId" /> | Creates or updates a Move Resource in the move collection. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, moveCollectionName, moveResourceName, resourceGroupName, subscriptionId" /> | Deletes a Move Resource from the move collection. |
