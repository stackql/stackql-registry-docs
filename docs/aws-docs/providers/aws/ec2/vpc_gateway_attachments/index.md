---
title: vpc_gateway_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_gateway_attachments
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

Creates, updates, deletes or gets a <code>vpc_gateway_attachment</code> resource or lists <code>vpc_gateway_attachments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_gateway_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::VPCGatewayAttachment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpc_gateway_attachments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="attachment_type" /></td><td><code>string</code></td><td>Used to identify if this resource is an Internet Gateway or Vpn Gateway Attachment</td></tr>
<tr><td><CopyableCode code="internet_gateway_id" /></td><td><code>string</code></td><td>The ID of the internet gateway. You must specify either InternetGatewayId or VpnGatewayId, but not both.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the VPC.</td></tr>
<tr><td><CopyableCode code="vpn_gateway_id" /></td><td><code>string</code></td><td>The ID of the virtual private gateway. You must specify either InternetGatewayId or VpnGatewayId, but not both.</td></tr>
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
    <td><CopyableCode code="VpcId, region" /></td>
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
List all <code>vpc_gateway_attachments</code> in a region.
```sql
SELECT
region,
attachment_type,
vpc_id
FROM aws.ec2.vpc_gateway_attachments
WHERE region = 'us-east-1';
```
Gets all properties from a <code>vpc_gateway_attachment</code>.
```sql
SELECT
region,
attachment_type,
internet_gateway_id,
vpc_id,
vpn_gateway_id
FROM aws.ec2.vpc_gateway_attachments
WHERE region = 'us-east-1' AND data__Identifier = '<AttachmentType>|<VpcId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vpc_gateway_attachment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.vpc_gateway_attachments (
 VpcId,
 region
)
SELECT 
'{{ VpcId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.vpc_gateway_attachments (
 InternetGatewayId,
 VpcId,
 VpnGatewayId,
 region
)
SELECT 
 '{{ InternetGatewayId }}',
 '{{ VpcId }}',
 '{{ VpnGatewayId }}',
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
  - name: vpc_gateway_attachment
    props:
      - name: InternetGatewayId
        value: '{{ InternetGatewayId }}'
      - name: VpcId
        value: '{{ VpcId }}'
      - name: VpnGatewayId
        value: '{{ VpnGatewayId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.vpc_gateway_attachments
WHERE data__Identifier = '<AttachmentType|VpcId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>vpc_gateway_attachments</code> resource, the following permissions are required:

### Create
```json
ec2:AttachInternetGateway,
ec2:AttachVpnGateway,
ec2:DescribeInternetGateways,
ec2:DescribeVpnGateways
```

### Read
```json
ec2:DescribeInternetGateways,
ec2:DescribeVpnGateways
```

### Update
```json
ec2:AttachInternetGateway,
ec2:AttachVpnGateway,
ec2:DetachInternetGateway,
ec2:DetachVpnGateway,
ec2:DescribeInternetGateways,
ec2:DescribeVpnGateways
```

### Delete
```json
ec2:DetachInternetGateway,
ec2:DetachVpnGateway,
ec2:DescribeInternetGateways,
ec2:DescribeVpnGateways
```

### List
```json
ec2:DescribeInternetGateways,
ec2:DescribeVpnGateways
```

