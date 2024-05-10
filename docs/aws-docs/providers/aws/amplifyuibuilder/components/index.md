---
title: components
hide_title: false
hide_table_of_contents: false
keywords:
  - components
  - amplifyuibuilder
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


Used to retrieve a list of <code>components</code> in a region or to create or delete a <code>components</code> resource, use <code>component</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>components</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::AmplifyUIBuilder::Component Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.amplifyuibuilder.components" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="app_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="environment_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
app_id,
environment_name,
id
FROM aws.amplifyuibuilder.components
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
 "AppId": "{{ AppId }}",
 "BindingProperties": {},
 "Children": [
  {
   "ComponentType": "{{ ComponentType }}",
   "Name": "{{ Name }}",
   "Properties": {},
   "Children": [
    null
   ],
   "Events": {},
   "SourceId": "{{ SourceId }}"
  }
 ],
 "CollectionProperties": {},
 "ComponentType": "{{ ComponentType }}",
 "EnvironmentName": "{{ EnvironmentName }}",
 "Events": null,
 "Name": "{{ Name }}",
 "Overrides": {},
 "Properties": null,
 "SchemaVersion": "{{ SchemaVersion }}",
 "SourceId": "{{ SourceId }}",
 "Tags": {},
 "Variants": [
  {
   "VariantValues": {},
   "Overrides": null
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.amplifyuibuilder.components (
 AppId,
 BindingProperties,
 Children,
 CollectionProperties,
 ComponentType,
 EnvironmentName,
 Events,
 Name,
 Overrides,
 Properties,
 SchemaVersion,
 SourceId,
 Tags,
 Variants,
 region
)
SELECT 
{{ AppId }},
 {{ BindingProperties }},
 {{ Children }},
 {{ CollectionProperties }},
 {{ ComponentType }},
 {{ EnvironmentName }},
 {{ Events }},
 {{ Name }},
 {{ Overrides }},
 {{ Properties }},
 {{ SchemaVersion }},
 {{ SourceId }},
 {{ Tags }},
 {{ Variants }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AppId": "{{ AppId }}",
 "BindingProperties": {},
 "Children": [
  {
   "ComponentType": "{{ ComponentType }}",
   "Name": "{{ Name }}",
   "Properties": {},
   "Children": [
    null
   ],
   "Events": {},
   "SourceId": "{{ SourceId }}"
  }
 ],
 "CollectionProperties": {},
 "ComponentType": "{{ ComponentType }}",
 "EnvironmentName": "{{ EnvironmentName }}",
 "Events": null,
 "Name": "{{ Name }}",
 "Overrides": {},
 "Properties": null,
 "SchemaVersion": "{{ SchemaVersion }}",
 "SourceId": "{{ SourceId }}",
 "Tags": {},
 "Variants": [
  {
   "VariantValues": {},
   "Overrides": null
  }
 ]
}
>>>
--all properties
INSERT INTO aws.amplifyuibuilder.components (
 AppId,
 BindingProperties,
 Children,
 CollectionProperties,
 ComponentType,
 EnvironmentName,
 Events,
 Name,
 Overrides,
 Properties,
 SchemaVersion,
 SourceId,
 Tags,
 Variants,
 region
)
SELECT 
 {{ AppId }},
 {{ BindingProperties }},
 {{ Children }},
 {{ CollectionProperties }},
 {{ ComponentType }},
 {{ EnvironmentName }},
 {{ Events }},
 {{ Name }},
 {{ Overrides }},
 {{ Properties }},
 {{ SchemaVersion }},
 {{ SourceId }},
 {{ Tags }},
 {{ Variants }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.amplifyuibuilder.components
WHERE data__Identifier = '<AppId|EnvironmentName|Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>components</code> resource, the following permissions are required:

### Create
```json
amplify:GetApp,
amplifyuibuilder:CreateComponent,
amplifyuibuilder:GetComponent,
amplifyuibuilder:TagResource
```

### Delete
```json
amplify:GetApp,
amplifyuibuilder:DeleteComponent,
amplifyuibuilder:GetComponent,
amplifyuibuilder:UntagResource
```

### List
```json
amplify:GetApp,
amplifyuibuilder:ListComponents
```

