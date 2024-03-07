---
title: member_invitations
hide_title: false
hide_table_of_contents: false
keywords:
  - member_invitations
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
Retrieves a list of <code>member_invitations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>member_invitations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>member_invitations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.detective.member_invitations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>graph_arn</code></td><td><code>string</code></td><td>The ARN of the graph to which the member account will be invited</td></tr>
<tr><td><code>member_id</code></td><td><code>string</code></td><td>The AWS account ID to be invited to join the graph as a member</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
graph_arn,
member_id
FROM awscc.detective.member_invitations
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>member_invitations</code> resource, the following permissions are required:

### Create
```json
detective:CreateMembers,
detective:GetMembers
```

### List
```json
detective:ListGraphs,
detective:ListMembers
```

