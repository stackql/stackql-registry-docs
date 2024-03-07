---
title: bridge
hide_title: false
hide_table_of_contents: false
keywords:
  - bridge
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
Gets an individual <code>bridge</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bridge</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>bridge</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.mediaconnect.bridge</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the bridge.</td></tr>
<tr><td><code>bridge_arn</code></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) of the bridge.</td></tr>
<tr><td><code>placement_arn</code></td><td><code>string</code></td><td>The placement Amazon Resource Number (ARN) of the bridge.</td></tr>
<tr><td><code>bridge_state</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>source_failover_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>outputs</code></td><td><code>array</code></td><td>The outputs on this bridge.</td></tr>
<tr><td><code>sources</code></td><td><code>array</code></td><td>The sources on this bridge.</td></tr>
<tr><td><code>ingress_gateway_bridge</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>egress_gateway_bridge</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
bridge_arn,
placement_arn,
bridge_state,
source_failover_config,
outputs,
sources,
ingress_gateway_bridge,
egress_gateway_bridge
FROM awscc.mediaconnect.bridge
WHERE region = 'us-east-1'
AND data__Identifier = '{BridgeArn}';
```

## Permissions

To operate on the <code>bridge</code> resource, the following permissions are required:

### Read
```json
mediaconnect:DescribeBridge
```

### Update
```json
mediaconnect:DescribeBridge,
mediaconnect:UpdateBridge
```

### Delete
```json
mediaconnect:DescribeBridge,
mediaconnect:DeleteBridge
```

