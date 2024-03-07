---
title: cloud_front_origin_access_identity
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_front_origin_access_identity
  - cloudfront
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>cloud_front_origin_access_identity</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_front_origin_access_identity</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cloud_front_origin_access_identity</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cloudfront.cloud_front_origin_access_identity</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>cloud_front_origin_access_identity_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>s3_canonical_user_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>cloud_front_origin_access_identity</code> resource, the following permissions are required:

### Delete
```json
cloudfront:DeleteCloudFrontOriginAccessIdentity,
cloudfront:GetCloudFrontOriginAccessIdentity
```

### Read
```json
cloudfront:GetCloudFrontOriginAccessIdentity
```

### Update
```json
cloudfront:UpdateCloudFrontOriginAccessIdentity,
cloudfront:GetCloudFrontOriginAccessIdentity
```


## Example
```sql
SELECT
region,
cloud_front_origin_access_identity_config,
id,
s3_canonical_user_id
FROM awscc.cloudfront.cloud_front_origin_access_identity
WHERE data__Identifier = '&lt;Id&gt;'
```
