---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - rum
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
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.rum.applications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | RUM application ID. |
| `attributes` | `object` | RUM application attributes. |
| `type` | `string` | RUM application response type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_rum_application` | `SELECT` | `id, dd_site` | Get the RUM application with given ID in your organization. |
| `get_rum_applications` | `SELECT` | `dd_site` | List all the RUM applications in your organization. |
| `create_rum_application` | `INSERT` | `data__data, dd_site` | Create a new RUM application in your organization. |
| `delete_rum_application` | `DELETE` | `id, dd_site` | Delete an existing RUM application in your organization. |
| `_get_rum_application` | `EXEC` | `id, dd_site` | Get the RUM application with given ID in your organization. |
| `_get_rum_applications` | `EXEC` | `dd_site` | List all the RUM applications in your organization. |
| `update_rum_application` | `EXEC` | `id, data__data, dd_site` | Update the RUM application with given ID in your organization. |
