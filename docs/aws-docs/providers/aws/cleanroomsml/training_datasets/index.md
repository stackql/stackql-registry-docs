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


Used to retrieve a list of <code>training_datasets</code> in a region or to create or delete a <code>training_datasets</code> resource, use <code>training_dataset</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>training_datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::CleanRoomsML::TrainingDataset Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cleanroomsml.training_datasets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="training_dataset_arn" /></td><td><code>string</code></td><td></td></tr>
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
training_dataset_arn
FROM aws.cleanroomsml.training_datasets
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
-- training_dataset.iql (required properties only)
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
-- training_dataset.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
cleanrooms-ml:DeleteTrainingDataset
```

### List
```json
cleanrooms-ml:ListTrainingDatasets
```

