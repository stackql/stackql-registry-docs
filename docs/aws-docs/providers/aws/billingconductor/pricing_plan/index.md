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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>pricing_plan</code> resource, use <code>pricing_plans</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pricing_plan</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Pricing Plan enables you to customize your billing details consistent with the usage that accrues in each of your billing groups.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.billingconductor.pricing_plan" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Pricing Plan ARN</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="pricing_rule_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="size" /></td><td><code>integer</code></td><td>Number of associated pricing rules</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>integer</code></td><td>Creation timestamp in UNIX epoch time format</td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>integer</code></td><td>Latest modified timestamp in UNIX epoch time format</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
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

