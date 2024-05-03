---
title: disk_accesses
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_accesses
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
<tr><td><b>Name</b></td><td><code>disk_accesses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.disk_accesses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="diskAccessName, resourceGroupName, subscriptionId" /> | Gets information about a disk access resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the disk access resources under a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the disk access resources under a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="diskAccessName, resourceGroupName, subscriptionId" /> | Creates or updates a disk access resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="diskAccessName, resourceGroupName, subscriptionId" /> | Deletes a disk access resource. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists all the disk access resources under a subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the disk access resources under a resource group. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="diskAccessName, resourceGroupName, subscriptionId" /> | Updates (patches) a disk access resource. |
