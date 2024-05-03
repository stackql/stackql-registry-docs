---
title: flow_output
hide_title: false
hide_table_of_contents: false
keywords:
  - flow_output
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

Gets or operates on an individual <code>flow_output</code> resource, use <code>flow_outputs</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_output</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaConnect::FlowOutput</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediaconnect.flow_output" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="flow_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.</td></tr>
<tr><td><CopyableCode code="output_arn" /></td><td><code>string</code></td><td>The ARN of the output.</td></tr>
<tr><td><CopyableCode code="cidr_allow_list" /></td><td><code>array</code></td><td>The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0&#x2F;16.</td></tr>
<tr><td><CopyableCode code="encryption" /></td><td><code>object</code></td><td>The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the output.</td></tr>
<tr><td><CopyableCode code="destination" /></td><td><code>string</code></td><td>The address where you want to send the output.</td></tr>
<tr><td><CopyableCode code="max_latency" /></td><td><code>integer</code></td><td>The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.</td></tr>
<tr><td><CopyableCode code="min_latency" /></td><td><code>integer</code></td><td>The minimum latency in milliseconds.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the output. This value must be unique within the current flow.</td></tr>
<tr><td><CopyableCode code="port" /></td><td><code>integer</code></td><td>The port to use when content is distributed to this output.</td></tr>
<tr><td><CopyableCode code="protocol" /></td><td><code>string</code></td><td>The protocol that is used by the source or output.</td></tr>
<tr><td><CopyableCode code="remote_id" /></td><td><code>string</code></td><td>The remote ID for the Zixi-pull stream.</td></tr>
<tr><td><CopyableCode code="smoothing_latency" /></td><td><code>integer</code></td><td>The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.</td></tr>
<tr><td><CopyableCode code="stream_id" /></td><td><code>string</code></td><td>The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.</td></tr>
<tr><td><CopyableCode code="vpc_interface_attachment" /></td><td><code>object</code></td><td>The name of the VPC interface attachment to use for this output.</td></tr>
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
flow_arn,
output_arn,
cidr_allow_list,
encryption,
description,
destination,
max_latency,
min_latency,
name,
port,
protocol,
remote_id,
smoothing_latency,
stream_id,
vpc_interface_attachment
FROM aws.mediaconnect.flow_output
WHERE data__Identifier = '<OutputArn>';
```

## Permissions

To operate on the <code>flow_output</code> resource, the following permissions are required:

### Read
```json
mediaconnect:DescribeFlow
```

### Update
```json
mediaconnect:DescribeFlow,
mediaconnect:UpdateFlowOutput
```

### Delete
```json
mediaconnect:DescribeFlow,
mediaconnect:RemoveFlowOutput
```

