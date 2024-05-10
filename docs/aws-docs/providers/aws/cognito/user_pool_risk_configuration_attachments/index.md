---
title: user_pool_risk_configuration_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pool_risk_configuration_attachments
  - cognito
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


Used to retrieve a list of <code>user_pool_risk_configuration_attachments</code> in a region or to create or delete a <code>user_pool_risk_configuration_attachments</code> resource, use <code>user_pool_risk_configuration_attachment</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool_risk_configuration_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::UserPoolRiskConfigurationAttachment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.user_pool_risk_configuration_attachments" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="user_pool_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="client_id" /></td><td><code>string</code></td><td></td></tr>
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
user_pool_id,
client_id
FROM aws.cognito.user_pool_risk_configuration_attachments
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
 "UserPoolId": "{{ UserPoolId }}",
 "ClientId": "{{ ClientId }}"
}
>>>
--required properties only
INSERT INTO aws.cognito.user_pool_risk_configuration_attachments (
 UserPoolId,
 ClientId,
 region
)
SELECT 
{{ .UserPoolId }},
 {{ .ClientId }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "UserPoolId": "{{ UserPoolId }}",
 "ClientId": "{{ ClientId }}",
 "RiskExceptionConfiguration": {
  "BlockedIPRangeList": [
   "{{ BlockedIPRangeList[0] }}"
  ],
  "SkippedIPRangeList": [
   "{{ SkippedIPRangeList[0] }}"
  ]
 },
 "CompromisedCredentialsRiskConfiguration": {
  "Actions": {
   "EventAction": "{{ EventAction }}"
  },
  "EventFilter": [
   "{{ EventFilter[0] }}"
  ]
 },
 "AccountTakeoverRiskConfiguration": {
  "Actions": {
   "HighAction": {
    "EventAction": "{{ EventAction }}",
    "Notify": "{{ Notify }}"
   },
   "LowAction": null,
   "MediumAction": null
  },
  "NotifyConfiguration": {
   "BlockEmail": {
    "HtmlBody": "{{ HtmlBody }}",
    "Subject": "{{ Subject }}",
    "TextBody": "{{ TextBody }}"
   },
   "MfaEmail": null,
   "NoActionEmail": null,
   "From": "{{ From }}",
   "ReplyTo": "{{ ReplyTo }}",
   "SourceArn": "{{ SourceArn }}"
  }
 }
}
>>>
--all properties
INSERT INTO aws.cognito.user_pool_risk_configuration_attachments (
 UserPoolId,
 ClientId,
 RiskExceptionConfiguration,
 CompromisedCredentialsRiskConfiguration,
 AccountTakeoverRiskConfiguration,
 region
)
SELECT 
 {{ .UserPoolId }},
 {{ .ClientId }},
 {{ .RiskExceptionConfiguration }},
 {{ .CompromisedCredentialsRiskConfiguration }},
 {{ .AccountTakeoverRiskConfiguration }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.cognito.user_pool_risk_configuration_attachments
WHERE data__Identifier = '<UserPoolId|ClientId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>user_pool_risk_configuration_attachments</code> resource, the following permissions are required:

### Create
```json
cognito-idp:SetRiskConfiguration,
cognito-idp:DescribeRiskConfiguration,
iam:PassRole
```

### Delete
```json
cognito-idp:SetRiskConfiguration,
cognito-idp:DescribeRiskConfiguration
```

