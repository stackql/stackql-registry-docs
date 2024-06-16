---
title: storage_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_containers
  - azure_stack_hci
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
<tr><td><b>Name</b></td><td><code>storage_containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.storage_containers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties under the storage container resource |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, storageContainerName, subscriptionId" /> | Gets a storage container |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the storage containers in the specified resource group. Use the nextLink property in the response to get the next page of storage containers. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, storageContainerName, subscriptionId" /> | The operation to create or update a storage container. Please note some properties can be set only during storage container creation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, storageContainerName, subscriptionId" /> | The operation to delete a storage container. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, storageContainerName, subscriptionId" /> | The operation to update a storage container. |
