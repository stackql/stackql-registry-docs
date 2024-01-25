---
title: web_apps_source_control
hide_title: false
hide_table_of_contents: false
keywords:
  - web_apps_source_control
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
<tr><td><b>Name</b></td><td><code>web_apps_source_control</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.web_apps_source_control</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `kind` | `string` | Kind of resource. |
| `properties` | `object` | SiteSourceControl resource specific properties |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `name, resourceGroupName, subscriptionId` | Description for Gets the source control configuration of an app. |
| `create_or_update` | `INSERT` | `name, resourceGroupName, subscriptionId` | Description for Updates the source control configuration of an app. |
| `delete` | `DELETE` | `name, resourceGroupName, subscriptionId` | Description for Deletes the source control configuration of an app. |
| `update` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Updates the source control configuration of an app. |
