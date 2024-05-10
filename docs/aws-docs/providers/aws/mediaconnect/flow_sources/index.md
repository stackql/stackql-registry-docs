---
title: flow_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - flow_sources
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


Used to retrieve a list of <code>flow_sources</code> in a region or to create or delete a <code>flow_sources</code> resource, use <code>flow_source</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaConnect::FlowSource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediaconnect.flow_sources" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="source_arn" /></td><td><code>string</code></td><td>The ARN of the source.</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
source_arn
FROM aws.mediaconnect.flow_sources
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "Description": "{{ Description }}",
 "Name": "{{ Name }}"
}
>>>
--required properties only
INSERT INTO aws.mediaconnect.flow_sources (
 Description,
 Name,
 region
)
SELECT 
{{ .Description }},
 {{ .Name }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "FlowArn": "{{ FlowArn }}",
 "Decryption": {
  "Algorithm": "{{ Algorithm }}",
  "ConstantInitializationVector": "{{ ConstantInitializationVector }}",
  "DeviceId": "{{ DeviceId }}",
  "KeyType": "{{ KeyType }}",
  "Region": "{{ Region }}",
  "ResourceId": "{{ ResourceId }}",
  "RoleArn": "{{ RoleArn }}",
  "SecretArn": "{{ SecretArn }}",
  "Url": "{{ Url }}"
 },
 "Description": "{{ Description }}",
 "EntitlementArn": "{{ EntitlementArn }}",
 "GatewayBridgeSource": {
  "BridgeArn": "{{ BridgeArn }}",
  "VpcInterfaceAttachment": {
   "VpcInterfaceName": "{{ VpcInterfaceName }}"
  }
 },
 "IngestPort": "{{ IngestPort }}",
 "MaxBitrate": "{{ MaxBitrate }}",
 "MaxLatency": "{{ MaxLatency }}",
 "MinLatency": "{{ MinLatency }}",
 "Name": "{{ Name }}",
 "Protocol": "{{ Protocol }}",
 "SenderIpAddress": "{{ SenderIpAddress }}",
 "SenderControlPort": "{{ SenderControlPort }}",
 "StreamId": "{{ StreamId }}",
 "SourceListenerAddress": "{{ SourceListenerAddress }}",
 "SourceListenerPort": "{{ SourceListenerPort }}",
 "VpcInterfaceName": "{{ VpcInterfaceName }}",
 "WhitelistCidr": "{{ WhitelistCidr }}"
}
>>>
--all properties
INSERT INTO aws.mediaconnect.flow_sources (
 FlowArn,
 Decryption,
 Description,
 EntitlementArn,
 GatewayBridgeSource,
 IngestPort,
 MaxBitrate,
 MaxLatency,
 MinLatency,
 Name,
 Protocol,
 SenderIpAddress,
 SenderControlPort,
 StreamId,
 SourceListenerAddress,
 SourceListenerPort,
 VpcInterfaceName,
 WhitelistCidr,
 region
)
SELECT 
 {{ .FlowArn }},
 {{ .Decryption }},
 {{ .Description }},
 {{ .EntitlementArn }},
 {{ .GatewayBridgeSource }},
 {{ .IngestPort }},
 {{ .MaxBitrate }},
 {{ .MaxLatency }},
 {{ .MinLatency }},
 {{ .Name }},
 {{ .Protocol }},
 {{ .SenderIpAddress }},
 {{ .SenderControlPort }},
 {{ .StreamId }},
 {{ .SourceListenerAddress }},
 {{ .SourceListenerPort }},
 {{ .VpcInterfaceName }},
 {{ .WhitelistCidr }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.mediaconnect.flow_sources
WHERE data__Identifier = '<SourceArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>flow_sources</code> resource, the following permissions are required:

### Create
```json
mediaconnect:CreateFlow,
mediaconnect:DescribeFlow,
mediaconnect:AddFlowSources,
iam:PassRole
```

### Delete
```json
mediaconnect:DescribeFlow,
mediaconnect:RemoveFlowSource
```

### List
```json
mediaconnect:DescribeFlow
```

