---
title: response_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - response_plans
  - ssmincidents
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


Used to retrieve a list of <code>response_plans</code> in a region or to create or delete a <code>response_plans</code> resource, use <code>response_plan</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>response_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::SSMIncidents::ResponsePlan</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssmincidents.response_plans" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the response plan.</td></tr>
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
FROM aws.ssmincidents.response_plans
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
 "IncidentTemplate": {
  "DedupeString": "{{ DedupeString }}",
  "Impact": "{{ Impact }}",
  "NotificationTargets": [
   {
    "SnsTopicArn": "{{ SnsTopicArn }}"
   }
  ],
  "Summary": "{{ Summary }}",
  "Title": "{{ Title }}",
  "IncidentTags": [
   {
    "Key": "{{ Key }}",
    "Value": "{{ Value }}"
   }
  ]
 }
}
>>>
--required properties only
INSERT INTO aws.ssmincidents.response_plans (
 Name,
 IncidentTemplate,
 region
)
SELECT 
{{ .Name }},
 {{ .IncidentTemplate }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "DisplayName": "{{ DisplayName }}",
 "ChatChannel": {
  "ChatbotSns": [
   "{{ ChatbotSns[0] }}"
  ]
 },
 "Engagements": [
  "{{ Engagements[0] }}"
 ],
 "Actions": [
  {
   "SsmAutomation": {
    "RoleArn": "{{ RoleArn }}",
    "DocumentName": "{{ DocumentName }}",
    "DocumentVersion": "{{ DocumentVersion }}",
    "TargetAccount": "{{ TargetAccount }}",
    "Parameters": [
     {
      "Key": "{{ Key }}",
      "Values": [
       "{{ Values[0] }}"
      ]
     }
    ],
    "DynamicParameters": [
     {
      "Key": "{{ Key }}",
      "Value": {
       "Variable": "{{ Variable }}"
      }
     }
    ]
   }
  }
 ],
 "Integrations": [
  {
   "PagerDutyConfiguration": {
    "Name": "{{ Name }}",
    "SecretId": "{{ SecretId }}",
    "PagerDutyIncidentConfiguration": {
     "ServiceId": "{{ ServiceId }}"
    }
   }
  }
 ],
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "IncidentTemplate": {
  "DedupeString": "{{ DedupeString }}",
  "Impact": "{{ Impact }}",
  "NotificationTargets": [
   {
    "SnsTopicArn": null
   }
  ],
  "Summary": "{{ Summary }}",
  "Title": "{{ Title }}",
  "IncidentTags": [
   null
  ]
 }
}
>>>
--all properties
INSERT INTO aws.ssmincidents.response_plans (
 Name,
 DisplayName,
 ChatChannel,
 Engagements,
 Actions,
 Integrations,
 Tags,
 IncidentTemplate,
 region
)
SELECT 
 {{ .Name }},
 {{ .DisplayName }},
 {{ .ChatChannel }},
 {{ .Engagements }},
 {{ .Actions }},
 {{ .Integrations }},
 {{ .Tags }},
 {{ .IncidentTemplate }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ssmincidents.response_plans
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>response_plans</code> resource, the following permissions are required:

### Create
```json
ssm-incidents:CreateResponsePlan,
ssm-incidents:GetResponsePlan,
ssm-incidents:TagResource,
ssm-incidents:ListTagsForResource,
iam:PassRole,
secretsmanager:GetSecretValue,
kms:Decrypt,
kms:GenerateDataKey*
```

### Delete
```json
ssm-incidents:DeleteResponsePlan,
ssm-incidents:GetResponsePlan
```

### List
```json
ssm-incidents:ListResponsePlans
```

