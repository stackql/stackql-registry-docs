---
title: pricing_plan
hide_title: false
hide_table_of_contents: false
keywords:
  - pricing_plan
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
Gets an individual <code>pricing_plan</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pricing_plan</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Pricing Plan enables you to customize your billing details consistent with the usage that accrues in each of your billing groups.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.billingconductor.pricing_plan</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Pricing Plan ARN</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>pricing_rule_arns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>size</code></td><td><code>integer</code></td><td>Number of associated pricing rules</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>creation_time</code></td><td><code>integer</code></td><td>Creation timestamp in UNIX epoch time format</td></tr>
<tr><td><code>last_modified_time</code></td><td><code>integer</code></td><td>Latest modified timestamp in UNIX epoch time format</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn,
name,
pricing_rule_arns,
size,
description,
creation_time,
last_modified_time,
tags
FROM aws.billingconductor.pricing_plan
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>pricing_plan</code> resource, the following permissions are required:

### Read
```json
billingconductor:ListPricingPlans,
billingconductor:ListPricingRulesAssociatedToPricingPlan,
billingconductor:ListTagsForResource
```

### Update
```json
billingconductor:ListPricingPlans,
billingconductor:UpdatePricingPlan,
billingconductor:ListPricingRulesAssociatedToPricingPlan,
billingconductor:AssociatePricingRules,
billingconductor:DisassociatePricingRules,
billingconductor:TagResource,
billingconductor:UntagResource
```

### Delete
```json
billingconductor:ListPricingPlans,
billingconductor:DeletePricingPlan,
billingconductor:UntagResource
```

