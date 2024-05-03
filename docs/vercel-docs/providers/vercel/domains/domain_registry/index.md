---
title: domain_registry
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_registry
  - domains
  - vercel    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Vercel resources using SQL
custom_edit_url: null
image: /img/providers/vercel/stackql-vercel-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_registry</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.domains.domain_registry" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="reason" /> | `string` | Description associated with transferable state. |
| <CopyableCode code="status" /> | `string` | The current state of an ongoing transfer. `pending_owner`: Awaiting approval by domain's admin contact (every transfer begins with this status). If approval is not given within five days, the transfer is cancelled. `pending_admin`: Waiting for approval by Vercel Registrar admin. `pending_registry`: Awaiting registry approval (the transfer completes after 7 days unless it is declined by the current registrar). `completed`: The transfer completed successfully. `cancelled`: The transfer was cancelled. `undef`: No transfer exists for this domain. `unknown`: This TLD is not supported by Vercel's Registrar. |
| <CopyableCode code="transferPolicy" /> | `string` | The domain's transfer policy (depends on TLD requirements). `charge-and-renew`: transfer will charge for renewal and will renew the existing domain's registration. `no-charge-no-change`: transfer will have no change to registration period and does not require charge. `no-change`: transfer charge is required, but no change in registration period. `new-term`: transfer charge is required and a new registry term is set based on the transfer date. `not-supported`: transfers are not supported for this domain or TLD. `null`: This TLD is not supported by Vercel's Registrar. |
| <CopyableCode code="transferable" /> | `boolean` | Whether or not the domain is transferable |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_domain_transfer" /> | `SELECT` | <CopyableCode code="domain, teamId" /> |
