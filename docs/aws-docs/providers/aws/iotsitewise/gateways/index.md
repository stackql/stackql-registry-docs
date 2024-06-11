---
title: gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - gateways
  - iotsitewise
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

Creates, updates, deletes or gets a <code>gateway</code> resource or lists <code>gateways</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTSiteWise::Gateway</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotsitewise.gateways" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="gateway_name" /></td><td><code>string</code></td><td>A unique, friendly name for the gateway.</td></tr>
<tr><td><CopyableCode code="gateway_platform" /></td><td><code>object</code></td><td>The gateway's platform. You can only specify one platform in a gateway.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the gateway.</td></tr>
<tr><td><CopyableCode code="gateway_id" /></td><td><code>string</code></td><td>The ID of the gateway device.</td></tr>
<tr><td><CopyableCode code="gateway_capability_summaries" /></td><td><code>array</code></td><td>A list of gateway capability summaries that each contain a namespace and status.</td></tr>
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
    <td><CopyableCode code="GatewayName, GatewayPlatform, region" /></td>
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
List all <code>gateways</code> in a region.
```sql
SELECT
region,
gateway_id
FROM aws.iotsitewise.gateways
WHERE region = 'us-east-1';
```
Gets all properties from a <code>gateway</code>.
```sql
SELECT
region,
gateway_name,
gateway_platform,
tags,
gateway_id,
gateway_capability_summaries
FROM aws.iotsitewise.gateways
WHERE region = 'us-east-1' AND data__Identifier = '<GatewayId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>gateway</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iotsitewise.gateways (
 GatewayName,
 GatewayPlatform,
 region
)
SELECT 
'{{ GatewayName }}',
 '{{ GatewayPlatform }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iotsitewise.gateways (
 GatewayName,
 GatewayPlatform,
 Tags,
 GatewayCapabilitySummaries,
 region
)
SELECT 
 '{{ GatewayName }}',
 '{{ GatewayPlatform }}',
 '{{ Tags }}',
 '{{ GatewayCapabilitySummaries }}',
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
  - name: gateway
    props:
      - name: GatewayName
        value: '{{ GatewayName }}'
      - name: GatewayPlatform
        value:
          Greengrass:
            GroupArn: '{{ GroupArn }}'
          GreengrassV2:
            CoreDeviceThingName: '{{ CoreDeviceThingName }}'
          SiemensIE:
            IotCoreThingName: '{{ IotCoreThingName }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: GatewayCapabilitySummaries
        value:
          - CapabilityNamespace: '{{ CapabilityNamespace }}'
            CapabilityConfiguration: '{{ CapabilityConfiguration }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iotsitewise.gateways
WHERE data__Identifier = '<GatewayId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>gateways</code> resource, the following permissions are required:

### Create
```json
iotsitewise:CreateGateway,
iotsitewise:DescribeGateway,
iotsitewise:DescribeGatewayCapabilityConfiguration,
iotsitewise:UpdateGatewayCapabilityConfiguration,
iam:PassRole,
iam:GetRole,
greengrass:GetCoreDevice,
iotsitewise:ListTagsForResource,
iotsitewise:TagResource,
iot:DescribeThing
```

### Read
```json
iotsitewise:DescribeGateway,
iotsitewise:DescribeGatewayCapabilityConfiguration,
iotsitewise:ListTagsForResource
```

### Update
```json
iotsitewise:UpdateGateway,
iotsitewise:UpdateGatewayCapabilityConfiguration,
iotsitewise:TagResource,
iotsitewise:UntagResource,
iotsitewise:DescribeGateway,
iotsitewise:DescribeGatewayCapabilityConfiguration,
iotsitewise:ListTagsForResource
```

### Delete
```json
iotsitewise:DescribeGateway,
iotsitewise:DescribeGatewayCapabilityConfiguration,
iotsitewise:DeleteGateway
```

### List
```json
iotsitewise:ListGateways
```

