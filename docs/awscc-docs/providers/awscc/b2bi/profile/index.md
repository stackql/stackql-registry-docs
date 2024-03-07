---
title: profile
hide_title: false
hide_table_of_contents: false
keywords:
  - profile
  - b2bi
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>profile</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>profile</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.b2bi.profile</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>business_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>email</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>log_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>logging</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>modified_at</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>phone</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>profile_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>profile_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
business_name,
created_at,
email,
log_group_name,
logging,
modified_at,
name,
phone,
profile_arn,
profile_id,
tags
FROM awscc.b2bi.profile
WHERE region = 'us-east-1'
AND data__Identifier = '{ProfileId}';
```

## Permissions

To operate on the <code>profile</code> resource, the following permissions are required:

### Read
```json
b2bi:GetProfile,
b2bi:ListTagsForResource
```

### Update
```json
b2bi:TagResource,
b2bi:UntagResource,
b2bi:UpdateProfile
```

### Delete
```json
b2bi:DeleteProfile,
logs:DeleteLogDelivery,
logs:ListLogDeliveries
```

