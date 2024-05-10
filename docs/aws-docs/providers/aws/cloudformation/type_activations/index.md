---
title: type_activations
hide_title: false
hide_table_of_contents: false
keywords:
  - type_activations
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


Used to retrieve a list of <code>type_activations</code> in a region or to create or delete a <code>type_activations</code> resource, use <code>type_activation</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>type_activations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Enable a resource that has been published in the CloudFormation Registry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.type_activations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the extension.</td></tr>
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
FROM aws.cloudformation.type_activations
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
 "ExecutionRoleArn": "{{ ExecutionRoleArn }}",
 "PublisherId": "{{ PublisherId }}",
 "LoggingConfig": {
  "LogGroupName": "{{ LogGroupName }}",
  "LogRoleArn": "{{ LogRoleArn }}"
 },
 "PublicTypeArn": "{{ PublicTypeArn }}",
 "AutoUpdate": "{{ AutoUpdate }}",
 "TypeNameAlias": "{{ TypeNameAlias }}",
 "VersionBump": "{{ VersionBump }}",
 "MajorVersion": "{{ MajorVersion }}",
 "TypeName": "{{ TypeName }}",
 "Type": "{{ Type }}"
}
>>>
--required properties only
INSERT INTO aws.cloudformation.type_activations (
 ExecutionRoleArn,
 PublisherId,
 LoggingConfig,
 PublicTypeArn,
 AutoUpdate,
 TypeNameAlias,
 VersionBump,
 MajorVersion,
 TypeName,
 Type,
 region
)
SELECT 
{{ .ExecutionRoleArn }},
 {{ .PublisherId }},
 {{ .LoggingConfig }},
 {{ .PublicTypeArn }},
 {{ .AutoUpdate }},
 {{ .TypeNameAlias }},
 {{ .VersionBump }},
 {{ .MajorVersion }},
 {{ .TypeName }},
 {{ .Type }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ExecutionRoleArn": "{{ ExecutionRoleArn }}",
 "PublisherId": "{{ PublisherId }}",
 "LoggingConfig": {
  "LogGroupName": "{{ LogGroupName }}",
  "LogRoleArn": "{{ LogRoleArn }}"
 },
 "PublicTypeArn": "{{ PublicTypeArn }}",
 "AutoUpdate": "{{ AutoUpdate }}",
 "TypeNameAlias": "{{ TypeNameAlias }}",
 "VersionBump": "{{ VersionBump }}",
 "MajorVersion": "{{ MajorVersion }}",
 "TypeName": "{{ TypeName }}",
 "Type": "{{ Type }}"
}
>>>
--all properties
INSERT INTO aws.cloudformation.type_activations (
 ExecutionRoleArn,
 PublisherId,
 LoggingConfig,
 PublicTypeArn,
 AutoUpdate,
 TypeNameAlias,
 VersionBump,
 MajorVersion,
 TypeName,
 Type,
 region
)
SELECT 
 {{ .ExecutionRoleArn }},
 {{ .PublisherId }},
 {{ .LoggingConfig }},
 {{ .PublicTypeArn }},
 {{ .AutoUpdate }},
 {{ .TypeNameAlias }},
 {{ .VersionBump }},
 {{ .MajorVersion }},
 {{ .TypeName }},
 {{ .Type }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.cloudformation.type_activations
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>type_activations</code> resource, the following permissions are required:

### Create
```json
cloudformation:ActivateType,
cloudformation:DescribeType,
iam:PassRole
```

### Delete
```json
cloudformation:DeactivateType,
cloudformation:DescribeType
```

### List
```json
cloudformation:ListTypes
```

