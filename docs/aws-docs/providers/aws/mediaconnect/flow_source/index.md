---
title: flow_source
hide_title: false
hide_table_of_contents: false
keywords:
  - flow_source
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


Gets or updates an individual <code>flow_source</code> resource, use <code>flow_sources</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_source</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaConnect::FlowSource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediaconnect.flow_source" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="flow_arn" /></td><td><code>string</code></td><td>The ARN of the flow.</td></tr>
<tr><td><CopyableCode code="source_arn" /></td><td><code>string</code></td><td>The ARN of the source.</td></tr>
<tr><td><CopyableCode code="decryption" /></td><td><code>object</code></td><td>The type of encryption that is used on the content ingested from this source.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.</td></tr>
<tr><td><CopyableCode code="entitlement_arn" /></td><td><code>string</code></td><td>The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account. The entitlement is set by the content originator and the ARN is generated as part of the originator's flow.</td></tr>
<tr><td><CopyableCode code="gateway_bridge_source" /></td><td><code>object</code></td><td>The source configuration for cloud flows receiving a stream from a bridge.</td></tr>
<tr><td><CopyableCode code="ingest_ip" /></td><td><code>string</code></td><td>The IP address that the flow will be listening on for incoming content.</td></tr>
<tr><td><CopyableCode code="ingest_port" /></td><td><code>integer</code></td><td>The port that the flow will be listening on for incoming content.</td></tr>
<tr><td><CopyableCode code="max_bitrate" /></td><td><code>integer</code></td><td>The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.</td></tr>
<tr><td><CopyableCode code="max_latency" /></td><td><code>integer</code></td><td>The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.</td></tr>
<tr><td><CopyableCode code="min_latency" /></td><td><code>integer</code></td><td>The minimum latency in milliseconds.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the source.</td></tr>
<tr><td><CopyableCode code="protocol" /></td><td><code>string</code></td><td>The protocol that is used by the source.</td></tr>
<tr><td><CopyableCode code="sender_ip_address" /></td><td><code>string</code></td><td>The IP address that the flow communicates with to initiate connection with the sender for fujitsu-qos protocol.</td></tr>
<tr><td><CopyableCode code="sender_control_port" /></td><td><code>integer</code></td><td>The port that the flow uses to send outbound requests to initiate connection with the sender for fujitsu-qos protocol.</td></tr>
<tr><td><CopyableCode code="stream_id" /></td><td><code>string</code></td><td>The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.</td></tr>
<tr><td><CopyableCode code="source_ingest_port" /></td><td><code>string</code></td><td>The port that the flow will be listening on for incoming content.(ReadOnly)</td></tr>
<tr><td><CopyableCode code="source_listener_address" /></td><td><code>string</code></td><td>Source IP or domain name for SRT-caller protocol.</td></tr>
<tr><td><CopyableCode code="source_listener_port" /></td><td><code>integer</code></td><td>Source port for SRT-caller protocol.</td></tr>
<tr><td><CopyableCode code="vpc_interface_name" /></td><td><code>string</code></td><td>The name of the VPC Interface this Source is configured with.</td></tr>
<tr><td><CopyableCode code="whitelist_cidr" /></td><td><code>string</code></td><td>The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0&#x2F;16.</td></tr>
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
flow_arn,
source_arn,
decryption,
description,
entitlement_arn,
gateway_bridge_source,
ingest_ip,
ingest_port,
max_bitrate,
max_latency,
min_latency,
name,
protocol,
sender_ip_address,
sender_control_port,
stream_id,
source_ingest_port,
source_listener_address,
source_listener_port,
vpc_interface_name,
whitelist_cidr
FROM aws.mediaconnect.flow_source
WHERE region = 'us-east-1' AND data__Identifier = '<SourceArn>';
```


## Permissions

To operate on the <code>flow_source</code> resource, the following permissions are required:

### Read
```json
mediaconnect:DescribeFlow
```

### Update
```json
mediaconnect:DescribeFlow,
mediaconnect:UpdateFlowSource
```

