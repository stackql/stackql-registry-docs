---
title: listeners
hide_title: false
hide_table_of_contents: false
keywords:
  - listeners
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


Used to retrieve a list of <code>listeners</code> in a region or to create or delete a <code>listeners</code> resource, use <code>listener</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>listeners</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::GlobalAccelerator::Listener</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.globalaccelerator.listeners" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="listener_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the listener.</td></tr>
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
listener_arn
FROM aws.globalaccelerator.listeners
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
 "AcceleratorArn": "{{ AcceleratorArn }}",
 "PortRanges": [
  {
   "FromPort": "{{ FromPort }}",
   "ToPort": null
  }
 ],
 "Protocol": "{{ Protocol }}"
}
>>>
--required properties only
INSERT INTO aws.globalaccelerator.listeners (
 AcceleratorArn,
 PortRanges,
 Protocol,
 region
)
SELECT 
{{ AcceleratorArn }},
 {{ PortRanges }},
 {{ Protocol }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AcceleratorArn": "{{ AcceleratorArn }}",
 "PortRanges": [
  {
   "FromPort": "{{ FromPort }}",
   "ToPort": null
  }
 ],
 "Protocol": "{{ Protocol }}",
 "ClientAffinity": "{{ ClientAffinity }}"
}
>>>
--all properties
INSERT INTO aws.globalaccelerator.listeners (
 AcceleratorArn,
 PortRanges,
 Protocol,
 ClientAffinity,
 region
)
SELECT 
 {{ AcceleratorArn }},
 {{ PortRanges }},
 {{ Protocol }},
 {{ ClientAffinity }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.globalaccelerator.listeners
WHERE data__Identifier = '<ListenerArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>listeners</code> resource, the following permissions are required:

### Create
```json
globalaccelerator:CreateListener,
globalaccelerator:DescribeListener,
globalaccelerator:DescribeAccelerator
```

### Delete
```json
globalaccelerator:DescribeListener,
globalaccelerator:DeleteListener,
globalaccelerator:DescribeAccelerator
```

### List
```json
globalaccelerator:ListListeners
```

