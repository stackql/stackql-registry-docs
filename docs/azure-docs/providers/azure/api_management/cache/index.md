---
title: cache
hide_title: false
hide_table_of_contents: false
keywords:
  - cache
  - api_management
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
<tr><td><b>Name</b></td><td><code>cache</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.cache</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `cacheId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the Cache specified by its identifier. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of all external Caches in the specified service instance. |
| `create_or_update` | `INSERT` | `cacheId, resourceGroupName, serviceName, subscriptionId` | Creates or updates an External Cache to be used in Api Management instance. |
| `delete` | `DELETE` | `If-Match, cacheId, resourceGroupName, serviceName, subscriptionId` | Deletes specific Cache. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of all external Caches in the specified service instance. |
| `update` | `EXEC` | `If-Match, cacheId, resourceGroupName, serviceName, subscriptionId` | Updates the details of the cache specified by its identifier. |
