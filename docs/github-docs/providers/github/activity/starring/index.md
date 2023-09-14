---
title: starring
hide_title: false
hide_table_of_contents: false
keywords:
  - starring
  - activity
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
<tr><td><b>Name</b></td><td><code>starring</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.starring</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `starred_at` | `string` |  |
| `repo` | `object` | A repository on GitHub. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_starred_by_authenticated_user` | `SELECT` |  | Lists repositories the authenticated user has starred.<br /><br />You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: `application/vnd.github.star+json`. |
| `list_repos_starred_by_user` | `SELECT` | `username` | Lists repositories a user has starred.<br /><br />You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: `application/vnd.github.star+json`. |
| `check_repo_is_starred_by_authenticated_user` | `EXEC` | `owner, repo` | Whether the authenticated user has starred the repository. |
| `star_repo_for_authenticated_user` | `EXEC` | `owner, repo` | Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
| `unstar_repo_for_authenticated_user` | `EXEC` | `owner, repo` | Unstar a repository that the authenticated user has previously starred. |
