---
title: changelogs
hide_title: false
hide_table_of_contents: false
keywords:
  - changelogs
  - dialogflow
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
<tr><td><b>Name</b></td><td><code>changelogs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dialogflow.changelogs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The unique identifier of the changelog. Format: `projects//locations//agents//changelogs/`. |
| `type` | `string` | The affected resource type. |
| `userEmail` | `string` | Email address of the authenticated user. |
| `action` | `string` | The action of the change. |
| `createTime` | `string` | The timestamp of the change. |
| `displayName` | `string` | The affected resource display name of the change. |
| `resource` | `string` | The affected resource name of the change. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_agents_changelogs_get` | `SELECT` | `agentsId, changelogsId, locationsId, projectsId` | Retrieves the specified Changelog. |
| `projects_locations_agents_changelogs_list` | `SELECT` | `agentsId, locationsId, projectsId` | Returns the list of Changelogs. |
