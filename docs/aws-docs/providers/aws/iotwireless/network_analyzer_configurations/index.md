---
title: network_analyzer_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - network_analyzer_configurations
  - iotwireless
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

Creates, updates, deletes or gets a <code>network_analyzer_configuration</code> resource or lists <code>network_analyzer_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_analyzer_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Create and manage NetworkAnalyzerConfiguration resource.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.network_analyzer_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the network analyzer configuration</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the new resource</td></tr>
<tr><td><CopyableCode code="trace_content" /></td><td><code>object</code></td><td>Trace content for your wireless gateway and wireless device resources</td></tr>
<tr><td><CopyableCode code="wireless_devices" /></td><td><code>array</code></td><td>List of wireless gateway resources that have been added to the network analyzer configuration</td></tr>
<tr><td><CopyableCode code="wireless_gateways" /></td><td><code>array</code></td><td>List of wireless gateway resources that have been added to the network analyzer configuration</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Arn for network analyzer configuration, Returned upon successful create.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html"><code>AWS::IoTWireless::NetworkAnalyzerConfiguration</code></a>.

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
    <td><CopyableCode code="Name, region" /></td>
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
Gets all <code>network_analyzer_configurations</code> in a region.
```sql
SELECT
region,
name,
description,
trace_content,
wireless_devices,
wireless_gateways,
arn,
tags
FROM aws.iotwireless.network_analyzer_configurations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>network_analyzer_configuration</code>.
```sql
SELECT
region,
name,
description,
trace_content,
wireless_devices,
wireless_gateways,
arn,
tags
FROM aws.iotwireless.network_analyzer_configurations
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_analyzer_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iotwireless.network_analyzer_configurations (
 Name,
 region
)
SELECT 
'{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iotwireless.network_analyzer_configurations (
 Name,
 Description,
 TraceContent,
 WirelessDevices,
 WirelessGateways,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ TraceContent }}',
 '{{ WirelessDevices }}',
 '{{ WirelessGateways }}',
 '{{ Tags }}',
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
  - name: network_analyzer_configuration
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: TraceContent
        value:
          WirelessDeviceFrameInfo: '{{ WirelessDeviceFrameInfo }}'
          LogLevel: '{{ LogLevel }}'
      - name: WirelessDevices
        value:
          - '{{ WirelessDevices[0] }}'
      - name: WirelessGateways
        value:
          - '{{ WirelessGateways[0] }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iotwireless.network_analyzer_configurations
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>network_analyzer_configurations</code> resource, the following permissions are required:

### Create
```json
iotwireless:CreateNetworkAnalyzerConfiguration,
iotwireless:TagResource
```

### Read
```json
iotwireless:GetNetworkAnalyzerConfiguration,
iotwireless:ListTagsForResource
```

### Update
```json
iotwireless:UpdateNetworkAnalyzerConfiguration,
iotwireless:GetNetworkAnalyzerConfiguration,
iotwireless:TagResource,
iotwireless:UntagResource
```

### Delete
```json
iotwireless:DeleteNetworkAnalyzerConfiguration
```

### List
```json
iotwireless:ListNetworkAnalyzerConfigurations,
iotwireless:ListTagsForResource
```
