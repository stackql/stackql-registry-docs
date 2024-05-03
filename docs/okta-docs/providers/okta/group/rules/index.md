---
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
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
<tr><td><b>Name</b></td><td><code>rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.group.rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="actions" /> | `object` |
| <CopyableCode code="conditions" /> | `object` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="type" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ruleId, subdomain" /> | Fetches a specific group rule by id from your organization |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subdomain" /> | Lists all group rules for your organization. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="subdomain" /> | Creates a group rule to dynamically add users to the specified group if they match the condition |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="ruleId, subdomain" /> | Removes a specific group rule by id from your organization |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="ruleId, subdomain" /> | Updates a group rule. Only `INACTIVE` rules can be updated. |
