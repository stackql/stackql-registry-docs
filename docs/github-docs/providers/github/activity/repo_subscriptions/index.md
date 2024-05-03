---
title: repo_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - repo_subscriptions
  - activity
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
<tr><td><b>Name</b></td><td><code>repo_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.activity.repo_subscriptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="ignored" /> | `boolean` | Determines if all notifications should be blocked from this repository. |
| <CopyableCode code="reason" /> | `string` |  |
| <CopyableCode code="repository_url" /> | `string` |  |
| <CopyableCode code="subscribed" /> | `boolean` | Determines if notifications should be received from this repository. |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_repo_subscription" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Gets information about whether the authenticated user is subscribed to the repository. |
| <CopyableCode code="delete_repo_subscription" /> | `DELETE` | <CopyableCode code="owner, repo" /> | This endpoint should only be used to stop watching a repository. To control whether or not you wish to receive notifications from a repository, [set the repository's subscription manually](https://docs.github.com/rest/activity/watching#set-a-repository-subscription). |
| <CopyableCode code="set_repo_subscription" /> | `EXEC` | <CopyableCode code="owner, repo" /> | If you would like to watch a repository, set `subscribed` to `true`. If you would like to ignore notifications made within a repository, set `ignored` to `true`. If you would like to stop watching a repository, [delete the repository's subscription](https://docs.github.com/rest/activity/watching#delete-a-repository-subscription) completely. |
