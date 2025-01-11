---
title: ipams
hide_title: false
hide_table_of_contents: false
keywords:
  - ipams
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

Creates, updates, deletes or gets an <code>ipam</code> resource or lists <code>ipams</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema of AWS::EC2::IPAM Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.ipams" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="ipam_id" /></td><td><code>string</code></td><td>Id of the IPAM.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IPAM.</td></tr>
<tr><td><CopyableCode code="default_resource_discovery_id" /></td><td><code>string</code></td><td>The Id of the default resource discovery, created with this IPAM.</td></tr>
<tr><td><CopyableCode code="default_resource_discovery_association_id" /></td><td><code>string</code></td><td>The Id of the default association to the default resource discovery, created with this IPAM.</td></tr>
<tr><td><CopyableCode code="resource_discovery_association_count" /></td><td><code>integer</code></td><td>The count of resource discoveries associated with this IPAM.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="public_default_scope_id" /></td><td><code>string</code></td><td>The Id of the default scope for publicly routable IP space, created with this IPAM.</td></tr>
<tr><td><CopyableCode code="private_default_scope_id" /></td><td><code>string</code></td><td>The Id of the default scope for publicly routable IP space, created with this IPAM.</td></tr>
<tr><td><CopyableCode code="scope_count" /></td><td><code>integer</code></td><td>The number of scopes that currently exist in this IPAM.</td></tr>
<tr><td><CopyableCode code="operating_regions" /></td><td><code>array</code></td><td>The regions IPAM is enabled for. Allows pools to be created in these regions, as well as enabling monitoring</td></tr>
<tr><td><CopyableCode code="tier" /></td><td><code>string</code></td><td>The tier of the IPAM.</td></tr>
<tr><td><CopyableCode code="enable_private_gua" /></td><td><code>boolean</code></td><td>Enable provisioning of GUA space in private pools.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipam.html"><code>AWS::EC2::IPAM</code></a>.

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
    <td><CopyableCode code=", region" /></td>
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
Gets all <code>ipams</code> in a region.
```sql
SELECT
region,
ipam_id,
arn,
default_resource_discovery_id,
default_resource_discovery_association_id,
resource_discovery_association_count,
description,
public_default_scope_id,
private_default_scope_id,
scope_count,
operating_regions,
tier,
enable_private_gua,
tags
FROM aws.ec2.ipams
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>ipam</code>.
```sql
SELECT
region,
ipam_id,
arn,
default_resource_discovery_id,
default_resource_discovery_association_id,
resource_discovery_association_count,
description,
public_default_scope_id,
private_default_scope_id,
scope_count,
operating_regions,
tier,
enable_private_gua,
tags
FROM aws.ec2.ipams
WHERE region = 'us-east-1' AND data__Identifier = '<IpamId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ipam</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.ipams (
 ,
 region
)
SELECT 
'{{  }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.ipams (
 Description,
 OperatingRegions,
 Tier,
 EnablePrivateGua,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ OperatingRegions }}',
 '{{ Tier }}',
 '{{ EnablePrivateGua }}',
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
  - name: ipam
    props:
      - name: Description
        value: '{{ Description }}'
      - name: OperatingRegions
        value:
          - RegionName: '{{ RegionName }}'
      - name: Tier
        value: '{{ Tier }}'
      - name: EnablePrivateGua
        value: '{{ EnablePrivateGua }}'
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
DELETE FROM aws.ec2.ipams
WHERE data__Identifier = '<IpamId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>ipams</code> resource, the following permissions are required:

### Create
```json
ec2:CreateIpam,
iam:CreateServiceLinkedRole,
ec2:CreateTags,
ec2:DescribeIpams
```

### Read
```json
ec2:DescribeIpams
```

### Update
```json
ec2:ModifyIpam,
ec2:CreateTags,
ec2:DeleteTags,
ec2:DescribeIpams
```

### Delete
```json
ec2:DeleteIpam,
ec2:DeleteTags,
ec2:DescribeIpams
```

### List
```json
ec2:DescribeIpams
```
