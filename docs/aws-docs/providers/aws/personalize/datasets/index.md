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


Used to retrieve a list of <code>datasets</code> in a region or to create or delete a <code>datasets</code> resource, use <code>dataset</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Personalize::Dataset.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.personalize.datasets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="dataset_arn" /></td><td><code>string</code></td><td>The ARN of the dataset</td></tr>
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
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
dataset_arn
FROM aws.personalize.datasets
WHERE region = 'us-east-1';
```

## `INSERT` Example

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

## `DELETE` Example

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

### Delete
```json
personalize:DeleteDataset,
personalize:DescribeDataset
```

### List
```json
personalize:ListDatasets
```

