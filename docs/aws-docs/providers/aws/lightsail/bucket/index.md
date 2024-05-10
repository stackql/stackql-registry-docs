---
title: bucket
hide_title: false
hide_table_of_contents: false
keywords:
  - bucket
  - lightsail
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
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lightsail::Bucket</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lightsail.bucket" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="bucket_name" /></td><td><code>string</code></td><td>The name for the bucket.</td></tr>
<tr><td><CopyableCode code="bundle_id" /></td><td><code>string</code></td><td>The ID of the bundle to use for the bucket.</td></tr>
<tr><td><CopyableCode code="bucket_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="object_versioning" /></td><td><code>boolean</code></td><td>Specifies whether to enable or disable versioning of objects in the bucket.</td></tr>
<tr><td><CopyableCode code="access_rules" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="resources_receiving_access" /></td><td><code>array</code></td><td>The names of the Lightsail resources for which to set bucket access.</td></tr>
<tr><td><CopyableCode code="read_only_access_accounts" /></td><td><code>array</code></td><td>An array of strings to specify the AWS account IDs that can access the bucket.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="url" /></td><td><code>string</code></td><td>The URL of the bucket.</td></tr>
<tr><td><CopyableCode code="able_to_update_bundle" /></td><td><code>boolean</code></td><td>Indicates whether the bundle that is currently applied to a bucket can be changed to another bundle. You can update a bucket's bundle only one time within a monthly AWS billing cycle.</td></tr>
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
bucket_name,
bundle_id,
bucket_arn,
object_versioning,
access_rules,
resources_receiving_access,
read_only_access_accounts,
tags,
url,
able_to_update_bundle
FROM aws.lightsail.bucket
WHERE region = 'us-east-1' AND data__Identifier = '<BucketName>';
```


## Permissions

To operate on the <code>bucket</code> resource, the following permissions are required:

### Read
```json
lightsail:GetBuckets
```

### Update
```json
lightsail:GetBuckets,
lightsail:GetInstance,
lightsail:UpdateBucket,
lightsail:UpdateBucketBundle,
lightsail:SetResourceAccessForBucket,
lightsail:TagResource,
lightsail:UntagResource
```

