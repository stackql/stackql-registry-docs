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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>payments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.account.payments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The unique ID of the Payment. |
| `date` | `string` | When the Payment was made. |
| `usd` | `integer` | The amount, in US dollars, of the Payment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getPayment` | `SELECT` | `paymentId` | Returns information about a specific Payment.<br /> |
| `getPayments` | `SELECT` |  | Returns a paginated list of Payments made on this Account.<br /> |
| `createPayment` | `INSERT` | `data__usd` | Makes a Payment to your Account.<br /><br />* The requested amount is charged to the default Payment Method if no `payment_method_id` is specified.<br /><br />* A `payment_submitted` event is generated when a payment is successfully submitted.<br /> |
| `_getPayment` | `EXEC` | `paymentId` | Returns information about a specific Payment.<br /> |
| `_getPayments` | `EXEC` |  | Returns a paginated list of Payments made on this Account.<br /> |
