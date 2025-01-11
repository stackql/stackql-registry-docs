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

Creates, updates, deletes or gets an <code>user_pool</code> resource or lists <code>user_pools</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Cognito::UserPool Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.user_pools" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="user_pool_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="policies" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="account_recovery_setting" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="admin_create_user_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="alias_attributes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="username_attributes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="auto_verified_attributes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="device_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="email_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="email_verification_message" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="email_verification_subject" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="deletion_protection" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="lambda_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="mfa_configuration" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="enabled_mfas" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="sms_authentication_message" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="email_authentication_message" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="email_authentication_subject" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sms_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="sms_verification_message" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="web_authn_relying_party_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="web_authn_user_verification" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="schema" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="username_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="user_attribute_update_settings" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="user_pool_tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="verification_message_template" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="user_pool_add_ons" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="provider_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="provider_url" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="user_pool_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="user_pool_tier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html"><code>AWS::Cognito::UserPool</code></a>.

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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>user_pools</code> in a region.
```sql
SELECT
region,
user_pool_name,
policies,
account_recovery_setting,
admin_create_user_config,
alias_attributes,
username_attributes,
auto_verified_attributes,
device_configuration,
email_configuration,
email_verification_message,
email_verification_subject,
deletion_protection,
lambda_config,
mfa_configuration,
enabled_mfas,
sms_authentication_message,
email_authentication_message,
email_authentication_subject,
sms_configuration,
sms_verification_message,
web_authn_relying_party_id,
web_authn_user_verification,
schema,
username_configuration,
user_attribute_update_settings,
user_pool_tags,
verification_message_template,
user_pool_add_ons,
provider_name,
provider_url,
arn,
user_pool_id,
user_pool_tier
FROM aws.cognito.user_pools
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>user_pool</code>.
```sql
SELECT
region,
user_pool_name,
policies,
account_recovery_setting,
admin_create_user_config,
alias_attributes,
username_attributes,
auto_verified_attributes,
device_configuration,
email_configuration,
email_verification_message,
email_verification_subject,
deletion_protection,
lambda_config,
mfa_configuration,
enabled_mfas,
sms_authentication_message,
email_authentication_message,
email_authentication_subject,
sms_configuration,
sms_verification_message,
web_authn_relying_party_id,
web_authn_user_verification,
schema,
username_configuration,
user_attribute_update_settings,
user_pool_tags,
verification_message_template,
user_pool_add_ons,
provider_name,
provider_url,
arn,
user_pool_id,
user_pool_tier
FROM aws.cognito.user_pools
WHERE region = 'us-east-1' AND data__Identifier = '<UserPoolId>';
```

## `INSERT` example

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
 EmailAuthenticationMessage,
 EmailAuthenticationSubject,
 SmsConfiguration,
 SmsVerificationMessage,
 WebAuthnRelyingPartyID,
 WebAuthnUserVerification,
 Schema,
 UsernameConfiguration,
 UserAttributeUpdateSettings,
 UserPoolTags,
 VerificationMessageTemplate,
 UserPoolAddOns,
 UserPoolTier,
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
 '{{ EmailAuthenticationMessage }}',
 '{{ EmailAuthenticationSubject }}',
 '{{ SmsConfiguration }}',
 '{{ SmsVerificationMessage }}',
 '{{ WebAuthnRelyingPartyID }}',
 '{{ WebAuthnUserVerification }}',
 '{{ Schema }}',
 '{{ UsernameConfiguration }}',
 '{{ UserAttributeUpdateSettings }}',
 '{{ UserPoolTags }}',
 '{{ VerificationMessageTemplate }}',
 '{{ UserPoolAddOns }}',
 '{{ UserPoolTier }}',
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
 EmailAuthenticationMessage,
 EmailAuthenticationSubject,
 SmsConfiguration,
 SmsVerificationMessage,
 WebAuthnRelyingPartyID,
 WebAuthnUserVerification,
 Schema,
 UsernameConfiguration,
 UserAttributeUpdateSettings,
 UserPoolTags,
 VerificationMessageTemplate,
 UserPoolAddOns,
 UserPoolTier,
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
 '{{ EmailAuthenticationMessage }}',
 '{{ EmailAuthenticationSubject }}',
 '{{ SmsConfiguration }}',
 '{{ SmsVerificationMessage }}',
 '{{ WebAuthnRelyingPartyID }}',
 '{{ WebAuthnUserVerification }}',
 '{{ Schema }}',
 '{{ UsernameConfiguration }}',
 '{{ UserAttributeUpdateSettings }}',
 '{{ UserPoolTags }}',
 '{{ VerificationMessageTemplate }}',
 '{{ UserPoolAddOns }}',
 '{{ UserPoolTier }}',
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
            PasswordHistorySize: '{{ PasswordHistorySize }}'
          SignInPolicy:
            AllowedFirstAuthFactors:
              - '{{ AllowedFirstAuthFactors[0] }}'
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
      - name: EmailAuthenticationMessage
        value: '{{ EmailAuthenticationMessage }}'
      - name: EmailAuthenticationSubject
        value: '{{ EmailAuthenticationSubject }}'
      - name: SmsConfiguration
        value:
          ExternalId: '{{ ExternalId }}'
          SnsCallerArn: '{{ SnsCallerArn }}'
          SnsRegion: '{{ SnsRegion }}'
      - name: SmsVerificationMessage
        value: '{{ SmsVerificationMessage }}'
      - name: WebAuthnRelyingPartyID
        value: '{{ WebAuthnRelyingPartyID }}'
      - name: WebAuthnUserVerification
        value: '{{ WebAuthnUserVerification }}'
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
          AdvancedSecurityAdditionalFlows:
            CustomAuthMode: '{{ CustomAuthMode }}'
      - name: UserPoolTier
        value: '{{ UserPoolTier }}'

```
</TabItem>
</Tabs>

## `DELETE` example

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
iam:CreateServiceLinkedRole,
cognito-idp:TagResource
```

### Read
```json
cognito-idp:DescribeUserPool,
cognito-idp:GetUserPoolMfaConfig
```

### Update
```json
cognito-idp:UpdateUserPool,
cognito-idp:ListTagsForResource,
cognito-idp:UntagResource,
cognito-idp:TagResource,
cognito-idp:SetUserPoolMfaConfig,
cognito-idp:AddCustomAttributes,
cognito-idp:DescribeUserPool,
cognito-idp:GetUserPoolMfaConfig,
iam:PassRole
```

### Delete
```json
cognito-idp:DeleteUserPool
```

### List
```json
cognito-idp:ListUserPools
```
