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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>profile</code> resource, use <code>profiles</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Transfer::Profile</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer.profile" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="as2_id" /></td><td><code>string</code></td><td>AS2 identifier agreed with a trading partner.</td></tr>
<tr><td><CopyableCode code="profile_type" /></td><td><code>string</code></td><td>Enum specifying whether the profile is local or associated with a trading partner.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="certificate_ids" /></td><td><code>array</code></td><td>List of the certificate IDs associated with this profile to be used for encryption and signing of AS2 messages.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Specifies the unique Amazon Resource Name (ARN) for the profile.</td></tr>
<tr><td><CopyableCode code="profile_id" /></td><td><code>string</code></td><td>A unique identifier for the profile</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
as2_id,
profile_type,
tags,
certificate_ids,
arn,
profile_id
FROM aws.transfer.profile
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

