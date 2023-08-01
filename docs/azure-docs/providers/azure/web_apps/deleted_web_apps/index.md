---
title: deleted_web_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_web_apps
  - web_apps
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
<tr><td><b>Id</b></td><td><code>azure.web_apps.deleted_web_apps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `properties` | `object` | DeletedSite resource specific properties |
| `type` | `string` | Resource type. |
| `kind` | `string` | Kind of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DeletedWebApps_List` | `SELECT` | `subscriptionId` | Description for Get all deleted apps for a subscription. |
| `DeletedWebApps_ListByLocation` | `SELECT` | `location, subscriptionId` | Description for Get all deleted apps for a subscription at location |
| `DeletedWebApps_GetDeletedWebAppByLocation` | `EXEC` | `deletedSiteId, location, subscriptionId` | Description for Get deleted app for a subscription at location. |
