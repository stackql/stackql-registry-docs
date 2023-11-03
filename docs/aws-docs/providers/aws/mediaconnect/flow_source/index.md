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
Gets an individual <code>flow_source</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_source</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.mediaconnect.flow_source</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>FlowArn</code></td><td><code>string</code></td><td>The ARN of the flow.</td></tr><tr><td><code>SourceArn</code></td><td><code>string</code></td><td>The ARN of the source.</td></tr><tr><td><code>Decryption</code></td><td><code>undefined</code></td><td>The type of encryption that is used on the content ingested from this source.</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.</td></tr><tr><td><code>EntitlementArn</code></td><td><code>string</code></td><td>The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account. The entitlement is set by the content originator and the ARN is generated as part of the originator's flow.</td></tr><tr><td><code>IngestIp</code></td><td><code>string</code></td><td>The IP address that the flow will be listening on for incoming content.</td></tr><tr><td><code>IngestPort</code></td><td><code>integer</code></td><td>The port that the flow will be listening on for incoming content.</td></tr><tr><td><code>MaxBitrate</code></td><td><code>integer</code></td><td>The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.</td></tr><tr><td><code>MaxLatency</code></td><td><code>integer</code></td><td>The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the source.</td></tr><tr><td><code>Protocol</code></td><td><code>string</code></td><td>The protocol that is used by the source.</td></tr><tr><td><code>StreamId</code></td><td><code>string</code></td><td>The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.</td></tr><tr><td><code>SourceIngestPort</code></td><td><code>string</code></td><td>The port that the flow will be listening on for incoming content.(ReadOnly)</td></tr><tr><td><code>VpcInterfaceName</code></td><td><code>string</code></td><td>The name of the VPC Interface this Source is configured with.</td></tr><tr><td><code>WhitelistCidr</code></td><td><code>string</code></td><td>The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.mediaconnect.flow_source
WHERE region = 'us-east-1' AND data__Identifier = '{SourceArn}'
```
