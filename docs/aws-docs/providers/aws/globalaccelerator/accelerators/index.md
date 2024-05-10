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


Used to retrieve a list of <code>accelerators</code> in a region or to create or delete a <code>accelerators</code> resource, use <code>accelerator</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accelerators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::GlobalAccelerator::Accelerator</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.globalaccelerator.accelerators" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="accelerator_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the accelerator.</td></tr>
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
accelerator_arn
FROM aws.globalaccelerator.accelerators
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
 "Name": "{{ Name }}"
}
>>>
--required properties only
INSERT INTO aws.globalaccelerator.accelerators (
 Name,
 region
)
SELECT 
{{ .Name }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "IpAddressType": "{{ IpAddressType }}",
 "IpAddresses": [
  "{{ IpAddresses[0] }}"
 ],
 "Enabled": "{{ Enabled }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.globalaccelerator.accelerators (
 Name,
 IpAddressType,
 IpAddresses,
 Enabled,
 Tags,
 region
)
SELECT 
 {{ .Name }},
 {{ .IpAddressType }},
 {{ .IpAddresses }},
 {{ .Enabled }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

