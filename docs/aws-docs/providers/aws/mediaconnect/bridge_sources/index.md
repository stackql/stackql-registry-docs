---
title: bridge_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - bridge_sources
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

Creates, updates, deletes or gets a <code>bridge_source</code> resource or lists <code>bridge_sources</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bridge_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaConnect::BridgeSource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediaconnect.bridge_sources" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the source.</td></tr>
<tr><td><CopyableCode code="bridge_arn" /></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) of the bridge.</td></tr>
<tr><td><CopyableCode code="flow_source" /></td><td><code>object</code></td><td>The source of the bridge. A flow source originates in MediaConnect as an existing cloud flow.</td></tr>
<tr><td><CopyableCode code="network_source" /></td><td><code>object</code></td><td>The source of the bridge. A network source originates at your premises.</td></tr>
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
    <td><CopyableCode code="Name, BridgeArn, region" /></td>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from an individual <code>bridge_source</code>.
```sql
SELECT
region,
name,
bridge_arn,
flow_source,
network_source
FROM aws.mediaconnect.bridge_sources
WHERE region = 'us-east-1' AND data__Identifier = '<BridgeArn>|<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>bridge_source</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.mediaconnect.bridge_sources (
 Name,
 BridgeArn,
 region
)
SELECT 
'{{ Name }}',
 '{{ BridgeArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.mediaconnect.bridge_sources (
 Name,
 BridgeArn,
 FlowSource,
 NetworkSource,
 region
)
SELECT 
 '{{ Name }}',
 '{{ BridgeArn }}',
 '{{ FlowSource }}',
 '{{ NetworkSource }}',
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
  - name: bridge_source
    props:
      - name: Name
        value: '{{ Name }}'
      - name: BridgeArn
        value: '{{ BridgeArn }}'
      - name: FlowSource
        value:
          FlowArn: '{{ FlowArn }}'
          FlowVpcInterfaceAttachment:
            VpcInterfaceName: '{{ VpcInterfaceName }}'
      - name: NetworkSource
        value:
          Protocol: '{{ Protocol }}'
          MulticastIp: '{{ MulticastIp }}'
          Port: '{{ Port }}'
          NetworkName: '{{ NetworkName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.mediaconnect.bridge_sources
WHERE data__Identifier = '<BridgeArn|Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>bridge_sources</code> resource, the following permissions are required:

### Create
```json
mediaconnect:AddBridgeSources,
mediaconnect:DescribeBridge
```

### Read
```json
mediaconnect:DescribeBridge
```

### Update
```json
mediaconnect:DescribeBridge,
mediaconnect:UpdateBridgeSource
```

### Delete
```json
mediaconnect:RemoveBridgeSource
```

