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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Used to retrieve a list of <code>multi_region_access_points</code> in a region or create a <code>multi_region_access_points</code> resource, use <code>multi_region_access_point</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>multi_region_access_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::S3::MultiRegionAccessPoint is an Amazon S3 resource type that dynamically routes S3 requests to easily satisfy geographic compliance requirements based on customer-defined routing policies.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3.multi_region_access_points" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name you want to assign to this Multi Region Access Point.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
name
FROM aws.s3.multi_region_access_points
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>multi_region_access_points</code> resource, the following permissions are required:

### Create
```json
s3:CreateMultiRegionAccessPoint,
s3:DescribeMultiRegionAccessPointOperation,
s3:GetMultiRegionAccessPoint
```

### List
```json
s3:ListMultiRegionAccessPoints
```
