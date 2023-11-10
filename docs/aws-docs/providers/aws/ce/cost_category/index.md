---
title: cost_category
hide_title: false
hide_table_of_contents: false
keywords:
  - cost_category
  - ce
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>cost_category</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cost_category</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cost_category</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ce.cost_category</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Cost category ARN</td></tr>
<tr><td><code>effective_start</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>rule_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>rules</code></td><td><code>string</code></td><td>JSON array format of Expression in Billing and Cost Management API</td></tr>
<tr><td><code>split_charge_rules</code></td><td><code>string</code></td><td>Json array format of CostCategorySplitChargeRule in Billing and Cost Management API</td></tr>
<tr><td><code>default_value</code></td><td><code>string</code></td><td>The default value for the cost category</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
effective_start,
name,
rule_version,
rules,
split_charge_rules,
default_value
FROM aws.ce.cost_category
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
