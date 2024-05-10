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


Used to retrieve a list of <code>virtualmfa_devices</code> in a region or to create or delete a <code>virtualmfa_devices</code> resource, use <code>virtualmfa_device</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtualmfa_devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IAM::VirtualMFADevice</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.virtualmfa_devices" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="serial_number" /></td><td><code>string</code></td><td></td></tr>
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
serial_number
FROM aws.iam.virtualmfa_devices
;
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "Users": [
  "{{ Users[0] }}"
 ]
}
>>>
--required properties only
INSERT INTO aws.iam.virtualmfa_devices (
 Users,
 region
)
SELECT 
{{ Users }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "VirtualMfaDeviceName": "{{ VirtualMfaDeviceName }}",
 "Path": "{{ Path }}",
 "Users": [
  "{{ Users[0] }}"
 ],
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.iam.virtualmfa_devices (
 VirtualMfaDeviceName,
 Path,
 Users,
 Tags,
 region
)
SELECT 
 {{ VirtualMfaDeviceName }},
 {{ Path }},
 {{ Users }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
iam:DeleteVirtualMFADevice,
iam:DeactivateMFADevice
```

### List
```json
iam:ListVirtualMFADevices
```

