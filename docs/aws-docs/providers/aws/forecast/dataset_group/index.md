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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>dataset_group</code> resource, use <code>dataset_groups</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataset_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a dataset group that holds a collection of related datasets</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.forecast.dataset_group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="dataset_arns" /></td><td><code>array</code></td><td>An array of Amazon Resource Names (ARNs) of the datasets that you want to include in the dataset group.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
dataset_arns,
dataset_group_name,
domain,
tags,
dataset_group_arn
FROM aws.forecast.dataset_group
WHERE data__Identifier = '<DatasetGroupArn>';
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

