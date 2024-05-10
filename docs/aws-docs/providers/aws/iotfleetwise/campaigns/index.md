---
title: campaigns
hide_title: false
hide_table_of_contents: false
keywords:
  - campaigns
  - iotfleetwise
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
<tr><td><b>Description</b></td><td>Definition of AWS::IoTFleetWise::Campaign Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotfleetwise.campaigns" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
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
name
FROM aws.iotfleetwise.campaigns
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
 "Action": "{{ Action }}",
 "Name": "{{ Name }}",
 "SignalCatalogArn": "{{ SignalCatalogArn }}",
 "TargetArn": "{{ TargetArn }}",
 "CollectionScheme": null
}
>>>
--required properties only
INSERT INTO aws.iotfleetwise.campaigns (
 Action,
 Name,
 SignalCatalogArn,
 TargetArn,
 CollectionScheme,
 region
)
SELECT 
{{ Action }},
 {{ Name }},
 {{ SignalCatalogArn }},
 {{ TargetArn }},
 {{ CollectionScheme }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Action": "{{ Action }}",
 "Compression": "{{ Compression }}",
 "Description": "{{ Description }}",
 "Priority": "{{ Priority }}",
 "SignalsToCollect": [
  {
   "MaxSampleCount": null,
   "Name": "{{ Name }}",
   "MinimumSamplingIntervalMs": null
  }
 ],
 "DataDestinationConfigs": [
  null
 ],
 "StartTime": "{{ StartTime }}",
 "Name": "{{ Name }}",
 "ExpiryTime": "{{ ExpiryTime }}",
 "SpoolingMode": "{{ SpoolingMode }}",
 "SignalCatalogArn": "{{ SignalCatalogArn }}",
 "PostTriggerCollectionDuration": null,
 "DataExtraDimensions": [
  "{{ DataExtraDimensions[0] }}"
 ],
 "DiagnosticsMode": "{{ DiagnosticsMode }}",
 "TargetArn": "{{ TargetArn }}",
 "CollectionScheme": null,
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.iotfleetwise.campaigns (
 Action,
 Compression,
 Description,
 Priority,
 SignalsToCollect,
 DataDestinationConfigs,
 StartTime,
 Name,
 ExpiryTime,
 SpoolingMode,
 SignalCatalogArn,
 PostTriggerCollectionDuration,
 DataExtraDimensions,
 DiagnosticsMode,
 TargetArn,
 CollectionScheme,
 Tags,
 region
)
SELECT 
 {{ Action }},
 {{ Compression }},
 {{ Description }},
 {{ Priority }},
 {{ SignalsToCollect }},
 {{ DataDestinationConfigs }},
 {{ StartTime }},
 {{ Name }},
 {{ ExpiryTime }},
 {{ SpoolingMode }},
 {{ SignalCatalogArn }},
 {{ PostTriggerCollectionDuration }},
 {{ DataExtraDimensions }},
 {{ DiagnosticsMode }},
 {{ TargetArn }},
 {{ CollectionScheme }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iotfleetwise.campaigns
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>campaigns</code> resource, the following permissions are required:

### Create
```json
iotfleetwise:CreateCampaign,
iotfleetwise:GetCampaign,
iotfleetwise:ListTagsForResource,
iotfleetwise:TagResource,
iam:PassRole,
timestream:DescribeEndpoints,
timestream:DescribeTable
```

### List
```json
iotfleetwise:ListCampaigns,
iotfleetwise:GetCampaign
```

### Delete
```json
iotfleetwise:DeleteCampaign,
iotfleetwise:GetCampaign
```

