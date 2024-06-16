---
title: redis_enterprise
hide_title: false
hide_table_of_contents: false
keywords:
  - redis_enterprise
  - redis_enterprise
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>redis_enterprise</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.redis_enterprise.redis_enterprise" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of RedisEnterprise clusters, as opposed to general resource properties like location, tags |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="zones" /> | `array` | The Availability Zones where this cluster will be deployed. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Gets information about a RedisEnterprise cluster |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all RedisEnterprise clusters in the specified subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all RedisEnterprise clusters in a resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__sku" /> | Creates or updates an existing (overwrite/recreate, with potential downtime) cache cluster |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Deletes a RedisEnterprise cache cluster. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Updates an existing RedisEnterprise cluster |
