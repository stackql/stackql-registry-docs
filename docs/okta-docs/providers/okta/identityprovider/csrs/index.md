---
title: csrs
hide_title: false
hide_table_of_contents: false
keywords:
  - csrs
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
<tr><td><b>Name</b></td><td><code>csrs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.identityprovider.csrs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="csr" /> | `string` |
| <CopyableCode code="kty" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="csrId, idpId, subdomain" /> | Gets a specific Certificate Signing Request model by id |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="idpId, subdomain" /> | Enumerates Certificate Signing Requests for an IdP |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="idpId, subdomain" /> | Generates a new key pair and returns a Certificate Signing Request for it. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="csrId, idpId, subdomain" /> | Revoke a Certificate Signing Request and delete the key pair from the IdP |
