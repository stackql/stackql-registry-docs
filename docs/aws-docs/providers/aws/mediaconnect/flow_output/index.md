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
Gets an individual <code>flow_output</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_output</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>flow_output</td></tr>
<tr><td><b>Id</b></td><td><code>aws.mediaconnect.flow_output</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>flow_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.</td></tr>
<tr><td><code>output_arn</code></td><td><code>string</code></td><td>The ARN of the output.</td></tr>
<tr><td><code>cidr_allow_list</code></td><td><code>array</code></td><td>The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0&#x2F;16.</td></tr>
<tr><td><code>encryption</code></td><td><code>object</code></td><td>The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description of the output.</td></tr>
<tr><td><code>destination</code></td><td><code>string</code></td><td>The address where you want to send the output.</td></tr>
<tr><td><code>max_latency</code></td><td><code>integer</code></td><td>The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.</td></tr>
<tr><td><code>min_latency</code></td><td><code>integer</code></td><td>The minimum latency in milliseconds.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the output. This value must be unique within the current flow.</td></tr>
<tr><td><code>port</code></td><td><code>integer</code></td><td>The port to use when content is distributed to this output.</td></tr>
<tr><td><code>protocol</code></td><td><code>string</code></td><td>The protocol that is used by the source or output.</td></tr>
<tr><td><code>remote_id</code></td><td><code>string</code></td><td>The remote ID for the Zixi-pull stream.</td></tr>
<tr><td><code>smoothing_latency</code></td><td><code>integer</code></td><td>The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.</td></tr>
<tr><td><code>stream_id</code></td><td><code>string</code></td><td>The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.</td></tr>
<tr><td><code>vpc_interface_attachment</code></td><td><code>object</code></td><td>The name of the VPC interface attachment to use for this output.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;OutputArn&gt;'
```
