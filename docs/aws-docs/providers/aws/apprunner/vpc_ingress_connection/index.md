---
title: vpc_ingress_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_ingress_connection
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>vpc_ingress_connection</code> resource, use <code>vpc_ingress_connections</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_ingress_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AppRunner::VpcIngressConnection resource is an App Runner resource that specifies an App Runner VpcIngressConnection.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apprunner.vpc_ingress_connection" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="vpc_ingress_connection_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the VpcIngressConnection.</td></tr>
<tr><td><CopyableCode code="vpc_ingress_connection_name" /></td><td><code>string</code></td><td>The customer-provided Vpc Ingress Connection name.</td></tr>
<tr><td><CopyableCode code="service_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the service.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The current status of the VpcIngressConnection.</td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The Domain name associated with the VPC Ingress Connection.</td></tr>
<tr><td><CopyableCode code="ingress_vpc_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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
vpc_ingress_connection_arn,
vpc_ingress_connection_name,
service_arn,
status,
domain_name,
ingress_vpc_configuration,
tags
FROM aws.apprunner.vpc_ingress_connection
WHERE region = 'us-east-1' AND data__Identifier = '<VpcIngressConnectionArn>';
```


## Permissions

To operate on the <code>vpc_ingress_connection</code> resource, the following permissions are required:

### Read
```json
apprunner:DescribeVpcIngressConnection
```

### Update
```json
apprunner:UpdateVpcIngressConnection
```

