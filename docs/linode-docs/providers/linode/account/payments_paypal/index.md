---
title: payments_paypal
hide_title: false
hide_table_of_contents: false
keywords:
  - payments_paypal
  - account
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>payments_paypal</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.account.payments_paypal" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="createPayPalPayment" /> | `INSERT` | <CopyableCode code="data__cancel_url, data__redirect_url, data__usd" /> |
| <CopyableCode code="executePayPalPayment" /> | `EXEC` | <CopyableCode code="data__payer_id, data__payment_id" /> |
