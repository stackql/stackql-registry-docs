---
title: flows
hide_title: false
hide_table_of_contents: false
keywords:
  - flows
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

Creates, updates, deletes or gets a <code>flow</code> resource or lists <code>flows</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaConnect::Flow</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediaconnect.flows" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="flow_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.</td></tr>
<tr><td><CopyableCode code="egress_ip" /></td><td><code>string</code></td><td>The IP address from which video will be sent to output destinations.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the flow.</td></tr>
<tr><td><CopyableCode code="availability_zone" /></td><td><code>string</code></td><td>The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.</td></tr>
<tr><td><CopyableCode code="flow_availability_zone" /></td><td><code>string</code></td><td>The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.(ReadOnly)</td></tr>
<tr><td><CopyableCode code="source" /></td><td><code>object</code></td><td>The source of the flow.</td></tr>
<tr><td><CopyableCode code="source_failover_config" /></td><td><code>object</code></td><td>The source failover config of the flow.</td></tr>
<tr><td><CopyableCode code="vpc_interfaces" /></td><td><code>array</code></td><td>The VPC interfaces that you added to this flow.</td></tr>
<tr><td><CopyableCode code="media_streams" /></td><td><code>array</code></td><td>The media streams associated with the flow. You can associate any of these media streams with sources and outputs on the flow.</td></tr>
<tr><td><CopyableCode code="maintenance" /></td><td><code>object</code></td><td>The maintenance settings you want to use for the flow.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="Name, Source, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>flows</code> in a region.
```sql
SELECT
region,
flow_arn
FROM aws.mediaconnect.flows
WHERE region = 'us-east-1';
```
Gets all properties from a <code>flow</code>.
```sql
SELECT
region,
flow_arn,
egress_ip,
name,
availability_zone,
flow_availability_zone,
source,
source_failover_config,
vpc_interfaces,
media_streams,
maintenance
FROM aws.mediaconnect.flows
WHERE region = 'us-east-1' AND data__Identifier = '<FlowArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>flow</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.mediaconnect.flows (
 Name,
 Source,
 region
)
SELECT 
'{{ Name }}',
 '{{ Source }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.mediaconnect.flows (
 Name,
 AvailabilityZone,
 Source,
 SourceFailoverConfig,
 VpcInterfaces,
 MediaStreams,
 Maintenance,
 region
)
SELECT 
 '{{ Name }}',
 '{{ AvailabilityZone }}',
 '{{ Source }}',
 '{{ SourceFailoverConfig }}',
 '{{ VpcInterfaces }}',
 '{{ MediaStreams }}',
 '{{ Maintenance }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: flow
    props:
      - name: Name
        value: '{{ Name }}'
      - name: AvailabilityZone
        value: '{{ AvailabilityZone }}'
      - name: Source
        value:
          SourceArn: '{{ SourceArn }}'
          Decryption:
            Algorithm: '{{ Algorithm }}'
            ConstantInitializationVector: '{{ ConstantInitializationVector }}'
            DeviceId: '{{ DeviceId }}'
            KeyType: '{{ KeyType }}'
            Region: '{{ Region }}'
            ResourceId: '{{ ResourceId }}'
            RoleArn: '{{ RoleArn }}'
            SecretArn: '{{ SecretArn }}'
            Url: '{{ Url }}'
          Description: '{{ Description }}'
          EntitlementArn: '{{ EntitlementArn }}'
          GatewayBridgeSource:
            BridgeArn: '{{ BridgeArn }}'
            VpcInterfaceAttachment:
              VpcInterfaceName: '{{ VpcInterfaceName }}'
          IngestIp: '{{ IngestIp }}'
          IngestPort: '{{ IngestPort }}'
          MaxBitrate: '{{ MaxBitrate }}'
          MaxLatency: '{{ MaxLatency }}'
          MinLatency: '{{ MinLatency }}'
          Name: '{{ Name }}'
          Protocol: '{{ Protocol }}'
          SenderIpAddress: '{{ SenderIpAddress }}'
          SenderControlPort: '{{ SenderControlPort }}'
          StreamId: '{{ StreamId }}'
          SourceIngestPort: '{{ SourceIngestPort }}'
          SourceListenerAddress: '{{ SourceListenerAddress }}'
          SourceListenerPort: '{{ SourceListenerPort }}'
          VpcInterfaceName: '{{ VpcInterfaceName }}'
          WhitelistCidr: '{{ WhitelistCidr }}'
          MaxSyncBuffer: '{{ MaxSyncBuffer }}'
          MediaStreamSourceConfigurations:
            - EncodingName: '{{ EncodingName }}'
              InputConfigurations:
                - InputPort: '{{ InputPort }}'
                  Interface:
                    Name: '{{ Name }}'
              MediaStreamName: '{{ MediaStreamName }}'
      - name: SourceFailoverConfig
        value:
          State: '{{ State }}'
          RecoveryWindow: '{{ RecoveryWindow }}'
          FailoverMode: '{{ FailoverMode }}'
          SourcePriority:
            PrimarySource: '{{ PrimarySource }}'
      - name: VpcInterfaces
        value:
          - Name: '{{ Name }}'
            NetworkInterfaceType: '{{ NetworkInterfaceType }}'
            RoleArn: '{{ RoleArn }}'
            SecurityGroupIds:
              - '{{ SecurityGroupIds[0] }}'
            SubnetId: '{{ SubnetId }}'
            NetworkInterfaceIds:
              - '{{ NetworkInterfaceIds[0] }}'
      - name: MediaStreams
        value:
          - MediaStreamId: '{{ MediaStreamId }}'
            MediaStreamType: '{{ MediaStreamType }}'
            VideoFormat: '{{ VideoFormat }}'
            MediaStreamName: '{{ MediaStreamName }}'
            Description: '{{ Description }}'
            Attributes:
              Fmtp:
                ExactFramerate: '{{ ExactFramerate }}'
                Colorimetry: '{{ Colorimetry }}'
                ScanMode: '{{ ScanMode }}'
                Tcs: '{{ Tcs }}'
                Range: '{{ Range }}'
                Par: '{{ Par }}'
                ChannelOrder: '{{ ChannelOrder }}'
              Lang: '{{ Lang }}'
            ClockRate: '{{ ClockRate }}'
            Fmt: '{{ Fmt }}'
      - name: Maintenance
        value:
          MaintenanceDay: '{{ MaintenanceDay }}'
          MaintenanceStartHour: '{{ MaintenanceStartHour }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.mediaconnect.flows
WHERE data__Identifier = '<FlowArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>flows</code> resource, the following permissions are required:

### Create
```json
mediaconnect:CreateFlow,
iam:PassRole
```

### Read
```json
mediaconnect:DescribeFlow
```

### Update
```json
mediaconnect:DescribeFlow,
mediaconnect:UpdateFlow,
mediaconnect:UpdateFlowSource,
mediaconnect:UpdateFlowMediaStream,
mediaconnect:AddFlowMediaStreams,
mediaconnect:RemoveFlowMediaStream,
mediaconnect:AddFlowVpcInterfaces,
mediaconnect:RemoveFlowVpcInterface
```

### Delete
```json
mediaconnect:DescribeFlow,
mediaconnect:DeleteFlow
```

### List
```json
mediaconnect:ListFlows
```

