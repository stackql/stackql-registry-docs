---
title: access_points
hide_title: false
hide_table_of_contents: false
keywords:
  - access_points
  - s3objectlambda
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>access_points</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>access_points</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.s3objectlambda.access_points</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name you want to assign to this Object lambda Access Point.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>access_points</code> resource, the following permissions are required:

### Create
<pre>
s3:CreateAccessPointForObjectLambda,
s3:PutAccessPointConfigurationForObjectLambda,
s3:GetAccessPointForObjectLambda,
s3:GetAccessPointPolicyStatusForObjectLambda,
s3:GetAccessPointConfigurationForObjectLambda</pre>

### List
<pre>
s3:ListAccessPointsForObjectLambda</pre>


## Example
```sql
SELECT
region,
name
FROM awscc.s3objectlambda.access_points
WHERE region = 'us-east-1'
```
