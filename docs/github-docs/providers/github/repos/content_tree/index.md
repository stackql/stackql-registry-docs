---
title: content_tree
hide_title: false
hide_table_of_contents: false
keywords:
  - content_tree
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
<tr><td><b>Name</b></td><td><code>content_tree</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.content_tree" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="content" /> | `string` |
| <CopyableCode code="content-submodule__links" /> | `object` |
| <CopyableCode code="content-submodule_download_url" /> | `string` |
| <CopyableCode code="content-submodule_git_url" /> | `string` |
| <CopyableCode code="content-submodule_html_url" /> | `string` |
| <CopyableCode code="content-submodule_name" /> | `string` |
| <CopyableCode code="content-submodule_path" /> | `string` |
| <CopyableCode code="content-submodule_sha" /> | `string` |
| <CopyableCode code="content-submodule_size" /> | `integer` |
| <CopyableCode code="content-submodule_submodule_git_url" /> | `string` |
| <CopyableCode code="content-submodule_type" /> | `string` |
| <CopyableCode code="content-submodule_url" /> | `string` |
| <CopyableCode code="content-symlink__links" /> | `object` |
| <CopyableCode code="content-symlink_download_url" /> | `string` |
| <CopyableCode code="content-symlink_git_url" /> | `string` |
| <CopyableCode code="content-symlink_html_url" /> | `string` |
| <CopyableCode code="content-symlink_name" /> | `string` |
| <CopyableCode code="content-symlink_path" /> | `string` |
| <CopyableCode code="content-symlink_sha" /> | `string` |
| <CopyableCode code="content-symlink_size" /> | `integer` |
| <CopyableCode code="content-symlink_target" /> | `string` |
| <CopyableCode code="content-symlink_type" /> | `string` |
| <CopyableCode code="content-symlink_url" /> | `string` |
| <CopyableCode code="download_url" /> | `string` |
| <CopyableCode code="encoding" /> | `string` |
| <CopyableCode code="git_url" /> | `string` |
| <CopyableCode code="html_url" /> | `string` |
| <CopyableCode code="path" /> | `string` |
| <CopyableCode code="sha" /> | `string` |
| <CopyableCode code="size" /> | `integer` |
| <CopyableCode code="submodule_git_url" /> | `string` |
| <CopyableCode code="target" /> | `string` |
| <CopyableCode code="type" /> | `string` |
| <CopyableCode code="url" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_content" /> | `SELECT` | <CopyableCode code="owner, path, repo" /> |
