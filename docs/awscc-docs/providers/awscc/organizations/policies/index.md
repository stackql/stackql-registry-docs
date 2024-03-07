---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
  - organizations
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>policies</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.organizations.policies</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Id of the Policy</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>policies</code> resource, the following permissions are required:

### Create
<pre>
organizations:CreatePolicy,
organizations:DescribePolicy,
organizations:AttachPolicy,
organizations:ListTagsForResource,
organizations:ListTargetsForPolicy,
organizations:TagResource</pre>

### List
<pre>
organizations:ListPolicies</pre>


## Example
```sql
SELECT
region,
id
FROM awscc.organizations.policies
WHERE region = 'us-east-1'
```
