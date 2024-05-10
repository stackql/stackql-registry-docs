---
title: schemata
hide_title: false
hide_table_of_contents: false
keywords:
  - schemata
  - eventschemas
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


Used to retrieve a list of <code>schemata</code> in a region or to create or delete a <code>schemata</code> resource, use <code>schema</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schemata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EventSchemas::Schema</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eventschemas.schemata" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="schema_arn" /></td><td><code>string</code></td><td>The ARN of the schema.</td></tr>
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
schema_arn
FROM aws.eventschemas.schemata
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
 "Type": "{{ Type }}",
 "Content": "{{ Content }}",
 "RegistryName": "{{ RegistryName }}"
}
>>>
--required properties only
INSERT INTO aws.eventschemas.schemata (
 Type,
 Content,
 RegistryName,
 region
)
SELECT 
{{ .Type }},
 {{ .Content }},
 {{ .RegistryName }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Type": "{{ Type }}",
 "Description": "{{ Description }}",
 "Content": "{{ Content }}",
 "RegistryName": "{{ RegistryName }}",
 "SchemaName": "{{ SchemaName }}",
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.eventschemas.schemata (
 Type,
 Description,
 Content,
 RegistryName,
 SchemaName,
 Tags,
 region
)
SELECT 
 {{ .Type }},
 {{ .Description }},
 {{ .Content }},
 {{ .RegistryName }},
 {{ .SchemaName }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.eventschemas.schemata
WHERE data__Identifier = '<SchemaArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>schemata</code> resource, the following permissions are required:

### Create
```json
schemas:DescribeSchema,
schemas:CreateSchema,
schemas:TagResource
```

### Delete
```json
schemas:DescribeSchema,
schemas:DeleteSchema,
schemas:DeleteSchemaVersion
```

### List
```json
schemas:ListSchemas,
schemas:ListSchemaVersions
```

