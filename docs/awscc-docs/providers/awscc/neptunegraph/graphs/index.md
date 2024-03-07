---
title: graphs
hide_title: false
hide_table_of_contents: false
keywords:
  - graphs
  - neptunegraph
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>graphs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>graphs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>graphs</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.neptunegraph.graphs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>graph_id</code></td><td><code>string</code></td><td>The auto-generated id assigned by the service.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
graph_id
FROM awscc.neptunegraph.graphs
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>graphs</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
neptune-graph:CreateGraph,
neptune-graph:GetGraph,
neptune-graph:ListTagsForResource,
neptune-graph:TagResource,
kms:DescribeKey,
kms:CreateGrant,
kms:Decrypt,
iam:CreateServiceLinkedRole
```

### List
```json
neptune-graph:GetGraph,
neptune-graph:ListGraphs,
kms:DescribeKey,
kms:CreateGrant,
kms:Decrypt
```

