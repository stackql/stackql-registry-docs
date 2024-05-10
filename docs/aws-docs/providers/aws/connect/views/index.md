---
title: views
hide_title: false
hide_table_of_contents: false
keywords:
  - views
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


Used to retrieve a list of <code>views</code> in a region or to create or delete a <code>views</code> resource, use <code>view</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.views" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="view_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the view.</td></tr>
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
view_arn
FROM aws.connect.views
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
 "Template": {},
 "Actions": [
  "{{ Actions[0] }}"
 ]
}
>>>
--required properties only
INSERT INTO aws.connect.views (
 InstanceArn,
 Name,
 Template,
 Actions,
 region
)
SELECT 
{{ InstanceArn }},
 {{ Name }},
 {{ Template }},
 {{ Actions }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "InstanceArn": "{{ InstanceArn }}",
 "Name": "{{ Name }}",
 "Description": "{{ Description }}",
 "Template": {},
 "Actions": [
  "{{ Actions[0] }}"
 ],
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.connect.views (
 InstanceArn,
 Name,
 Description,
 Template,
 Actions,
 Tags,
 region
)
SELECT 
 {{ InstanceArn }},
 {{ Name }},
 {{ Description }},
 {{ Template }},
 {{ Actions }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.connect.views
WHERE data__Identifier = '<ViewArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>views</code> resource, the following permissions are required:

### Create
```json
connect:CreateView,
connect:TagResource
```

### Delete
```json
connect:DeleteView,
connect:UntagResource
```

### List
```json
connect:ListViews
```

