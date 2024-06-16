---
title: disk_encryption_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_encryption_sets
  - compute
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
<tr><td><b>Name</b></td><td><code>disk_encryption_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.disk_encryption_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="identity" /> | `object` | The managed identity for the disk encryption set. It should be given permission on the key vault before it can be used to encrypt disks. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="diskEncryptionSetName, resourceGroupName, subscriptionId" /> | Gets information about a disk encryption set. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the disk encryption sets under a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the disk encryption sets under a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="diskEncryptionSetName, resourceGroupName, subscriptionId" /> | Creates or updates a disk encryption set |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="diskEncryptionSetName, resourceGroupName, subscriptionId" /> | Deletes a disk encryption set. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="diskEncryptionSetName, resourceGroupName, subscriptionId" /> | Updates (patches) a disk encryption set. |
