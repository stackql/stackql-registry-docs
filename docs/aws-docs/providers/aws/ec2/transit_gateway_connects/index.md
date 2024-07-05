---
title: transit_gateway_connects
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_connects
  - ec2
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

Creates, updates, deletes or gets a <code>transit_gateway_connect</code> resource or lists <code>transit_gateway_connects</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_connects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::TransitGatewayConnect type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.transit_gateway_connects" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="transit_gateway_attachment_id" /></td><td><code>string</code></td><td>The ID of the Connect attachment.</td></tr>
<tr><td><CopyableCode code="transport_transit_gateway_attachment_id" /></td><td><code>string</code></td><td>The ID of the attachment from which the Connect attachment was created.</td></tr>
<tr><td><CopyableCode code="transit_gateway_id" /></td><td><code>string</code></td><td>The ID of the transit gateway.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the attachment.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The creation time.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags for the attachment.</td></tr>
<tr><td><CopyableCode code="options" /></td><td><code>object</code></td><td>The Connect attachment options.</td></tr>
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
    <td><CopyableCode code="TransportTransitGatewayAttachmentId, Options, region" /></td>
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
Gets all <code>transit_gateway_connects</code> in a region.
```sql
SELECT
region,
transit_gateway_attachment_id,
transport_transit_gateway_attachment_id,
transit_gateway_id,
state,
creation_time,
tags,
options
FROM aws.ec2.transit_gateway_connects
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>transit_gateway_connect</code>.
```sql
SELECT
region,
transit_gateway_attachment_id,
transport_transit_gateway_attachment_id,
transit_gateway_id,
state,
creation_time,
tags,
options
FROM aws.ec2.transit_gateway_connects
WHERE region = 'us-east-1' AND data__Identifier = '<TransitGatewayAttachmentId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>transit_gateway_connect</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.transit_gateway_connects (
 TransportTransitGatewayAttachmentId,
 Options,
 region
)
SELECT 
'{{ TransportTransitGatewayAttachmentId }}',
 '{{ Options }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.transit_gateway_connects (
 TransportTransitGatewayAttachmentId,
 Tags,
 Options,
 region
)
SELECT 
 '{{ TransportTransitGatewayAttachmentId }}',
 '{{ Tags }}',
 '{{ Options }}',
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
  - name: transit_gateway_connect
    props:
      - name: TransportTransitGatewayAttachmentId
        value: '{{ TransportTransitGatewayAttachmentId }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Options
        value:
          Protocol: '{{ Protocol }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.transit_gateway_connects
WHERE data__Identifier = '<TransitGatewayAttachmentId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>transit_gateway_connects</code> resource, the following permissions are required:

### Create
```json
ec2:CreateTransitGatewayConnect,
ec2:DescribeTransitGatewayConnects,
ec2:CreateTags
```

### Read
```json
ec2:DescribeTransitGatewayConnects
```

### Update
```json
ec2:DescribeTransitGatewayConnects,
ec2:DeleteTags,
ec2:CreateTags
```

### Delete
```json
ec2:DeleteTransitGatewayConnect,
ec2:DescribeTransitGatewayConnects,
ec2:DeleteTags
```

### List
```json
ec2:DescribeTransitGatewayConnects
```

