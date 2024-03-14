---
title: profile
hide_title: false
hide_table_of_contents: false
keywords:
  - profile
  - transfer
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
<tr><td><b>Id</b></td><td><code>awscc.transfer.profile</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>as2_id</code></td><td><code>string</code></td><td>AS2 identifier agreed with a trading partner.</td></tr>
<tr><td><code>profile_type</code></td><td><code>string</code></td><td>Enum specifying whether the profile is local or associated with a trading partner.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>certificate_ids</code></td><td><code>array</code></td><td>List of the certificate IDs associated with this profile to be used for encryption and signing of AS2 messages.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Specifies the unique Amazon Resource Name (ARN) for the profile.</td></tr>
<tr><td><code>profile_id</code></td><td><code>string</code></td><td>A unique identifier for the profile</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
as2_id,
profile_type,
tags,
certificate_ids,
arn,
profile_id
FROM awscc.transfer.profile
WHERE data__Identifier = '<ProfileId>';
```

## Permissions

To operate on the <code>profile</code> resource, the following permissions are required:

### Read
```json
transfer:DescribeProfile
```

### Update
```json
transfer:UpdateProfile,
transfer:UnTagResource,
transfer:TagResource
```

### Delete
```json
transfer:DeleteProfile
```

