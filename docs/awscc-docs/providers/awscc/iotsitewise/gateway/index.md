---
title: gateway
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway
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
Gets an individual <code>gateway</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateway</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>gateway</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotsitewise.gateway</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>gateway_name</code></td><td><code>string</code></td><td>A unique, friendly name for the gateway.</td></tr>
<tr><td><code>gateway_platform</code></td><td><code>object</code></td><td>The gateway's platform. You can only specify one platform in a gateway.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the gateway.</td></tr>
<tr><td><code>gateway_id</code></td><td><code>string</code></td><td>The ID of the gateway device.</td></tr>
<tr><td><code>gateway_capability_summaries</code></td><td><code>array</code></td><td>A list of gateway capability summaries that each contain a namespace and status.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>gateway</code> resource, the following permissions are required:

### Read
```json
iotsitewise:DescribeGateway,
iotsitewise:DescribeGatewayCapabilityConfiguration,
iotsitewise:ListTagsForResource
```

### Update
```json
iotsitewise:UpdateGateway,
iotsitewise:UpdateGatewayCapabilityConfiguration,
iotsitewise:TagResource,
iotsitewise:UntagResource,
iotsitewise:DescribeGateway,
iotsitewise:DescribeGatewayCapabilityConfiguration,
iotsitewise:ListTagsForResource
```

### Delete
```json
iotsitewise:DescribeGateway,
iotsitewise:DescribeGatewayCapabilityConfiguration,
iotsitewise:DeleteGateway
```


## Example
```sql
SELECT
region,
gateway_name,
gateway_platform,
tags,
gateway_id,
gateway_capability_summaries
FROM awscc.iotsitewise.gateway
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;GatewayId&gt;'
```
