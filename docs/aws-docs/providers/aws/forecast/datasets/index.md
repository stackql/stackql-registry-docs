---
title: datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - datasets
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

Creates, updates, deletes or gets a <code>dataset</code> resource or lists <code>datasets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type Definition for AWS::Forecast::Dataset</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.forecast.datasets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="dataset_name" /></td><td><code>string</code></td><td>A name for the dataset</td></tr>
<tr><td><CopyableCode code="dataset_type" /></td><td><code>string</code></td><td>The dataset type</td></tr>
<tr><td><CopyableCode code="data_frequency" /></td><td><code>string</code></td><td>Frequency of data collection. This parameter is required for RELATED_TIME_SERIES</td></tr>
<tr><td><CopyableCode code="domain" /></td><td><code>string</code></td><td>The domain associated with the dataset</td></tr>
<tr><td><CopyableCode code="encryption_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="schema" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="DatasetName, DatasetType, Domain, Schema, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
arn,
dataset_name,
dataset_type,
data_frequency,
domain,
encryption_config,
schema,
tags
FROM aws.forecast.datasets
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>dataset</code>.
```sql
SELECT
region,
arn,
dataset_name,
dataset_type,
data_frequency,
domain,
encryption_config,
schema,
tags
FROM aws.forecast.datasets
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
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
INSERT INTO aws.forecast.datasets (
 DatasetName,
 DatasetType,
 Domain,
 Schema,
 region
)
SELECT 
'{{ DatasetName }}',
 '{{ DatasetType }}',
 '{{ Domain }}',
 '{{ Schema }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.forecast.datasets (
 DatasetName,
 DatasetType,
 DataFrequency,
 Domain,
 EncryptionConfig,
 Schema,
 Tags,
 region
)
SELECT 
 '{{ DatasetName }}',
 '{{ DatasetType }}',
 '{{ DataFrequency }}',
 '{{ Domain }}',
 '{{ EncryptionConfig }}',
 '{{ Schema }}',
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
      - name: DatasetName
        value: '{{ DatasetName }}'
      - name: DatasetType
        value: '{{ DatasetType }}'
      - name: DataFrequency
        value: '{{ DataFrequency }}'
      - name: Domain
        value: '{{ Domain }}'
      - name: EncryptionConfig
        value:
          KmsKeyArn: '{{ KmsKeyArn }}'
          RoleArn: '{{ RoleArn }}'
      - name: Schema
        value:
          Attributes:
            - AttributeName: '{{ AttributeName }}'
              AttributeType: '{{ AttributeType }}'
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
DELETE FROM aws.forecast.datasets
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>datasets</code> resource, the following permissions are required:

### Create
```json
forecast:CreateDataset
```

### Read
```json
forecast:DescribeDataset
```

### Delete
```json
forecast:DeleteDataset
```

### List
```json
forecast:ListDatasets
```

