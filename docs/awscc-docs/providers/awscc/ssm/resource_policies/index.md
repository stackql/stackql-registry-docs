---
title: resource_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_policies
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
Retrieves a list of <code>resource_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resource_policies</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ssm.resource_policies</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>policy_id</code></td><td><code>string</code></td><td>An unique identifier within the policies of a resource. </td></tr>
<tr><td><code>resource_arn</code></td><td><code>string</code></td><td>Arn of OpsItemGroup etc.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>resource_policies</code> resource, the following permissions are required:

### Create
<pre>
ssm:PutResourcePolicy</pre>

### List
<pre>
ssm:GetResourcePolicies</pre>


## Example
```sql
SELECT
region,
policy_id,
resource_arn
FROM awscc.ssm.resource_policies
WHERE region = 'us-east-1'
```
