---
title: vpc_endpoint_service
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_endpoint_service
  - ec2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>vpc_endpoint_service</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_endpoint_service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::VPCEndpointService</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.vpc_endpoint_service</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>network_load_balancer_arns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>contributor_insights_enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>payer_responsibility</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>acceptance_required</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>gateway_load_balancer_arns</code></td><td><code>array</code></td><td></td></tr>
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
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
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
network_load_balancer_arns,
contributor_insights_enabled,
payer_responsibility,
service_id,
acceptance_required,
gateway_load_balancer_arns
FROM aws.ec2.vpc_endpoint_service
WHERE data__Identifier = '<ServiceId>';
```

## Permissions

To operate on the <code>vpc_endpoint_service</code> resource, the following permissions are required:

### Update
```json
ec2:ModifyVpcEndpointServiceConfiguration,
ec2:DeleteVpcEndpointServiceConfigurations,
ec2:DescribeVpcEndpointServiceConfigurations,
ec2:ModifyVpcEndpointServicePayerResponsibility,
cloudwatch:ListManagedInsightRules,
cloudwatch:DeleteInsightRules,
cloudwatch:PutManagedInsightRules
```

### Read
```json
ec2:DescribeVpcEndpointServiceConfigurations,
cloudwatch:ListManagedInsightRules
```

### Delete
```json
ec2:DeleteVpcEndpointServiceConfigurations,
ec2:DescribeVpcEndpointServiceConfigurations,
cloudwatch:ListManagedInsightRules,
cloudwatch:DeleteInsightRules
```

