---
title: static_sites_user_provided_function_apps_for_static_site
hide_title: false
hide_table_of_contents: false
keywords:
  - static_sites_user_provided_function_apps_for_static_site
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
<tr><td><b>Name</b></td><td><code>static_sites_user_provided_function_apps_for_static_site</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.static_sites_user_provided_function_apps_for_static_site</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `kind` | `string` | Kind of resource. |
| `properties` | `object` | StaticSiteUserProvidedFunctionAppARMResource resource specific properties |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `name, resourceGroupName, subscriptionId` |
| `_get` | `EXEC` | `name, resourceGroupName, subscriptionId` |
