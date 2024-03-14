---
title: access_grants_instance
hide_title: false
hide_table_of_contents: false
keywords:
  - access_grants_instance
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
Gets an individual <code>access_grants_instance</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_grants_instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>access_grants_instance</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.s3.access_grants_instance</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>access_grants_instance_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified Access Grants instance.</td></tr>
<tr><td><code>identity_center_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified AWS Identity Center.</td></tr>
<tr><td><code>access_grants_instance_id</code></td><td><code>string</code></td><td>A unique identifier for the specified access grants instance.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
access_grants_instance_arn,
identity_center_arn,
access_grants_instance_id,
tags
FROM awscc.s3.access_grants_instance
WHERE data__Identifier = '<AccessGrantsInstanceArn>';
```

## Permissions

To operate on the <code>access_grants_instance</code> resource, the following permissions are required:

### Read
```json
s3:GetAccessGrantsInstance
```

### Delete
```json
s3:DeleteAccessGrantsInstance
```

### Update
```json
s3:TagResource
```

