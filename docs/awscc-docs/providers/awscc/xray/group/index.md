---
title: group
hide_title: false
hide_table_of_contents: false
keywords:
  - group
  - xray
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.xray.group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>filter_expression</code></td><td><code>string</code></td><td>The filter expression defining criteria by which to group traces.</td></tr>
<tr><td><code>group_name</code></td><td><code>string</code></td><td>The case-sensitive name of the new group. Names must be unique.</td></tr>
<tr><td><code>group_arn</code></td><td><code>string</code></td><td>The ARN of the group that was generated on creation.</td></tr>
<tr><td><code>insights_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
filter_expression,
group_name,
group_ar_n,
insights_configuration,
tags
FROM awscc.xray.group
WHERE region = 'us-east-1'
AND data__Identifier = '{GroupARN}';
```

## Permissions

To operate on the <code>group</code> resource, the following permissions are required:

### Read
```json
xray:GetGroup,
xray:ListTagsForResource
```

### Update
```json
xray:UpdateGroup,
xray:TagResource,
xray:UntagResource,
xray:ListTagsForResource
```

### Delete
```json
xray:DeleteGroup
```

