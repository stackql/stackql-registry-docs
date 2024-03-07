---
title: access_grants_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - access_grants_instances
  - s3
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>access_grants_instances</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_grants_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>access_grants_instances</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.s3.access_grants_instances</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>access_grants_instance_arn</code></td><td><code>undefined</code></td><td>The Amazon Resource Name (ARN) of the specified Access Grants instance.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>access_grants_instances</code> resource, the following permissions are required:

### Create
<pre>
s3:CreateAccessGrantsInstance,
s3:TagResource</pre>

### List
<pre>
s3:ListAccessGrantsInstances</pre>


## Example
```sql
SELECT
region,
access_grants_instance_arn
FROM awscc.s3.access_grants_instances
WHERE region = 'us-east-1'
```
