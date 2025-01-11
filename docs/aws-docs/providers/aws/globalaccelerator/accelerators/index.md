---
title: accelerators
hide_title: false
hide_table_of_contents: false
keywords:
  - accelerators
  - globalaccelerator
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

Creates, updates, deletes or gets an <code>accelerator</code> resource or lists <code>accelerators</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accelerators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::GlobalAccelerator::Accelerator</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.globalaccelerator.accelerators" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of accelerator.</td></tr>
<tr><td><CopyableCode code="ip_address_type" /></td><td><code>string</code></td><td>IP Address type.</td></tr>
<tr><td><CopyableCode code="ip_addresses" /></td><td><code>array</code></td><td>The IP addresses from BYOIP Prefix pool.</td></tr>
<tr><td><CopyableCode code="enabled" /></td><td><code>boolean</code></td><td>Indicates whether an accelerator is enabled. The value is true or false.</td></tr>
<tr><td><CopyableCode code="dns_name" /></td><td><code>string</code></td><td>The Domain Name System (DNS) name that Global Accelerator creates that points to your accelerator's static IPv4 addresses.</td></tr>
<tr><td><CopyableCode code="ipv4_addresses" /></td><td><code>array</code></td><td>The IPv4 addresses assigned to the accelerator.</td></tr>
<tr><td><CopyableCode code="ipv6_addresses" /></td><td><code>array</code></td><td>The IPv6 addresses assigned if the accelerator is dualstack</td></tr>
<tr><td><CopyableCode code="dual_stack_dns_name" /></td><td><code>string</code></td><td>The Domain Name System (DNS) name that Global Accelerator creates that points to your accelerator's static IPv4 and IPv6 addresses.</td></tr>
<tr><td><CopyableCode code="accelerator_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the accelerator.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html"><code>AWS::GlobalAccelerator::Accelerator</code></a>.

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
    <td><CopyableCode code="Name, region" /></td>
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
Gets all <code>accelerators</code> in a region.
```sql
SELECT
region,
name,
ip_address_type,
ip_addresses,
enabled,
dns_name,
ipv4_addresses,
ipv6_addresses,
dual_stack_dns_name,
accelerator_arn,
tags
FROM aws.globalaccelerator.accelerators
;
```
Gets all properties from an individual <code>accelerator</code>.
```sql
SELECT
region,
name,
ip_address_type,
ip_addresses,
enabled,
dns_name,
ipv4_addresses,
ipv6_addresses,
dual_stack_dns_name,
accelerator_arn,
tags
FROM aws.globalaccelerator.accelerators
WHERE data__Identifier = '<AcceleratorArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>accelerator</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.globalaccelerator.accelerators (
 Name,
 region
)
SELECT 
'{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.globalaccelerator.accelerators (
 Name,
 IpAddressType,
 IpAddresses,
 Enabled,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ IpAddressType }}',
 '{{ IpAddresses }}',
 '{{ Enabled }}',
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
  - name: accelerator
    props:
      - name: Name
        value: '{{ Name }}'
      - name: IpAddressType
        value: '{{ IpAddressType }}'
      - name: IpAddresses
        value:
          - '{{ IpAddresses[0] }}'
      - name: Enabled
        value: '{{ Enabled }}'
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
DELETE FROM aws.globalaccelerator.accelerators
WHERE data__Identifier = '<AcceleratorArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>accelerators</code> resource, the following permissions are required:

### Create
```json
globalaccelerator:CreateAccelerator,
globalaccelerator:DescribeAccelerator,
globalaccelerator:TagResource
```

### Read
```json
globalaccelerator:DescribeAccelerator
```

### Update
```json
globalaccelerator:UpdateAccelerator,
globalaccelerator:TagResource,
globalaccelerator:UntagResource,
globalaccelerator:DescribeAccelerator
```

### Delete
```json
globalaccelerator:UpdateAccelerator,
globalaccelerator:DeleteAccelerator,
globalaccelerator:DescribeAccelerator
```

### List
```json
globalaccelerator:ListAccelerators
```
