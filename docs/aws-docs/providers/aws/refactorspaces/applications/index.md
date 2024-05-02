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
Used to retrieve a list of <code>applications</code> in a region or create a <code>applications</code> resource, use <code>application</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RefactorSpaces::Application Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.refactorspaces.applications</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>environment_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>application_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
environment_identifier,
application_identifier
FROM aws.refactorspaces.applications
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>applications</code> resource, the following permissions are required:

### Create
```json
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
iam:CreateServiceLinkedRole
```

### List
```json
refactor-spaces:ListApplications,
refactor-spaces:ListTagsForResource
```

