---
title: dashboard_list_items
hide_title: false
hide_table_of_contents: false
keywords:
  - dashboard_list_items
  - dashboard_lists
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboard_list_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.dashboard_lists.dashboard_list_items</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the dashboard. |
| `author` | `object` | Creator of the object. |
| `created` | `string` | Date of creation of the dashboard. |
| `icon` | `string` | URL to the icon of the dashboard. |
| `integration_id` | `string` | The short name of the integration. |
| `is_favorite` | `boolean` | Whether or not the dashboard is in the favorites. |
| `is_read_only` | `boolean` | Whether or not the dashboard is read only. |
| `is_shared` | `boolean` | Whether the dashboard is publicly shared or not. |
| `modified` | `string` | Date of last edition of the dashboard. |
| `popularity` | `integer` | Popularity of the dashboard. |
| `tags` | `array` | List of team names representing ownership of a dashboard. |
| `title` | `string` | Title of the dashboard. |
| `type` | `string` | The type of the dashboard. |
| `url` | `string` | URL path to the dashboard. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_dashboard_list_items` | `SELECT` | `dashboard_list_id, dd_site` | Fetch the dashboard list’s dashboard definitions. |
| `create_dashboard_list_items` | `INSERT` | `dashboard_list_id, dd_site` | Add dashboards to an existing dashboard list. |
| `delete_dashboard_list_items` | `DELETE` | `dashboard_list_id, dd_site` | Delete dashboards from an existing dashboard list. |
| `_get_dashboard_list_items` | `EXEC` | `dashboard_list_id, dd_site` | Fetch the dashboard list’s dashboard definitions. |
| `update_dashboard_list_items` | `EXEC` | `dashboard_list_id, dd_site` | Update dashboards of an existing dashboard list. |
