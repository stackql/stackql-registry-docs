---
title: parameters
hide_title: false
hide_table_of_contents: false
keywords:
  - parameters
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
Retrieves a list of <code>parameters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>parameters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>parameters</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ssm.parameters</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the parameter.&lt;br&#x2F;&gt; The maximum length constraint listed below includes capacity for additional system attributes that aren't part of the name. The maximum length for a parameter name, including the full length of the parameter ARN, is 1011 characters. For example, the length of the following parameter name is 65 characters, not 20 characters: ``arn:aws:ssm:us-east-2:111222333444:parameter&#x2F;ExampleParameterName``</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>parameters</code> resource, the following permissions are required:

### Create
<pre>
ssm:PutParameter,
ssm:AddTagsToResource,
ssm:GetParameters</pre>

### List
<pre>
ssm:DescribeParameters</pre>


## Example
```sql
SELECT
region,
name
FROM awscc.ssm.parameters
WHERE region = 'us-east-1'
```
