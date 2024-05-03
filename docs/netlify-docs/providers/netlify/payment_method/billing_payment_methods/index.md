---
title: billing_payment_methods
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_payment_methods
  - payment_method
  - netlify    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Netlify resources using SQL
custom_edit_url: null
image: /img/providers/netlify/stackql-netlify-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>billing_payment_methods</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="netlify.payment_method.billing_payment_methods" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="created_at" /> | `string` |
| <CopyableCode code="data" /> | `object` |
| <CopyableCode code="method_name" /> | `string` |
| <CopyableCode code="state" /> | `string` |
| <CopyableCode code="type" /> | `string` |
| <CopyableCode code="updated_at" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="listPaymentMethodsForUser" /> | `SELECT` |  |
