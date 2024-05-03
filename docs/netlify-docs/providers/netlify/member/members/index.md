---
title: members
hide_title: false
hide_table_of_contents: false
keywords:
  - members
  - member
  - netlify    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Netlify resources using SQL
custom_edit_url: null
image: /img/providers/netlify/stackql-netlify-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="netlify.member.members" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="avatar" /> | `string` |
| <CopyableCode code="email" /> | `string` |
| <CopyableCode code="full_name" /> | `string` |
| <CopyableCode code="role" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="listMembersForAccount" /> | `SELECT` | <CopyableCode code="account_slug" /> |
| <CopyableCode code="addMemberToAccount" /> | `INSERT` | <CopyableCode code="account_slug" /> |
