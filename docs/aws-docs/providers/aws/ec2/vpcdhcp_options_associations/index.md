---
title: vpcdhcp_options_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - vpcdhcp_options_associations
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

Creates, updates, deletes or gets a <code>vpcdhcp_options_association</code> resource or lists <code>vpcdhcp_options_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpcdhcp_options_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Associates a set of DHCP options with a VPC, or associates no DHCP options with the VPC.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpcdhcp_options_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="dhcp_options_id" /></td><td><code>string</code></td><td>The ID of the DHCP options set, or default to associate no DHCP options with the VPC.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the VPC.</td></tr>
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
    <td><CopyableCode code="VpcId, DhcpOptionsId, region" /></td>
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
Gets all <code>vpcdhcp_options_associations</code> in a region.
```sql
SELECT
region,
dhcp_options_id,
vpc_id
FROM aws.ec2.vpcdhcp_options_associations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>vpcdhcp_options_association</code>.
```sql
SELECT
region,
dhcp_options_id,
vpc_id
FROM aws.ec2.vpcdhcp_options_associations
WHERE region = 'us-east-1' AND data__Identifier = '<DhcpOptionsId>|<VpcId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vpcdhcp_options_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.vpcdhcp_options_associations (
 DhcpOptionsId,
 VpcId,
 region
)
SELECT 
'{{ DhcpOptionsId }}',
 '{{ VpcId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.vpcdhcp_options_associations (
 DhcpOptionsId,
 VpcId,
 region
)
SELECT 
 '{{ DhcpOptionsId }}',
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
  - name: vpcdhcp_options_association
    props:
      - name: DhcpOptionsId
        value: '{{ DhcpOptionsId }}'
      - name: VpcId
        value: '{{ VpcId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.vpcdhcp_options_associations
WHERE data__Identifier = '<DhcpOptionsId|VpcId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>vpcdhcp_options_associations</code> resource, the following permissions are required:

### Create
```json
ec2:AssociateDhcpOptions
```

### Update
```json
ec2:AssociateDhcpOptions
```

### Delete
```json
ec2:AssociateDhcpOptions
```

### Read
```json
ec2:DescribeVpcs
```

### List
```json
ec2:DescribeVpcs
```

