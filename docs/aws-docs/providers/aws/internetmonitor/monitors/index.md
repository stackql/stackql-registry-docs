---
title: monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors
  - internetmonitor
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


Used to retrieve a list of <code>monitors</code> in a region or to create or delete a <code>monitors</code> resource, use <code>monitor</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a monitor, which defines the monitoring boundaries for measurements that Internet Monitor publishes information about for an application</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.internetmonitor.monitors" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="monitor_name" /></td><td><code>string</code></td><td></td></tr>
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
monitor_name
FROM aws.internetmonitor.monitors
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
 "MonitorName": "{{ MonitorName }}"
}
>>>
--required properties only
INSERT INTO aws.internetmonitor.monitors (
 MonitorName,
 region
)
SELECT 
{{ MonitorName }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "MonitorName": "{{ MonitorName }}",
 "LinkedAccountId": "{{ LinkedAccountId }}",
 "IncludeLinkedAccounts": "{{ IncludeLinkedAccounts }}",
 "Resources": [
  "{{ Resources[0] }}"
 ],
 "ResourcesToAdd": [
  "{{ ResourcesToAdd[0] }}"
 ],
 "ResourcesToRemove": [
  "{{ ResourcesToRemove[0] }}"
 ],
 "Status": "{{ Status }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "MaxCityNetworksToMonitor": "{{ MaxCityNetworksToMonitor }}",
 "TrafficPercentageToMonitor": "{{ TrafficPercentageToMonitor }}",
 "InternetMeasurementsLogDelivery": {
  "S3Config": {
   "BucketName": "{{ BucketName }}",
   "BucketPrefix": "{{ BucketPrefix }}",
   "LogDeliveryStatus": "{{ LogDeliveryStatus }}"
  }
 },
 "HealthEventsConfig": {
  "AvailabilityScoreThreshold": null,
  "PerformanceScoreThreshold": null,
  "AvailabilityLocalHealthEventsConfig": {
   "Status": "{{ Status }}",
   "HealthScoreThreshold": null,
   "MinTrafficImpact": null
  },
  "PerformanceLocalHealthEventsConfig": null
 }
}
>>>
--all properties
INSERT INTO aws.internetmonitor.monitors (
 MonitorName,
 LinkedAccountId,
 IncludeLinkedAccounts,
 Resources,
 ResourcesToAdd,
 ResourcesToRemove,
 Status,
 Tags,
 MaxCityNetworksToMonitor,
 TrafficPercentageToMonitor,
 InternetMeasurementsLogDelivery,
 HealthEventsConfig,
 region
)
SELECT 
 {{ MonitorName }},
 {{ LinkedAccountId }},
 {{ IncludeLinkedAccounts }},
 {{ Resources }},
 {{ ResourcesToAdd }},
 {{ ResourcesToRemove }},
 {{ Status }},
 {{ Tags }},
 {{ MaxCityNetworksToMonitor }},
 {{ TrafficPercentageToMonitor }},
 {{ InternetMeasurementsLogDelivery }},
 {{ HealthEventsConfig }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.internetmonitor.monitors
WHERE data__Identifier = '<MonitorName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>monitors</code> resource, the following permissions are required:

### Create
```json
internetmonitor:CreateMonitor,
internetmonitor:GetMonitor,
internetmonitor:TagResource,
internetmonitor:UntagResource,
logs:CreateLogDelivery,
logs:GetLogDelivery,
s3:GetBucketPolicy,
s3:PutBucketPolicy,
s3:ListBucket,
iam:PassRole
```

### Delete
```json
internetmonitor:UpdateMonitor,
internetmonitor:DeleteMonitor,
internetmonitor:GetMonitor,
logs:DeleteLogDelivery
```

### List
```json
internetmonitor:ListMonitors,
internetmonitor:GetMonitor,
logs:GetLogDelivery
```

