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


Used to retrieve a list of <code>campaigns</code> in a region or to create or delete a <code>campaigns</code> resource, use <code>campaign</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>campaigns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::ConnectCampaigns::Campaign Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connectcampaigns.campaigns" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Connect Campaign Arn</td></tr>
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
FROM aws.connectcampaigns.campaigns
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
 "ConnectInstanceArn": "{{ ConnectInstanceArn }}",
 "DialerConfig": {
  "ProgressiveDialerConfig": {
   "BandwidthAllocation": null,
   "DialingCapacity": null
  },
  "PredictiveDialerConfig": {
   "BandwidthAllocation": null,
   "DialingCapacity": null
  },
  "AgentlessDialerConfig": {
   "DialingCapacity": null
  }
 },
 "Name": "{{ Name }}",
 "OutboundCallConfig": {
  "ConnectContactFlowArn": "{{ ConnectContactFlowArn }}",
  "ConnectSourcePhoneNumber": "{{ ConnectSourcePhoneNumber }}",
  "ConnectQueueArn": "{{ ConnectQueueArn }}",
  "AnswerMachineDetectionConfig": {
   "EnableAnswerMachineDetection": "{{ EnableAnswerMachineDetection }}"
  }
 }
}
>>>
--required properties only
INSERT INTO aws.connectcampaigns.campaigns (
 ConnectInstanceArn,
 DialerConfig,
 Name,
 OutboundCallConfig,
 region
)
SELECT 
{{ .ConnectInstanceArn }},
 {{ .DialerConfig }},
 {{ .Name }},
 {{ .OutboundCallConfig }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ConnectInstanceArn": "{{ ConnectInstanceArn }}",
 "DialerConfig": {
  "ProgressiveDialerConfig": {
   "BandwidthAllocation": null,
   "DialingCapacity": null
  },
  "PredictiveDialerConfig": {
   "BandwidthAllocation": null,
   "DialingCapacity": null
  },
  "AgentlessDialerConfig": {
   "DialingCapacity": null
  }
 },
 "Name": "{{ Name }}",
 "OutboundCallConfig": {
  "ConnectContactFlowArn": "{{ ConnectContactFlowArn }}",
  "ConnectSourcePhoneNumber": "{{ ConnectSourcePhoneNumber }}",
  "ConnectQueueArn": "{{ ConnectQueueArn }}",
  "AnswerMachineDetectionConfig": {
   "EnableAnswerMachineDetection": "{{ EnableAnswerMachineDetection }}"
  }
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.connectcampaigns.campaigns (
 ConnectInstanceArn,
 DialerConfig,
 Name,
 OutboundCallConfig,
 Tags,
 region
)
SELECT 
 {{ .ConnectInstanceArn }},
 {{ .DialerConfig }},
 {{ .Name }},
 {{ .OutboundCallConfig }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
connect-campaigns:DeleteCampaign
```

### List
```json
connect-campaigns:ListCampaigns
```

