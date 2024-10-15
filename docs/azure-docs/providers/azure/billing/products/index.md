---
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
  - billing
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>products</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.products" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A product. |
| <CopyableCode code="tags" /> | `object` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="billingAccountName, productName" /> | Gets a product by ID. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="list_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | Lists the products for a billing account. These don't include products billed based on usage. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement. |
| <CopyableCode code="list_by_billing_profile" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName" /> | Lists the products for a billing profile. These don't include products billed based on usage. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement. |
| <CopyableCode code="list_by_customer" /> | `SELECT` | <CopyableCode code="billingAccountName, customerName" /> | Lists the products for a customer. These don't include products billed based on usage.The operation is supported only for billing accounts with agreement type Microsoft Partner Agreement. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="billingAccountName, productName" /> | Updates the properties of a Product. Currently, auto renew can be updated. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="move" /> | `EXEC` | <CopyableCode code="billingAccountName, productName, data__destinationInvoiceSectionId" /> | Moves a product's charges to a new invoice section. The new invoice section must belong to the same billing profile as the existing invoice section. This operation is supported only for products that are purchased with a recurring charge and for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="validate_move_eligibility" /> | `EXEC` | <CopyableCode code="billingAccountName, productName, data__destinationInvoiceSectionId" /> | Validates if a product's charges can be moved to a new invoice section. This operation is supported only for products that are purchased with a recurring charge and for billing accounts with agreement type Microsoft Customer Agreement. |

## `SELECT` examples

Lists the products for a billing account. These don't include products billed based on usage. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement.


```sql
SELECT
properties,
tags
FROM azure.billing.products
WHERE billingAccountName = '{{ billingAccountName }}';
```
## `UPDATE` example

Updates a <code>products</code> resource.

```sql
/*+ update */
UPDATE azure.billing.products
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
billingAccountName = '{{ billingAccountName }}'
AND productName = '{{ productName }}';
```
