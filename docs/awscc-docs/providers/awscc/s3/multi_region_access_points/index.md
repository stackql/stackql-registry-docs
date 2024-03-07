---
title: multi_region_access_points
hide_title: false
hide_table_of_contents: false
keywords:
  - multi_region_access_points
  - s3
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>multi_region_access_points</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>multi_region_access_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>multi_region_access_points</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.s3.multi_region_access_points</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name you want to assign to this Multi Region Access Point.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>multi_region_access_points</code> resource, the following permissions are required:

### Create
<pre>
s3:CreateMultiRegionAccessPoint,
s3:DescribeMultiRegionAccessPointOperation,
s3:GetMultiRegionAccessPoint</pre>

### List
<pre>
s3:ListMultiRegionAccessPoints</pre>


## Example
```sql
SELECT
region,
name
FROM awscc.s3.multi_region_access_points
WHERE region = 'us-east-1'
```
