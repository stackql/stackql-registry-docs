---
title: deploy_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - deploy_keys
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
<tr><td><b>Name</b></td><td><code>deploy_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.deploy_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `integer` |
| <CopyableCode code="added_by" /> | `string` |
| <CopyableCode code="created_at" /> | `string` |
| <CopyableCode code="key" /> | `string` |
| <CopyableCode code="last_used" /> | `string` |
| <CopyableCode code="read_only" /> | `boolean` |
| <CopyableCode code="title" /> | `string` |
| <CopyableCode code="url" /> | `string` |
| <CopyableCode code="verified" /> | `boolean` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_deploy_key" /> | `SELECT` | <CopyableCode code="key_id, owner, repo" /> |  |
| <CopyableCode code="list_deploy_keys" /> | `SELECT` | <CopyableCode code="owner, repo" /> |  |
| <CopyableCode code="create_deploy_key" /> | `INSERT` | <CopyableCode code="owner, repo, data__key" /> | You can create a read-only deploy key. |
| <CopyableCode code="delete_deploy_key" /> | `DELETE` | <CopyableCode code="key_id, owner, repo" /> | Deploy keys are immutable. If you need to update a key, remove the key and create a new one instead. |
