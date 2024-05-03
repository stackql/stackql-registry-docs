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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>bridge</code> resource, use <code>bridges</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bridge</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaConnect::Bridge</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediaconnect.bridge" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the bridge.</td></tr>
<tr><td><CopyableCode code="bridge_arn" /></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) of the bridge.</td></tr>
<tr><td><CopyableCode code="placement_arn" /></td><td><code>string</code></td><td>The placement Amazon Resource Number (ARN) of the bridge.</td></tr>
<tr><td><CopyableCode code="bridge_state" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="source_failover_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="outputs" /></td><td><code>array</code></td><td>The outputs on this bridge.</td></tr>
<tr><td><CopyableCode code="sources" /></td><td><code>array</code></td><td>The sources on this bridge.</td></tr>
<tr><td><CopyableCode code="ingress_gateway_bridge" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="egress_gateway_bridge" /></td><td><code>object</code></td><td></td></tr>
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
name,
bridge_arn,
placement_arn,
bridge_state,
source_failover_config,
outputs,
sources,
ingress_gateway_bridge,
egress_gateway_bridge
FROM aws.mediaconnect.bridge
WHERE data__Identifier = '<BridgeArn>';
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

