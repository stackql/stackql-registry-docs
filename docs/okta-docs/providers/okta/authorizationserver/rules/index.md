---
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - authorizationserver
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
<tr><td><b>Id</b></td><td><CopyableCode code="okta.authorizationserver.rules" /></td></tr>
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
| <CopyableCode code="priority" /> | `integer` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="system" /> | `boolean` |
| <CopyableCode code="type" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authServerId, policyId, ruleId, subdomain" /> | Returns a Policy Rule by ID that is defined in the specified Custom Authorization Server and Policy. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="authServerId, policyId, subdomain" /> | Enumerates all policy rules for the specified Custom Authorization Server and Policy. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="authServerId, policyId, subdomain" /> | Creates a policy rule for the specified Custom Authorization Server and Policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="authServerId, policyId, ruleId, subdomain" /> | Deletes a Policy Rule defined in the specified Custom Authorization Server and Policy. |
| <CopyableCode code="activate" /> | `EXEC` | <CopyableCode code="authServerId, policyId, ruleId, subdomain" /> | Activate Authorization Server Policy Rule |
| <CopyableCode code="deactivate" /> | `EXEC` | <CopyableCode code="authServerId, policyId, ruleId, subdomain" /> | Deactivate Authorization Server Policy Rule |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="authServerId, policyId, ruleId, subdomain" /> | Updates the configuration of the Policy Rule defined in the specified Custom Authorization Server and Policy. |
