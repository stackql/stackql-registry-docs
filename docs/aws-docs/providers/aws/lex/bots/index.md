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

Creates, updates, deletes or gets a <code>bot</code> resource or lists <code>bots</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Amazon Lex conversational bot performing automated tasks such as ordering a pizza, booking a hotel, and so on.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lex.bots" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Unique ID of resource</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A unique identifier for a resource.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the version. Use the description to help identify the version in lists.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an IAM role that has permission to access the bot.</td></tr>
<tr><td><CopyableCode code="data_privacy" /></td><td><code>object</code></td><td>Data privacy setting of the Bot.</td></tr>
<tr><td><CopyableCode code="idle_session_ttl_in_seconds" /></td><td><code>integer</code></td><td>IdleSessionTTLInSeconds of the resource</td></tr>
<tr><td><CopyableCode code="bot_locales" /></td><td><code>array</code></td><td>List of bot locales</td></tr>
<tr><td><CopyableCode code="bot_file_s3_location" /></td><td><code>object</code></td><td>S3 location of bot definitions zip file, if it's not defined inline in CloudFormation.</td></tr>
<tr><td><CopyableCode code="bot_tags" /></td><td><code>array</code></td><td>A list of tags to add to the bot, which can only be added at bot creation.</td></tr>
<tr><td><CopyableCode code="test_bot_alias_tags" /></td><td><code>array</code></td><td>A list of tags to add to the test alias for a bot, , which can only be added at bot/bot alias creation.</td></tr>
<tr><td><CopyableCode code="auto_build_bot_locales" /></td><td><code>boolean</code></td><td>Specifies whether to build the bot locales after bot creation completes.</td></tr>
<tr><td><CopyableCode code="test_bot_alias_settings" /></td><td><code>object</code></td><td>Configuring the test bot alias settings for a given bot</td></tr>
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
    <td><CopyableCode code="Name, RoleArn, DataPrivacy, IdleSessionTTLInSeconds, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>bots</code> in a region.
```sql
SELECT
region,
id
FROM aws.lex.bots
WHERE region = 'us-east-1';
```
Gets all properties from a <code>bot</code>.
```sql
SELECT
region,
id,
arn,
name,
description,
role_arn,
data_privacy,
idle_session_ttl_in_seconds,
bot_locales,
bot_file_s3_location,
bot_tags,
test_bot_alias_tags,
auto_build_bot_locales,
test_bot_alias_settings
FROM aws.lex.bots
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
lex:DescribeBot,
lex:ListTagsForResource
```

### Update
```json
iam:PassRole,
lex:DescribeBot,
lex:CreateUploadUrl,
lex:StartImport,
lex:DescribeImport,
lex:ListTagsForResource,
lex:TagResource,
lex:UntagResource,
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

