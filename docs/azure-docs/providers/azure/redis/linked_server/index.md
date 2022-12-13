---
title: linked_server
hide_title: false
hide_table_of_contents: false
keywords:
  - linked_server
  - redis
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
<tr><td><b>Name</b></td><td><code>linked_server</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.redis.linked_server</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `LinkedServer_Get` | `SELECT` | `linkedServerName, name, resourceGroupName, subscriptionId` | Gets the detailed information about a linked server of a redis cache (requires Premium SKU). |
| `LinkedServer_List` | `SELECT` | `name, resourceGroupName, subscriptionId` | Gets the list of linked servers associated with this redis cache (requires Premium SKU). |
| `LinkedServer_Create` | `INSERT` | `linkedServerName, name, resourceGroupName, subscriptionId, data__properties` | Adds a linked server to the Redis cache (requires Premium SKU). |
| `LinkedServer_Delete` | `DELETE` | `linkedServerName, name, resourceGroupName, subscriptionId` | Deletes the linked server from a redis cache (requires Premium SKU). |
