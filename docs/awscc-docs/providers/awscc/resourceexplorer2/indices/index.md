---
title: indices
hide_title: false
hide_table_of_contents: false
keywords:
  - indices
  - resourceexplorer2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>indices</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>indices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>indices</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.resourceexplorer2.indices</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>indices</code> resource, the following permissions are required:

### Create
<pre>
resource-explorer-2:CreateIndex,
resource-explorer-2:GetIndex,
resource-explorer-2:TagResource,
resource-explorer-2:UpdateIndexType,
resource-explorer-2:DeleteIndex,
iam:CreateServiceLinkedRole</pre>

### List
<pre>
resource-explorer-2:ListIndexes</pre>


## Example
```sql
SELECT
region,
arn
FROM awscc.resourceexplorer2.indices
WHERE region = 'us-east-1'
```