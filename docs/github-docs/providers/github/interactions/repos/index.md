---
title: repos
hide_title: false
hide_table_of_contents: false
keywords:
  - repos
  - interactions
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
<tr><td><b>Name</b></td><td><code>repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.interactions.repos" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="expires_at" /> | `string` |  |
| <CopyableCode code="limit" /> | `string` | The type of GitHub user that can comment, open issues, or create pull requests while the interaction limit is in effect. |
| <CopyableCode code="origin" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_restrictions_for_repo" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Shows which type of GitHub user can interact with this repository and when the restriction expires. If there are no restrictions, you will see an empty response. |
| <CopyableCode code="remove_restrictions_for_repo" /> | `DELETE` | <CopyableCode code="owner, repo" /> | Removes all interaction restrictions from the given repository. You must have owner or admin access to remove restrictions. If the interaction limit is set for the user or organization that owns this repository, you will receive a `409 Conflict` response and will not be able to use this endpoint to change the interaction limit for a single repository. |
| <CopyableCode code="set_restrictions_for_repo" /> | `EXEC` | <CopyableCode code="owner, repo, data__limit" /> | Temporarily restricts interactions to a certain type of GitHub user within the given repository. You must have owner or admin access to set these restrictions. If an interaction limit is set for the user or organization that owns this repository, you will receive a `409 Conflict` response and will not be able to use this endpoint to change the interaction limit for a single repository. |
