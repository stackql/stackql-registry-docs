---
title: transactions
hide_title: false
hide_table_of_contents: false
keywords:
  - transactions
  - userfactor
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
<tr><td><b>Name</b></td><td><code>transactions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.userfactor.transactions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="_embedded" /> | `object` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="expiresAt" /> | `string` |
| <CopyableCode code="factorResult" /> | `string` |
| <CopyableCode code="factorResultMessage" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="factorId, transactionId, userId, subdomain" /> |
