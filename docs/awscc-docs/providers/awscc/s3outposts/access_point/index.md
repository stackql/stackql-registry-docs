---
title: access_point
hide_title: false
hide_table_of_contents: false
keywords:
  - access_point
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
Gets an individual <code>access_point</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_point</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>access_point</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.s3outposts.access_point</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified AccessPoint.</td></tr>
<tr><td><code>bucket</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the bucket you want to associate this AccessPoint with.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>A name for the AccessPoint.</td></tr>
<tr><td><code>vpc_configuration</code></td><td><code>object</code></td><td>Virtual Private Cloud (VPC) from which requests can be made to the AccessPoint.</td></tr>
<tr><td><code>policy</code></td><td><code>object</code></td><td>The access point policy associated with this access point.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
bucket,
name,
vpc_configuration,
policy
FROM awscc.s3outposts.access_point
WHERE region = 'us-east-1'
AND data__Identifier = '{Arn}';
```

## Permissions

To operate on the <code>access_point</code> resource, the following permissions are required:

### Read
```json
s3-outposts:GetAccessPoint,
s3-outposts:GetAccessPointPolicy
```

### Update
```json
s3-outposts:GetAccessPoint,
s3-outposts:PutAccessPointPolicy,
s3-outposts:GetAccessPointPolicy,
s3-outposts:DeleteAccessPointPolicy
```

### Delete
```json
s3-outposts:DeleteAccessPoint,
s3-outposts:DeleteAccessPointPolicy
```

