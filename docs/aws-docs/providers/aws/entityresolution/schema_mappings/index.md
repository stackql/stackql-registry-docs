---
title: schema_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - schema_mappings
  - entityresolution
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

Creates, updates, deletes or gets a <code>schema_mapping</code> resource or lists <code>schema_mappings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schema_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>SchemaMapping defined in AWS Entity Resolution service</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.entityresolution.schema_mappings" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="schema_name" /></td><td><code>string</code></td><td>The name of the SchemaMapping</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the SchemaMapping</td></tr>
<tr><td><CopyableCode code="mapped_input_fields" /></td><td><code>array</code></td><td>The SchemaMapping attributes input</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="schema_arn" /></td><td><code>string</code></td><td>The SchemaMapping arn associated with the Schema</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The time of this SchemaMapping got created</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>The time of this SchemaMapping got last updated at</td></tr>
<tr><td><CopyableCode code="has_workflows" /></td><td><code>boolean</code></td><td>The boolean value that indicates whether or not a SchemaMapping has MatchingWorkflows that are associated with</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-schemamapping.html"><code>AWS::EntityResolution::SchemaMapping</code></a>.

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
    <td><CopyableCode code="SchemaName, MappedInputFields, region" /></td>
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
Gets all <code>schema_mappings</code> in a region.
```sql
SELECT
region,
schema_name,
description,
mapped_input_fields,
tags,
schema_arn,
created_at,
updated_at,
has_workflows
FROM aws.entityresolution.schema_mappings
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>schema_mapping</code>.
```sql
SELECT
region,
schema_name,
description,
mapped_input_fields,
tags,
schema_arn,
created_at,
updated_at,
has_workflows
FROM aws.entityresolution.schema_mappings
WHERE region = 'us-east-1' AND data__Identifier = '<SchemaName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>schema_mapping</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.entityresolution.schema_mappings (
 SchemaName,
 MappedInputFields,
 region
)
SELECT 
'{{ SchemaName }}',
 '{{ MappedInputFields }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.entityresolution.schema_mappings (
 SchemaName,
 Description,
 MappedInputFields,
 Tags,
 region
)
SELECT 
 '{{ SchemaName }}',
 '{{ Description }}',
 '{{ MappedInputFields }}',
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
  - name: schema_mapping
    props:
      - name: SchemaName
        value: '{{ SchemaName }}'
      - name: Description
        value: '{{ Description }}'
      - name: MappedInputFields
        value:
          - FieldName: '{{ FieldName }}'
            Type: '{{ Type }}'
            SubType: '{{ SubType }}'
            GroupName: null
            MatchKey: null
            Hashed: '{{ Hashed }}'
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
DELETE FROM aws.entityresolution.schema_mappings
WHERE data__Identifier = '<SchemaName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>schema_mappings</code> resource, the following permissions are required:

### Create
```json
entityresolution:CreateSchemaMapping,
entityresolution:GetSchemaMapping,
entityresolution:TagResource
```

### Read
```json
entityresolution:GetSchemaMapping,
entityresolution:ListTagsForResource
```

### Delete
```json
entityresolution:DeleteSchemaMapping,
entityresolution:GetSchemaMapping
```

### Update
```json
entityresolution:GetSchemaMapping,
entityresolution:UpdateSchemaMapping,
entityresolution:ListTagsForResource,
entityresolution:TagResource,
entityresolution:UntagResource
```

### List
```json
entityresolution:ListSchemaMappings
```
