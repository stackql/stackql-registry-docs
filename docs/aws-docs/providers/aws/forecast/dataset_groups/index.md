---
title: dataset_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - dataset_groups
  - forecast
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

Creates, updates, deletes or gets a <code>dataset_group</code> resource or lists <code>dataset_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataset_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a dataset group that holds a collection of related datasets</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.forecast.dataset_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="dataset_arns" /></td><td><code>array</code></td><td>An array of Amazon Resource Names (ARNs) of the datasets that you want to include in the dataset group.</td></tr>
<tr><td><CopyableCode code="dataset_group_name" /></td><td><code>string</code></td><td>A name for the dataset group.</td></tr>
<tr><td><CopyableCode code="domain" /></td><td><code>string</code></td><td>The domain associated with the dataset group. When you add a dataset to a dataset group, this value and the value specified for the Domain parameter of the CreateDataset operation must match.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags of Application Insights application.</td></tr>
<tr><td><CopyableCode code="dataset_group_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the dataset group to delete.</td></tr>
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
    <td><CopyableCode code="DatasetGroupName, Domain, region" /></td>
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
List all <code>dataset_groups</code> in a region.
```sql
SELECT
region,
dataset_group_arn
FROM aws.forecast.dataset_groups
WHERE region = 'us-east-1';
```
Gets all properties from a <code>dataset_group</code>.
```sql
SELECT
region,
dataset_arns,
dataset_group_name,
domain,
tags,
dataset_group_arn
FROM aws.forecast.dataset_groups
WHERE region = 'us-east-1' AND data__Identifier = '<DatasetGroupArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dataset_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.forecast.dataset_groups (
 DatasetGroupName,
 Domain,
 region
)
SELECT 
'{{ DatasetGroupName }}',
 '{{ Domain }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.forecast.dataset_groups (
 DatasetArns,
 DatasetGroupName,
 Domain,
 Tags,
 region
)
SELECT 
 '{{ DatasetArns }}',
 '{{ DatasetGroupName }}',
 '{{ Domain }}',
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
  - name: dataset_group
    props:
      - name: DatasetArns
        value:
          - '{{ DatasetArns[0] }}'
      - name: DatasetGroupName
        value: '{{ DatasetGroupName }}'
      - name: Domain
        value: '{{ Domain }}'
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
DELETE FROM aws.forecast.dataset_groups
WHERE data__Identifier = '<DatasetGroupArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>dataset_groups</code> resource, the following permissions are required:

### Create
```json
forecast:CreateDatasetGroup
```

### Read
```json
forecast:DescribeDatasetGroup
```

### Update
```json
forecast:UpdateDatasetGroup
```

### Delete
```json
forecast:DeleteDatasetGroup
```

### List
```json
forecast:ListDatasetGroups
```

