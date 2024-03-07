---
title: memberships
hide_title: false
hide_table_of_contents: false
keywords:
  - memberships
  - cleanrooms
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>memberships</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>memberships</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>memberships</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cleanrooms.memberships</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>membership_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>memberships</code> resource, the following permissions are required:

### Create
<pre>
cleanrooms:CreateMembership,
logs:CreateLogDelivery,
logs:GetLogDelivery,
logs:UpdateLogDelivery,
logs:DeleteLogDelivery,
logs:ListLogDeliveries,
logs:DescribeLogGroups,
logs:DescribeResourcePolicies,
logs:PutResourcePolicy,
logs:CreateLogGroup,
cleanrooms:GetMembership,
cleanrooms:ListTagsForResource,
cleanrooms:TagResource,
cleanrooms:ListMemberships,
iam:PassRole</pre>

### List
<pre>
cleanrooms:ListMemberships</pre>


## Example
```sql
SELECT
region,
membership_identifier
FROM awscc.cleanrooms.memberships
WHERE region = 'us-east-1'
```
