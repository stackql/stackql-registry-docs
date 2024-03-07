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
Gets an individual <code>multi_region_access_point</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>multi_region_access_point</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>multi_region_access_point</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.s3.multi_region_access_point</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name you want to assign to this Multi Region Access Point.</td></tr>
<tr><td><code>alias</code></td><td><code>string</code></td><td>The alias is a unique identifier to, and is part of the public DNS name for this Multi Region Access Point</td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>The timestamp of the when the Multi Region Access Point is created</td></tr>
<tr><td><code>public_access_block_configuration</code></td><td><code>object</code></td><td>The PublicAccessBlock configuration that you want to apply to this Multi Region Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;dev&#x2F;access-control-block-public-access.html#access-control-block-public-access-policy-status 'The Meaning of Public' in the Amazon Simple Storage Service Developer Guide.</td></tr>
<tr><td><code>regions</code></td><td><code>array</code></td><td>The list of buckets that you want to associate this Multi Region Access Point with.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
alias,
created_at,
public_access_block_configuration,
regions
FROM awscc.s3.multi_region_access_point
WHERE region = 'us-east-1'
AND data__Identifier = '{Name}';
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

