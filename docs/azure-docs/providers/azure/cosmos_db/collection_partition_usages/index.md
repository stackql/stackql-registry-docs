---
title: collection_partition_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - collection_partition_usages
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>collection_partition_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.collection_partition_usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `object` | A metric name. |
| `currentValue` | `integer` | Current value for this metric |
| `limit` | `integer` | Maximum value for this metric |
| `partitionId` | `string` | The partition id (GUID identifier) of the usages. |
| `partitionKeyRangeId` | `string` | The partition key range id (integer identifier) of the usages. |
| `quotaPeriod` | `string` | The quota period used to summarize the usage values. |
| `unit` | `string` | The unit of the metric. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `accountName, collectionRid, databaseRid, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `accountName, collectionRid, databaseRid, resourceGroupName, subscriptionId` |
