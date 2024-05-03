---
title: payments
hide_title: false
hide_table_of_contents: false
keywords:
  - payments
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
<tr><td><b>Name</b></td><td><code>payments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.account.payments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | The unique ID of the Payment. |
| <CopyableCode code="date" /> | `string` | When the Payment was made. |
| <CopyableCode code="usd" /> | `integer` | The amount, in US dollars, of the Payment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getPayment" /> | `SELECT` | <CopyableCode code="paymentId" /> | Returns information about a specific Payment.<br /> |
| <CopyableCode code="getPayments" /> | `SELECT` |  | Returns a paginated list of Payments made on this Account.<br /> |
| <CopyableCode code="createPayment" /> | `INSERT` | <CopyableCode code="data__usd" /> | Makes a Payment to your Account.<br /><br />* The requested amount is charged to the default Payment Method if no `payment_method_id` is specified.<br /><br />* A `payment_submitted` event is generated when a payment is successfully submitted.<br /> |
| <CopyableCode code="_getPayment" /> | `EXEC` | <CopyableCode code="paymentId" /> | Returns information about a specific Payment.<br /> |
| <CopyableCode code="_getPayments" /> | `EXEC` |  | Returns a paginated list of Payments made on this Account.<br /> |
