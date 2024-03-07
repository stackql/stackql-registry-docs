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
Retrieves a list of <code>datasets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>datasets</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.personalize.datasets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>dataset_arn</code></td><td><code>string</code></td><td>The ARN of the dataset</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

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

### List
```json
personalize:ListDatasets
```


## Example
```sql
SELECT
region,
dataset_arn
FROM awscc.personalize.datasets
WHERE region = 'us-east-1'
```
