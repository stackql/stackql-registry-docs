---
title: protected_items
hide_title: false
hide_table_of_contents: false
keywords:
  - protected_items
  - recovery_services_backup
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
<tr><td><b>Name</b></td><td><code>protected_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.protected_items" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id represents the complete path to the resource. |
| <CopyableCode code="name" /> | `string` | Resource name associated with the resource. |
| <CopyableCode code="eTag" /> | `string` | Optional ETag. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Base class for backup items. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, containerName, fabricName, protectedItemName, resourceGroupName, subscriptionId, vaultName" /> | Provides the details of the backed up item. This is an asynchronous operation. To know the status of the operation,<br />call the GetItemOperationResult API. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, containerName, fabricName, protectedItemName, resourceGroupName, subscriptionId, vaultName" /> | Enables backup of an item or to modifies the backup policy information of an already backed up item. This is an<br />asynchronous operation. To know the status of the operation, call the GetItemOperationResult API. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, containerName, fabricName, protectedItemName, resourceGroupName, subscriptionId, vaultName" /> | Used to disable backup of an item within a container. This is an asynchronous operation. To know the status of the<br />request, call the GetItemOperationResult API. |
