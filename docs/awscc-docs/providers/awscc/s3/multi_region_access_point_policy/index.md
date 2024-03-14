---
title: multi_region_access_point_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - multi_region_access_point_policy
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
Gets an individual <code>multi_region_access_point_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>multi_region_access_point_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>multi_region_access_point_policy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.s3.multi_region_access_point_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>mrap_name</code></td><td><code>string</code></td><td>The name of the Multi Region Access Point to apply policy</td></tr>
<tr><td><code>policy</code></td><td><code>object</code></td><td>Policy document to apply to a Multi Region Access Point</td></tr>
<tr><td><code>policy_status</code></td><td><code>object</code></td><td>The Policy Status associated with this Multi Region Access Point</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
mrap_name,
policy,
policy_status
FROM awscc.s3.multi_region_access_point_policy
WHERE data__Identifier = '<MrapName>';
```

## Permissions

To operate on the <code>multi_region_access_point_policy</code> resource, the following permissions are required:

### Update
```json
s3:PutMultiRegionAccessPointPolicy,
s3:DescribeMultiRegionAccessPointOperation
```

### Read
```json
s3:GetMultiRegionAccessPointPolicy,
s3:GetMultiRegionAccessPointPolicyStatus
```

### Delete
```json
s3:GetMultiRegionAccessPointPolicy,
s3:GetMultiRegionAccessPoint
```

