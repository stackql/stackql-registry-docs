---
title: dataset_group
hide_title: false
hide_table_of_contents: false
keywords:
  - dataset_group
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
Gets an individual <code>dataset_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataset_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>dataset_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.forecast.dataset_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>dataset_arns</code></td><td><code>array</code></td><td>An array of Amazon Resource Names (ARNs) of the datasets that you want to include in the dataset group.</td></tr>
<tr><td><code>dataset_group_name</code></td><td><code>string</code></td><td>A name for the dataset group.</td></tr>
<tr><td><code>domain</code></td><td><code>string</code></td><td>The domain associated with the dataset group. When you add a dataset to a dataset group, this value and the value specified for the Domain parameter of the CreateDataset operation must match.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags of Application Insights application.</td></tr>
<tr><td><code>dataset_group_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the dataset group to delete.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
dataset_arns,
dataset_group_name,
domain,
tags,
dataset_group_arn
FROM awscc.forecast.dataset_group
WHERE region = 'us-east-1'
AND data__Identifier = '{DatasetGroupArn}';
```

## Permissions

To operate on the <code>dataset_group</code> resource, the following permissions are required:

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

