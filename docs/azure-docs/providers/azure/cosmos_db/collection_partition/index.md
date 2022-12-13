---
title: collection_partition
hide_title: false
hide_table_of_contents: false
keywords:
  - collection_partition
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
<tr><td><b>Name</b></td><td><code>collection_partition</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.collection_partition</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CollectionPartition_ListMetrics` | `EXEC` | `$filter, accountName, collectionRid, databaseRid, resourceGroupName, subscriptionId` | Retrieves the metrics determined by the given filter for the given collection, split by partition. |
| `CollectionPartition_ListUsages` | `EXEC` | `accountName, collectionRid, databaseRid, resourceGroupName, subscriptionId` | Retrieves the usages (most recent storage data) for the given collection, split by partition. |
