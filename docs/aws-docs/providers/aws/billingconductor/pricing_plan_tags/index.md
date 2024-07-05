---
title: pricing_plan_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - pricing_plan_tags
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

Expands all tag keys and values for <code>pricing_plans</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pricing_plan_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Pricing Plan enables you to customize your billing details consistent with the usage that accrues in each of your billing groups.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.billingconductor.pricing_plan_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Pricing Plan ARN</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="pricing_rule_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="size" /></td><td><code>integer</code></td><td>Number of associated pricing rules</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>integer</code></td><td>Creation timestamp in UNIX epoch time format</td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>integer</code></td><td>Latest modified timestamp in UNIX epoch time format</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>pricing_plans</code> in a region.
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
tag_key,
tag_value
FROM aws.billingconductor.pricing_plan_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>pricing_plan_tags</code> resource, see <a href="/providers/aws/billingconductor/pricing_plans/#permissions"><code>pricing_plans</code></a>


