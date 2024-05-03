---
title: orgs_for_user
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs_for_user
  - orgs
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
<tr><td><b>Name</b></td><td><code>orgs_for_user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.orgs.orgs_for_user" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `integer` |
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="avatar_url" /> | `string` |
| <CopyableCode code="events_url" /> | `string` |
| <CopyableCode code="hooks_url" /> | `string` |
| <CopyableCode code="issues_url" /> | `string` |
| <CopyableCode code="login" /> | `string` |
| <CopyableCode code="members_url" /> | `string` |
| <CopyableCode code="node_id" /> | `string` |
| <CopyableCode code="public_members_url" /> | `string` |
| <CopyableCode code="repos_url" /> | `string` |
| <CopyableCode code="url" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_for_authenticated_user" /> | `SELECT` |  |
