---
title: sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - sessions
  - session
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
<tr><td><b>Name</b></td><td><code>sessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.session.sessions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="amr" /> | `array` |
| <CopyableCode code="createdAt" /> | `string` |
| <CopyableCode code="expiresAt" /> | `string` |
| <CopyableCode code="idp" /> | `object` |
| <CopyableCode code="lastFactorVerification" /> | `string` |
| <CopyableCode code="lastPasswordVerification" /> | `string` |
| <CopyableCode code="login" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="userId" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="sessionId, subdomain" /> | Get details about a session. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="subdomain" /> | Creates a new session for a user with a valid session token. Use this API if, for example, you want to set the session cookie yourself instead of allowing Okta to set it, or want to hold the session ID in order to delete a session via the API instead of visiting the logout URL. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="sessionId, subdomain" /> |  |
| <CopyableCode code="refresh" /> | `EXEC` | <CopyableCode code="sessionId, subdomain" /> |  |
