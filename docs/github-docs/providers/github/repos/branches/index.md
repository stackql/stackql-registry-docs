---
title: branches
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
<tr><td><b>Name</b></td><td><code>branches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.branches</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` |  |
| `protection_url` | `string` |  |
| `required_approving_review_count` | `integer` |  |
| `_links` | `object` |  |
| `commit` | `object` | Commit |
| `pattern` | `string` |  |
| `protected` | `boolean` |  |
| `protection` | `object` | Branch Protection |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_branch` | `SELECT` | `branch, owner, repo` |  |
| `list_branches` | `SELECT` | `owner, repo` |  |
| `merge_upstream` | `EXEC` | `owner, repo, data__branch` | Sync a branch of a forked repository to keep it up-to-date with the upstream repository. |
| `rename_branch` | `EXEC` | `branch, owner, repo, data__new_name` | Renames a branch in a repository.<br /><br />**Note:** Although the API responds immediately, the branch rename process might take some extra time to complete in the background. You won't be able to push to the old branch name while the rename process is in progress. For more information, see "[Renaming a branch](https://docs.github.com/github/administering-a-repository/renaming-a-branch)".<br /><br />The permissions required to use this endpoint depends on whether you are renaming the default branch.<br /><br />To rename a non-default branch:<br /><br />* Users must have push access.<br />* GitHub Apps must have the `contents:write` repository permission.<br /><br />To rename the default branch:<br /><br />* Users must have admin or owner permissions.<br />* GitHub Apps must have the `administration:write` repository permission. |
