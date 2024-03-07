---
title: gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - gateways
  - iotsitewise
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>gateways</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>gateways</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotsitewise.gateways</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>gateway_id</code></td><td><code>string</code></td><td>The ID of the gateway device.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>gateways</code> resource, the following permissions are required:

### Create
```json
iotsitewise:CreateGateway,
iotsitewise:DescribeGateway,
iotsitewise:DescribeGatewayCapabilityConfiguration,
iotsitewise:UpdateGatewayCapabilityConfiguration,
iam:PassRole,
iam:GetRole,
greengrass:GetCoreDevice,
iotsitewise:ListTagsForResource,
iotsitewise:TagResource,
iot:DescribeThing
```

### List
```json
iotsitewise:ListGateways
```


## Example
```sql
SELECT
region,
gateway_id
FROM awscc.iotsitewise.gateways
WHERE region = 'us-east-1'
```
