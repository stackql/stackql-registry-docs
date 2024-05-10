---
title: hook_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - hook_versions
  - cloudformation
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


Used to retrieve a list of <code>hook_versions</code> in a region or to create or delete a <code>hook_versions</code> resource, use <code>hook_version</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hook_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Publishes new or first hook version to AWS CloudFormation Registry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.hook_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the type, here the HookVersion. This is used to uniquely identify a HookVersion resource</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn
FROM aws.cloudformation.hook_versions
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "SchemaHandlerPackage": "{{ SchemaHandlerPackage }}",
 "TypeName": "{{ TypeName }}"
}
>>>
--required properties only
INSERT INTO aws.cloudformation.hook_versions (
 SchemaHandlerPackage,
 TypeName,
 region
)
SELECT 
{{ SchemaHandlerPackage }},
 {{ TypeName }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ExecutionRoleArn": "{{ ExecutionRoleArn }}",
 "LoggingConfig": {
  "LogGroupName": "{{ LogGroupName }}",
  "LogRoleArn": "{{ LogRoleArn }}"
 },
 "SchemaHandlerPackage": "{{ SchemaHandlerPackage }}",
 "TypeName": "{{ TypeName }}"
}
>>>
--all properties
INSERT INTO aws.cloudformation.hook_versions (
 ExecutionRoleArn,
 LoggingConfig,
 SchemaHandlerPackage,
 TypeName,
 region
)
SELECT 
 {{ ExecutionRoleArn }},
 {{ LoggingConfig }},
 {{ SchemaHandlerPackage }},
 {{ TypeName }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.cloudformation.hook_versions
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>hook_versions</code> resource, the following permissions are required:

### Create
```json
cloudformation:DescribeType,
cloudformation:DescribeTypeRegistration,
cloudformation:RegisterType,
iam:PassRole,
s3:GetObject,
s3:ListBucket,
kms:Decrypt
```

### Delete
```json
cloudformation:DeregisterType,
cloudformation:DescribeType
```

### List
```json
cloudformation:ListTypes,
cloudformation:ListTypeVersions
```

