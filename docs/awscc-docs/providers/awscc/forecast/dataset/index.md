---
title: dataset
hide_title: false
hide_table_of_contents: false
keywords:
  - dataset
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
Gets an individual <code>dataset</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataset</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>dataset</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.forecast.dataset</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>dataset_name</code></td><td><code>string</code></td><td>A name for the dataset</td></tr>
<tr><td><code>dataset_type</code></td><td><code>string</code></td><td>The dataset type</td></tr>
<tr><td><code>data_frequency</code></td><td><code>string</code></td><td>Frequency of data collection. This parameter is required for RELATED_TIME_SERIES</td></tr>
<tr><td><code>domain</code></td><td><code>string</code></td><td>The domain associated with the dataset</td></tr>
<tr><td><code>encryption_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>schema</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>dataset</code> resource, the following permissions are required:

### Read
```json
forecast:DescribeDataset
```

### Delete
```json
forecast:DeleteDataset
```


## Example
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
FROM awscc.forecast.dataset
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
