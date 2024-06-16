---
title: cassandra_data_centers
hide_title: false
hide_table_of_contents: false
keywords:
  - cassandra_data_centers
  - cosmos_db
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
<tr><td><b>Name</b></td><td><code>cassandra_data_centers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.cassandra_data_centers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique resource identifier of the database account. |
| <CopyableCode code="name" /> | `string` | The name of the database account. |
| <CopyableCode code="properties" /> | `object` | Properties of a managed Cassandra data center. |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, dataCenterName, resourceGroupName, subscriptionId" /> | Get the properties of a managed Cassandra data center. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | List all data centers in a particular managed Cassandra cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, dataCenterName, resourceGroupName, subscriptionId" /> | Delete a managed Cassandra data center. |
| <CopyableCode code="create_update" /> | `EXEC` | <CopyableCode code="clusterName, dataCenterName, resourceGroupName, subscriptionId" /> | Create or update a managed Cassandra data center. When updating, overwrite all properties. To update only some properties, use PATCH. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="clusterName, dataCenterName, resourceGroupName, subscriptionId" /> | Update some of the properties of a managed Cassandra data center. |
