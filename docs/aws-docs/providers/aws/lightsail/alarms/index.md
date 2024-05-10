---
title: alarms
hide_title: false
hide_table_of_contents: false
keywords:
  - alarms
  - lightsail
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


Used to retrieve a list of <code>alarms</code> in a region or to create or delete a <code>alarms</code> resource, use <code>alarm</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alarms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lightsail::Alarm</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lightsail.alarms" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="alarm_name" /></td><td><code>string</code></td><td>The name for the alarm. Specify the name of an existing alarm to update, and overwrite the previous configuration of the alarm.</td></tr>
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
alarm_name
FROM aws.lightsail.alarms
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
 "AlarmName": "{{ AlarmName }}",
 "MonitoredResourceName": "{{ MonitoredResourceName }}",
 "MetricName": "{{ MetricName }}",
 "ComparisonOperator": "{{ ComparisonOperator }}",
 "EvaluationPeriods": "{{ EvaluationPeriods }}",
 "Threshold": null
}
>>>
--required properties only
INSERT INTO aws.lightsail.alarms (
 AlarmName,
 MonitoredResourceName,
 MetricName,
 ComparisonOperator,
 EvaluationPeriods,
 Threshold,
 region
)
SELECT 
{{ AlarmName }},
 {{ MonitoredResourceName }},
 {{ MetricName }},
 {{ ComparisonOperator }},
 {{ EvaluationPeriods }},
 {{ Threshold }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AlarmName": "{{ AlarmName }}",
 "MonitoredResourceName": "{{ MonitoredResourceName }}",
 "MetricName": "{{ MetricName }}",
 "ComparisonOperator": "{{ ComparisonOperator }}",
 "ContactProtocols": [
  "{{ ContactProtocols[0] }}"
 ],
 "DatapointsToAlarm": "{{ DatapointsToAlarm }}",
 "EvaluationPeriods": "{{ EvaluationPeriods }}",
 "NotificationEnabled": "{{ NotificationEnabled }}",
 "NotificationTriggers": [
  "{{ NotificationTriggers[0] }}"
 ],
 "Threshold": null,
 "TreatMissingData": "{{ TreatMissingData }}"
}
>>>
--all properties
INSERT INTO aws.lightsail.alarms (
 AlarmName,
 MonitoredResourceName,
 MetricName,
 ComparisonOperator,
 ContactProtocols,
 DatapointsToAlarm,
 EvaluationPeriods,
 NotificationEnabled,
 NotificationTriggers,
 Threshold,
 TreatMissingData,
 region
)
SELECT 
 {{ AlarmName }},
 {{ MonitoredResourceName }},
 {{ MetricName }},
 {{ ComparisonOperator }},
 {{ ContactProtocols }},
 {{ DatapointsToAlarm }},
 {{ EvaluationPeriods }},
 {{ NotificationEnabled }},
 {{ NotificationTriggers }},
 {{ Threshold }},
 {{ TreatMissingData }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.lightsail.alarms
WHERE data__Identifier = '<AlarmName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>alarms</code> resource, the following permissions are required:

### Create
```json
lightsail:PutAlarm,
lightsail:GetAlarms
```

### Delete
```json
lightsail:DeleteAlarm,
lightsail:GetAlarms
```

### List
```json
lightsail:GetAlarms
```

