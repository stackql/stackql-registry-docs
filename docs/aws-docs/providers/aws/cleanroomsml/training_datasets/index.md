---
title: training_datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - training_datasets
  - cleanroomsml
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

Creates, updates, deletes or gets a <code>training_dataset</code> resource or lists <code>training_datasets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>training_datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::CleanRoomsML::TrainingDataset Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cleanroomsml.training_datasets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this cleanrooms-ml training dataset.</td></tr>
<tr><td><CopyableCode code="training_data" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="training_dataset_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="Name, RoleArn, TrainingData, region" /></td>
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
List all <code>training_datasets</code> in a region.
```sql
SELECT
region,
training_dataset_arn
FROM aws.cleanroomsml.training_datasets
WHERE region = 'us-east-1';
```
Gets all properties from a <code>training_dataset</code>.
```sql
SELECT
region,
description,
name,
role_arn,
tags,
training_data,
training_dataset_arn,
status
FROM aws.cleanroomsml.training_datasets
WHERE region = 'us-east-1' AND data__Identifier = '<TrainingDatasetArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>training_dataset</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cleanroomsml.training_datasets (
 Name,
 RoleArn,
 TrainingData,
 region
)
SELECT 
'{{ Name }}',
 '{{ RoleArn }}',
 '{{ TrainingData }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cleanroomsml.training_datasets (
 Description,
 Name,
 RoleArn,
 Tags,
 TrainingData,
 region
)
SELECT 
 '{{ Description }}',
 '{{ Name }}',
 '{{ RoleArn }}',
 '{{ Tags }}',
 '{{ TrainingData }}',
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
  - name: training_dataset
    props:
      - name: Description
        value: '{{ Description }}'
      - name: Name
        value: '{{ Name }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: TrainingData
        value:
          - Type: '{{ Type }}'
            InputConfig:
              Schema:
                - ColumnName: '{{ ColumnName }}'
                  ColumnTypes:
                    - '{{ ColumnTypes[0] }}'
              DataSource:
                GlueDataSource:
                  TableName: '{{ TableName }}'
                  DatabaseName: '{{ DatabaseName }}'
                  CatalogId: '{{ CatalogId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cleanroomsml.training_datasets
WHERE data__Identifier = '<TrainingDatasetArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>training_datasets</code> resource, the following permissions are required:

### Create
```json
cleanrooms-ml:CreateTrainingDataset,
cleanrooms-ml:GetTrainingDataset,
cleanrooms-ml:TagResource,
iam:PassRole
```

### Read
```json
cleanrooms-ml:GetTrainingDataset
```

### Delete
```json
cleanrooms-ml:DeleteTrainingDataset
```

### List
```json
cleanrooms-ml:ListTrainingDatasets
```

### Update
```json
cleanrooms-ml:TagResource,
cleanrooms-ml:UntagResource
```

