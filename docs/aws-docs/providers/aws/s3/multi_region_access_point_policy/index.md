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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>multi_region_access_point_policy</code> resource, use <code>multi_region_access_point_policies</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>multi_region_access_point_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The policy to be attached to a Multi Region Access Point</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3.multi_region_access_point_policy" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="mrap_name" /></td><td><code>string</code></td><td>The name of the Multi Region Access Point to apply policy</td></tr>
<tr><td><CopyableCode code="policy" /></td><td><code>object</code></td><td>Policy document to apply to a Multi Region Access Point</td></tr>
<tr><td><CopyableCode code="policy_status" /></td><td><code>object</code></td><td>The Policy Status associated with this Multi Region Access Point</td></tr>
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
mrap_name,
policy,
policy_status
FROM aws.s3.multi_region_access_point_policy
WHERE region = 'us-east-1' AND data__Identifier = '<MrapName>';
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

