---
title: role_alias
hide_title: false
hide_table_of_contents: false
keywords:
  - role_alias
  - iot
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>role_alias</code> resource, use <code>role_aliases</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_alias</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Use the AWS::IoT::RoleAlias resource to declare an AWS IoT RoleAlias.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.role_alias" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="role_alias" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="role_alias_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="credential_duration_seconds" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
role_alias,
role_alias_arn,
role_arn,
credential_duration_seconds,
tags
FROM aws.iot.role_alias
WHERE region = 'us-east-1' AND data__Identifier = '<RoleAlias>';
```


## Permissions

To operate on the <code>role_alias</code> resource, the following permissions are required:

### Read
```json
iam:GetRole,
iam:PassRole,
iot:DescribeRoleAlias,
iot:ListTagsForResource
```

### Update
```json
iam:GetRole,
iam:PassRole,
iot:UpdateRoleAlias,
iot:DescribeRoleAlias,
iot:TagResource,
iot:UntagResource,
iot:ListTagsForResource
```

