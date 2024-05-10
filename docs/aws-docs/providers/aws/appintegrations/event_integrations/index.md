---
title: event_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - event_integrations
  - appintegrations
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


Used to retrieve a list of <code>event_integrations</code> in a region or to create or delete a <code>event_integrations</code> resource, use <code>event_integration</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppIntegrations::EventIntegration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appintegrations.event_integrations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the event integration.</td></tr>
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
name
FROM aws.appintegrations.event_integrations
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
 "Name": "{{ Name }}",
 "EventBridgeBus": "{{ EventBridgeBus }}",
 "EventFilter": {
  "Source": "{{ Source }}"
 }
}
>>>
--required properties only
INSERT INTO aws.appintegrations.event_integrations (
 Name,
 EventBridgeBus,
 EventFilter,
 region
)
SELECT 
{{ .Name }},
 {{ .EventBridgeBus }},
 {{ .EventFilter }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Description": "{{ Description }}",
 "Name": "{{ Name }}",
 "EventBridgeBus": "{{ EventBridgeBus }}",
 "EventFilter": {
  "Source": "{{ Source }}"
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
INSERT INTO aws.appintegrations.event_integrations (
 Description,
 Name,
 EventBridgeBus,
 EventFilter,
 Tags,
 region
)
SELECT 
 {{ .Description }},
 {{ .Name }},
 {{ .EventBridgeBus }},
 {{ .EventFilter }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.appintegrations.event_integrations
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>event_integrations</code> resource, the following permissions are required:

### Create
```json
app-integrations:CreateEventIntegration,
app-integrations:TagResource
```

### List
```json
app-integrations:ListEventIntegrations
```

### Delete
```json
app-integrations:DeleteEventIntegration
```

