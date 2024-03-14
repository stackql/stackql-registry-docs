---
title: route_calculator
hide_title: false
hide_table_of_contents: false
keywords:
  - route_calculator
  - location
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>route_calculator</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>route_calculator</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>route_calculator</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.location.route_calculator</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>calculator_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>calculator_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>create_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>data_source</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>pricing_plan</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>update_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
calculator_arn,
calculator_name,
create_time,
data_source,
description,
pricing_plan,
tags,
update_time,
arn
FROM awscc.location.route_calculator
WHERE data__Identifier = '<CalculatorName>';
```

## Permissions

To operate on the <code>route_calculator</code> resource, the following permissions are required:

### Read
```json
geo:DescribeRouteCalculator
```

### Update
```json
geo:CreateRouteCalculator,
geo:DescribeRouteCalculator,
geo:TagResource,
geo:UntagResource,
geo:UpdateRouteCalculator
```

### Delete
```json
geo:DeleteRouteCalculator,
geo:DescribeRouteCalculator
```

