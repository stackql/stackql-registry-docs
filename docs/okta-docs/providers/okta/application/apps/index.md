---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
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
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.application.apps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="_embedded" /> | `object` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="accessibility" /> | `object` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="credentials" /> | `object` |
| <CopyableCode code="features" /> | `array` |
| <CopyableCode code="label" /> | `string` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="licensing" /> | `object` |
| <CopyableCode code="profile" /> | `object` |
| <CopyableCode code="settings" /> | `object` |
| <CopyableCode code="signOnMode" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="visibility" /> | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appId, subdomain" /> | Fetches an application from your Okta organization by `id`. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subdomain" /> | Enumerates apps added to your organization with pagination. A subset of apps can be returned that match a supported filter expression or query. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="subdomain" /> | Adds a new application to your Okta organization. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appId, subdomain" /> | Removes an inactive application. |
| <CopyableCode code="activate" /> | `EXEC` | <CopyableCode code="appId, subdomain" /> | Activates an inactive application. |
| <CopyableCode code="deactivate" /> | `EXEC` | <CopyableCode code="appId, subdomain" /> | Deactivates an active application. |
| <CopyableCode code="deleteall" /> | `EXEC` | <CopyableCode code="appId, subdomain" /> | Revokes all tokens for the specified application |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="appId, subdomain" /> | Updates an application in your organization. |
