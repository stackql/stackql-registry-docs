---
title: security_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - security_profiles
  - iot
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


Used to retrieve a list of <code>security_profiles</code> in a region or to create or delete a <code>security_profiles</code> resource, use <code>security_profile</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A security profile defines a set of expected behaviors for devices in your account.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.security_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="security_profile_name" /></td><td><code>string</code></td><td>A unique identifier for the security profile.</td></tr>
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
security_profile_name
FROM aws.iot.security_profiles
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
{}
>>>
--required properties only
INSERT INTO aws.iot.security_profiles (
 ,
 region
)
SELECT 
{{ . }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "SecurityProfileName": "{{ SecurityProfileName }}",
 "SecurityProfileDescription": "{{ SecurityProfileDescription }}",
 "Behaviors": [
  {
   "Name": "{{ Name }}",
   "Metric": "{{ Metric }}",
   "MetricDimension": {
    "DimensionName": "{{ DimensionName }}",
    "Operator": "{{ Operator }}"
   },
   "Criteria": {
    "ComparisonOperator": "{{ ComparisonOperator }}",
    "Value": {
     "Count": "{{ Count }}",
     "Cidrs": [
      "{{ Cidrs[0] }}"
     ],
     "Ports": [
      "{{ Ports[0] }}"
     ],
     "Number": null,
     "Numbers": [
      null
     ],
     "Strings": [
      "{{ Strings[0] }}"
     ]
    },
    "DurationSeconds": "{{ DurationSeconds }}",
    "ConsecutiveDatapointsToAlarm": "{{ ConsecutiveDatapointsToAlarm }}",
    "ConsecutiveDatapointsToClear": "{{ ConsecutiveDatapointsToClear }}",
    "StatisticalThreshold": {
     "Statistic": "{{ Statistic }}"
    },
    "MlDetectionConfig": {
     "ConfidenceLevel": "{{ ConfidenceLevel }}"
    }
   },
   "SuppressAlerts": "{{ SuppressAlerts }}",
   "ExportMetric": "{{ ExportMetric }}"
  }
 ],
 "AlertTargets": {},
 "AdditionalMetricsToRetainV2": [
  {
   "Metric": "{{ Metric }}",
   "MetricDimension": null,
   "ExportMetric": null
  }
 ],
 "MetricsExportConfig": {
  "MqttTopic": "{{ MqttTopic }}",
  "RoleArn": "{{ RoleArn }}"
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "TargetArns": [
  "{{ TargetArns[0] }}"
 ]
}
>>>
--all properties
INSERT INTO aws.iot.security_profiles (
 SecurityProfileName,
 SecurityProfileDescription,
 Behaviors,
 AlertTargets,
 AdditionalMetricsToRetainV2,
 MetricsExportConfig,
 Tags,
 TargetArns,
 region
)
SELECT 
 {{ .SecurityProfileName }},
 {{ .SecurityProfileDescription }},
 {{ .Behaviors }},
 {{ .AlertTargets }},
 {{ .AdditionalMetricsToRetainV2 }},
 {{ .MetricsExportConfig }},
 {{ .Tags }},
 {{ .TargetArns }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iot.security_profiles
WHERE data__Identifier = '<SecurityProfileName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>security_profiles</code> resource, the following permissions are required:

### Create
```json
iot:CreateSecurityProfile,
iot:AttachSecurityProfile,
iot:DescribeSecurityProfile,
iot:TagResource,
iam:PassRole
```

### Delete
```json
iot:DescribeSecurityProfile,
iot:DeleteSecurityProfile
```

### List
```json
iot:ListSecurityProfiles
```

