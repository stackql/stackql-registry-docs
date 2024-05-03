---
title: grants
hide_title: false
hide_table_of_contents: false
keywords:
  - grants
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
<tr><td><b>Name</b></td><td><code>grants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.application.grants" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="_embedded" /> | `object` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="clientId" /> | `string` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="createdBy" /> | `object` |
| <CopyableCode code="issuer" /> | `string` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="scopeId" /> | `string` |
| <CopyableCode code="source" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="userId" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appId, grantId, subdomain" /> | Fetches a single scope consent grant for the application |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="appId, subdomain" /> | Lists all scope consent grants for the application |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="appId, subdomain" /> | Grants consent for the application to request an OAuth 2.0 Okta scope |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appId, grantId, subdomain" /> | Revokes permission for the application to request the given scope |
