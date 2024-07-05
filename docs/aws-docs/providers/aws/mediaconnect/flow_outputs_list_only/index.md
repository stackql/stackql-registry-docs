---
title: flow_outputs_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - flow_outputs_list_only
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

Lists <code>flow_outputs</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/flow_outputs/"><code>flow_outputs</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_outputs_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaConnect::FlowOutput</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediaconnect.flow_outputs_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="flow_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.</td></tr>
<tr><td><CopyableCode code="output_arn" /></td><td><code>string</code></td><td>The ARN of the output.</td></tr>
<tr><td><CopyableCode code="cidr_allow_list" /></td><td><code>array</code></td><td>The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.</td></tr>
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
<tr><td><CopyableCode code="media_stream_output_configurations" /></td><td><code>array</code></td><td>The definition for each media stream that is associated with the output.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>flow_outputs</code> in a region.
```sql
SELECT
region,
output_arn
FROM aws.mediaconnect.flow_outputs_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>flow_outputs_list_only</code> resource, see <a href="/providers/aws/mediaconnect/flow_outputs/#permissions"><code>flow_outputs</code></a>


