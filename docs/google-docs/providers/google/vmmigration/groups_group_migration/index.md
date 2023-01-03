---
title: groups_group_migration
hide_title: false
hide_table_of_contents: false
keywords:
  - groups_group_migration
  - vmmigration
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>groups_group_migration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.vmmigration.groups_group_migration</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_groups_addGroupMigration` | `INSERT` | `groupsId, locationsId, projectsId` | Adds a MigratingVm to a Group. |
| `projects_locations_groups_removeGroupMigration` | `DELETE` | `groupsId, locationsId, projectsId` | Removes a MigratingVm from a Group. |
