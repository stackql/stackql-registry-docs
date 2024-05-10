---
title: contact_flows
hide_title: false
hide_table_of_contents: false
keywords:
  - contact_flows
  - connect
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


Used to retrieve a list of <code>contact_flows</code> in a region or to create or delete a <code>contact_flows</code> resource, use <code>contact_flow</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contact_flows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::ContactFlow</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.contact_flows" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="contact_flow_arn" /></td><td><code>string</code></td><td>The identifier of the contact flow (ARN).</td></tr>
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
contact_flow_arn
FROM aws.connect.contact_flows
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
 "InstanceArn": "{{ InstanceArn }}",
 "Name": "{{ Name }}",
 "Content": "{{ Content }}",
 "Type": "{{ Type }}"
}
>>>
--required properties only
INSERT INTO aws.connect.contact_flows (
 InstanceArn,
 Name,
 Content,
 Type,
 region
)
SELECT 
{{ InstanceArn }},
 {{ Name }},
 {{ Content }},
 {{ Type }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "InstanceArn": "{{ InstanceArn }}",
 "Name": "{{ Name }}",
 "Content": "{{ Content }}",
 "Description": "{{ Description }}",
 "State": "{{ State }}",
 "Type": "{{ Type }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.connect.contact_flows (
 InstanceArn,
 Name,
 Content,
 Description,
 State,
 Type,
 Tags,
 region
)
SELECT 
 {{ InstanceArn }},
 {{ Name }},
 {{ Content }},
 {{ Description }},
 {{ State }},
 {{ Type }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.connect.contact_flows
WHERE data__Identifier = '<ContactFlowArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>contact_flows</code> resource, the following permissions are required:

### Create
```json
connect:CreateContactFlow,
connect:TagResource
```

### Delete
```json
connect:DeleteContactFlow,
connect:UntagResource
```

### List
```json
connect:ListContactFlows
```

