---
title: static_sites_basic_auth
hide_title: false
hide_table_of_contents: false
keywords:
  - static_sites_basic_auth
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
<tr><td><b>Name</b></td><td><code>static_sites_basic_auth</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.static_sites_basic_auth</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `kind` | `string` | Kind of resource. |
| `properties` | `object` | StaticSiteBasicAuthPropertiesARMResource resource specific properties |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `basicAuthName, name, resourceGroupName, subscriptionId` | Description for Gets the basic auth properties for a static site. |
| `list` | `SELECT` | `name, resourceGroupName, subscriptionId` | Description for Gets the basic auth properties for a static site as a collection. |
| `create_or_update` | `INSERT` | `basicAuthName, name, resourceGroupName, subscriptionId` | Description for Adds or updates basic auth for a static site. |
| `_list` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the basic auth properties for a static site as a collection. |
