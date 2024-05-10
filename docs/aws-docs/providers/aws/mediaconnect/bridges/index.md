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


Used to retrieve a list of <code>bridges</code> in a region or to create or delete a <code>bridges</code> resource, use <code>bridge</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bridges</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaConnect::Bridge</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediaconnect.bridges" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="bridge_arn" /></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) of the bridge.</td></tr>
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
bridge_arn
FROM aws.mediaconnect.bridges
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
 "Name": "{{ Name }}",
 "PlacementArn": "{{ PlacementArn }}",
 "Sources": [
  {
   "Name": "{{ Name }}",
   "BridgeArn": "{{ BridgeArn }}"
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.mediaconnect.bridges (
 Name,
 PlacementArn,
 Sources,
 region
)
SELECT 
{{ .Name }},
 {{ .PlacementArn }},
 {{ .Sources }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "PlacementArn": "{{ PlacementArn }}",
 "SourceFailoverConfig": {
  "State": "{{ State }}",
  "RecoveryWindow": "{{ RecoveryWindow }}",
  "FailoverMode": "{{ FailoverMode }}",
  "SourcePriority": {
   "PrimarySource": "{{ PrimarySource }}"
  }
 },
 "Outputs": [
  {
   "BridgeArn": "{{ BridgeArn }}",
   "NetworkOutput": {
    "Protocol": "{{ Protocol }}",
    "IpAddress": "{{ IpAddress }}",
    "Port": "{{ Port }}",
    "NetworkName": "{{ NetworkName }}",
    "Ttl": "{{ Ttl }}"
   },
   "Name": "{{ Name }}"
  }
 ],
 "Sources": [
  {
   "Name": "{{ Name }}",
   "BridgeArn": "{{ BridgeArn }}",
   "FlowSource": {
    "FlowArn": "{{ FlowArn }}",
    "FlowVpcInterfaceAttachment": {
     "VpcInterfaceName": "{{ VpcInterfaceName }}"
    }
   },
   "NetworkSource": {
    "Protocol": "{{ Protocol }}",
    "MulticastIp": "{{ MulticastIp }}",
    "Port": "{{ Port }}",
    "NetworkName": "{{ NetworkName }}"
   }
  }
 ],
 "IngressGatewayBridge": {
  "MaxBitrate": "{{ MaxBitrate }}",
  "MaxOutputs": "{{ MaxOutputs }}"
 },
 "EgressGatewayBridge": {
  "MaxBitrate": "{{ MaxBitrate }}"
 }
}
>>>
--all properties
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
 {{ .Name }},
 {{ .PlacementArn }},
 {{ .SourceFailoverConfig }},
 {{ .Outputs }},
 {{ .Sources }},
 {{ .IngressGatewayBridge }},
 {{ .EgressGatewayBridge }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
mediaconnect:DescribeBridge,
mediaconnect:DeleteBridge
```

### List
```json
mediaconnect:ListBridges
```

