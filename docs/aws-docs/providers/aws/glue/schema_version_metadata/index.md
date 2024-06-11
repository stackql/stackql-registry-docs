---
title: schema_version_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - schema_version_metadata
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

Creates, updates, deletes or gets a <code>schema_version_metadatum</code> resource or lists <code>schema_version_metadata</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schema_version_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This resource adds Key-Value metadata to a Schema version of Glue Schema Registry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.glue.schema_version_metadata" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="schema_version_id" /></td><td><code>string</code></td><td>Represents the version ID associated with the schema version.</td></tr>
<tr><td><CopyableCode code="key" /></td><td><code>string</code></td><td>Metadata key</td></tr>
<tr><td><CopyableCode code="value" /></td><td><code>string</code></td><td>Metadata value</td></tr>
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
    <td><CopyableCode code="SchemaVersionId, Key, Value, region" /></td>
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
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>schema_version_metadata</code> in a region.
```sql
SELECT
region,
schema_version_id,
key,
value
FROM aws.glue.schema_version_metadata
WHERE region = 'us-east-1';
```
Gets all properties from a <code>schema_version_metadatum</code>.
```sql
SELECT
region,
schema_version_id,
key,
value
FROM aws.glue.schema_version_metadata
WHERE region = 'us-east-1' AND data__Identifier = '<SchemaVersionId>|<Key>|<Value>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>schema_version_metadatum</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.glue.schema_version_metadata (
 SchemaVersionId,
 Key,
 Value,
 region
)
SELECT 
'{{ SchemaVersionId }}',
 '{{ Key }}',
 '{{ Value }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.glue.schema_version_metadata (
 SchemaVersionId,
 Key,
 Value,
 region
)
SELECT 
 '{{ SchemaVersionId }}',
 '{{ Key }}',
 '{{ Value }}',
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
  - name: schema_version_metadatum
    props:
      - name: SchemaVersionId
        value: '{{ SchemaVersionId }}'
      - name: Key
        value: '{{ Key }}'
      - name: Value
        value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.glue.schema_version_metadata
WHERE data__Identifier = '<SchemaVersionId|Key|Value>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>schema_version_metadata</code> resource, the following permissions are required:

### Create
```json
glue:putSchemaVersionMetadata
```

### Read
```json
glue:querySchemaVersionMetadata
```

### Delete
```json
glue:removeSchemaVersionMetadata
```

### List
```json
glue:querySchemaVersionMetadata
```

