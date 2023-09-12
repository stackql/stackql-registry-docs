---
title: user
hide_title: false
hide_table_of_contents: false
keywords:
  - user
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
<tr><td><b>Name</b></td><td><code>user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.migrations.user</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `org_metadata_only` | `boolean` |  |
| `exclude_git_data` | `boolean` |  |
| `url` | `string` |  |
| `guid` | `string` |  |
| `exclude_attachments` | `boolean` |  |
| `state` | `string` |  |
| `node_id` | `string` |  |
| `updated_at` | `string` |  |
| `lock_repositories` | `boolean` |  |
| `archive_url` | `string` |  |
| `exclude_owner_projects` | `boolean` |  |
| `exclude_releases` | `boolean` |  |
| `exclude` | `array` | Exclude related items from being returned in the response in order to improve performance of the request. The array can include any of: `"repositories"`. |
| `owner` | `object` | A GitHub user. |
| `repositories` | `array` | The repositories included in the migration. Only returned for export migrations. |
| `created_at` | `string` |  |
| `exclude_metadata` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_status_for_authenticated_user` | `SELECT` | `migration_id` | Fetches a single user migration. The response includes the `state` of the migration, which can be one of the following values:<br /><br />*   `pending` - the migration hasn't started yet.<br />*   `exporting` - the migration is in progress.<br />*   `exported` - the migration finished successfully.<br />*   `failed` - the migration failed.<br /><br />Once the migration has been `exported` you can [download the migration archive](https://docs.github.com/rest/migrations/users#download-a-user-migration-archive). |
| `list_for_authenticated_user` | `SELECT` |  | Lists all migrations a user has started. |
| `start_for_authenticated_user` | `EXEC` | `data__repositories` | Initiates the generation of a user migration archive. |
