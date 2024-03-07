---
title: associations
hide_title: false
hide_table_of_contents: false
keywords:
  - associations
  - ssm
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>associations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ssm.associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>association_id</code></td><td><code>string</code></td><td>Unique identifier of the association.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>associations</code> resource, the following permissions are required:

### Create
```json
ec2:DescribeInstanceStatus,
iam:PassRole,
iam:CreateServiceLinkedRole,
ssm:CreateAssociation,
ssm:DescribeAssociation,
ssm:GetCalendarState
```

### List
```json
ssm:ListAssociations
```


## Example
```sql
SELECT
region,
association_id
FROM awscc.ssm.associations
WHERE region = 'us-east-1'
```
