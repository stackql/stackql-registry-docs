---
title: elastic_pool_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - elastic_pool_operations
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>elastic_pool_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.elastic_pool_operations</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_by_elastic_pool` | `SELECT` | `elasticPoolName, resourceGroupName, serverName, subscriptionId` | Gets a list of operations performed on the elastic pool. |
| `_list_by_elastic_pool` | `EXEC` | `elasticPoolName, resourceGroupName, serverName, subscriptionId` | Gets a list of operations performed on the elastic pool. |
| `cancel` | `EXEC` | `elasticPoolName, operationId, resourceGroupName, serverName, subscriptionId` | Cancels the asynchronous operation on the elastic pool. |
