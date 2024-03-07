---
title: data_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - data_providers
  - dms
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>data_providers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>data_providers</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.dms.data_providers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>data_provider_arn</code></td><td><code>string</code></td><td>The data provider ARN.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>data_providers</code> resource, the following permissions are required:

### Create
```json
dms:CreateDataProvider,
dms:ListDataProviders,
dms:DescribeDataProviders,
dms:AddTagsToResource,
dms:ListTagsForResource
```

### List
```json
dms:ListDataProviders,
dms:DescribeDataProviders,
dms:ListTagsForResource
```


## Example
```sql
SELECT
region,
data_provider_arn
FROM awscc.dms.data_providers
WHERE region = 'us-east-1'
```
