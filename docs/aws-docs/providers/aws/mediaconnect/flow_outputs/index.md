---
title: flow_outputs
hide_title: false
hide_table_of_contents: false
keywords:
  - flow_outputs
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

Creates, updates, deletes or gets a <code>flow_output</code> resource or lists <code>flow_outputs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_outputs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaConnect::FlowOutput</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediaconnect.flow_outputs" /></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="FlowArn, Protocol, region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>flow_outputs</code> in a region.
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
vpc_interface_attachment,
media_stream_output_configurations
FROM aws.mediaconnect.flow_outputs
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>flow_output</code>.
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
vpc_interface_attachment,
media_stream_output_configurations
FROM aws.mediaconnect.flow_outputs
WHERE region = 'us-east-1' AND data__Identifier = '<OutputArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>flow_output</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.mediaconnect.flow_outputs (
 FlowArn,
 Protocol,
 region
)
SELECT 
'{{ FlowArn }}',
 '{{ Protocol }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.mediaconnect.flow_outputs (
 FlowArn,
 CidrAllowList,
 Encryption,
 Description,
 Destination,
 MaxLatency,
 MinLatency,
 Name,
 Port,
 Protocol,
 RemoteId,
 SmoothingLatency,
 StreamId,
 VpcInterfaceAttachment,
 MediaStreamOutputConfigurations,
 region
)
SELECT 
 '{{ FlowArn }}',
 '{{ CidrAllowList }}',
 '{{ Encryption }}',
 '{{ Description }}',
 '{{ Destination }}',
 '{{ MaxLatency }}',
 '{{ MinLatency }}',
 '{{ Name }}',
 '{{ Port }}',
 '{{ Protocol }}',
 '{{ RemoteId }}',
 '{{ SmoothingLatency }}',
 '{{ StreamId }}',
 '{{ VpcInterfaceAttachment }}',
 '{{ MediaStreamOutputConfigurations }}',
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
  - name: flow_output
    props:
      - name: FlowArn
        value: '{{ FlowArn }}'
      - name: CidrAllowList
        value:
          - '{{ CidrAllowList[0] }}'
      - name: Encryption
        value:
          Algorithm: '{{ Algorithm }}'
          ConstantInitializationVector: '{{ ConstantInitializationVector }}'
          DeviceId: '{{ DeviceId }}'
          KeyType: '{{ KeyType }}'
          Region: '{{ Region }}'
          ResourceId: '{{ ResourceId }}'
          RoleArn: '{{ RoleArn }}'
          SecretArn: '{{ SecretArn }}'
          Url: '{{ Url }}'
      - name: Description
        value: '{{ Description }}'
      - name: Destination
        value: '{{ Destination }}'
      - name: MaxLatency
        value: '{{ MaxLatency }}'
      - name: MinLatency
        value: '{{ MinLatency }}'
      - name: Name
        value: '{{ Name }}'
      - name: Port
        value: '{{ Port }}'
      - name: Protocol
        value: '{{ Protocol }}'
      - name: RemoteId
        value: '{{ RemoteId }}'
      - name: SmoothingLatency
        value: '{{ SmoothingLatency }}'
      - name: StreamId
        value: '{{ StreamId }}'
      - name: VpcInterfaceAttachment
        value:
          VpcInterfaceName: '{{ VpcInterfaceName }}'
      - name: MediaStreamOutputConfigurations
        value:
          - EncodingName: '{{ EncodingName }}'
            DestinationConfigurations:
              - DestinationIp: '{{ DestinationIp }}'
                DestinationPort: '{{ DestinationPort }}'
                Interface:
                  Name: '{{ Name }}'
            MediaStreamName: '{{ MediaStreamName }}'
            EncodingParameters:
              CompressionFactor: null
              EncoderProfile: '{{ EncoderProfile }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.mediaconnect.flow_outputs
WHERE data__Identifier = '<OutputArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>flow_outputs</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
mediaconnect:AddFlowOutputs
```

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

### List
```json
mediaconnect:DescribeFlow
```

