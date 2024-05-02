---
title: application
hide_title: false
hide_table_of_contents: false
keywords:
  - application
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
Gets or operates on an individual <code>application</code> resource, use <code>applications</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RefactorSpaces::Application Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.refactorspaces.application</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>api_gateway_proxy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>api_gateway_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>vpc_link_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>nlb_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>nlb_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>application_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>environment_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>proxy_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stage_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>proxy_url</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.</td></tr>
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
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
api_gateway_proxy,
arn,
api_gateway_id,
vpc_link_id,
nlb_arn,
nlb_name,
application_identifier,
environment_identifier,
name,
proxy_type,
vpc_id,
stage_name,
proxy_url,
tags
FROM aws.refactorspaces.application
WHERE data__Identifier = '<EnvironmentIdentifier>|<ApplicationIdentifier>';
```

## Permissions

To operate on the <code>application</code> resource, the following permissions are required:

### Read
```json
refactor-spaces:GetApplication,
refactor-spaces:ListTagsForResource
```

### Delete
```json
refactor-spaces:GetApplication,
refactor-spaces:DeleteApplication,
refactor-spaces:UntagResource,
ec2:DescribeVpcEndpointServiceConfigurations,
ec2:DeleteRoute,
ec2:DeleteSecurityGroup,
ec2:DeleteTransitGateway,
ec2:DeleteTransitGatewayVpcAttachment,
ec2:DeleteVpcEndpointServiceConfigurations,
ec2:DeleteTags,
ec2:RevokeSecurityGroupIngress,
elasticloadbalancing:DeleteLoadBalancer,
apigateway:Update*,
apigateway:Delete*,
apigateway:Get*,
apigateway:Put*
```

