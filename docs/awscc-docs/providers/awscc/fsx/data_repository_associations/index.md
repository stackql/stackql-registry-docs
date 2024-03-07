---
title: data_repository_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - data_repository_associations
  - fsx
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>data_repository_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_repository_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>data_repository_associations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.fsx.data_repository_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>association_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>data_repository_associations</code> resource, the following permissions are required:

### Create
<pre>
fsx:CreateDataRepositoryAssociation,
fsx:DescribeDataRepositoryAssociations,
fsx:TagResource,
s3:ListBucket,
s3:GetBucketPolicy,
s3:PutBucketPolicy,
iam:CreateServiceLinkedRole,
iam:PutRolePolicy</pre>

### List
<pre>
fsx:DescribeDataRepositoryAssociations</pre>


## Example
```sql
SELECT
region,
association_id
FROM awscc.fsx.data_repository_associations
WHERE region = 'us-east-1'
```
