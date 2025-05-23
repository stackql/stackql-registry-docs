---
title: internet_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - internet_gateways
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

Creates, updates, deletes or gets an <code>internet_gateway</code> resource or lists <code>internet_gateways</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>internet_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Allocates an internet gateway for use with a VPC. After creating the Internet gateway, you then attach it to a VPC.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.internet_gateways" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="internet_gateway_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Any tags to assign to the internet gateway.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-internetgateway.html"><code>AWS::EC2::InternetGateway</code></a>.

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
    <td><CopyableCode code="region" /></td>
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
Gets all <code>internet_gateways</code> in a region.
```sql
SELECT
region,
internet_gateway_id,
tags
FROM aws.ec2.internet_gateways
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>internet_gateway</code>.
```sql
SELECT
region,
internet_gateway_id,
tags
FROM aws.ec2.internet_gateways
WHERE region = 'us-east-1' AND data__Identifier = '<InternetGatewayId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>internet_gateway</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.internet_gateways (
 Tags,
 region
)
SELECT 
'{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.internet_gateways (
 Tags,
 region
)
SELECT 
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
  - name: internet_gateway
    props:
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
DELETE FROM aws.ec2.internet_gateways
WHERE data__Identifier = '<InternetGatewayId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>internet_gateways</code> resource, the following permissions are required:

### Create
```json
ec2:CreateInternetGateway,
ec2:CreateTags,
ec2:DescribeInternetGateways
```

### Read
```json
ec2:DescribeInternetGateways
```

### Delete
```json
ec2:DeleteInternetGateway,
ec2:DescribeInternetGateways
```

### Update
```json
ec2:DeleteTags,
ec2:CreateTags,
ec2:DescribeInternetGateways
```

### List
```json
ec2:DescribeInternetGateways
```
