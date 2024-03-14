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
Gets an individual <code>custom_line_item</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_line_item</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>custom_line_item</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.billingconductor.custom_line_item</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>custom_line_item_charge_details</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>billing_group_arn</code></td><td><code>string</code></td><td>Billing Group ARN</td></tr>
<tr><td><code>billing_period_range</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>ARN</td></tr>
<tr><td><code>creation_time</code></td><td><code>integer</code></td><td>Creation timestamp in UNIX epoch time format</td></tr>
<tr><td><code>last_modified_time</code></td><td><code>integer</code></td><td>Latest modified timestamp in UNIX epoch time format</td></tr>
<tr><td><code>association_size</code></td><td><code>integer</code></td><td>Number of source values associated to this custom line item</td></tr>
<tr><td><code>product_code</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>currency_code</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>account_id</code></td><td><code>string</code></td><td>The account which this custom line item will be charged to</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.billingconductor.custom_line_item
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

