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

Creates, updates, deletes or gets an <code>user_pool_risk_configuration_attachment</code> resource or lists <code>user_pool_risk_configuration_attachments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool_risk_configuration_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::UserPoolRiskConfigurationAttachment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.user_pool_risk_configuration_attachments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="user_pool_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="client_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="risk_exception_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="compromised_credentials_risk_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="account_takeover_risk_configuration" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="UserPoolId, ClientId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from an individual <code>user_pool_risk_configuration_attachment</code>.
```sql
SELECT
region,
user_pool_id,
client_id,
risk_exception_configuration,
compromised_credentials_risk_configuration,
account_takeover_risk_configuration
FROM aws.cognito.user_pool_risk_configuration_attachments
WHERE region = 'us-east-1' AND data__Identifier = '<UserPoolId>|<ClientId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>user_pool_risk_configuration_attachment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.cognito.user_pool_risk_configuration_attachments (
 UserPoolId,
 ClientId,
 region
)
SELECT 
'{{ UserPoolId }}',
 '{{ ClientId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cognito.user_pool_risk_configuration_attachments (
 UserPoolId,
 ClientId,
 RiskExceptionConfiguration,
 CompromisedCredentialsRiskConfiguration,
 AccountTakeoverRiskConfiguration,
 region
)
SELECT 
 '{{ UserPoolId }}',
 '{{ ClientId }}',
 '{{ RiskExceptionConfiguration }}',
 '{{ CompromisedCredentialsRiskConfiguration }}',
 '{{ AccountTakeoverRiskConfiguration }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: user_pool_risk_configuration_attachment
    props:
      - name: UserPoolId
        value: '{{ UserPoolId }}'
      - name: ClientId
        value: '{{ ClientId }}'
      - name: RiskExceptionConfiguration
        value:
          BlockedIPRangeList:
            - '{{ BlockedIPRangeList[0] }}'
          SkippedIPRangeList:
            - '{{ SkippedIPRangeList[0] }}'
      - name: CompromisedCredentialsRiskConfiguration
        value:
          Actions:
            EventAction: '{{ EventAction }}'
          EventFilter:
            - '{{ EventFilter[0] }}'
      - name: AccountTakeoverRiskConfiguration
        value:
          Actions:
            HighAction:
              EventAction: '{{ EventAction }}'
              Notify: '{{ Notify }}'
            LowAction: null
            MediumAction: null
          NotifyConfiguration:
            BlockEmail:
              HtmlBody: '{{ HtmlBody }}'
              Subject: '{{ Subject }}'
              TextBody: '{{ TextBody }}'
            MfaEmail: null
            NoActionEmail: null
            From: '{{ From }}'
            ReplyTo: '{{ ReplyTo }}'
            SourceArn: '{{ SourceArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
cognito-idp:DescribeRiskConfiguration
```

### Update
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

