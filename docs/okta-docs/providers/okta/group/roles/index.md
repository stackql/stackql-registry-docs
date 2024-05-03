---
title: roles
hide_title: false
hide_table_of_contents: false
keywords:
  - roles
  - group
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
<tr><td><b>Name</b></td><td><code>roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.group.roles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="_embedded" /> | `object` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="assignmentType" /> | `string` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="label" /> | `string` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="type" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupId, roleId, subdomain" /> | Success |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="groupId, subdomain" /> | Success |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="groupId, subdomain" /> | Assigns a Role to a Group |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupId, roleId, subdomain" /> | Unassigns a Role from a Group |
