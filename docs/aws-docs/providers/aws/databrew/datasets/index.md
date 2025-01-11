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

Creates, updates, deletes or gets a <code>dataset</code> resource or lists <code>datasets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataBrew::Dataset.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.databrew.datasets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Dataset name</td></tr>
<tr><td><CopyableCode code="format" /></td><td><code>string</code></td><td>Dataset format</td></tr>
<tr><td><CopyableCode code="format_options" /></td><td><code>object</code></td><td>Format options for dataset</td></tr>
<tr><td><CopyableCode code="input" /></td><td><code>object</code></td><td>Input</td></tr>
<tr><td><CopyableCode code="source" /></td><td><code>string</code></td><td>Source type of the dataset</td></tr>
<tr><td><CopyableCode code="path_options" /></td><td><code>object</code></td><td>PathOptions</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html"><code>AWS::DataBrew::Dataset</code></a>.

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
    <td><CopyableCode code="Name, Input, region" /></td>
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
Gets all <code>datasets</code> in a region.
```sql
SELECT
region,
name,
format,
format_options,
input,
source,
path_options,
tags
FROM aws.databrew.datasets
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>dataset</code>.
```sql
SELECT
region,
name,
format,
format_options,
input,
source,
path_options,
tags
FROM aws.databrew.datasets
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dataset</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
INSERT INTO aws.databrew.datasets (
 Name,
 Format,
 FormatOptions,
 Input,
 Source,
 PathOptions,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Format }}',
 '{{ FormatOptions }}',
 '{{ Input }}',
 '{{ Source }}',
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
      - name: Source
        value: '{{ Source }}'
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
databrew:DescribeDataset,
databrew:ListTagsForResource,
iam:ListRoles
```

### Update
```json
databrew:UpdateDataset,
glue:GetConnection,
glue:GetTable
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
