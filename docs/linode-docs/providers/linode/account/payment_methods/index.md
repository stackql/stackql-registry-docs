---
title: payment_methods
hide_title: false
hide_table_of_contents: false
keywords:
  - payment_methods
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
<tr><td><b>Name</b></td><td><code>payment_methods</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.account.payment_methods" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | The unique ID of this Payment Method. |
| <CopyableCode code="created" /> | `string` | When the Payment Method was added to the Account. |
| <CopyableCode code="data" /> | `` |  |
| <CopyableCode code="is_default" /> | `boolean` | Whether this Payment Method is the default method for automatically processing service charges.<br /> |
| <CopyableCode code="type" /> | `string` | The type of Payment Method. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getPaymentMethod" /> | `SELECT` | <CopyableCode code="paymentMethodId" /> | View the details of the specified Payment Method.<br /> |
| <CopyableCode code="getPaymentMethods" /> | `SELECT` |  | Returns a paginated list of Payment Methods for this Account.<br /> |
| <CopyableCode code="createPaymentMethod" /> | `INSERT` | <CopyableCode code="data__data, data__is_default, data__type" /> | Adds a Payment Method to your Account with the option to set it as the default method.<br /><br />* Adding a default Payment Method removes the default status from any other Payment Method.<br /><br />* An Account can have up to 6 active Payment Methods.<br /><br />* Up to 60 Payment Methods can be added each day.<br /><br />* Prior to adding a Payment Method, ensure that your billing address information is up-to-date<br />with a valid `zip` by using the Account Update ([PUT /account](/docs/api/account/#account-update)) endpoint.<br /><br />* A `payment_method_add` event is generated when a payment is successfully submitted.<br /> |
| <CopyableCode code="deletePaymentMethod" /> | `DELETE` | <CopyableCode code="paymentMethodId" /> | Deactivate the specified Payment Method.<br /><br />The default Payment Method can not be deleted. To add a new default Payment Method, access the Payment Method<br />Add ([POST /account/payment-methods](/docs/api/account/#payment-method-add)) endpoint. To designate an existing<br />Payment Method as the default method, access the Payment Method Make Default<br />([POST /account/payment-methods/&#123;paymentMethodId&#125;/make-default](/docs/api/account/#payment-method-make-default))<br />endpoint.<br /> |
| <CopyableCode code="_getPaymentMethod" /> | `EXEC` | <CopyableCode code="paymentMethodId" /> | View the details of the specified Payment Method.<br /> |
| <CopyableCode code="_getPaymentMethods" /> | `EXEC` |  | Returns a paginated list of Payment Methods for this Account.<br /> |
| <CopyableCode code="makePaymentMethodDefault" /> | `EXEC` | <CopyableCode code="paymentMethodId" /> | Make the specified Payment Method the default method for automatically processing payments.<br /><br />Removes the default status from any other Payment Method.<br /> |
