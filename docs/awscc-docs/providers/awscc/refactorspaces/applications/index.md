---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
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
Retrieves a list of <code>applications</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>applications</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.refactorspaces.applications</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>environment_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>application_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>applications</code> resource, the following permissions are required:

### Create
<pre>
refactor-spaces:GetApplication,
refactor-spaces:CreateApplication,
refactor-spaces:TagResource,
ec2:CreateTags,
ec2:CreateVpcEndpointServiceConfiguration,
ec2:DescribeVpcs,
ec2:DescribeSubnets,
ec2:DescribeVpcEndpointServiceConfigurations,
ec2:DescribeAccountAttributes,
ec2:DescribeInternetGateways,
ec2:ModifyVpcEndpointServicePermissions,
apigateway:DELETE,
apigateway:GET,
apigateway:PATCH,
apigateway:POST,
apigateway:PUT,
apigateway:UpdateRestApiPolicy,
apigateway:Update*,
apigateway:Delete*,
apigateway:Get*,
apigateway:Put*,
elasticloadbalancing:CreateLoadBalancer,
elasticloadbalancing:DescribeLoadBalancers,
elasticloadbalancing:DescribeTags,
elasticloadbalancing:AddTags,
iam:CreateServiceLinkedRole</pre>

### List
<pre>
refactor-spaces:ListApplications,
refactor-spaces:ListTagsForResource</pre>


## Example
```sql
SELECT
region,
environment_identifier,
application_identifier
FROM awscc.refactorspaces.applications
WHERE region = 'us-east-1'
```
