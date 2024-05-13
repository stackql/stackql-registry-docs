---
title: user_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pools
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


Used to retrieve a list of <code>user_pools</code> in a region or to create or delete a <code>user_pools</code> resource, use <code>user_pool</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::UserPool</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.user_pools" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="user_pool_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="region" /></td>
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
user_pool_id
FROM aws.cognito.user_pools
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>user_pool</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cognito.user_pools (
 UserPoolName,
 Policies,
 AccountRecoverySetting,
 AdminCreateUserConfig,
 AliasAttributes,
 UsernameAttributes,
 AutoVerifiedAttributes,
 DeviceConfiguration,
 EmailConfiguration,
 EmailVerificationMessage,
 EmailVerificationSubject,
 DeletionProtection,
 LambdaConfig,
 MfaConfiguration,
 EnabledMfas,
 SmsAuthenticationMessage,
 SmsConfiguration,
 SmsVerificationMessage,
 Schema,
 UsernameConfiguration,
 UserAttributeUpdateSettings,
 UserPoolTags,
 VerificationMessageTemplate,
 UserPoolAddOns,
 region
)
SELECT 
'{{ UserPoolName }}',
 '{{ Policies }}',
 '{{ AccountRecoverySetting }}',
 '{{ AdminCreateUserConfig }}',
 '{{ AliasAttributes }}',
 '{{ UsernameAttributes }}',
 '{{ AutoVerifiedAttributes }}',
 '{{ DeviceConfiguration }}',
 '{{ EmailConfiguration }}',
 '{{ EmailVerificationMessage }}',
 '{{ EmailVerificationSubject }}',
 '{{ DeletionProtection }}',
 '{{ LambdaConfig }}',
 '{{ MfaConfiguration }}',
 '{{ EnabledMfas }}',
 '{{ SmsAuthenticationMessage }}',
 '{{ SmsConfiguration }}',
 '{{ SmsVerificationMessage }}',
 '{{ Schema }}',
 '{{ UsernameConfiguration }}',
 '{{ UserAttributeUpdateSettings }}',
 '{{ UserPoolTags }}',
 '{{ VerificationMessageTemplate }}',
 '{{ UserPoolAddOns }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cognito.user_pools (
 UserPoolName,
 Policies,
 AccountRecoverySetting,
 AdminCreateUserConfig,
 AliasAttributes,
 UsernameAttributes,
 AutoVerifiedAttributes,
 DeviceConfiguration,
 EmailConfiguration,
 EmailVerificationMessage,
 EmailVerificationSubject,
 DeletionProtection,
 LambdaConfig,
 MfaConfiguration,
 EnabledMfas,
 SmsAuthenticationMessage,
 SmsConfiguration,
 SmsVerificationMessage,
 Schema,
 UsernameConfiguration,
 UserAttributeUpdateSettings,
 UserPoolTags,
 VerificationMessageTemplate,
 UserPoolAddOns,
 region
)
SELECT 
 '{{ UserPoolName }}',
 '{{ Policies }}',
 '{{ AccountRecoverySetting }}',
 '{{ AdminCreateUserConfig }}',
 '{{ AliasAttributes }}',
 '{{ UsernameAttributes }}',
 '{{ AutoVerifiedAttributes }}',
 '{{ DeviceConfiguration }}',
 '{{ EmailConfiguration }}',
 '{{ EmailVerificationMessage }}',
 '{{ EmailVerificationSubject }}',
 '{{ DeletionProtection }}',
 '{{ LambdaConfig }}',
 '{{ MfaConfiguration }}',
 '{{ EnabledMfas }}',
 '{{ SmsAuthenticationMessage }}',
 '{{ SmsConfiguration }}',
 '{{ SmsVerificationMessage }}',
 '{{ Schema }}',
 '{{ UsernameConfiguration }}',
 '{{ UserAttributeUpdateSettings }}',
 '{{ UserPoolTags }}',
 '{{ VerificationMessageTemplate }}',
 '{{ UserPoolAddOns }}',
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
  - name: user_pool
    props:
      - name: UserPoolName
        value: '{{ UserPoolName }}'
      - name: Policies
        value:
          PasswordPolicy:
            MinimumLength: '{{ MinimumLength }}'
            RequireLowercase: '{{ RequireLowercase }}'
            RequireNumbers: '{{ RequireNumbers }}'
            RequireSymbols: '{{ RequireSymbols }}'
            RequireUppercase: '{{ RequireUppercase }}'
            TemporaryPasswordValidityDays: '{{ TemporaryPasswordValidityDays }}'
      - name: AccountRecoverySetting
        value:
          RecoveryMechanisms:
            - Name: '{{ Name }}'
              Priority: '{{ Priority }}'
      - name: AdminCreateUserConfig
        value:
          AllowAdminCreateUserOnly: '{{ AllowAdminCreateUserOnly }}'
          InviteMessageTemplate:
            EmailMessage: '{{ EmailMessage }}'
            EmailSubject: '{{ EmailSubject }}'
            SMSMessage: '{{ SMSMessage }}'
          UnusedAccountValidityDays: '{{ UnusedAccountValidityDays }}'
      - name: AliasAttributes
        value:
          - '{{ AliasAttributes[0] }}'
      - name: UsernameAttributes
        value:
          - '{{ UsernameAttributes[0] }}'
      - name: AutoVerifiedAttributes
        value:
          - '{{ AutoVerifiedAttributes[0] }}'
      - name: DeviceConfiguration
        value:
          ChallengeRequiredOnNewDevice: '{{ ChallengeRequiredOnNewDevice }}'
          DeviceOnlyRememberedOnUserPrompt: '{{ DeviceOnlyRememberedOnUserPrompt }}'
      - name: EmailConfiguration
        value:
          ReplyToEmailAddress: '{{ ReplyToEmailAddress }}'
          SourceArn: '{{ SourceArn }}'
          From: '{{ From }}'
          ConfigurationSet: '{{ ConfigurationSet }}'
          EmailSendingAccount: '{{ EmailSendingAccount }}'
      - name: EmailVerificationMessage
        value: '{{ EmailVerificationMessage }}'
      - name: EmailVerificationSubject
        value: '{{ EmailVerificationSubject }}'
      - name: DeletionProtection
        value: '{{ DeletionProtection }}'
      - name: LambdaConfig
        value:
          CreateAuthChallenge: '{{ CreateAuthChallenge }}'
          CustomMessage: '{{ CustomMessage }}'
          DefineAuthChallenge: '{{ DefineAuthChallenge }}'
          PostAuthentication: '{{ PostAuthentication }}'
          PostConfirmation: '{{ PostConfirmation }}'
          PreAuthentication: '{{ PreAuthentication }}'
          PreSignUp: '{{ PreSignUp }}'
          VerifyAuthChallengeResponse: '{{ VerifyAuthChallengeResponse }}'
          UserMigration: '{{ UserMigration }}'
          PreTokenGeneration: '{{ PreTokenGeneration }}'
          CustomEmailSender:
            LambdaVersion: '{{ LambdaVersion }}'
            LambdaArn: '{{ LambdaArn }}'
          CustomSMSSender:
            LambdaVersion: '{{ LambdaVersion }}'
            LambdaArn: '{{ LambdaArn }}'
          KMSKeyID: '{{ KMSKeyID }}'
          PreTokenGenerationConfig:
            LambdaVersion: '{{ LambdaVersion }}'
            LambdaArn: '{{ LambdaArn }}'
      - name: MfaConfiguration
        value: '{{ MfaConfiguration }}'
      - name: EnabledMfas
        value:
          - '{{ EnabledMfas[0] }}'
      - name: SmsAuthenticationMessage
        value: '{{ SmsAuthenticationMessage }}'
      - name: SmsConfiguration
        value:
          ExternalId: '{{ ExternalId }}'
          SnsCallerArn: '{{ SnsCallerArn }}'
          SnsRegion: '{{ SnsRegion }}'
      - name: SmsVerificationMessage
        value: '{{ SmsVerificationMessage }}'
      - name: Schema
        value:
          - AttributeDataType: '{{ AttributeDataType }}'
            DeveloperOnlyAttribute: '{{ DeveloperOnlyAttribute }}'
            Mutable: '{{ Mutable }}'
            Name: '{{ Name }}'
            NumberAttributeConstraints:
              MaxValue: '{{ MaxValue }}'
              MinValue: '{{ MinValue }}'
            StringAttributeConstraints:
              MaxLength: '{{ MaxLength }}'
              MinLength: '{{ MinLength }}'
            Required: '{{ Required }}'
      - name: UsernameConfiguration
        value:
          CaseSensitive: '{{ CaseSensitive }}'
      - name: UserAttributeUpdateSettings
        value:
          AttributesRequireVerificationBeforeUpdate:
            - '{{ AttributesRequireVerificationBeforeUpdate[0] }}'
      - name: UserPoolTags
        value: {}
      - name: VerificationMessageTemplate
        value:
          DefaultEmailOption: '{{ DefaultEmailOption }}'
          EmailMessage: '{{ EmailMessage }}'
          EmailMessageByLink: '{{ EmailMessageByLink }}'
          EmailSubject: '{{ EmailSubject }}'
          EmailSubjectByLink: '{{ EmailSubjectByLink }}'
          SmsMessage: '{{ SmsMessage }}'
      - name: UserPoolAddOns
        value:
          AdvancedSecurityMode: '{{ AdvancedSecurityMode }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.cognito.user_pools
WHERE data__Identifier = '<UserPoolId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>user_pools</code> resource, the following permissions are required:

### Create
```json
cognito-idp:CreateUserPool,
iam:PassRole,
cognito-idp:SetUserPoolMfaConfig,
cognito-idp:DescribeUserPool,
kms:CreateGrant,
iam:CreateServiceLinkedRole
```

### Delete
```json
cognito-idp:DeleteUserPool
```

### List
```json
cognito-idp:ListUserPools
```

