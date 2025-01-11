---
title: vpc_block_public_access_exclusions
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_block_public_access_exclusions
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

Creates, updates, deletes or gets a <code>vpc_block_public_access_exclusion</code> resource or lists <code>vpc_block_public_access_exclusions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_block_public_access_exclusions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::VPCBlockPublicAccessExclusion.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpc_block_public_access_exclusions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="exclusion_id" /></td><td><code>string</code></td><td>The ID of the exclusion</td></tr>
<tr><td><CopyableCode code="internet_gateway_exclusion_mode" /></td><td><code>string</code></td><td>The desired Block Public Access Exclusion Mode for a specific VPC/Subnet.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the vpc. Required only if you don't specify SubnetId.</td></tr>
<tr><td><CopyableCode code="subnet_id" /></td><td><code>string</code></td><td>The ID of the subnet. Required only if you don't specify VpcId</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcblockpublicaccessexclusion.html"><code>AWS::EC2::VPCBlockPublicAccessExclusion</code></a>.

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
    <td><CopyableCode code="InternetGatewayExclusionMode, region" /></td>
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
Gets all <code>vpc_block_public_access_exclusions</code> in a region.
```sql
SELECT
region,
exclusion_id,
internet_gateway_exclusion_mode,
vpc_id,
subnet_id,
tags
FROM aws.ec2.vpc_block_public_access_exclusions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>vpc_block_public_access_exclusion</code>.
```sql
SELECT
region,
exclusion_id,
internet_gateway_exclusion_mode,
vpc_id,
subnet_id,
tags
FROM aws.ec2.vpc_block_public_access_exclusions
WHERE region = 'us-east-1' AND data__Identifier = '<ExclusionId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vpc_block_public_access_exclusion</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.vpc_block_public_access_exclusions (
 InternetGatewayExclusionMode,
 region
)
SELECT 
'{{ InternetGatewayExclusionMode }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.vpc_block_public_access_exclusions (
 InternetGatewayExclusionMode,
 VpcId,
 SubnetId,
 Tags,
 region
)
SELECT 
 '{{ InternetGatewayExclusionMode }}',
 '{{ VpcId }}',
 '{{ SubnetId }}',
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
  - name: vpc_block_public_access_exclusion
    props:
      - name: InternetGatewayExclusionMode
        value: '{{ InternetGatewayExclusionMode }}'
      - name: VpcId
        value: '{{ VpcId }}'
      - name: SubnetId
        value: '{{ SubnetId }}'
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
DELETE FROM aws.ec2.vpc_block_public_access_exclusions
WHERE data__Identifier = '<ExclusionId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>vpc_block_public_access_exclusions</code> resource, the following permissions are required:

### Create
```json
ec2:DescribeVpcBlockPublicAccessExclusions,
ec2:CreateVpcBlockPublicAccessExclusion,
ec2:CreateTags
```

### Read
```json
ec2:DescribeVpcBlockPublicAccessExclusions
```

### Update
```json
ec2:DescribeVpcBlockPublicAccessExclusions,
ec2:ModifyVpcBlockPublicAccessExclusion,
ec2:CreateTags,
ec2:DeleteTags
```

### Delete
```json
ec2:DescribeVpcBlockPublicAccessExclusions,
ec2:DeleteVpcBlockPublicAccessExclusion
```

### List
```json
ec2:DescribeVpcBlockPublicAccessExclusions
```
