---
title: mitigation_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - mitigation_actions
  - iot
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


Used to retrieve a list of <code>mitigation_actions</code> in a region or to create or delete a <code>mitigation_actions</code> resource, use <code>mitigation_action</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mitigation_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Mitigation actions can be used to take actions to mitigate issues that were found in an Audit finding or Detect violation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.mitigation_actions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="action_name" /></td><td><code>string</code></td><td>A unique identifier for the mitigation action.</td></tr>
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
action_name
FROM aws.iot.mitigation_actions
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
 "RoleArn": "{{ RoleArn }}",
 "ActionParams": {
  "AddThingsToThingGroupParams": {
   "OverrideDynamicGroups": "{{ OverrideDynamicGroups }}",
   "ThingGroupNames": [
    "{{ ThingGroupNames[0] }}"
   ]
  },
  "EnableIoTLoggingParams": {
   "LogLevel": "{{ LogLevel }}",
   "RoleArnForLogging": "{{ RoleArnForLogging }}"
  },
  "PublishFindingToSnsParams": {
   "TopicArn": "{{ TopicArn }}"
  },
  "ReplaceDefaultPolicyVersionParams": {
   "TemplateName": "{{ TemplateName }}"
  },
  "UpdateCACertificateParams": {
   "Action": "{{ Action }}"
  },
  "UpdateDeviceCertificateParams": {
   "Action": "{{ Action }}"
  }
 }
}
>>>
--required properties only
INSERT INTO aws.iot.mitigation_actions (
 RoleArn,
 ActionParams,
 region
)
SELECT 
{{ .RoleArn }},
 {{ .ActionParams }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ActionName": "{{ ActionName }}",
 "RoleArn": "{{ RoleArn }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "ActionParams": {
  "AddThingsToThingGroupParams": {
   "OverrideDynamicGroups": "{{ OverrideDynamicGroups }}",
   "ThingGroupNames": [
    "{{ ThingGroupNames[0] }}"
   ]
  },
  "EnableIoTLoggingParams": {
   "LogLevel": "{{ LogLevel }}",
   "RoleArnForLogging": "{{ RoleArnForLogging }}"
  },
  "PublishFindingToSnsParams": {
   "TopicArn": "{{ TopicArn }}"
  },
  "ReplaceDefaultPolicyVersionParams": {
   "TemplateName": "{{ TemplateName }}"
  },
  "UpdateCACertificateParams": {
   "Action": "{{ Action }}"
  },
  "UpdateDeviceCertificateParams": {
   "Action": "{{ Action }}"
  }
 }
}
>>>
--all properties
INSERT INTO aws.iot.mitigation_actions (
 ActionName,
 RoleArn,
 Tags,
 ActionParams,
 region
)
SELECT 
 {{ .ActionName }},
 {{ .RoleArn }},
 {{ .Tags }},
 {{ .ActionParams }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iot.mitigation_actions
WHERE data__Identifier = '<ActionName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>mitigation_actions</code> resource, the following permissions are required:

### Create
```json
iot:CreateMitigationAction,
iot:DescribeMitigationAction,
iot:TagResource,
iam:PassRole
```

### Delete
```json
iot:DescribeMitigationAction,
iot:DeleteMitigationAction
```

### List
```json
iot:ListMitigationActions
```

