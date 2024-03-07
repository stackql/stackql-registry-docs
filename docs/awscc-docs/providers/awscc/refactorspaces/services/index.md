---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - refactorspaces
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>services</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>services</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.refactorspaces.services</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>environment_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>application_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>services</code> resource, the following permissions are required:

### Create
<pre>
refactor-spaces:CreateService,
refactor-spaces:GetService,
refactor-spaces:TagResource,
ec2:DescribeVpcs,
ec2:DescribeSubnets,
ec2:DescribeRouteTables,
ec2:CreateTags,
ec2:CreateTransitGatewayVpcAttachment,
ec2:DescribeTransitGatewayVpcAttachments,
ec2:CreateSecurityGroup,
ec2:AuthorizeSecurityGroupIngress,
ec2:CreateRoute,
lambda:GetFunctionConfiguration</pre>

### List
<pre>
refactor-spaces:ListServices,
refactor-spaces:ListTagsForResource</pre>


## Example
```sql
SELECT
region,
environment_identifier,
application_identifier,
service_identifier
FROM awscc.refactorspaces.services
WHERE region = 'us-east-1'
```
