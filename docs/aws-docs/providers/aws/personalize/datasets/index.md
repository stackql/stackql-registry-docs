---
title: datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - datasets
  - personalize
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
<tr><td><b>Description</b></td><td>Resource schema for AWS::Personalize::Dataset.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.personalize.datasets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name for the dataset</td></tr>
<tr><td><CopyableCode code="dataset_arn" /></td><td><code>string</code></td><td>The ARN of the dataset</td></tr>
<tr><td><CopyableCode code="dataset_type" /></td><td><code>string</code></td><td>The type of dataset</td></tr>
<tr><td><CopyableCode code="dataset_group_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the dataset group to add the dataset to</td></tr>
<tr><td><CopyableCode code="schema_arn" /></td><td><code>string</code></td><td>The ARN of the schema to associate with the dataset. The schema defines the dataset fields.</td></tr>
<tr><td><CopyableCode code="dataset_import_job" /></td><td><code>object</code></td><td>Initial DatasetImportJob for the created dataset</td></tr>
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
    <td><CopyableCode code="Name, DatasetType, DatasetGroupArn, SchemaArn, region" /></td>
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
dataset_arn,
dataset_type,
dataset_group_arn,
schema_arn,
dataset_import_job
FROM aws.personalize.datasets
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>dataset</code>.
```sql
SELECT
region,
name,
dataset_arn,
dataset_type,
dataset_group_arn,
schema_arn,
dataset_import_job
FROM aws.personalize.datasets
WHERE region = 'us-east-1' AND data__Identifier = '<DatasetArn>';
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
INSERT INTO aws.personalize.datasets (
 Name,
 DatasetType,
 DatasetGroupArn,
 SchemaArn,
 region
)
SELECT 
'{{ Name }}',
 '{{ DatasetType }}',
 '{{ DatasetGroupArn }}',
 '{{ SchemaArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.personalize.datasets (
 Name,
 DatasetType,
 DatasetGroupArn,
 SchemaArn,
 DatasetImportJob,
 region
)
SELECT 
 '{{ Name }}',
 '{{ DatasetType }}',
 '{{ DatasetGroupArn }}',
 '{{ SchemaArn }}',
 '{{ DatasetImportJob }}',
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
      - name: DatasetType
        value: '{{ DatasetType }}'
      - name: DatasetGroupArn
        value: '{{ DatasetGroupArn }}'
      - name: SchemaArn
        value: '{{ SchemaArn }}'
      - name: DatasetImportJob
        value:
          JobName: '{{ JobName }}'
          DatasetImportJobArn: '{{ DatasetImportJobArn }}'
          DatasetArn: '{{ DatasetArn }}'
          DataSource:
            DataLocation: '{{ DataLocation }}'
          RoleArn: '{{ RoleArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.personalize.datasets
WHERE data__Identifier = '<DatasetArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>datasets</code> resource, the following permissions are required:

### Create
```json
personalize:CreateDataset,
personalize:DescribeDataset,
personalize:CreateDatasetImportJob,
personalize:DescribeDatasetImportJob,
iam:PassRole
```

### Read
```json
personalize:DescribeDataset
```

### Update
```json
personalize:DescribeDataset,
personalize:CreateDatasetImportJob,
personalize:DescribeDatasetImportJob,
iam:PassRole
```

### Delete
```json
personalize:DeleteDataset,
personalize:DescribeDataset
```

### List
```json
personalize:ListDatasets
```

