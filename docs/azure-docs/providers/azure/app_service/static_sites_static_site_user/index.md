---
title: static_sites_static_site_user
hide_title: false
hide_table_of_contents: false
keywords:
  - static_sites_static_site_user
  - app_service
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
<tr><td><b>Name</b></td><td><code>static_sites_static_site_user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.static_sites_static_site_user</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `delete` | `DELETE` | `authprovider, name, resourceGroupName, subscriptionId, userid` | Description for Deletes the user entry from the static site. |
| `update` | `EXEC` | `authprovider, name, resourceGroupName, subscriptionId, userid` | Description for Updates a user entry with the listed roles |
