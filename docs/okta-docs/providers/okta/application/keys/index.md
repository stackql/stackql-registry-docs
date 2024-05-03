---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
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
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.application.keys" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appId, keyId, subdomain" /> | Gets a specific application key credential by kid |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="appId, subdomain" /> | Enumerates key credentials for an application |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="appId, subdomain" /> | Generates a new X.509 certificate for an application key credential |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appId, csrId, subdomain" /> |  |
