---
title: gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - gateways
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

Creates, updates, deletes or gets a <code>gateway</code> resource or lists <code>gateways</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaConnect::Gateway</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediaconnect.gateways" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the gateway. This name can not be modified after the gateway is created.</td></tr>
<tr><td><CopyableCode code="gateway_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the gateway.</td></tr>
<tr><td><CopyableCode code="gateway_state" /></td><td><code>string</code></td><td>The current status of the gateway.</td></tr>
<tr><td><CopyableCode code="egress_cidr_blocks" /></td><td><code>array</code></td><td>The range of IP addresses that contribute content or initiate output requests for flows communicating with this gateway. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.</td></tr>
<tr><td><CopyableCode code="networks" /></td><td><code>array</code></td><td>The list of networks in the gateway.</td></tr>
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
    <td><CopyableCode code="Name, EgressCidrBlocks, Networks, region" /></td>
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
gateway_arn
FROM aws.mediaconnect.gateways
WHERE region = 'us-east-1';
```
Gets all properties from a <code>gateway</code>.
```sql
SELECT
region,
name,
gateway_arn,
gateway_state,
egress_cidr_blocks,
networks
FROM aws.mediaconnect.gateways
WHERE region = 'us-east-1' AND data__Identifier = '<GatewayArn>';
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
INSERT INTO aws.mediaconnect.gateways (
 Name,
 EgressCidrBlocks,
 Networks,
 region
)
SELECT 
'{{ Name }}',
 '{{ EgressCidrBlocks }}',
 '{{ Networks }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.mediaconnect.gateways (
 Name,
 EgressCidrBlocks,
 Networks,
 region
)
SELECT 
 '{{ Name }}',
 '{{ EgressCidrBlocks }}',
 '{{ Networks }}',
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
      - name: Name
        value: '{{ Name }}'
      - name: EgressCidrBlocks
        value:
          - '{{ EgressCidrBlocks[0] }}'
      - name: Networks
        value:
          - Name: '{{ Name }}'
            CidrBlock: '{{ CidrBlock }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.mediaconnect.gateways
WHERE data__Identifier = '<GatewayArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>gateways</code> resource, the following permissions are required:

### Create
```json
iam:CreateServiceLinkedRole,
mediaconnect:CreateGateway,
mediaconnect:DescribeGateway
```

### Read
```json
mediaconnect:DescribeGateway
```

### Delete
```json
iam:CreateServiceLinkedRole,
mediaconnect:DescribeGateway,
mediaconnect:DeleteGateway
```

### List
```json
mediaconnect:ListGateways
```

