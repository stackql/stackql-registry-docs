---
title: service_linked_role
hide_title: false
hide_table_of_contents: false
keywords:
  - service_linked_role
  - iam
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

Gets or operates on an individual <code>service_linked_role</code> resource, use <code>service_linked_roles</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_linked_role</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IAM::ServiceLinkedRole</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.service_linked_role" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="role_name" /></td><td><code>string</code></td><td>The name of the role.</td></tr>
<tr><td><CopyableCode code="custom_suffix" /></td><td><code>string</code></td><td>A string that you provide, which is combined with the service-provided prefix to form the complete role name.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the role.</td></tr>
<tr><td><CopyableCode code="aws_service_name" /></td><td><code>string</code></td><td>The service principal for the AWS service to which this role is attached.</td></tr>
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
role_name,
custom_suffix,
description,
aws_service_name
FROM aws.iam.service_linked_role
WHERE data__Identifier = '<RoleName>';
```

## Permissions

To operate on the <code>service_linked_role</code> resource, the following permissions are required:

### Read
```json
iam:GetRole
```

### Update
```json
iam:UpdateRole,
iam:GetRole
```

### Delete
```json
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus,
iam:GetRole
```

