---
title: maintenance_windows
hide_title: false
hide_table_of_contents: false
keywords:
  - maintenance_windows
  - maintenance_windows
  - pagerduty    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, manage, and integrate PagerDuty resources using SQL
custom_edit_url: null
image: /img/providers/pagerduty/stackql-pagerduty-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>maintenance_windows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.maintenance_windows.maintenance_windows</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `description` | `string` | A description for this maintenance window. |
| `_type` | `string` | The type of object being created. |
| `created_by` | `object` |  |
| `end_time` | `string` | This maintenance window's end time. This is when the services will start creating incidents again. This date must be in the future and after the `start_time`. |
| `html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `self` | `string` | the API show URL at which the object is accessible |
| `sequence_number` | `integer` | The order in which the maintenance window was created. |
| `services` | `array` |  |
| `start_time` | `string` | This maintenance window's start time. This is when the services will stop creating incidents. If this date is in the past, it will be updated to be the current time. |
| `summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `teams` | `array` |  |
| `type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_maintenance_window` | `SELECT` | `id` | Get an existing maintenance window.<br /><br />A Maintenance Window is used to temporarily disable one or more Services for a set period of time.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#maintenance-windows)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| `list_maintenance_windows` | `SELECT` |  | List existing maintenance windows, optionally filtered by service and/or team, or whether they are from the past, present or future.<br /><br />A Maintenance Window is used to temporarily disable one or more Services for a set period of time.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#maintenance-windows)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| `create_maintenance_window` | `INSERT` | `From, data__maintenance_window` | Create a new maintenance window for the specified services. No new incidents will be created for a service that is in maintenance.<br /><br />A Maintenance Window is used to temporarily disable one or more Services for a set period of time.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#maintenance-windows)<br /><br />Scoped OAuth requires: `services.write`<br /> |
| `delete_maintenance_window` | `DELETE` | `id` | Delete an existing maintenance window if it's in the future, or end it if it's currently on-going. If the maintenance window has already ended it cannot be deleted.<br /><br />A Maintenance Window is used to temporarily disable one or more Services for a set period of time.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#maintenance-windows)<br /><br />Scoped OAuth requires: `services.write`<br /> |
| `_get_maintenance_window` | `EXEC` | `id` | Get an existing maintenance window.<br /><br />A Maintenance Window is used to temporarily disable one or more Services for a set period of time.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#maintenance-windows)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| `_list_maintenance_windows` | `EXEC` |  | List existing maintenance windows, optionally filtered by service and/or team, or whether they are from the past, present or future.<br /><br />A Maintenance Window is used to temporarily disable one or more Services for a set period of time.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#maintenance-windows)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| `update_maintenance_window` | `EXEC` | `id, data__maintenance_window` | Update an existing maintenance window.<br /><br />A Maintenance Window is used to temporarily disable one or more Services for a set period of time.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#maintenance-windows)<br /><br />Scoped OAuth requires: `services.write`<br /> |
