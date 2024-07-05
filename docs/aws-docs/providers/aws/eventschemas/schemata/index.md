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

Creates, updates, deletes or gets a <code>schema</code> resource or lists <code>schemata</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schemata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EventSchemas::Schema</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eventschemas.schemata" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of schema. Valid types include OpenApi3 and JSONSchemaDraft4.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the schema.</td></tr>
<tr><td><CopyableCode code="schema_version" /></td><td><code>string</code></td><td>The version number of the schema.</td></tr>
<tr><td><CopyableCode code="content" /></td><td><code>string</code></td><td>The source of the schema definition.</td></tr>
<tr><td><CopyableCode code="registry_name" /></td><td><code>string</code></td><td>The name of the schema registry.</td></tr>
<tr><td><CopyableCode code="schema_arn" /></td><td><code>string</code></td><td>The ARN of the schema.</td></tr>
<tr><td><CopyableCode code="schema_name" /></td><td><code>string</code></td><td>The name of the schema.</td></tr>
<tr><td><CopyableCode code="last_modified" /></td><td><code>string</code></td><td>The last modified time of the schema.</td></tr>
<tr><td><CopyableCode code="version_created_date" /></td><td><code>string</code></td><td>The date the schema version was created.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags associated with the resource.</td></tr>
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
    <td><CopyableCode code="Type, Content, RegistryName, region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>schemata</code> in a region.
```sql
SELECT
region,
type,
description,
schema_version,
content,
registry_name,
schema_arn,
schema_name,
last_modified,
version_created_date,
tags
FROM aws.eventschemas.schemata
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>schema</code>.
```sql
SELECT
region,
type,
description,
schema_version,
content,
registry_name,
schema_arn,
schema_name,
last_modified,
version_created_date,
tags
FROM aws.eventschemas.schemata
WHERE region = 'us-east-1' AND data__Identifier = '<SchemaArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>schema</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.eventschemas.schemata (
 Type,
 Content,
 RegistryName,
 region
)
SELECT 
'{{ Type }}',
 '{{ Content }}',
 '{{ RegistryName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ Type }}',
 '{{ Description }}',
 '{{ Content }}',
 '{{ RegistryName }}',
 '{{ SchemaName }}',
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
  - name: schema
    props:
      - name: Type
        value: '{{ Type }}'
      - name: Description
        value: '{{ Description }}'
      - name: Content
        value: '{{ Content }}'
      - name: RegistryName
        value: '{{ RegistryName }}'
      - name: SchemaName
        value: '{{ SchemaName }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
schemas:DescribeSchema
```

### Update
```json
schemas:DescribeSchema,
schemas:UpdateSchema,
schemas:TagResource,
schemas:UntagResource,
schemas:ListTagsForResource
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

