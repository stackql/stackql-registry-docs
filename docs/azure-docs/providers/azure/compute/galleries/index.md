---
title: galleries
hide_title: false
hide_table_of_contents: false
keywords:
  - galleries
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
<tr><td><b>Name</b></td><td><code>galleries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.galleries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a Shared Image Gallery. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="galleryName, resourceGroupName, subscriptionId" /> | Retrieves information about a Shared Image Gallery. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List galleries under a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List galleries under a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="galleryName, resourceGroupName, subscriptionId" /> | Create or update a Shared Image Gallery. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="galleryName, resourceGroupName, subscriptionId" /> | Delete a Shared Image Gallery. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | List galleries under a subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List galleries under a resource group. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="galleryName, resourceGroupName, subscriptionId" /> | Update a Shared Image Gallery. |
