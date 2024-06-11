---
title: bridges
hide_title: false
hide_table_of_contents: false
keywords:
  - bridges
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

Creates, updates, deletes or gets a <code>bridge</code> resource or lists <code>bridges</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bridges</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaConnect::Bridge</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediaconnect.bridges" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the bridge.</td></tr>
<tr><td><CopyableCode code="bridge_arn" /></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) of the bridge.</td></tr>
<tr><td><CopyableCode code="placement_arn" /></td><td><code>string</code></td><td>The placement Amazon Resource Number (ARN) of the bridge.</td></tr>
<tr><td><CopyableCode code="bridge_state" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="source_failover_config" /></td><td><code>The settings for source failover</code></td><td></td></tr>
<tr><td><CopyableCode code="outputs" /></td><td><code>array</code></td><td>The outputs on this bridge.</td></tr>
<tr><td><CopyableCode code="sources" /></td><td><code>array</code></td><td>The sources on this bridge.</td></tr>
<tr><td><CopyableCode code="ingress_gateway_bridge" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="egress_gateway_bridge" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="Name, PlacementArn, Sources, region" /></td>
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
List all <code>bridges</code> in a region.
```sql
SELECT
region,
bridge_arn
FROM aws.mediaconnect.bridges
WHERE region = 'us-east-1';
```
Gets all properties from a <code>bridge</code>.
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
FROM aws.mediaconnect.bridges
WHERE region = 'us-east-1' AND data__Identifier = '<BridgeArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>bridge</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.mediaconnect.bridges (
 Name,
 PlacementArn,
 Sources,
 region
)
SELECT 
'{{ Name }}',
 '{{ PlacementArn }}',
 '{{ Sources }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.mediaconnect.bridges (
 Name,
 PlacementArn,
 SourceFailoverConfig,
 Outputs,
 Sources,
 IngressGatewayBridge,
 EgressGatewayBridge,
 region
)
SELECT 
 '{{ Name }}',
 '{{ PlacementArn }}',
 '{{ SourceFailoverConfig }}',
 '{{ Outputs }}',
 '{{ Sources }}',
 '{{ IngressGatewayBridge }}',
 '{{ EgressGatewayBridge }}',
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
  - name: bridge
    props:
      - name: Name
        value: '{{ Name }}'
      - name: PlacementArn
        value: '{{ PlacementArn }}'
      - name: SourceFailoverConfig
        value:
          State: '{{ State }}'
          RecoveryWindow: '{{ RecoveryWindow }}'
          FailoverMode: '{{ FailoverMode }}'
          SourcePriority:
            PrimarySource: '{{ PrimarySource }}'
      - name: Outputs
        value:
          - BridgeArn: '{{ BridgeArn }}'
            NetworkOutput:
              Protocol: '{{ Protocol }}'
              IpAddress: '{{ IpAddress }}'
              Port: '{{ Port }}'
              NetworkName: '{{ NetworkName }}'
              Ttl: '{{ Ttl }}'
            Name: '{{ Name }}'
      - name: Sources
        value:
          - Name: '{{ Name }}'
            BridgeArn: '{{ BridgeArn }}'
            FlowSource:
              FlowArn: '{{ FlowArn }}'
              FlowVpcInterfaceAttachment:
                VpcInterfaceName: '{{ VpcInterfaceName }}'
            NetworkSource:
              Protocol: '{{ Protocol }}'
              MulticastIp: '{{ MulticastIp }}'
              Port: '{{ Port }}'
              NetworkName: '{{ NetworkName }}'
      - name: IngressGatewayBridge
        value:
          MaxBitrate: '{{ MaxBitrate }}'
          MaxOutputs: '{{ MaxOutputs }}'
      - name: EgressGatewayBridge
        value:
          MaxBitrate: '{{ MaxBitrate }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.mediaconnect.bridges
WHERE data__Identifier = '<BridgeArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>bridges</code> resource, the following permissions are required:

### Create
```json
mediaconnect:CreateBridge,
mediaconnect:DescribeBridge
```

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

### List
```json
mediaconnect:ListBridges
```

