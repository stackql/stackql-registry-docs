---
title: elastic_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - elastic_pools
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
<tr><td><b>Name</b></td><td><code>elastic_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.elastic_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Kind of elastic pool. This is metadata used for the Azure portal experience. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of an elastic pool |
| <CopyableCode code="sku" /> | `object` | An ARM Resource SKU. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="elasticPoolName, resourceGroupName, serverName, subscriptionId" /> | Gets an elastic pool. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets all elastic pools in a server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="elasticPoolName, resourceGroupName, serverName, subscriptionId, data__location" /> | Creates or updates an elastic pool. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="elasticPoolName, resourceGroupName, serverName, subscriptionId" /> | Deletes an elastic pool. |
| <CopyableCode code="_list_by_server" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets all elastic pools in a server. |
| <CopyableCode code="failover" /> | `EXEC` | <CopyableCode code="elasticPoolName, resourceGroupName, serverName, subscriptionId" /> | Failovers an elastic pool. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="elasticPoolName, resourceGroupName, serverName, subscriptionId" /> | Updates an elastic pool. |
