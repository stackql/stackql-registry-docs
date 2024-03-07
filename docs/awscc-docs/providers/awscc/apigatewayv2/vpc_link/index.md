---
title: vpc_link
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_link
  - apigatewayv2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>vpc_link</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_link</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>vpc_link</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigatewayv2.vpc_link</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>vpc_link_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>subnet_ids</code></td><td><code>array</code></td><td>A list of subnet IDs to include in the VPC link.</td></tr>
<tr><td><code>security_group_ids</code></td><td><code>array</code></td><td>A list of security group IDs for the VPC link.</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>The collection of tags. Each tag element is associated with a given resource.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the VPC link.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>vpc_link</code> resource, the following permissions are required:

### Update
<pre>
apigateway:PATCH,
apigateway:GET,
apigateway:TagResource,
apigateway:unTagResource,
iam:CreateServiceLinkedRole,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus</pre>

### Read
<pre>
apigateway:GET,
iam:CreateServiceLinkedRole,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus</pre>

### Delete
<pre>
apigateway:GET,
apigateway:DELETE,
iam:CreateServiceLinkedRole,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus</pre>


## Example
```sql
SELECT
region,
vpc_link_id,
subnet_ids,
security_group_ids,
tags,
name
FROM awscc.apigatewayv2.vpc_link
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;VpcLinkId&gt;'
```
