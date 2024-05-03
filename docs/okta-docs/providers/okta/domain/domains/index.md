---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - domain
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
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.domain.domains" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainId, subdomain" /> | Fetches a Domain by `id`. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subdomain" /> | List all verified custom Domains for the org. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="subdomain" /> | Creates your domain. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="domainId, subdomain" /> | Deletes a Domain by `id`. |
| <CopyableCode code="verify" /> | `EXEC` | <CopyableCode code="domainId, subdomain" /> | Verifies the Domain by `id`. |
