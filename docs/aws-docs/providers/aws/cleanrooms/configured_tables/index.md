---
title: configured_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - configured_tables
  - cleanrooms
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


Used to retrieve a list of <code>configured_tables</code> in a region or to create or delete a <code>configured_tables</code> resource, use <code>configured_table</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configured_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a table that can be associated with collaborations</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cleanrooms.configured_tables" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="configured_table_identifier" /></td><td><code>string</code></td><td></td></tr>
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
configured_table_identifier
FROM aws.cleanrooms.configured_tables
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>configured_table</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- configured_table.iql (required properties only)
INSERT INTO aws.cleanrooms.configured_tables (
 AllowedColumns,
 AnalysisMethod,
 Name,
 TableReference,
 region
)
SELECT 
'{{ AllowedColumns }}',
 '{{ AnalysisMethod }}',
 '{{ Name }}',
 '{{ TableReference }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- configured_table.iql (all properties)
INSERT INTO aws.cleanrooms.configured_tables (
 Tags,
 AllowedColumns,
 AnalysisMethod,
 Description,
 Name,
 AnalysisRules,
 TableReference,
 region
)
SELECT 
 '{{ Tags }}',
 '{{ AllowedColumns }}',
 '{{ AnalysisMethod }}',
 '{{ Description }}',
 '{{ Name }}',
 '{{ AnalysisRules }}',
 '{{ TableReference }}',
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
  - name: configured_table
    props:
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: AllowedColumns
        value:
          - '{{ AllowedColumns[0] }}'
      - name: AnalysisMethod
        value: '{{ AnalysisMethod }}'
      - name: Description
        value: '{{ Description }}'
      - name: Name
        value: '{{ Name }}'
      - name: AnalysisRules
        value:
          - Type: '{{ Type }}'
            Policy:
              V1: null
      - name: TableReference
        value:
          Glue:
            TableName: '{{ TableName }}'
            DatabaseName: '{{ DatabaseName }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.cleanrooms.configured_tables
WHERE data__Identifier = '<ConfiguredTableIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>configured_tables</code> resource, the following permissions are required:

### Create
```json
cleanrooms:CreateConfiguredTable,
cleanrooms:DeleteConfiguredTable,
cleanrooms:DeleteConfiguredTableAnalysisRule,
cleanrooms:CreateConfiguredTableAnalysisRule,
cleanrooms:GetConfiguredTable,
cleanrooms:GetConfiguredTableAnalysisRule,
glue:GetDatabase,
glue:GetDatabases,
glue:GetTable,
glue:GetTables,
glue:GetPartition,
glue:GetPartitions,
glue:BatchGetPartition,
glue:GetSchemaVersion,
cleanrooms:ListTagsForResource,
cleanrooms:TagResource,
cleanrooms:ListConfiguredTables
```

### Delete
```json
cleanrooms:DeleteConfiguredTable,
cleanrooms:GetConfiguredTable,
cleanrooms:ListConfiguredTables,
cleanrooms:GetConfiguredTableAnalysisRule,
cleanrooms:DeleteConfiguredTableAnalysisRule,
cleanrooms:ListTagsForResource,
cleanrooms:UntagResource,
glue:GetDatabase,
glue:GetDatabases,
glue:GetTable,
glue:GetTables,
glue:GetPartition,
glue:GetPartitions,
glue:BatchGetPartition,
glue:GetSchemaVersion
```

### List
```json
cleanrooms:ListConfiguredTables
```

