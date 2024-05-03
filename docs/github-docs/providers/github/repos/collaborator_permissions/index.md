---
title: collaborator_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - collaborator_permissions
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
<tr><td><b>Name</b></td><td><code>collaborator_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.collaborator_permissions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="permission" /> | `string` |  |
| <CopyableCode code="role_name" /> | `string` |  |
| <CopyableCode code="user" /> | `object` | Collaborator |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_collaborator_permission_level" /> | `SELECT` | <CopyableCode code="owner, repo, username" /> |
