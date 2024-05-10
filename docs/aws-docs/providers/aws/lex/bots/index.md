---
title: bots
hide_title: false
hide_table_of_contents: false
keywords:
  - bots
  - lex
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


Used to retrieve a list of <code>bots</code> in a region or to create or delete a <code>bots</code> resource, use <code>bot</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Amazon Lex conversational bot performing automated tasks such as ordering a pizza, booking a hotel, and so on.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lex.bots" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>undefined</code></td><td></td></tr>
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
id
FROM aws.lex.bots
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>bot</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- bot.iql (required properties only)
INSERT INTO aws.lex.bots (
 Name,
 RoleArn,
 DataPrivacy,
 IdleSessionTTLInSeconds,
 region
)
SELECT 
'{{ Name }}',
 '{{ RoleArn }}',
 '{{ DataPrivacy }}',
 '{{ IdleSessionTTLInSeconds }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- bot.iql (all properties)
INSERT INTO aws.lex.bots (
 Name,
 Description,
 RoleArn,
 DataPrivacy,
 IdleSessionTTLInSeconds,
 BotLocales,
 BotFileS3Location,
 BotTags,
 TestBotAliasTags,
 AutoBuildBotLocales,
 TestBotAliasSettings,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ RoleArn }}',
 '{{ DataPrivacy }}',
 '{{ IdleSessionTTLInSeconds }}',
 '{{ BotLocales }}',
 '{{ BotFileS3Location }}',
 '{{ BotTags }}',
 '{{ TestBotAliasTags }}',
 '{{ AutoBuildBotLocales }}',
 '{{ TestBotAliasSettings }}',
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
  - name: bot
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: DataPrivacy
        value:
          ChildDirected: '{{ ChildDirected }}'
      - name: IdleSessionTTLInSeconds
        value: '{{ IdleSessionTTLInSeconds }}'
      - name: BotLocales
        value:
          - LocaleId: '{{ LocaleId }}'
            Description: null
            VoiceSettings:
              VoiceId: '{{ VoiceId }}'
              Engine: '{{ Engine }}'
            NluConfidenceThreshold: null
            Intents:
              - Name: null
                Description: null
                ParentIntentSignature: '{{ ParentIntentSignature }}'
                SampleUtterances:
                  - Utterance: '{{ Utterance }}'
                DialogCodeHook:
                  Enabled: '{{ Enabled }}'
                FulfillmentCodeHook:
                  FulfillmentUpdatesSpecification:
                    StartResponse:
                      MessageGroups:
                        - Message:
                            PlainTextMessage:
                              Value: '{{ Value }}'
                            CustomPayload:
                              Value: '{{ Value }}'
                            SSMLMessage:
                              Value: '{{ Value }}'
                            ImageResponseCard:
                              Title: '{{ Title }}'
                              Subtitle: null
                              ImageUrl: '{{ ImageUrl }}'
                              Buttons:
                                - Text: '{{ Text }}'
                                  Value: '{{ Value }}'
                          Variations:
                            - null
                      DelayInSeconds: '{{ DelayInSeconds }}'
                      AllowInterrupt: '{{ AllowInterrupt }}'
                    UpdateResponse:
                      MessageGroups: null
                      FrequencyInSeconds: '{{ FrequencyInSeconds }}'
                      AllowInterrupt: '{{ AllowInterrupt }}'
                    TimeoutInSeconds: '{{ TimeoutInSeconds }}'
                    Active: '{{ Active }}'
                  PostFulfillmentStatusSpecification:
                    SuccessResponse:
                      MessageGroupsList: null
                      AllowInterrupt: '{{ AllowInterrupt }}'
                    SuccessNextStep:
                      DialogAction:
                        Type: '{{ Type }}'
                        SlotToElicit: null
                        SuppressNextMessage: '{{ SuppressNextMessage }}'
                      Intent:
                        Name: null
                        Slots:
                          - SlotName: null
                            SlotValueOverride:
                              Shape: '{{ Shape }}'
                              Value:
                                InterpretedValue: '{{ InterpretedValue }}'
                              Values:
                                - null
                      SessionAttributes:
                        - Key: '{{ Key }}'
                          Value: '{{ Value }}'
                    SuccessConditional:
                      IsActive: '{{ IsActive }}'
                      ConditionalBranches:
                        - Name: null
                          Condition:
                            ExpressionString: '{{ ExpressionString }}'
                          NextStep: null
                          Response: null
                      DefaultBranch:
                        NextStep: null
                        Response: null
                    FailureResponse: null
                    FailureNextStep: null
                    FailureConditional: null
                    TimeoutResponse: null
                    TimeoutNextStep: null
                    TimeoutConditional: null
                  Enabled: '{{ Enabled }}'
                  IsActive: '{{ IsActive }}'
                IntentConfirmationSetting:
                  PromptSpecification:
                    MessageGroupsList: null
                    MaxRetries: '{{ MaxRetries }}'
                    AllowInterrupt: '{{ AllowInterrupt }}'
                    MessageSelectionStrategy: '{{ MessageSelectionStrategy }}'
                    PromptAttemptsSpecification: {}
                  IsActive: '{{ IsActive }}'
                  ConfirmationResponse: null
                  ConfirmationNextStep: null
                  ConfirmationConditional: null
                  DeclinationResponse: null
                  DeclinationNextStep: null
                  DeclinationConditional: null
                  FailureResponse: null
                  FailureNextStep: null
                  FailureConditional: null
                  CodeHook:
                    EnableCodeHookInvocation: '{{ EnableCodeHookInvocation }}'
                    IsActive: '{{ IsActive }}'
                    InvocationLabel: null
                    PostCodeHookSpecification:
                      SuccessResponse: null
                      SuccessNextStep: null
                      SuccessConditional: null
                      FailureResponse: null
                      FailureNextStep: null
                      FailureConditional: null
                      TimeoutResponse: null
                      TimeoutNextStep: null
                      TimeoutConditional: null
                  ElicitationCodeHook:
                    EnableCodeHookInvocation: '{{ EnableCodeHookInvocation }}'
                    InvocationLabel: null
                IntentClosingSetting:
                  ClosingResponse: null
                  IsActive: '{{ IsActive }}'
                  Conditional: null
                  NextStep: null
                InitialResponseSetting:
                  InitialResponse: null
                  NextStep: null
                  Conditional: null
                  CodeHook: null
                InputContexts:
                  - Name: null
                OutputContexts:
                  - Name: null
                    TimeToLiveInSeconds: '{{ TimeToLiveInSeconds }}'
                    TurnsToLive: '{{ TurnsToLive }}'
                KendraConfiguration:
                  KendraIndex: '{{ KendraIndex }}'
                  QueryFilterStringEnabled: '{{ QueryFilterStringEnabled }}'
                  QueryFilterString: '{{ QueryFilterString }}'
                SlotPriorities:
                  - Priority: '{{ Priority }}'
                    SlotName: null
                Slots:
                  - Name: null
                    Description: null
                    SlotTypeName: '{{ SlotTypeName }}'
                    ValueElicitationSetting:
                      DefaultValueSpecification:
                        DefaultValueList:
                          - DefaultValue: '{{ DefaultValue }}'
                      SlotConstraint: '{{ SlotConstraint }}'
                      PromptSpecification: null
                      SampleUtterances: null
                      WaitAndContinueSpecification:
                        WaitingResponse: null
                        ContinueResponse: null
                        StillWaitingResponse:
                          MessageGroupsList: null
                          FrequencyInSeconds: '{{ FrequencyInSeconds }}'
                          TimeoutInSeconds: '{{ TimeoutInSeconds }}'
                          AllowInterrupt: '{{ AllowInterrupt }}'
                        IsActive: '{{ IsActive }}'
                      SlotCaptureSetting:
                        CaptureResponse: null
                        CaptureNextStep: null
                        CaptureConditional: null
                        FailureResponse: null
                        FailureNextStep: null
                        FailureConditional: null
                        CodeHook: null
                        ElicitationCodeHook: null
                    ObfuscationSetting:
                      ObfuscationSettingType: '{{ ObfuscationSettingType }}'
                    MultipleValuesSetting:
                      AllowMultipleValues: '{{ AllowMultipleValues }}'
            SlotTypes:
              - Name: null
                Description: null
                ParentSlotTypeSignature: '{{ ParentSlotTypeSignature }}'
                SlotTypeValues:
                  - SampleValue:
                      Value: '{{ Value }}'
                    Synonyms:
                      - null
                ValueSelectionSetting:
                  ResolutionStrategy: '{{ ResolutionStrategy }}'
                  RegexFilter:
                    Pattern: '{{ Pattern }}'
                  AdvancedRecognitionSetting:
                    AudioRecognitionStrategy: '{{ AudioRecognitionStrategy }}'
                ExternalSourceSetting:
                  GrammarSlotTypeSetting:
                    Source:
                      S3BucketName: '{{ S3BucketName }}'
                      S3ObjectKey: '{{ S3ObjectKey }}'
                      KmsKeyArn: '{{ KmsKeyArn }}'
            CustomVocabulary:
              CustomVocabularyItems:
                - Phrase: '{{ Phrase }}'
                  Weight: '{{ Weight }}'
                  DisplayAs: '{{ DisplayAs }}'
      - name: BotFileS3Location
        value:
          S3Bucket: null
          S3ObjectKey: null
          S3ObjectVersion: '{{ S3ObjectVersion }}'
      - name: BotTags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: TestBotAliasTags
        value:
          - null
      - name: AutoBuildBotLocales
        value: '{{ AutoBuildBotLocales }}'
      - name: TestBotAliasSettings
        value:
          BotAliasLocaleSettings:
            - LocaleId: '{{ LocaleId }}'
              BotAliasLocaleSetting:
                CodeHookSpecification:
                  LambdaCodeHook:
                    CodeHookInterfaceVersion: '{{ CodeHookInterfaceVersion }}'
                    LambdaArn: '{{ LambdaArn }}'
                Enabled: '{{ Enabled }}'
          ConversationLogSettings:
            AudioLogSettings:
              - Destination:
                  S3Bucket:
                    S3BucketArn: '{{ S3BucketArn }}'
                    LogPrefix: '{{ LogPrefix }}'
                    KmsKeyArn: '{{ KmsKeyArn }}'
                Enabled: '{{ Enabled }}'
            TextLogSettings:
              - Destination:
                  CloudWatch:
                    CloudWatchLogGroupArn: '{{ CloudWatchLogGroupArn }}'
                    LogPrefix: '{{ LogPrefix }}'
                Enabled: '{{ Enabled }}'
          Description: null
          SentimentAnalysisSettings:
            DetectSentiment: '{{ DetectSentiment }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.lex.bots
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>bots</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
lex:DescribeBot,
lex:CreateUploadUrl,
lex:StartImport,
lex:DescribeImport,
lex:ListTagsForResource,
lex:TagResource,
lex:CreateBot,
lex:CreateBotLocale,
lex:CreateIntent,
lex:CreateSlot,
lex:CreateSlotType,
lex:UpdateBot,
lex:UpdateBotLocale,
lex:UpdateIntent,
lex:UpdateSlot,
lex:UpdateSlotType,
lex:DeleteBotLocale,
lex:DeleteIntent,
lex:DeleteSlot,
lex:DeleteSlotType,
lex:DescribeBotLocale,
lex:BuildBotLocale,
lex:ListBots,
lex:ListBotLocales,
lex:CreateCustomVocabulary,
lex:UpdateCustomVocabulary,
lex:DeleteCustomVocabulary,
s3:GetObject,
lex:UpdateBotAlias
```

### Delete
```json
lex:DeleteBot,
lex:DescribeBot,
lex:DeleteBotLocale,
lex:DeleteIntent,
lex:DeleteSlotType,
lex:DeleteSlot,
lex:DeleteBotVersion,
lex:DeleteBotChannel,
lex:DeleteBotAlias,
lex:DeleteCustomVocabulary
```

### List
```json
lex:ListBots
```

