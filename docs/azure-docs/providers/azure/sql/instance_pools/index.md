---
title: instance_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_pools
  - sql
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
<tr><td><b>Name</b></td><td><code>instance_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.instance_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of an instance pool. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instancePoolName, resourceGroupName, subscriptionId" /> | Gets an instance pool. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of all instance pools in the subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of instance pools in the resource group |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="instancePoolName, resourceGroupName, subscriptionId, data__location" /> | Creates or updates an instance pool. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instancePoolName, resourceGroupName, subscriptionId" /> | Deletes an instance pool |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="instancePoolName, resourceGroupName, subscriptionId" /> | Updates an instance pool. |
