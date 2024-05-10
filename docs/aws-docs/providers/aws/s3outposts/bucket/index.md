---
title: bucket
hide_title: false
hide_table_of_contents: false
keywords:
  - bucket
  - s3outposts
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


Gets or updates an individual <code>bucket</code> resource, use <code>buckets</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bucket</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type Definition for AWS::S3Outposts::Bucket</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3outposts.bucket" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified bucket.</td></tr>
<tr><td><CopyableCode code="bucket_name" /></td><td><code>string</code></td><td>A name for the bucket.</td></tr>
<tr><td><CopyableCode code="outpost_id" /></td><td><code>string</code></td><td>The id of the customer outpost on which the bucket resides.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this S3Outposts bucket.</td></tr>
<tr><td><CopyableCode code="lifecycle_configuration" /></td><td><code>object</code></td><td>Rules that define how Amazon S3Outposts manages objects during their lifetime.</td></tr>
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
arn,
bucket_name,
outpost_id,
tags,
lifecycle_configuration
FROM aws.s3outposts.bucket
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## Permissions

To operate on the <code>bucket</code> resource, the following permissions are required:

### Read
```json
s3-outposts:GetBucket,
s3-outposts:GetBucketTagging,
s3-outposts:GetLifecycleConfiguration
```

### Update
```json
s3-outposts:PutBucketTagging,
s3-outposts:DeleteBucketTagging,
s3-outposts:PutLifecycleConfiguration
```

