---
title: route_calculators
hide_title: false
hide_table_of_contents: false
keywords:
  - route_calculators
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
Retrieves a list of <code>route_calculators</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>route_calculators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>route_calculators</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.location.route_calculators</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>calculator_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>route_calculators</code> resource, the following permissions are required:

### Create
<pre>
geo:CreateRouteCalculator,
geo:DescribeRouteCalculator,
geo:TagResource,
geo:UntagResource</pre>

### List
<pre>
geo:ListRouteCalculators</pre>


## Example
```sql
SELECT
region,
calculator_name
FROM awscc.location.route_calculators
WHERE region = 'us-east-1'
```
