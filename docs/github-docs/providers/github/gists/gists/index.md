---
title: gists
hide_title: false
hide_table_of_contents: false
keywords:
  - gists
  - gists
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.gists.gists" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="description" /> | `string` |  |
| <CopyableCode code="comments" /> | `integer` |  |
| <CopyableCode code="comments_url" /> | `string` |  |
| <CopyableCode code="commits_url" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="files" /> | `object` |  |
| <CopyableCode code="forks" /> | `array` |  |
| <CopyableCode code="forks_url" /> | `string` |  |
| <CopyableCode code="git_pull_url" /> | `string` |  |
| <CopyableCode code="git_push_url" /> | `string` |  |
| <CopyableCode code="history" /> | `array` |  |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="owner" /> | `object` | A GitHub user. |
| <CopyableCode code="public" /> | `boolean` |  |
| <CopyableCode code="truncated" /> | `boolean` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
| <CopyableCode code="user" /> | `object` | A GitHub user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` |  | Lists the authenticated user's gists or if called anonymously, this endpoint returns all public gists: |
| <CopyableCode code="list_for_user" /> | `SELECT` | <CopyableCode code="username" /> | Lists public gists for the specified user: |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="data__files" /> | Allows you to add a new gist with one or more files.<br /><br />**Note:** Don't name your files "gistfile" with a numerical suffix. This is the format of the automatic naming scheme that Gist uses internally. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="gist_id" /> |  |
| <CopyableCode code="check_is_starred" /> | `EXEC` | <CopyableCode code="gist_id" /> |  |
| <CopyableCode code="fork" /> | `EXEC` | <CopyableCode code="gist_id" /> |  |
| <CopyableCode code="star" /> | `EXEC` | <CopyableCode code="gist_id" /> | Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
| <CopyableCode code="unstar" /> | `EXEC` | <CopyableCode code="gist_id" /> |  |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="gist_id" /> | Allows you to update a gist's description and to update, delete, or rename gist files. Files from the previous version of the gist that aren't explicitly changed during an edit are unchanged.<br />At least one of `description` or `files` is required. |
