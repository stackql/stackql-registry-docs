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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>application</code> resource, use <code>applications</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RefactorSpaces::Application Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.refactorspaces.application" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="api_gateway_proxy" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="api_gateway_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_link_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="nlb_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="nlb_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="application_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="environment_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="proxy_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stage_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="proxy_url" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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

