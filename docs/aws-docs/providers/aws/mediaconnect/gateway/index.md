---
title: gateway
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway
  - mediaconnect
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


Gets or updates an individual <code>gateway</code> resource, use <code>gateways</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateway</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaConnect::Gateway</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediaconnect.gateway" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the gateway. This name can not be modified after the gateway is created.</td></tr>
<tr><td><CopyableCode code="gateway_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the gateway.</td></tr>
<tr><td><CopyableCode code="gateway_state" /></td><td><code>string</code></td><td>The current status of the gateway.</td></tr>
<tr><td><CopyableCode code="egress_cidr_blocks" /></td><td><code>array</code></td><td>The range of IP addresses that contribute content or initiate output requests for flows communicating with this gateway. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0&#x2F;16.</td></tr>
<tr><td><CopyableCode code="networks" /></td><td><code>array</code></td><td>The list of networks in the gateway.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
name,
gateway_arn,
gateway_state,
egress_cidr_blocks,
networks
FROM aws.mediaconnect.gateway
WHERE region = 'us-east-1' AND data__Identifier = '<GatewayArn>';
```


## Permissions

To operate on the <code>gateway</code> resource, the following permissions are required:

### Read
```json
mediaconnect:DescribeGateway
```

