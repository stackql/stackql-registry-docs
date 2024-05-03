---
title: csrs
hide_title: false
hide_table_of_contents: false
keywords:
  - csrs
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
<tr><td><b>Name</b></td><td><code>csrs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.application.csrs" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appId, csrId, subdomain" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="appId, subdomain" /> | Enumerates Certificate Signing Requests for an application |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="appId, subdomain" /> | Generates a new key pair and returns the Certificate Signing Request for it. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appId, csrId, subdomain" /> |  |
