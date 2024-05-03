---
title: idpkeys
hide_title: false
hide_table_of_contents: false
keywords:
  - idpkeys
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
<tr><td><b>Name</b></td><td><code>idpkeys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.identityprovider.idpkeys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="alg" /> | `string` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="e" /> | `string` |
| <CopyableCode code="expiresAt" /> | `string` |
| <CopyableCode code="false" /> | `string` |
| <CopyableCode code="key_ops" /> | `array` |
| <CopyableCode code="kid" /> | `string` |
| <CopyableCode code="kty" /> | `string` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="use" /> | `string` |
| <CopyableCode code="x5c" /> | `array` |
| <CopyableCode code="x5t" /> | `string` |
| <CopyableCode code="x5t#S256" /> | `string` |
| <CopyableCode code="x5u" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="idpId, keyId, subdomain" /> | Gets a specific IdP Key Credential by `kid` |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="idpId, subdomain" /> | Enumerates signing key credentials for an IdP |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="idpId, validityYears, subdomain" /> | Generates a new X.509 certificate for an IdP signing key credential to be used for signing assertions sent to the IdP |
| <CopyableCode code="clone" /> | `EXEC` | <CopyableCode code="idpId, keyId, targetIdpId, subdomain" /> | Clones a X.509 certificate for an IdP signing key credential from a source IdP to target IdP |
