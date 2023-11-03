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
Gets an individual <code>bucket</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bucket</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lightsail.bucket</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>BucketName</code></td><td><code>string</code></td><td>The name for the bucket.</td></tr><tr><td><code>BundleId</code></td><td><code>string</code></td><td>The ID of the bundle to use for the bucket.</td></tr><tr><td><code>BucketArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ObjectVersioning</code></td><td><code>boolean</code></td><td>Specifies whether to enable or disable versioning of objects in the bucket.</td></tr><tr><td><code>AccessRules</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ResourcesReceivingAccess</code></td><td><code>array</code></td><td>The names of the Lightsail resources for which to set bucket access.</td></tr><tr><td><code>ReadOnlyAccessAccounts</code></td><td><code>array</code></td><td>An array of strings to specify the AWS account IDs that can access the bucket.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr><tr><td><code>Url</code></td><td><code>string</code></td><td>The URL of the bucket.</td></tr><tr><td><code>AbleToUpdateBundle</code></td><td><code>boolean</code></td><td>Indicates whether the bundle that is currently applied to a bucket can be changed to another bundle. You can update a bucket's bundle only one time within a monthly AWS billing cycle.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.lightsail.bucket
WHERE region = 'us-east-1' AND data__Identifier = '{BucketName}'
```
