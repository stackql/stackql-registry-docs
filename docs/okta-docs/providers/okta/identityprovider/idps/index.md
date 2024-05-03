---
title: idps
hide_title: false
hide_table_of_contents: false
keywords:
  - idps
  - identityprovider
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
<tr><td><b>Id</b></td><td><CopyableCode code="okta.identityprovider.idps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="issuerMode" /> | `string` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="policy" /> | `object` |
| <CopyableCode code="protocol" /> | `object` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="type" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="idpId, subdomain" /> | Fetches an IdP by `id`. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subdomain" /> | Enumerates IdPs in your organization with pagination. A subset of IdPs can be returned that match a supported filter expression or query. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="subdomain" /> | Adds a new IdP to your organization. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="idpId, subdomain" /> | Removes an IdP from your organization. |
| <CopyableCode code="activate" /> | `EXEC` | <CopyableCode code="idpId, subdomain" /> | Activates an inactive IdP. |
| <CopyableCode code="deactivate" /> | `EXEC` | <CopyableCode code="idpId, subdomain" /> | Activates an inactive IdP. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="idpId, subdomain" /> | Updates the configuration for an IdP. |
