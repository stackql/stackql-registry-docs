---
title: permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - permissions
  - ram
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

Creates, updates, deletes or gets a <code>permission</code> resource or lists <code>permissions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::RAM::Permission</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ram.permissions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the permission.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>Version of the permission.</td></tr>
<tr><td><CopyableCode code="is_resource_type_default" /></td><td><code>boolean</code></td><td>Set to true to use this as the default permission.</td></tr>
<tr><td><CopyableCode code="permission_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_type" /></td><td><code>string</code></td><td>The resource type this permission can be used with.</td></tr>
<tr><td><CopyableCode code="policy_template" /></td><td><code>object</code></td><td>Policy template for the permission.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="Name, ResourceType, PolicyTemplate, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>permissions</code> in a region.
```sql
SELECT
region,
arn
FROM aws.ram.permissions
WHERE region = 'us-east-1';
```
Gets all properties from a <code>permission</code>.
```sql
SELECT
region,
arn,
name,
version,
is_resource_type_default,
permission_type,
resource_type,
policy_template,
tags
FROM aws.ram.permissions
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>permission</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.ram.permissions (
 Name,
 ResourceType,
 PolicyTemplate,
 region
)
SELECT 
'{{ Name }}',
 '{{ ResourceType }}',
 '{{ PolicyTemplate }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ram.permissions (
 Name,
 ResourceType,
 PolicyTemplate,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ ResourceType }}',
 '{{ PolicyTemplate }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: permission
    props:
      - name: Name
        value: '{{ Name }}'
      - name: ResourceType
        value: '{{ ResourceType }}'
      - name: PolicyTemplate
        value: {}
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ram.permissions
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>permissions</code> resource, the following permissions are required:

### Create
```json
ram:CreatePermission,
ram:TagResource
```

### Read
```json
ram:GetPermission
```

### Update
```json
ram:CreatePermissionVersion,
ram:DeletePermissionVersion,
ram:SetDefaultPermissionVersion,
ram:GetPermission,
ram:ReplacePermissionAssociations,
ram:ListReplacePermissionAssociationsWork,
ram:ListPermissionVersions,
ram:UntagResource,
ram:TagResource
```

### Delete
```json
ram:DeletePermissionVersion,
ram:DeletePermission
```

### List
```json
ram:ListPermissions,
ram:ListPermissionVersions
```

