---
title: claims
hide_title: false
hide_table_of_contents: false
keywords:
  - claims
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
<tr><td><b>Name</b></td><td><code>claims</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.authorizationserver.claims" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="alwaysIncludeInToken" /> | `boolean` |
| <CopyableCode code="claimType" /> | `string` |
| <CopyableCode code="conditions" /> | `object` |
| <CopyableCode code="group_filter_type" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="system" /> | `boolean` |
| <CopyableCode code="value" /> | `string` |
| <CopyableCode code="valueType" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authServerId, claimId, subdomain" /> |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="authServerId, subdomain" /> |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="authServerId, subdomain" /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="authServerId, claimId, subdomain" /> |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="authServerId, claimId, subdomain" /> |
