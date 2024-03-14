---
title: access_grant
hide_title: false
hide_table_of_contents: false
keywords:
  - access_grant
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
Gets an individual <code>access_grant</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_grant</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>access_grant</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.s3.access_grant</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>access_grant_id</code></td><td><code>string</code></td><td>The ID assigned to this access grant.</td></tr>
<tr><td><code>access_grants_location_id</code></td><td><code>string</code></td><td>The custom S3 location to be accessed by the grantee</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>permission</code></td><td><code>string</code></td><td>The level of access to be afforded to the grantee</td></tr>
<tr><td><code>application_arn</code></td><td><code>string</code></td><td>The ARN of the application grantees will use to access the location</td></tr>
<tr><td><code>s3_prefix_type</code></td><td><code>string</code></td><td>The type of S3SubPrefix.</td></tr>
<tr><td><code>grant_scope</code></td><td><code>string</code></td><td>The S3 path of the data to which you are granting access. It is a combination of the S3 path of the registered location and the subprefix.</td></tr>
<tr><td><code>access_grant_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified access grant.</td></tr>
<tr><td><code>grantee</code></td><td><code>object</code></td><td>The principal who will be granted permission to access S3.</td></tr>
<tr><td><code>access_grants_location_configuration</code></td><td><code>object</code></td><td>The configuration options of the grant location, which is the S3 path to the data to which you are granting access.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
access_grant_id,
access_grants_location_id,
tags,
permission,
application_arn,
s3_prefix_type,
grant_scope,
access_grant_arn,
grantee,
access_grants_location_configuration
FROM awscc.s3.access_grant
WHERE data__Identifier = '<AccessGrantId>';
```

## Permissions

To operate on the <code>access_grant</code> resource, the following permissions are required:

### Read
```json
s3:GetAccessGrant
```

### Delete
```json
s3:DeleteAccessGrant
```

### Update
```json
s3:TagResource
```

