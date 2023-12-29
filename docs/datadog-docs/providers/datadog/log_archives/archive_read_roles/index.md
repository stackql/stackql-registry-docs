---
title: archive_read_roles
hide_title: false
hide_table_of_contents: false
keywords:
  - archive_read_roles
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
<tr><td><b>Name</b></td><td><code>archive_read_roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.log_archives.archive_read_roles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique identifier of the role. |
| `attributes` | `object` | Attributes of the role. |
| `relationships` | `object` | Relationships of the role object returned by the API. |
| `type` | `string` | Roles type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_archive_read_roles` | `SELECT` | `archive_id, dd_site` |
| `_list_archive_read_roles` | `EXEC` | `archive_id, dd_site` |
