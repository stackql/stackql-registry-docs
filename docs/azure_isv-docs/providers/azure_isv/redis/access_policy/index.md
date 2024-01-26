---
title: access_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - access_policy
  - redis
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>access_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.redis.access_policy</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accessPolicyName, cacheName, resourceGroupName, subscriptionId` | Gets the detailed information about an access policy of a redis cache |
| `list` | `SELECT` | `cacheName, resourceGroupName, subscriptionId` | Gets the list of access policies associated with this redis cache |
| `delete` | `DELETE` | `accessPolicyName, cacheName, resourceGroupName, subscriptionId` | Deletes the access policy from a redis cache |
| `_list` | `EXEC` | `cacheName, resourceGroupName, subscriptionId` | Gets the list of access policies associated with this redis cache |
| `create_update` | `EXEC` | `accessPolicyName, cacheName, resourceGroupName, subscriptionId` | Adds an access policy to the redis cache |
