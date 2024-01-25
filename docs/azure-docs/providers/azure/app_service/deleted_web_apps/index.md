---
title: deleted_web_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_web_apps
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
<tr><td><b>Name</b></td><td><code>deleted_web_apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.deleted_web_apps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `kind` | `string` | Kind of resource. |
| `properties` | `object` | DeletedSite resource specific properties |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `subscriptionId` | Description for Get all deleted apps for a subscription. |
| `list_by_location` | `SELECT` | `location, subscriptionId` | Description for Get all deleted apps for a subscription at location |
| `_list` | `EXEC` | `subscriptionId` | Description for Get all deleted apps for a subscription. |
| `_list_by_location` | `EXEC` | `location, subscriptionId` | Description for Get all deleted apps for a subscription at location |
