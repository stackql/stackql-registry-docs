---
title: archives
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>archives</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.migrations.archives</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `delete_archive_for_authenticated_user` | `DELETE` | `migration_id` | Deletes a previous migration archive. Downloadable migration archives are automatically deleted after seven days. Migration metadata, which is returned in the [List user migrations](https://docs.github.com/rest/reference/migrations#list-user-migrations) and [Get a user migration status](https://docs.github.com/rest/reference/migrations#get-a-user-migration-status) endpoints, will continue to be available even after an archive is deleted. |
| `delete_archive_for_org` | `DELETE` | `migration_id, org` | Deletes a previous migration archive. Migration archives are automatically deleted after seven days. |
| `download_archive_for_org` | `EXEC` | `migration_id, org` | Fetches the URL to a migration archive. |
| `get_archive_for_authenticated_user` | `EXEC` | `migration_id` | Fetches the URL to download the migration archive as a `tar.gz` file. Depending on the resources your repository uses, the migration archive can contain JSON files with data for these objects:<br /><br />*   attachments<br />*   bases<br />*   commit\_comments<br />*   issue\_comments<br />*   issue\_events<br />*   issues<br />*   milestones<br />*   organizations<br />*   projects<br />*   protected\_branches<br />*   pull\_request\_reviews<br />*   pull\_requests<br />*   releases<br />*   repositories<br />*   review\_comments<br />*   schema<br />*   users<br /><br />The archive will also contain an `attachments` directory that includes all attachment files uploaded to GitHub.com and a `repositories` directory that contains the repository's Git data. |
