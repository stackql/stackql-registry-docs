---
title: route
hide_title: false
hide_table_of_contents: false
keywords:
  - route
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
Gets an individual <code>route</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>route</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>route</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.refactorspaces.route</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>path_resource_to_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>application_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>environment_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>route_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>route_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>default_route</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>uri_path_route</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
path_resource_to_id,
arn,
application_identifier,
environment_identifier,
route_identifier,
route_type,
service_identifier,
default_route,
uri_path_route,
tags
FROM awscc.refactorspaces.route
WHERE data__Identifier = '<EnvironmentIdentifier>|<ApplicationIdentifier>|<RouteIdentifier>';
```

## Permissions

To operate on the <code>route</code> resource, the following permissions are required:

### Read
```json
refactor-spaces:GetRoute,
refactor-spaces:ListTagsForResource
```

### Delete
```json
refactor-spaces:DeleteRoute,
refactor-spaces:GetRoute,
refactor-spaces:UntagResource,
apigateway:GET,
apigateway:PATCH,
apigateway:POST,
apigateway:PUT,
apigateway:DELETE,
apigateway:UpdateRestApiPolicy,
lambda:GetFunctionConfiguration,
lambda:AddPermission,
elasticloadbalancing:DescribeListeners,
elasticloadbalancing:DescribeTargetGroups,
elasticloadbalancing:CreateListener,
elasticloadbalancing:CreateTargetGroup,
elasticloadbalancing:DeleteListener,
elasticloadbalancing:DeleteTargetGroup,
elasticloadbalancing:DescribeTags,
elasticloadbalancing:AddTags,
elasticloadbalancing:RegisterTargets,
elasticloadbalancing:DescribeTargetHealth,
ec2:DescribeSubnets,
tag:GetResources
```

### Update
```json
refactor-spaces:UpdateRoute,
refactor-spaces:GetRoute,
refactor-spaces:TagResource,
iam:CreateServiceLinkedRole,
apigateway:GET,
apigateway:PATCH,
apigateway:POST,
apigateway:PUT,
apigateway:DELETE,
apigateway:UpdateRestApiPolicy,
lambda:GetFunctionConfiguration,
lambda:AddPermission,
elasticloadbalancing:DescribeListeners,
elasticloadbalancing:DescribeTargetGroups,
elasticloadbalancing:CreateListener,
elasticloadbalancing:CreateTargetGroup,
elasticloadbalancing:DeleteListener,
elasticloadbalancing:DeleteTargetGroup,
elasticloadbalancing:DescribeTags,
elasticloadbalancing:AddTags,
elasticloadbalancing:RegisterTargets,
elasticloadbalancing:DescribeTargetHealth,
ec2:DescribeSubnets,
ec2:DescribeSubnets,
tag:GetResources
```

