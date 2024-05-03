---
title: idps
hide_title: false
hide_table_of_contents: false
keywords:
  - idps
  - inlinehook
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
<tr><td><b>Name</b></td><td><code>idps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.inlinehook.idps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="channel" /> | `object` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="type" /> | `string` |
| <CopyableCode code="version" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="inlineHookId, subdomain" /> | Gets an inline hook by ID |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subdomain" /> | Success |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="subdomain" /> | Success |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="inlineHookId, subdomain" /> | Deletes the Inline Hook matching the provided id. Once deleted, the Inline Hook is unrecoverable. As a safety precaution, only Inline Hooks with a status of INACTIVE are eligible for deletion. |
| <CopyableCode code="activate" /> | `EXEC` | <CopyableCode code="inlineHookId, subdomain" /> | Activates the Inline Hook matching the provided id |
| <CopyableCode code="deactivate" /> | `EXEC` | <CopyableCode code="inlineHookId, subdomain" /> | Deactivates the Inline Hook matching the provided id |
| <CopyableCode code="execute" /> | `EXEC` | <CopyableCode code="inlineHookId, subdomain" /> | Executes the Inline Hook matching the provided inlineHookId using the request body as the input. This will send the provided data through the Channel and return a response if it matches the correct data contract. This execution endpoint should only be used for testing purposes. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="inlineHookId, subdomain" /> | Updates an inline hook by ID |
