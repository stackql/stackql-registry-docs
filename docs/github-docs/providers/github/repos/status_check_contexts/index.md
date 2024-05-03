---
title: status_check_contexts
hide_title: false
hide_table_of_contents: false
keywords:
  - status_check_contexts
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
<tr><td><b>Name</b></td><td><code>status_check_contexts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.status_check_contexts" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_all_status_check_contexts" /> | `SELECT` | <CopyableCode code="branch, owner, repo" /> |
| <CopyableCode code="add_status_check_contexts" /> | `INSERT` | <CopyableCode code="branch, owner, repo" /> |
| <CopyableCode code="remove_status_check_contexts" /> | `DELETE` | <CopyableCode code="branch, owner, repo" /> |
| <CopyableCode code="set_status_check_contexts" /> | `EXEC` | <CopyableCode code="branch, owner, repo" /> |
