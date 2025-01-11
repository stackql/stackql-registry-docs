---
title: campaigns
hide_title: false
hide_table_of_contents: false
keywords:
  - campaigns
  - connectcampaignsv2
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

Creates, updates, deletes or gets a <code>campaign</code> resource or lists <code>campaigns</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>campaigns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::ConnectCampaignsV2::Campaign Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connectcampaignsv2.campaigns" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Connect Campaign Arn</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Campaign name</td></tr>
<tr><td><CopyableCode code="connect_instance_id" /></td><td><code>string</code></td><td>Amazon Connect Instance Id</td></tr>
<tr><td><CopyableCode code="channel_subtype_config" /></td><td><code>object</code></td><td>The possible types of channel subtype config parameters</td></tr>
<tr><td><CopyableCode code="source" /></td><td><code>object</code></td><td>The possible source of the campaign</td></tr>
<tr><td><CopyableCode code="connect_campaign_flow_arn" /></td><td><code>string</code></td><td>Arn</td></tr>
<tr><td><CopyableCode code="schedule" /></td><td><code>object</code></td><td>Campaign schedule</td></tr>
<tr><td><CopyableCode code="communication_time_config" /></td><td><code>object</code></td><td>Campaign communication time config</td></tr>
<tr><td><CopyableCode code="communication_limits_override" /></td><td><code>object</code></td><td>Communication limits config</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>One or more tags.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaignsv2-campaign.html"><code>AWS::ConnectCampaignsV2::Campaign</code></a>.

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
    <td><CopyableCode code="Name, ConnectInstanceId, ChannelSubtypeConfig, region" /></td>
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
Gets all <code>campaigns</code> in a region.
```sql
SELECT
region,
arn,
name,
connect_instance_id,
channel_subtype_config,
source,
connect_campaign_flow_arn,
schedule,
communication_time_config,
communication_limits_override,
tags
FROM aws.connectcampaignsv2.campaigns
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>campaign</code>.
```sql
SELECT
region,
arn,
name,
connect_instance_id,
channel_subtype_config,
source,
connect_campaign_flow_arn,
schedule,
communication_time_config,
communication_limits_override,
tags
FROM aws.connectcampaignsv2.campaigns
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>campaign</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.connectcampaignsv2.campaigns (
 Name,
 ConnectInstanceId,
 ChannelSubtypeConfig,
 region
)
SELECT 
'{{ Name }}',
 '{{ ConnectInstanceId }}',
 '{{ ChannelSubtypeConfig }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.connectcampaignsv2.campaigns (
 Name,
 ConnectInstanceId,
 ChannelSubtypeConfig,
 Source,
 ConnectCampaignFlowArn,
 Schedule,
 CommunicationTimeConfig,
 CommunicationLimitsOverride,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ ConnectInstanceId }}',
 '{{ ChannelSubtypeConfig }}',
 '{{ Source }}',
 '{{ ConnectCampaignFlowArn }}',
 '{{ Schedule }}',
 '{{ CommunicationTimeConfig }}',
 '{{ CommunicationLimitsOverride }}',
 '{{ Tags }}',
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
  - name: campaign
    props:
      - name: Name
        value: '{{ Name }}'
      - name: ConnectInstanceId
        value: '{{ ConnectInstanceId }}'
      - name: ChannelSubtypeConfig
        value:
          Telephony:
            Capacity: null
            ConnectQueueId: '{{ ConnectQueueId }}'
            OutboundMode:
              ProgressiveConfig:
                BandwidthAllocation: null
              PredictiveConfig:
                BandwidthAllocation: null
              AgentlessConfig: {}
            DefaultOutboundConfig:
              ConnectContactFlowId: '{{ ConnectContactFlowId }}'
              ConnectSourcePhoneNumber: '{{ ConnectSourcePhoneNumber }}'
              AnswerMachineDetectionConfig:
                EnableAnswerMachineDetection: '{{ EnableAnswerMachineDetection }}'
                AwaitAnswerMachinePrompt: '{{ AwaitAnswerMachinePrompt }}'
          Sms:
            Capacity: null
            OutboundMode:
              AgentlessConfig: null
            DefaultOutboundConfig:
              ConnectSourcePhoneNumberArn: '{{ ConnectSourcePhoneNumberArn }}'
              WisdomTemplateArn: null
          Email:
            Capacity: null
            OutboundMode:
              AgentlessConfig: null
            DefaultOutboundConfig:
              ConnectSourceEmailAddress: '{{ ConnectSourceEmailAddress }}'
              SourceEmailAddressDisplayName: '{{ SourceEmailAddressDisplayName }}'
              WisdomTemplateArn: null
      - name: Source
        value:
          CustomerProfilesSegmentArn: null
          EventTrigger:
            CustomerProfilesDomainArn: null
      - name: ConnectCampaignFlowArn
        value: null
      - name: Schedule
        value:
          StartTime: '{{ StartTime }}'
          EndTime: null
          RefreshFrequency: '{{ RefreshFrequency }}'
      - name: CommunicationTimeConfig
        value:
          LocalTimeZoneConfig:
            DefaultTimeZone: '{{ DefaultTimeZone }}'
            LocalTimeZoneDetection:
              - '{{ LocalTimeZoneDetection[0] }}'
          Telephony:
            OpenHours:
              DailyHours:
                - Key: '{{ Key }}'
                  Value:
                    - StartTime: '{{ StartTime }}'
                      EndTime: null
            RestrictedPeriods:
              RestrictedPeriodList:
                - Name: '{{ Name }}'
                  StartDate: '{{ StartDate }}'
                  EndDate: null
          Sms: null
          Email: null
      - name: CommunicationLimitsOverride
        value:
          AllChannelsSubtypes:
            CommunicationLimitList:
              - MaxCountPerRecipient: '{{ MaxCountPerRecipient }}'
                Frequency: '{{ Frequency }}'
                Unit: '{{ Unit }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.connectcampaignsv2.campaigns
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>campaigns</code> resource, the following permissions are required:

