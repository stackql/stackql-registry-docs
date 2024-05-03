---
title: licenses
hide_title: false
hide_table_of_contents: false
keywords:
  - licenses
  - licenses
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
<tr><td><b>Name</b></td><td><code>licenses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.licenses.licenses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="_links" /> | `object` |  |
| <CopyableCode code="content" /> | `string` |  |
| <CopyableCode code="download_url" /> | `string` |  |
| <CopyableCode code="encoding" /> | `string` |  |
| <CopyableCode code="git_url" /> | `string` |  |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="license" /> | `object` | License Simple |
| <CopyableCode code="path" /> | `string` |  |
| <CopyableCode code="sha" /> | `string` |  |
| <CopyableCode code="size" /> | `integer` |  |
| <CopyableCode code="type" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="license" /> | Gets information about a specific license. For more information, see "[Licensing a repository ](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)." |
| <CopyableCode code="get_all_commonly_used" /> | `SELECT` |  | Lists the most commonly used licenses on GitHub. For more information, see "[Licensing a repository ](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)." |
| <CopyableCode code="get_for_repo" /> | `SELECT` | <CopyableCode code="owner, repo" /> | This method returns the contents of the repository's license file, if one is detected.<br /><br />Similar to [Get repository content](https://docs.github.com/rest/repos/contents#get-repository-content), this method also supports [custom media types](https://docs.github.com/rest/overview/media-types) for retrieving the raw license content or rendered license HTML. |
