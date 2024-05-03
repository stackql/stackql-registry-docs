---
title: timeline
hide_title: false
hide_table_of_contents: false
keywords:
  - timeline
  - issues
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
<tr><td><b>Name</b></td><td><code>timeline</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.issues.timeline" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="actor" /> | `object` | A GitHub user. |
| <CopyableCode code="commit_id" /> | `string` |  |
| <CopyableCode code="commit_url" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="event" /> | `string` |  |
| <CopyableCode code="label" /> | `object` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="performed_via_github_app" /> | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_events_for_timeline" /> | `SELECT` | <CopyableCode code="issue_number, owner, repo" /> |
