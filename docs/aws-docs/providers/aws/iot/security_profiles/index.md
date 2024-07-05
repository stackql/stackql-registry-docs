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

Creates, updates, deletes or gets a <code>security_profile</code> resource or lists <code>security_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A security profile defines a set of expected behaviors for devices in your account.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.security_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="security_profile_name" /></td><td><code>string</code></td><td>A unique identifier for the security profile.</td></tr>
<tr><td><CopyableCode code="security_profile_description" /></td><td><code>string</code></td><td>A description of the security profile.</td></tr>
<tr><td><CopyableCode code="behaviors" /></td><td><code>array</code></td><td>Specifies the behaviors that, when violated by a device (thing), cause an alert.</td></tr>
<tr><td><CopyableCode code="alert_targets" /></td><td><code>object</code></td><td>Specifies the destinations to which alerts are sent.</td></tr>
<tr><td><CopyableCode code="additional_metrics_to_retain_v2" /></td><td><code>array</code></td><td>A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile's behaviors, but it is also retained for any metric specified here.</td></tr>
<tr><td><CopyableCode code="metrics_export_config" /></td><td><code>object</code></td><td>A structure containing the mqtt topic for metrics export.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Metadata that can be used to manage the security profile.</td></tr>
<tr><td><CopyableCode code="target_arns" /></td><td><code>array</code></td><td>A set of target ARNs that the security profile is attached to.</td></tr>
<tr><td><CopyableCode code="security_profile_arn" /></td><td><code>string</code></td><td>The ARN (Amazon resource name) of the created security profile.</td></tr>
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
    <td><CopyableCode code=", region" /></td>
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
Gets all <code>security_profiles</code> in a region.
```sql
SELECT
region,
security_profile_name,
security_profile_description,
behaviors,
alert_targets,
additional_metrics_to_retain_v2,
metrics_export_config,
tags,
target_arns,
security_profile_arn
FROM aws.iot.security_profiles
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>security_profile</code>.
```sql
SELECT
region,
security_profile_name,
security_profile_description,
behaviors,
alert_targets,
additional_metrics_to_retain_v2,
metrics_export_config,
tags,
target_arns,
security_profile_arn
FROM aws.iot.security_profiles
WHERE region = 'us-east-1' AND data__Identifier = '<SecurityProfileName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>security_profile</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iot.security_profiles (
 ,
 region
)
SELECT 
'{{  }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ SecurityProfileName }}',
 '{{ SecurityProfileDescription }}',
 '{{ Behaviors }}',
 '{{ AlertTargets }}',
 '{{ AdditionalMetricsToRetainV2 }}',
 '{{ MetricsExportConfig }}',
 '{{ Tags }}',
 '{{ TargetArns }}',
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
  - name: security_profile
    props:
      - name: SecurityProfileName
        value: '{{ SecurityProfileName }}'
      - name: SecurityProfileDescription
        value: '{{ SecurityProfileDescription }}'
      - name: Behaviors
        value:
          - Name: '{{ Name }}'
            Metric: '{{ Metric }}'
            MetricDimension:
              DimensionName: '{{ DimensionName }}'
              Operator: '{{ Operator }}'
            Criteria:
              ComparisonOperator: '{{ ComparisonOperator }}'
              Value:
                Count: '{{ Count }}'
                Cidrs:
                  - '{{ Cidrs[0] }}'
                Ports:
                  - '{{ Ports[0] }}'
                Number: null
                Numbers:
                  - null
                Strings:
                  - '{{ Strings[0] }}'
              DurationSeconds: '{{ DurationSeconds }}'
              ConsecutiveDatapointsToAlarm: '{{ ConsecutiveDatapointsToAlarm }}'
              ConsecutiveDatapointsToClear: '{{ ConsecutiveDatapointsToClear }}'
              StatisticalThreshold:
                Statistic: '{{ Statistic }}'
              MlDetectionConfig:
                ConfidenceLevel: '{{ ConfidenceLevel }}'
            SuppressAlerts: '{{ SuppressAlerts }}'
            ExportMetric: '{{ ExportMetric }}'
      - name: AlertTargets
        value: {}
      - name: AdditionalMetricsToRetainV2
        value:
          - Metric: '{{ Metric }}'
            MetricDimension: null
            ExportMetric: null
      - name: MetricsExportConfig
        value:
          MqttTopic: '{{ MqttTopic }}'
          RoleArn: '{{ RoleArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: TargetArns
        value:
          - '{{ TargetArns[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
iot:DescribeSecurityProfile,
iot:ListTagsForResource,
iot:ListTargetsForSecurityProfile
```

### Update
```json
iot:UpdateSecurityProfile,
iot:ListTargetsForSecurityProfile,
iot:AttachSecurityProfile,
iot:DetachSecurityProfile,
iot:ListTagsForResource,
iot:UntagResource,
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

