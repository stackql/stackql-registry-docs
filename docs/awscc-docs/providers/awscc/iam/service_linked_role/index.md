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
Gets an individual <code>service_linked_role</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_linked_role</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>service_linked_role</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iam.service_linked_role</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>role_name</code></td><td><code>string</code></td><td>The name of the role.</td></tr>
<tr><td><code>custom_suffix</code></td><td><code>string</code></td><td>A string that you provide, which is combined with the service-provided prefix to form the complete role name.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the role.</td></tr>
<tr><td><code>a_ws_service_name</code></td><td><code>string</code></td><td>The service principal for the AWS service to which this role is attached.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
role_name,
custom_suffix,
description,
a_ws_service_name
FROM awscc.iam.service_linked_role
WHERE data__Identifier = '{RoleName}';
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

