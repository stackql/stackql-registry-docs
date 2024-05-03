---
title: branch
hide_title: false
hide_table_of_contents: false
keywords:
  - branch
  - repos
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
<tr><td><b>Name</b></td><td><code>branch</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.branch" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="_links" /> | `object` |  |
| <CopyableCode code="commit" /> | `object` | Commit |
| <CopyableCode code="pattern" /> | `string` |  |
| <CopyableCode code="protected" /> | `boolean` |  |
| <CopyableCode code="protection" /> | `object` | Branch Protection |
| <CopyableCode code="protection_url" /> | `string` |  |
| <CopyableCode code="required_approving_review_count" /> | `integer` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_branch" /> | `SELECT` | <CopyableCode code="branch, owner, repo" /> |  |
| <CopyableCode code="merge" /> | `EXEC` | <CopyableCode code="owner, repo, data__base, data__head" /> |  |
| <CopyableCode code="merge_upstream" /> | `EXEC` | <CopyableCode code="owner, repo, data__branch" /> | Sync a branch of a forked repository to keep it up-to-date with the upstream repository. |
| <CopyableCode code="rename_branch" /> | `EXEC` | <CopyableCode code="branch, owner, repo, data__new_name" /> | Renames a branch in a repository.<br /><br />**Note:** Although the API responds immediately, the branch rename process might take some extra time to complete in the background. You won't be able to push to the old branch name while the rename process is in progress. For more information, see "[Renaming a branch](https://docs.github.com/github/administering-a-repository/renaming-a-branch)".<br /><br />The permissions required to use this endpoint depends on whether you are renaming the default branch.<br /><br />To rename a non-default branch:<br /><br />* Users must have push access.<br />* GitHub Apps must have the `contents:write` repository permission.<br /><br />To rename the default branch:<br /><br />* Users must have admin or owner permissions.<br />* GitHub Apps must have the `administration:write` repository permission. |
