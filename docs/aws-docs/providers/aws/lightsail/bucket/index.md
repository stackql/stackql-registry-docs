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
Gets or operates on an individual <code>bucket</code> resource, use <code>buckets</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bucket</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lightsail::Bucket</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lightsail.bucket</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>bucket_name</code></td><td><code>string</code></td><td>The name for the bucket.</td></tr>
<tr><td><code>bundle_id</code></td><td><code>string</code></td><td>The ID of the bundle to use for the bucket.</td></tr>
<tr><td><code>bucket_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>object_versioning</code></td><td><code>boolean</code></td><td>Specifies whether to enable or disable versioning of objects in the bucket.</td></tr>
<tr><td><code>access_rules</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>resources_receiving_access</code></td><td><code>array</code></td><td>The names of the Lightsail resources for which to set bucket access.</td></tr>
<tr><td><code>read_only_access_accounts</code></td><td><code>array</code></td><td>An array of strings to specify the AWS account IDs that can access the bucket.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>url</code></td><td><code>string</code></td><td>The URL of the bucket.</td></tr>
<tr><td><code>able_to_update_bundle</code></td><td><code>boolean</code></td><td>Indicates whether the bundle that is currently applied to a bucket can be changed to another bundle. You can update a bucket's bundle only one time within a monthly AWS billing cycle.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
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
WHERE data__Identifier = '<BucketName>';
```

## Permissions

To operate on the <code>bucket</code> resource, the following permissions are required:

### Read
```json
lightsail:GetBuckets
```

### Delete
```json
lightsail:DeleteBucket,
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

