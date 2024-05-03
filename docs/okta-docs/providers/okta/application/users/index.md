---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - application
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.application.users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="_embedded" /> | `object` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="credentials" /> | `object` |
| <CopyableCode code="externalId" /> | `string` |
| <CopyableCode code="lastSync" /> | `string` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="passwordChanged" /> | `string` |
| <CopyableCode code="profile" /> | `object` |
| <CopyableCode code="scope" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="statusChanged" /> | `string` |
| <CopyableCode code="syncState" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appId, userId, subdomain" /> | Fetches a specific user assignment for application by `id`. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="appId, subdomain" /> | Enumerates all assigned [application users](#application-user-model) for an application. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="appId, subdomain" /> | Assigns an user to an application with [credentials](#application-user-credentials-object) and an app-specific [profile](#application-user-profile-object). Profile mappings defined for the application are first applied before applying any profile properties specified in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appId, userId, subdomain" /> | Removes an assignment for a user from an application. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="appId, userId, subdomain" /> | Updates a user's profile for an application |
