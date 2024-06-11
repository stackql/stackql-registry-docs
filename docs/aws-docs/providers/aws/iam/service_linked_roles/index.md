---
title: service_linked_roles
hide_title: false
hide_table_of_contents: false
keywords:
  - service_linked_roles
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>service_linked_role</code> resource or lists <code>service_linked_roles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_linked_roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IAM::ServiceLinkedRole</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.service_linked_roles" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="role_name" /></td><td><code>string</code></td><td>The name of the role.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code=", region" /></td>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from a <code>service_linked_role</code>.
```sql
SELECT
region,
role_name,
custom_suffix,
description,
aws_service_name
FROM aws.iam.service_linked_roles
WHERE data__Identifier = '<RoleName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>service_linked_role</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iam.service_linked_roles (
 ,
 region
)
SELECT 
'{{  }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iam.service_linked_roles (
 CustomSuffix,
 Description,
 AWSServiceName,
 region
)
SELECT 
 '{{ CustomSuffix }}',
 '{{ Description }}',
 '{{ AWSServiceName }}',
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
  - name: service_linked_role
    props:
      - name: CustomSuffix
        value: '{{ CustomSuffix }}'
      - name: Description
        value: '{{ Description }}'
      - name: AWSServiceName
        value: '{{ AWSServiceName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iam.service_linked_roles
WHERE data__Identifier = '<RoleName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>service_linked_roles</code> resource, the following permissions are required:

### Create
```json
iam:CreateServiceLinkedRole,
iam:GetRole
```

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

