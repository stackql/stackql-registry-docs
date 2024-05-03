---
title: branch_restrictions
hide_title: false
hide_table_of_contents: false
keywords:
  - branch_restrictions
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
<tr><td><b>Name</b></td><td><code>branch_restrictions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.branch_restrictions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="apps" /> | `array` |
| <CopyableCode code="apps_url" /> | `string` |
| <CopyableCode code="teams" /> | `array` |
| <CopyableCode code="teams_url" /> | `string` |
| <CopyableCode code="url" /> | `string` |
| <CopyableCode code="users" /> | `array` |
| <CopyableCode code="users_url" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_access_restrictions" /> | `SELECT` | <CopyableCode code="branch, owner, repo" /> | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />Lists who has access to this protected branch.<br /><br />**Note**: Users, apps, and teams `restrictions` are only available for organization-owned repositories. |
| <CopyableCode code="delete_access_restrictions" /> | `DELETE` | <CopyableCode code="branch, owner, repo" /> | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />Disables the ability to restrict who can push to this branch. |
