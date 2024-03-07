---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - m2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>applications</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>applications</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.m2.applications</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>application_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
application_arn
FROM awscc.m2.applications
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>applications</code> resource, the following permissions are required:

### Create
```json
m2:CreateApplication,
m2:GetApplication,
m2:ListTagsForResource,
m2:TagResource,
s3:GetObject,
s3:ListBucket,
kms:DescribeKey,
kms:CreateGrant,
iam:PassRole
```

### List
```json
m2:ListApplications
```