### Create
```json
connect-campaigns:CreateCampaign,
connect-campaigns:DescribeCampaign,
connect-campaigns:TagResource,
connect:DescribeContactFlow,
connect:DescribeEmailAddress,
connect:DescribeInstance,
connect:DescribePhoneNumber,
connect:DescribeQueue,
profile:GetSegmentDefinition,
wisdom:GetMessageTemplate
```

### Read
```json
connect-campaigns:DescribeCampaign
```

### Delete
```json
connect-campaigns:DeleteCampaign,
connect-campaigns:DeleteCampaignChannelSubtypeConfig,
connect-campaigns:DeleteCampaignCommunicationLimits,
connect-campaigns:DeleteCampaignCommunicationTime
```

### List
```json
connect-campaigns:ListCampaigns
```

### Update
```json
connect-campaigns:DeleteCampaignChannelSubtypeConfig,
connect-campaigns:DeleteCampaignCommunicationLimits,
connect-campaigns:DeleteCampaignCommunicationTime,
connect-campaigns:UpdateCampaignChannelSubtypeConfig,
connect-campaigns:UpdateCampaignCommunicationLimits,
connect-campaigns:UpdateCampaignCommunicationTime,
connect-campaigns:UpdateCampaignName,
connect-campaigns:UpdateCampaignFlowAssociation,
connect-campaigns:UpdateCampaignSchedule,
connect-campaigns:UpdateCampaignSource,
connect-campaigns:TagResource,
connect-campaigns:UntagResource,
connect-campaigns:DescribeCampaign,
connect:DescribeContactFlow,
connect:DescribeEmailAddress,
connect:DescribePhoneNumber,
connect:DescribeQueue,
profile:GetSegmentDefinition,
wisdom:GetMessageTemplate
```
