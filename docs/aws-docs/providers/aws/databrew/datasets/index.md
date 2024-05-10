---
title: datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - datasets
  - databrew
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


Used to retrieve a list of <code>datasets</code> in a region or to create or delete a <code>datasets</code> resource, use <code>dataset</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataBrew::Dataset.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.databrew.datasets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Dataset name</td></tr>
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
name
FROM aws.databrew.datasets
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>dataset</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- dataset.iql (required properties only)
INSERT INTO aws.databrew.datasets (
 Name,
 Input,
 region
)
SELECT 
'{{ Name }}',
 '{{ Input }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- dataset.iql (all properties)
INSERT INTO aws.databrew.datasets (
 Name,
 Format,
 FormatOptions,
 Input,
 PathOptions,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Format }}',
 '{{ FormatOptions }}',
 '{{ Input }}',
 '{{ PathOptions }}',
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
  - name: dataset
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Format
        value: '{{ Format }}'
      - name: FormatOptions
        value:
          Json:
            MultiLine: '{{ MultiLine }}'
          Excel:
            SheetNames:
              - '{{ SheetNames[0] }}'
            SheetIndexes:
              - '{{ SheetIndexes[0] }}'
            HeaderRow: '{{ HeaderRow }}'
          Csv:
            Delimiter: '{{ Delimiter }}'
            HeaderRow: '{{ HeaderRow }}'
      - name: Input
        value:
          S3InputDefinition:
            Bucket: '{{ Bucket }}'
            Key: '{{ Key }}'
          DataCatalogInputDefinition:
            CatalogId: '{{ CatalogId }}'
            DatabaseName: '{{ DatabaseName }}'
            TableName: '{{ TableName }}'
            TempDirectory: null
          DatabaseInputDefinition:
            GlueConnectionName: '{{ GlueConnectionName }}'
            DatabaseTableName: '{{ DatabaseTableName }}'
            TempDirectory: null
            QueryString: '{{ QueryString }}'
          Metadata:
            SourceArn: '{{ SourceArn }}'
      - name: PathOptions
        value:
          FilesLimit:
            MaxFiles: '{{ MaxFiles }}'
            OrderedBy: '{{ OrderedBy }}'
            Order: '{{ Order }}'
          LastModifiedDateCondition:
            Expression: '{{ Expression }}'
            ValuesMap:
              - ValueReference: '{{ ValueReference }}'
                Value: '{{ Value }}'
          Parameters:
            - PathParameterName: '{{ PathParameterName }}'
              DatasetParameter:
                Name: null
                Type: '{{ Type }}'
                DatetimeOptions:
                  Format: '{{ Format }}'
                  TimezoneOffset: '{{ TimezoneOffset }}'
                  LocaleCode: '{{ LocaleCode }}'
                CreateColumn: '{{ CreateColumn }}'
                Filter: null
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.databrew.datasets
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>datasets</code> resource, the following permissions are required:

### Create
```json
databrew:CreateDataset,
databrew:TagResource,
databrew:UntagResource,
glue:GetConnection,
glue:GetTable,
iam:PassRole
```

### Delete
```json
databrew:DeleteDataset
```

### List
```json
databrew:ListDatasets,
databrew:ListTagsForResource,
iam:ListRoles
```

