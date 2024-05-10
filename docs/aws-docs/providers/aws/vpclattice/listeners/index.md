---
title: listeners
hide_title: false
hide_table_of_contents: false
keywords:
  - listeners
  - vpclattice
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
<tr><td><b>Description</b></td><td>Creates a listener for a service. Before you start using your Amazon VPC Lattice service, you must add one or more listeners. A listener is a process that checks for connection requests to your services.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.vpclattice.listeners" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
arn
FROM aws.vpclattice.listeners
WHERE region = 'us-east-1';
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
 "DefaultAction": {
  "Forward": {
   "TargetGroups": [
    {
     "TargetGroupIdentifier": "{{ TargetGroupIdentifier }}",
     "Weight": "{{ Weight }}"
    }
   ]
  },
  "FixedResponse": {
   "StatusCode": "{{ StatusCode }}"
  }
 },
 "Protocol": "{{ Protocol }}"
}
>>>
--required properties only
INSERT INTO aws.vpclattice.listeners (
 DefaultAction,
 Protocol,
 region
)
SELECT 
{{ .DefaultAction }},
 {{ .Protocol }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "DefaultAction": {
  "Forward": {
   "TargetGroups": [
    {
     "TargetGroupIdentifier": "{{ TargetGroupIdentifier }}",
     "Weight": "{{ Weight }}"
    }
   ]
  },
  "FixedResponse": {
   "StatusCode": "{{ StatusCode }}"
  }
 },
 "Name": "{{ Name }}",
 "Port": "{{ Port }}",
 "Protocol": "{{ Protocol }}",
 "ServiceIdentifier": "{{ ServiceIdentifier }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.vpclattice.listeners (
 DefaultAction,
 Name,
 Port,
 Protocol,
 ServiceIdentifier,
 Tags,
 region
)
SELECT 
 {{ .DefaultAction }},
 {{ .Name }},
 {{ .Port }},
 {{ .Protocol }},
 {{ .ServiceIdentifier }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.vpclattice.listeners
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>listeners</code> resource, the following permissions are required:

### Create
```json
vpc-lattice:CreateListener,
vpc-lattice:TagResource,
vpc-lattice:GetListener,
vpc-lattice:ListTagsForResource
```

### Delete
```json
vpc-lattice:DeleteListener
```

### List
```json
vpc-lattice:ListListeners
```

