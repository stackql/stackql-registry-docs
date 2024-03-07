---
title: graph
hide_title: false
hide_table_of_contents: false
keywords:
  - graph
  - detective
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>graph</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>graph</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>graph</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.detective.graph</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Detective graph ARN</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>auto_enable_members</code></td><td><code>boolean</code></td><td>Indicates whether to automatically enable new organization accounts as member accounts in the organization behavior graph.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
tags,
auto_enable_members
FROM awscc.detective.graph
WHERE region = 'us-east-1'
AND data__Identifier = '{Arn}';
```

## Permissions

To operate on the <code>graph</code> resource, the following permissions are required:

### Update
```json
detective:UntagResource,
detective:TagResource,
detective:ListTagsForResource,
detective:UpdateOrganizationConfiguration,
organizations:DescribeOrganization
```

### Read
```json
detective:ListGraphs,
detective:ListTagsForResource,
detective:DescribeOrganizationConfiguration,
organizations:DescribeOrganization
```

### Delete
```json
detective:DeleteGraph
```

