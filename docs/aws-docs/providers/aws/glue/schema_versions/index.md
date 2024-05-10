---
title: schema_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - schema_versions
  - glue
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


Used to retrieve a list of <code>schema_versions</code> in a region or to create or delete a <code>schema_versions</code> resource, use <code>schema_version</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schema_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This resource represents an individual schema version of a schema defined in Glue Schema Registry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.glue.schema_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="version_id" /></td><td><code>string</code></td><td>Represents the version ID associated with the schema version.</td></tr>
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
version_id
FROM aws.glue.schema_versions
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
 "Schema": {
  "SchemaArn": "{{ SchemaArn }}",
  "SchemaName": "{{ SchemaName }}",
  "RegistryName": "{{ RegistryName }}"
 },
 "SchemaDefinition": "{{ SchemaDefinition }}"
}
>>>
--required properties only
INSERT INTO aws.glue.schema_versions (
 Schema,
 SchemaDefinition,
 region
)
SELECT 
{{ .Schema }},
 {{ .SchemaDefinition }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Schema": {
  "SchemaArn": "{{ SchemaArn }}",
  "SchemaName": "{{ SchemaName }}",
  "RegistryName": "{{ RegistryName }}"
 },
 "SchemaDefinition": "{{ SchemaDefinition }}"
}
>>>
--all properties
INSERT INTO aws.glue.schema_versions (
 Schema,
 SchemaDefinition,
 region
)
SELECT 
 {{ .Schema }},
 {{ .SchemaDefinition }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.glue.schema_versions
WHERE data__Identifier = '<VersionId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>schema_versions</code> resource, the following permissions are required:

### Create
```json
glue:RegisterSchemaVersion,
glue:GetSchemaVersion,
glue:GetSchemaByDefinition
```

### Delete
```json
glue:DeleteSchemaVersions,
glue:GetSchemaVersion
```

### List
```json
glue:ListSchemaVersions
```

