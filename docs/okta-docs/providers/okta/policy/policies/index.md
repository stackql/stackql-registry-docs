---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
  - policy
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
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.policy.policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="_embedded" /> | `object` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="conditions" /> | `object` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="priority" /> | `integer` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="system" /> | `boolean` |
| <CopyableCode code="type" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="policyId, subdomain" /> | Gets a policy. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="type, subdomain" /> | Gets all policies with the specified type. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="subdomain" /> | Creates a policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="policyId, subdomain" /> | Removes a policy. |
| <CopyableCode code="activate" /> | `EXEC` | <CopyableCode code="policyId, ruleId, subdomain" /> | Activates a policy rule. |
| <CopyableCode code="deactivate" /> | `EXEC` | <CopyableCode code="policyId, ruleId, subdomain" /> | Deactivates a policy rule. |
