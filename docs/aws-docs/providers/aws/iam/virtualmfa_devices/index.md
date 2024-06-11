---
title: virtualmfa_devices
hide_title: false
hide_table_of_contents: false
keywords:
  - virtualmfa_devices
  - iam
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

Creates, updates, deletes or gets a <code>virtualmfa_device</code> resource or lists <code>virtualmfa_devices</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtualmfa_devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IAM::VirtualMFADevice</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.virtualmfa_devices" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="virtual_mfa_device_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="path" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="serial_number" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="users" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="Users, region" /></td>
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
List all <code>virtualmfa_devices</code> in a region.
```sql
SELECT
region,
serial_number
FROM aws.iam.virtualmfa_devices
;
```
Gets all properties from a <code>virtualmfa_device</code>.
```sql
SELECT
region,
virtual_mfa_device_name,
path,
serial_number,
users,
tags
FROM aws.iam.virtualmfa_devices
WHERE data__Identifier = '<SerialNumber>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtualmfa_device</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iam.virtualmfa_devices (
 Users,
 region
)
SELECT 
'{{ Users }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iam.virtualmfa_devices (
 VirtualMfaDeviceName,
 Path,
 Users,
 Tags,
 region
)
SELECT 
 '{{ VirtualMfaDeviceName }}',
 '{{ Path }}',
 '{{ Users }}',
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
  - name: virtualmfa_device
    props:
      - name: VirtualMfaDeviceName
        value: '{{ VirtualMfaDeviceName }}'
      - name: Path
        value: '{{ Path }}'
      - name: Users
        value:
          - '{{ Users[0] }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iam.virtualmfa_devices
WHERE data__Identifier = '<SerialNumber>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>virtualmfa_devices</code> resource, the following permissions are required:

### Create
```json
iam:CreateVirtualMFADevice,
iam:EnableMFADevice,
iam:ListVirtualMFADevices
```

### Read
```json
iam:ListVirtualMFADevices
```

### Update
```json
iam:TagMFADevice,
iam:UntagMFADevice
```

### Delete
```json
iam:DeleteVirtualMFADevice,
iam:DeactivateMFADevice
```

### List
```json
iam:ListVirtualMFADevices
```

