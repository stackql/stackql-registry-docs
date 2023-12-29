---
title: log_archives
hide_title: false
hide_table_of_contents: false
keywords:
  - log_archives
  - log_archives
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
<tr><td><b>Name</b></td><td><code>log_archives</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.log_archives.log_archives</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The archive ID. |
| `attributes` | `object` | The attributes associated with the archive. |
| `type` | `string` | The type of the resource. The value should always be archives. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_logs_archive` | `SELECT` | `archive_id, dd_site` | Get a specific archive from your organization. |
| `list_logs_archives` | `SELECT` | `dd_site` | Get the list of configured logs archives with their definitions. |
| `create_logs_archive` | `INSERT` | `dd_site` | Create an archive in your organization. |
| `delete_logs_archive` | `DELETE` | `archive_id, dd_site` | Delete a given archive from your organization. |
| `_get_logs_archive` | `EXEC` | `archive_id, dd_site` | Get a specific archive from your organization. |
| `_list_logs_archives` | `EXEC` | `dd_site` | Get the list of configured logs archives with their definitions. |
| `add_read_role_to_archive` | `EXEC` | `archive_id, dd_site` | Adds a read role to an archive. ([Roles API](https://docs.datadoghq.com/api/v2/roles/)) |
| `remove_role_from_archive` | `EXEC` | `archive_id, dd_site` | Removes a role from an archive. ([Roles API](https://docs.datadoghq.com/api/v2/roles/)) |
| `update_logs_archive` | `EXEC` | `archive_id, dd_site` | Update a given archive configuration.<br /><br />**Note**: Using this method updates your archive configuration by **replacing**<br />your current configuration with the new one sent to your Datadog organization. |
