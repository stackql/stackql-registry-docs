---
title: refs
hide_title: false
hide_table_of_contents: false
keywords:
  - refs
  - git
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
<tr><td><b>Name</b></td><td><code>refs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.git.refs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="node_id" /> | `string` |
| <CopyableCode code="object" /> | `object` |
| <CopyableCode code="ref" /> | `string` |
| <CopyableCode code="url" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_matching_refs" /> | `SELECT` | <CopyableCode code="owner, ref, repo" /> | Returns an array of references from your Git database that match the supplied name. The `:ref` in the URL must be formatted as `heads/&lt;branch name&gt;` for branches and `tags/&lt;tag name&gt;` for tags. If the `:ref` doesn't exist in the repository, but existing refs start with `:ref`, they will be returned as an array.<br /><br />When you use this endpoint without providing a `:ref`, it will return an array of all the references from your Git database, including notes and stashes if they exist on the server. Anything in the namespace is returned, not just `heads` and `tags`.<br /><br />**Note:** You need to explicitly [request a pull request](https://docs.github.com/rest/pulls/pulls#get-a-pull-request) to trigger a test merge commit, which checks the mergeability of pull requests. For more information, see "[Checking mergeability of pull requests](https://docs.github.com/rest/guides/getting-started-with-the-git-database-api#checking-mergeability-of-pull-requests)".<br /><br />If you request matching references for a branch named `feature` but the branch `feature` doesn't exist, the response can still include other matching head refs that start with the word `feature`, such as `featureA` and `featureB`. |
| <CopyableCode code="create_ref" /> | `INSERT` | <CopyableCode code="owner, repo, data__ref, data__sha" /> | Creates a reference for your repository. You are unable to create new references for empty repositories, even if the commit SHA-1 hash used exists. Empty repositories are repositories without branches. |
| <CopyableCode code="delete_ref" /> | `DELETE` | <CopyableCode code="owner, ref, repo" /> |  |
| <CopyableCode code="update_ref" /> | `EXEC` | <CopyableCode code="owner, ref, repo, data__sha" /> |  |
