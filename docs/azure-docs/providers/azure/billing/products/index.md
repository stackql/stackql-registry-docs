---
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
  - billing
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.products" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | The properties of a product. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="billingAccountName, productName" /> | Gets a product by ID. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="list_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | Lists the products for a billing account. These don't include products billed based on usage. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement. |
| <CopyableCode code="list_by_billing_profile" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName" /> | Lists the products for a billing profile. These don't include products billed based on usage. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement. |
| <CopyableCode code="list_by_customer" /> | `SELECT` | <CopyableCode code="billingAccountName, customerName" /> | Lists the products for a customer. These don't include products billed based on usage.The operation is supported only for billing accounts with agreement type Microsoft Partner Agreement. |
| <CopyableCode code="list_by_invoice_section" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName" /> | Lists the products for an invoice section. These don't include products billed based on usage. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="move" /> | `EXEC` | <CopyableCode code="billingAccountName, productName" /> | Moves a product's charges to a new invoice section. The new invoice section must belong to the same billing profile as the existing invoice section. This operation is supported only for products that are purchased with a recurring charge and for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="billingAccountName, productName" /> | Updates the properties of a Product. Currently, auto renew can be updated. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="validate_move" /> | `EXEC` | <CopyableCode code="billingAccountName, productName" /> | Validates if a product's charges can be moved to a new invoice section. This operation is supported only for products that are purchased with a recurring charge and for billing accounts with agreement type Microsoft Customer Agreement. |
