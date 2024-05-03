---
title: teams
hide_title: false
hide_table_of_contents: false
keywords:
  - teams
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
<tr><td><b>Name</b></td><td><code>teams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.teams" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="description" /> | `string` |  |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="members_url" /> | `string` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="notification_setting" /> | `string` |  |
| <CopyableCode code="parent" /> | `object` | Groups of organization members that gives permissions on specified repositories. |
| <CopyableCode code="permission" /> | `string` |  |
| <CopyableCode code="permissions" /> | `object` |  |
| <CopyableCode code="privacy" /> | `string` |  |
| <CopyableCode code="repositories_url" /> | `string` |  |
| <CopyableCode code="slug" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_teams" /> | `SELECT` | <CopyableCode code="owner, repo" /> |
