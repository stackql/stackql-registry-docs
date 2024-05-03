---
title: dataset
hide_title: false
hide_table_of_contents: false
keywords:
  - dataset
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

Gets or operates on an individual <code>dataset</code> resource, use <code>datasets</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataset</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Personalize::Dataset.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.personalize.dataset" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name for the dataset</td></tr>
<tr><td><CopyableCode code="dataset_arn" /></td><td><code>string</code></td><td>The ARN of the dataset</td></tr>
<tr><td><CopyableCode code="dataset_type" /></td><td><code>string</code></td><td>The type of dataset</td></tr>
<tr><td><CopyableCode code="dataset_group_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the dataset group to add the dataset to</td></tr>
<tr><td><CopyableCode code="schema_arn" /></td><td><code>string</code></td><td>The ARN of the schema to associate with the dataset. The schema defines the dataset fields.</td></tr>
<tr><td><CopyableCode code="dataset_import_job" /></td><td><code>object</code></td><td></td></tr>
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
name,
dataset_arn,
dataset_type,
dataset_group_arn,
schema_arn,
dataset_import_job
FROM aws.personalize.dataset
WHERE data__Identifier = '<DatasetArn>';
```

## Permissions

To operate on the <code>dataset</code> resource, the following permissions are required:

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

