---
title: campaigns
hide_title: false
hide_table_of_contents: false
keywords:
  - campaigns
  - connectcampaigns
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
<tr><td><b>Description</b></td><td>Definition of AWS::ConnectCampaigns::Campaign Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connectcampaigns.campaigns" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="connect_instance_arn" /></td><td><code>string</code></td><td>Amazon Connect Instance Arn</td></tr>
<tr><td><CopyableCode code="dialer_config" /></td><td><code>object</code></td><td>The possible types of dialer config parameters</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Connect Campaign Arn</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Amazon Connect Campaign Name</td></tr>
<tr><td><CopyableCode code="outbound_call_config" /></td><td><code>object</code></td><td>The configuration used for outbound calls.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>One or more tags.</td></tr>
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
    <td><CopyableCode code="ConnectInstanceArn, DialerConfig, Name, OutboundCallConfig, region" /></td>
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
List all <code>campaigns</code> in a region.
```sql
SELECT
region,
arn
FROM aws.connectcampaigns.campaigns
WHERE region = 'us-east-1';
```
Gets all properties from a <code>campaign</code>.
```sql
SELECT
region,
connect_instance_arn,
dialer_config,
arn,
name,
outbound_call_config,
tags
FROM aws.connectcampaigns.campaigns
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
INSERT INTO aws.connectcampaigns.campaigns (
 ConnectInstanceArn,
 DialerConfig,
 Name,
 OutboundCallConfig,
 region
)
SELECT 
'{{ ConnectInstanceArn }}',
 '{{ DialerConfig }}',
 '{{ Name }}',
 '{{ OutboundCallConfig }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.connectcampaigns.campaigns (
 ConnectInstanceArn,
 DialerConfig,
 Name,
 OutboundCallConfig,
 Tags,
 region
)
SELECT 
 '{{ ConnectInstanceArn }}',
 '{{ DialerConfig }}',
 '{{ Name }}',
 '{{ OutboundCallConfig }}',
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
      - name: ConnectInstanceArn
        value: '{{ ConnectInstanceArn }}'
      - name: DialerConfig
        value:
          ProgressiveDialerConfig:
            BandwidthAllocation: null
            DialingCapacity: null
          PredictiveDialerConfig:
            BandwidthAllocation: null
            DialingCapacity: null
          AgentlessDialerConfig:
            DialingCapacity: null
      - name: Name
        value: '{{ Name }}'
      - name: OutboundCallConfig
        value:
          ConnectContactFlowArn: '{{ ConnectContactFlowArn }}'
          ConnectSourcePhoneNumber: '{{ ConnectSourcePhoneNumber }}'
          ConnectQueueArn: '{{ ConnectQueueArn }}'
          AnswerMachineDetectionConfig:
            EnableAnswerMachineDetection: '{{ EnableAnswerMachineDetection }}'
            AwaitAnswerMachinePrompt: '{{ AwaitAnswerMachinePrompt }}'
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
DELETE FROM aws.connectcampaigns.campaigns
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
connect:DescribeInstance,
connect:DescribeQueue
```

### Read
```json
connect-campaigns:DescribeCampaign
```

### Delete
```json
connect-campaigns:DeleteCampaign
```

### List
```json
connect-campaigns:ListCampaigns
```

### Update
```json
connect-campaigns:UpdateCampaignDialerConfig,
connect-campaigns:UpdateCampaignName,
connect-campaigns:UpdateCampaignOutboundCallConfig,
connect-campaigns:TagResource,
connect-campaigns:UntagResource,
connect-campaigns:DescribeCampaign
```

