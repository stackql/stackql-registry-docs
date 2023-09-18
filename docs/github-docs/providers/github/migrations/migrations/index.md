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
| `node_id` | `string` |  |
| `archive_url` | `string` |  |
| `updated_at` | `string` |  |
| `exclude_attachments` | `boolean` |  |
| `exclude_git_data` | `boolean` |  |
| `exclude` | `array` | Exclude related items from being returned in the response in order to improve performance of the request. The array can include any of: `"repositories"`. |
| `owner` | `object` | A GitHub user. |
| `state` | `string` |  |
| `exclude_metadata` | `boolean` |  |
| `guid` | `string` |  |
| `org_metadata_only` | `boolean` |  |
| `url` | `string` |  |
| `exclude_releases` | `boolean` |  |
| `exclude_owner_projects` | `boolean` |  |
| `repositories` | `array` | The repositories included in the migration. Only returned for export migrations. |
| `lock_repositories` | `boolean` |  |
| `created_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_status_for_authenticated_user` | `SELECT` | `migration_id` | Fetches a single user migration. The response includes the `state` of the migration, which can be one of the following values:<br /><br />*   `pending` - the migration hasn't started yet.<br />*   `exporting` - the migration is in progress.<br />*   `exported` - the migration finished successfully.<br />*   `failed` - the migration failed.<br /><br />Once the migration has been `exported` you can [download the migration archive](https://docs.github.com/rest/migrations/users#download-a-user-migration-archive). |
| `get_status_for_org` | `SELECT` | `migration_id, org` | Fetches the status of a migration.<br /><br />The `state` of a migration can be one of the following values:<br /><br />*   `pending`, which means the migration hasn't started yet.<br />*   `exporting`, which means the migration is in progress.<br />*   `exported`, which means the migration finished successfully.<br />*   `failed`, which means the migration failed. |
| `list_for_authenticated_user` | `SELECT` |  | Lists all migrations a user has started. |
| `list_for_org` | `SELECT` | `org` | Lists the most recent migrations, including both exports (which can be started through the REST API) and imports (which cannot be started using the REST API).<br /><br />A list of `repositories` is only returned for export migrations. |
| `start_for_authenticated_user` | `EXEC` | `data__repositories` | Initiates the generation of a user migration archive. |
| `start_for_org` | `EXEC` | `org, data__repositories` | Initiates the generation of a migration archive. |
