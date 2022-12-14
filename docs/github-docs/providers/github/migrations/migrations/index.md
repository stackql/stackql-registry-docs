---
title: migrations
hide_title: false
hide_table_of_contents: false
keywords:
  - migrations
  - migrations
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>migrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.migrations.migrations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `exclude` | `array` |  |
| `lock_repositories` | `boolean` |  |
| `updated_at` | `string` |  |
| `archive_url` | `string` |  |
| `exclude_metadata` | `boolean` |  |
| `exclude_releases` | `boolean` |  |
| `exclude_attachments` | `boolean` |  |
| `exclude_git_data` | `boolean` |  |
| `repositories` | `array` |  |
| `state` | `string` |  |
| `owner` | `object` | Simple User |
| `url` | `string` |  |
| `exclude_owner_projects` | `boolean` |  |
| `node_id` | `string` |  |
| `guid` | `string` |  |
| `created_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_status_for_authenticated_user` | `SELECT` | `migration_id` | Fetches a single user migration. The response includes the `state` of the migration, which can be one of the following values:<br /><br />*   `pending` - the migration hasn't started yet.<br />*   `exporting` - the migration is in progress.<br />*   `exported` - the migration finished successfully.<br />*   `failed` - the migration failed.<br /><br />Once the migration has been `exported` you can [download the migration archive](https://docs.github.com/rest/reference/migrations#download-a-user-migration-archive). |
| `get_status_for_org` | `SELECT` | `migration_id, org` | Fetches the status of a migration.<br /><br />The `state` of a migration can be one of the following values:<br /><br />*   `pending`, which means the migration hasn't started yet.<br />*   `exporting`, which means the migration is in progress.<br />*   `exported`, which means the migration finished successfully.<br />*   `failed`, which means the migration failed. |
| `list_for_authenticated_user` | `SELECT` |  | Lists all migrations a user has started. |
| `list_for_org` | `SELECT` | `org` | Lists the most recent migrations. |
| `start_for_authenticated_user` | `EXEC` | `data__repositories` | Initiates the generation of a user migration archive. |
| `start_for_org` | `EXEC` | `org, data__repositories` | Initiates the generation of a migration archive. |
