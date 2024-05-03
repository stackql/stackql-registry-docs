---
title: custom_line_item
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_line_item
  - billingconductor
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>custom_line_item</code> resource, use <code>custom_line_items</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_line_item</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A custom line item is an one time charge that is applied to a specific billing group's bill.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.billingconductor.custom_line_item" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="custom_line_item_charge_details" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="billing_group_arn" /></td><td><code>string</code></td><td>Billing Group ARN</td></tr>
<tr><td><CopyableCode code="billing_period_range" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>ARN</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>integer</code></td><td>Creation timestamp in UNIX epoch time format</td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>integer</code></td><td>Latest modified timestamp in UNIX epoch time format</td></tr>
<tr><td><CopyableCode code="association_size" /></td><td><code>integer</code></td><td>Number of source values associated to this custom line item</td></tr>
<tr><td><CopyableCode code="product_code" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="currency_code" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td>The account which this custom line item will be charged to</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
name,
description,
custom_line_item_charge_details,
billing_group_arn,
billing_period_range,
arn,
creation_time,
last_modified_time,
association_size,
product_code,
currency_code,
account_id,
tags
FROM aws.billingconductor.custom_line_item
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>custom_line_item</code> resource, the following permissions are required:

### Read
```json
billingconductor:ListCustomLineItems,
billingconductor:ListCustomLineItemVersions,
billingconductor:ListResourcesAssociatedToCustomLineItem,
billingconductor:ListTagsForResource
```

### Update
```json
billingconductor:UpdateCustomLineItem,
billingconductor:ListCustomLineItems,
billingconductor:ListResourcesAssociatedToCustomLineItem,
billingconductor:BatchAssociateResourcesToCustomLineItem,
billingconductor:BatchDisassociateResourcesFromCustomLineItem,
billingconductor:TagResource,
billingconductor:UntagResource
```

### Delete
```json
billingconductor:DeleteCustomLineItem,
billingconductor:ListCustomLineItems,
billingconductor:BatchDisassociateResourcesFromCustomLineItem,
billingconductor:ListResourcesAssociatedToCustomLineItem,
billingconductor:UntagResource
```

