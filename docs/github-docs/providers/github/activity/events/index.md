---
title: events
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
<tr><td><b>Name</b></td><td><code>events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `repo` | `object` |  |
| `type` | `string` |  |
| `actor` | `object` | Actor |
| `created_at` | `string` |  |
| `org` | `object` | Actor |
| `payload` | `object` |  |
| `public` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_events_for_authenticated_user` | `SELECT` | `username` | If you are authenticated as the given user, you will see your private events. Otherwise, you'll only see public events. |
| `list_org_events_for_authenticated_user` | `SELECT` | `org, username` | This is the user's organization dashboard. You must be authenticated as the user to view this. |
| `list_repo_events` | `SELECT` | `owner, repo` |  |
