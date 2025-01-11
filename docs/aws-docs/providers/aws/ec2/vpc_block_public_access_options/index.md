---
title: vpc_block_public_access_options
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_block_public_access_options
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

Creates, updates, deletes or gets a <code>vpc_block_public_access_option</code> resource or lists <code>vpc_block_public_access_options</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_block_public_access_options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::VPCBlockPublicAccessOptions</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpc_block_public_access_options" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="internet_gateway_block_mode" /></td><td><code>string</code></td><td>The desired Block Public Access mode for Internet Gateways in your account. We do not allow to create in a off mode as this is the default value</td></tr>
<tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td>The identifier for the specified AWS account.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcblockpublicaccessoption.html"><code>AWS::EC2::VPCBlockPublicAccessOptions</code></a>.

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
    <td><CopyableCode code="InternetGatewayBlockMode, region" /></td>
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

Gets all properties from an individual <code>vpc_block_public_access_option</code>.
```sql
SELECT
region,
internet_gateway_block_mode,
account_id
FROM aws.ec2.vpc_block_public_access_options
WHERE region = 'us-east-1' AND data__Identifier = '<AccountId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vpc_block_public_access_option</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.vpc_block_public_access_options (
 InternetGatewayBlockMode,
 region
)
SELECT 
'{{ InternetGatewayBlockMode }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.vpc_block_public_access_options (
 InternetGatewayBlockMode,
 region
)
SELECT 
 '{{ InternetGatewayBlockMode }}',
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
  - name: vpc_block_public_access_option
    props:
      - name: InternetGatewayBlockMode
        value: '{{ InternetGatewayBlockMode }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.vpc_block_public_access_options
WHERE data__Identifier = '<AccountId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>vpc_block_public_access_options</code> resource, the following permissions are required:

### Create
```json
ec2:DescribeVpcBlockPublicAccessOptions,
ec2:ModifyVpcBlockPublicAccessOptions
```

### Read
```json
ec2:DescribeVpcBlockPublicAccessOptions
```

### Update
```json
ec2:DescribeVpcBlockPublicAccessOptions,
ec2:ModifyVpcBlockPublicAccessOptions
```

### Delete
```json
ec2:DescribeVpcBlockPublicAccessOptions,
ec2:ModifyVpcBlockPublicAccessOptions
```
