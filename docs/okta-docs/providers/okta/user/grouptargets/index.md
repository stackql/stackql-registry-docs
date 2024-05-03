---
title: grouptargets
hide_title: false
hide_table_of_contents: false
keywords:
  - grouptargets
  - user
  - okta    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: /img/providers/okta/stackql-okta-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>grouptargets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.user.grouptargets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="_embedded" /> | `object` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="lastMembershipUpdated" /> | `string` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="objectClass" /> | `array` |
| <CopyableCode code="profile" /> | `object` |
| <CopyableCode code="type" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="roleId, userId, subdomain" /> |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="groupId, roleId, userId, subdomain" /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupId, roleId, userId, subdomain" /> |
