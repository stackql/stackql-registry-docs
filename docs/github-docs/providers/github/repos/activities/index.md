---
title: activities
hide_title: false
hide_table_of_contents: false
keywords:
  - activities
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
<tr><td><b>Name</b></td><td><code>activities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.activities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="activity_type" /> | `string` | The type of the activity that was performed. |
| <CopyableCode code="actor" /> | `object` | A GitHub user. |
| <CopyableCode code="after" /> | `string` | The SHA of the commit after the activity. |
| <CopyableCode code="before" /> | `string` | The SHA of the commit before the activity. |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="ref" /> | `string` | The full Git reference, formatted as `refs/heads/&lt;branch name&gt;`. |
| <CopyableCode code="timestamp" /> | `string` | The time when the activity occurred. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_activities" /> | `SELECT` | <CopyableCode code="owner, repo" /> |
