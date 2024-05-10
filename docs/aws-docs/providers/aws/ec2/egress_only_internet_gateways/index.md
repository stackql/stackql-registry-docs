---
title: egress_only_internet_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - egress_only_internet_gateways
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


Used to retrieve a list of <code>egress_only_internet_gateways</code> in a region or to create or delete a <code>egress_only_internet_gateways</code> resource, use <code>egress_only_internet_gateway</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>egress_only_internet_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::EgressOnlyInternetGateway</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.egress_only_internet_gateways" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Service Generated ID of the EgressOnlyInternetGateway</td></tr>
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
id
FROM aws.ec2.egress_only_internet_gateways
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>egress_only_internet_gateway</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- egress_only_internet_gateway.iql (required properties only)
INSERT INTO aws.ec2.egress_only_internet_gateways (
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
-- egress_only_internet_gateway.iql (all properties)
INSERT INTO aws.ec2.egress_only_internet_gateways (
 VpcId,
 region
)
SELECT 
 '{{ VpcId }}',
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
  - name: egress_only_internet_gateway
    props:
      - name: VpcId
        value: '{{ VpcId }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.egress_only_internet_gateways
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>egress_only_internet_gateways</code> resource, the following permissions are required:

### Create
```json
ec2:CreateEgressOnlyInternetGateway,
ec2:DescribeEgressOnlyInternetGateways
```

### Delete
```json
ec2:DeleteEgressOnlyInternetGateway,
ec2:DescribeEgressOnlyInternetGateways,
ec2:DescribeVpcs
```

### List
```json
ec2:DescribeEgressOnlyInternetGateways
```

