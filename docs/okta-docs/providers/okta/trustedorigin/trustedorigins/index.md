---
title: trustedorigins
hide_title: false
hide_table_of_contents: false
keywords:
  - trustedorigins
  - trustedorigin
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
<tr><td><b>Name</b></td><td><code>trustedorigins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.trustedorigin.trustedorigins" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="createdBy" /> | `string` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="lastUpdatedBy" /> | `string` |
| <CopyableCode code="origin" /> | `string` |
| <CopyableCode code="scopes" /> | `array` |
| <CopyableCode code="status" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="trustedOriginId, subdomain" /> |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subdomain" /> |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="subdomain" /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="trustedOriginId, subdomain" /> |
| <CopyableCode code="activate" /> | `EXEC` | <CopyableCode code="trustedOriginId, subdomain" /> |
| <CopyableCode code="deactivate" /> | `EXEC` | <CopyableCode code="trustedOriginId, subdomain" /> |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="trustedOriginId, subdomain" /> |
