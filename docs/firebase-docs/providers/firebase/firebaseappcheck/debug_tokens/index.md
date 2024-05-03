---
title: debug_tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - debug_tokens
  - firebaseappcheck
  - firebase    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/firebase/stackql-firebase-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>debug_tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="firebase.firebaseappcheck.debug_tokens" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The relative resource name of the debug token, in the format: ``` projects/&#123;project_number&#125;/apps/&#123;app_id&#125;/debugTokens/&#123;debug_token_id&#125; ``` |
| <CopyableCode code="displayName" /> | `string` | Required. A human readable display name used to identify this debug token. |
| <CopyableCode code="token" /> | `string` | Required. Input only. Immutable. The secret token itself. Must be provided during creation, and must be a UUID4, case insensitive. This field is immutable once set, and cannot be provided during an UpdateDebugToken request. You can, however, delete this debug token using DeleteDebugToken to revoke it. For security reasons, this field will never be populated in any response. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_apps_debugTokens_get" /> | `SELECT` | <CopyableCode code="appsId, debugTokensId, projectsId" /> | Gets the specified DebugToken. For security reasons, the `token` field is never populated in the response. |
| <CopyableCode code="projects_apps_debugTokens_list" /> | `SELECT` | <CopyableCode code="appsId, projectsId" /> | Lists all DebugTokens for the specified app. For security reasons, the `token` field is never populated in the response. |
| <CopyableCode code="projects_apps_debugTokens_create" /> | `INSERT` | <CopyableCode code="appsId, projectsId" /> | Creates a new DebugToken for the specified app. For security reasons, after the creation operation completes, the `token` field cannot be updated or retrieved, but you can revoke the debug token using DeleteDebugToken. Each app can have a maximum of 20 debug tokens. |
| <CopyableCode code="projects_apps_debugTokens_delete" /> | `DELETE` | <CopyableCode code="appsId, debugTokensId, projectsId" /> | Deletes the specified DebugToken. A deleted debug token cannot be used to exchange for an App Check token. Use this method when you suspect the secret `token` has been compromised or when you no longer need the debug token. |
| <CopyableCode code="projects_apps_debugTokens_patch" /> | `EXEC` | <CopyableCode code="appsId, debugTokensId, projectsId" /> | Updates the specified DebugToken. For security reasons, the `token` field cannot be updated, nor will it be populated in the response, but you can revoke the debug token using DeleteDebugToken. |
