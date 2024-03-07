---
title: access_grants_location
hide_title: false
hide_table_of_contents: false
keywords:
  - access_grants_location
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
Gets an individual <code>access_grants_location</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_grants_location</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>access_grants_location</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.s3.access_grants_location</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>access_grants_location_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified Access Grants location.</td></tr>
<tr><td><code>access_grants_location_id</code></td><td><code>string</code></td><td>The unique identifier for the specified Access Grants location.</td></tr>
<tr><td><code>iam_role_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the access grant location's associated IAM role.</td></tr>
<tr><td><code>location_scope</code></td><td><code>string</code></td><td>Descriptor for where the location actually points</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>access_grants_location</code> resource, the following permissions are required:

### Read
<pre>
s3:GetAccessGrantsLocation</pre>

### Delete
<pre>
s3:DeleteAccessGrantsLocation</pre>

### Update
<pre>
s3:UpdateAccessGrantsLocation,
s3:TagResource,
iam:PassRole</pre>


## Example
```sql
SELECT
region,
access_grants_location_arn,
access_grants_location_id,
iam_role_arn,
location_scope,
tags
FROM awscc.s3.access_grants_location
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;AccessGrantsLocationId&gt;'
```
