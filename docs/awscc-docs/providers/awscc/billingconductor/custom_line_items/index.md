---
title: custom_line_items
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_line_items
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
Retrieves a list of <code>custom_line_items</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_line_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>custom_line_items</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.billingconductor.custom_line_items</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>ARN</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>custom_line_items</code> resource, the following permissions are required:

### Create
```json
billingconductor:CreateCustomLineItem,
billingconductor:BatchAssociateResourcesToCustomLineItem,
billingconductor:ListCustomLineItems,
billingconductor:TagResource,
billingconductor:ListTagsForResource
```

### List
```json
billingconductor:ListCustomLineItems,
billingconductor:ListResourcesAssociatedToCustomLineItem,
billingconductor:ListTagsForResource
```


## Example
```sql
SELECT
region,
arn
FROM awscc.billingconductor.custom_line_items
WHERE region = 'us-east-1'
```
