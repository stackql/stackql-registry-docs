---
title: vpc_ingress_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_ingress_connections
  - apprunner
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

Used to retrieve a list of <code>vpc_ingress_connections</code> in a region or create a <code>vpc_ingress_connections</code> resource, use <code>vpc_ingress_connection</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_ingress_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AppRunner::VpcIngressConnection resource is an App Runner resource that specifies an App Runner VpcIngressConnection.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apprunner.vpc_ingress_connections" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="vpc_ingress_connection_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the VpcIngressConnection.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
vpc_ingress_connection_arn
FROM aws.apprunner.vpc_ingress_connections
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>vpc_ingress_connections</code> resource, the following permissions are required:

### Create
```json
apprunner:CreateVpcIngressConnection,
apprunner:DescribeVpcIngressConnection,
ec2:DescribeVpcs,
ec2:DescribeVpcEndpoints,
ec2:DescribeSubnets,
apprunner:TagResource
```

### List
```json
apprunner:ListVpcIngressConnections
```

