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
Gets an individual <code>gateway</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateway</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>gateway</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.mediaconnect.gateway</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the gateway. This name can not be modified after the gateway is created.</td></tr>
<tr><td><code>gateway_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the gateway.</td></tr>
<tr><td><code>gateway_state</code></td><td><code>string</code></td><td>The current status of the gateway.</td></tr>
<tr><td><code>egress_cidr_blocks</code></td><td><code>array</code></td><td>The range of IP addresses that contribute content or initiate output requests for flows communicating with this gateway. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0&#x2F;16.</td></tr>
<tr><td><code>networks</code></td><td><code>array</code></td><td>The list of networks in the gateway.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>gateway</code> resource, the following permissions are required:

### Read
```json
mediaconnect:DescribeGateway
```

### Delete
```json
iam:CreateServiceLinkedRole,
mediaconnect:DescribeGateway,
mediaconnect:DeleteGateway
```


## Example
```sql
SELECT
region,
name,
gateway_arn,
gateway_state,
egress_cidr_blocks,
networks
FROM awscc.mediaconnect.gateway
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;GatewayArn&gt;'
```
