---
title: user_exports
hide_title: false
hide_table_of_contents: false
keywords:
  - user_exports
  - codespaces
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
<tr><td><b>Name</b></td><td><code>user_exports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.codespaces.user_exports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Id for the export details |
| `state` | `string` | State of the latest export |
| `branch` | `string` | Name of the exported branch |
| `completed_at` | `string` | Completion time of the last export operation |
| `export_url` | `string` | Url for fetching export details |
| `html_url` | `string` | Web url for the exported branch |
| `sha` | `string` | Git commit SHA of the exported branch |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_export_details_for_authenticated_user` | `SELECT` | `codespace_name, export_id` | Gets information about an export of a codespace.<br /><br />You must authenticate using a personal access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have read access to the `codespaces_lifecycle_admin` repository permission to use this endpoint. |
| `export_for_authenticated_user` | `EXEC` | `codespace_name` | Triggers an export of the specified codespace and returns a URL and ID where the status of the export can be monitored.<br /><br />If changes cannot be pushed to the codespace's repository, they will be pushed to a new or previously-existing fork instead.<br /><br />You must authenticate using a personal access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have write access to the `codespaces_lifecycle_admin` repository permission to use this endpoint. |
