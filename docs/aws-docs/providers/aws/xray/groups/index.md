---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - xray
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


Used to retrieve a list of <code>groups</code> in a region or to create or delete a <code>groups</code> resource, use <code>group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This schema provides construct and validation rules for AWS-XRay Group resource parameters.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.xray.groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="group_arn" /></td><td><code>string</code></td><td>The ARN of the group that was generated on creation.</td></tr>
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
group_arn
FROM aws.xray.groups
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
 "GroupName": "{{ GroupName }}"
}
>>>
--required properties only
INSERT INTO aws.xray.groups (
 GroupName,
 region
)
SELECT 
{{ GroupName }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "FilterExpression": "{{ FilterExpression }}",
 "GroupName": "{{ GroupName }}",
 "InsightsConfiguration": {
  "InsightsEnabled": "{{ InsightsEnabled }}",
  "NotificationsEnabled": "{{ NotificationsEnabled }}"
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.xray.groups (
 FilterExpression,
 GroupName,
 InsightsConfiguration,
 Tags,
 region
)
SELECT 
 {{ FilterExpression }},
 {{ GroupName }},
 {{ InsightsConfiguration }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.xray.groups
WHERE data__Identifier = '<GroupARN>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>groups</code> resource, the following permissions are required:

### Create
```json
xray:CreateGroup,
xray:TagResource
```

### Delete
```json
xray:DeleteGroup
```

### List
```json
xray:GetGroups,
xray:ListTagsForResource
```

