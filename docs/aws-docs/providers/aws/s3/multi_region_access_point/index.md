---
title: multi_region_access_point
hide_title: false
hide_table_of_contents: false
keywords:
  - multi_region_access_point
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

Gets or operates on an individual <code>multi_region_access_point</code> resource, use <code>multi_region_access_points</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>multi_region_access_point</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::S3::MultiRegionAccessPoint is an Amazon S3 resource type that dynamically routes S3 requests to easily satisfy geographic compliance requirements based on customer-defined routing policies.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3.multi_region_access_point" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name you want to assign to this Multi Region Access Point.</td></tr>
<tr><td><CopyableCode code="alias" /></td><td><code>string</code></td><td>The alias is a unique identifier to, and is part of the public DNS name for this Multi Region Access Point</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The timestamp of the when the Multi Region Access Point is created</td></tr>
<tr><td><CopyableCode code="public_access_block_configuration" /></td><td><code>object</code></td><td>The PublicAccessBlock configuration that you want to apply to this Multi Region Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;dev&#x2F;access-control-block-public-access.html#access-control-block-public-access-policy-status 'The Meaning of Public' in the Amazon Simple Storage Service Developer Guide.</td></tr>
<tr><td><CopyableCode code="regions" /></td><td><code>array</code></td><td>The list of buckets that you want to associate this Multi Region Access Point with.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
name,
alias,
created_at,
public_access_block_configuration,
regions
FROM aws.s3.multi_region_access_point
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>multi_region_access_point</code> resource, the following permissions are required:

### Read
```json
s3:GetMultiRegionAccessPoint
```

### Delete
```json
s3:DeleteMultiRegionAccessPoint,
s3:DescribeMultiRegionAccessPointOperation,
s3:GetMultiRegionAccessPoint
```
