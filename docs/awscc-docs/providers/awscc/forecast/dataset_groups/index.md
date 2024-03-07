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
Retrieves a list of <code>dataset_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataset_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>dataset_groups</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.forecast.dataset_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>dataset_group_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the dataset group to delete.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>dataset_groups</code> resource, the following permissions are required:

### Create
<pre>
forecast:CreateDatasetGroup</pre>

### List
<pre>
forecast:ListDatasetGroups</pre>


## Example
```sql
SELECT
region,
dataset_group_arn
FROM awscc.forecast.dataset_groups
WHERE region = 'us-east-1'
```
