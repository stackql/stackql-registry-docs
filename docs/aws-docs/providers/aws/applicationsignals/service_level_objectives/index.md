---
title: service_level_objectives
hide_title: false
hide_table_of_contents: false
keywords:
  - service_level_objectives
  - applicationsignals
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

Creates, updates, deletes or gets a <code>service_level_objective</code> resource or lists <code>service_level_objectives</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_level_objectives</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ApplicationSignals::ServiceLevelObjective</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.applicationsignals.service_level_objectives" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of this SLO.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of this SLO.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>An optional description for this SLO. Default is 'No description'</td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>integer</code></td><td>Epoch time in seconds of the time that this SLO was created</td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>integer</code></td><td>Epoch time in seconds of the time that this SLO was most recently updated</td></tr>
<tr><td><CopyableCode code="sli" /></td><td><code>object</code></td><td>This structure contains information about the performance metric that an SLO monitors.</td></tr>
<tr><td><CopyableCode code="request_based_sli" /></td><td><code>object</code></td><td>This structure contains information about the performance metric that a request-based SLO monitors.</td></tr>
<tr><td><CopyableCode code="evaluation_type" /></td><td><code>string</code></td><td>Displays whether this is a period-based SLO or a request-based SLO.</td></tr>
<tr><td><CopyableCode code="goal" /></td><td><code>object</code></td><td>A structure that contains the attributes that determine the goal of the SLO. This includes the time period for evaluation and the attainment threshold.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The list of tag keys and values associated with the resource you specified</td></tr>
<tr><td><CopyableCode code="burn_rate_configurations" /></td><td><code>array</code></td><td>Each object in this array defines the length of the look-back window used to calculate one burn rate metric for this SLO. The burn rate measures how fast the service is consuming the error budget, relative to the attainment goal of the SLO.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationsignals-servicelevelobjective.html"><code>AWS::ApplicationSignals::ServiceLevelObjective</code></a>.

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
    <td><CopyableCode code="Name, region" /></td>
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
Gets all <code>service_level_objectives</code> in a region.
```sql
SELECT
region,
arn,
name,
description,
created_time,
last_updated_time,
sli,
request_based_sli,
evaluation_type,
goal,
tags,
burn_rate_configurations
FROM aws.applicationsignals.service_level_objectives
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>service_level_objective</code>.
```sql
SELECT
region,
arn,
name,
description,
created_time,
last_updated_time,
sli,
request_based_sli,
evaluation_type,
goal,
tags,
burn_rate_configurations
FROM aws.applicationsignals.service_level_objectives
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>service_level_objective</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.applicationsignals.service_level_objectives (
 Name,
 region
)
SELECT 
'{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.applicationsignals.service_level_objectives (
 Name,
 Description,
 Sli,
 RequestBasedSli,
 Goal,
 Tags,
 BurnRateConfigurations,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ Sli }}',
 '{{ RequestBasedSli }}',
 '{{ Goal }}',
 '{{ Tags }}',
 '{{ BurnRateConfigurations }}',
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
  - name: service_level_objective
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: Sli
        value:
          SliMetric:
            KeyAttributes: null
            OperationName: '{{ OperationName }}'
            MetricType: '{{ MetricType }}'
            Statistic: '{{ Statistic }}'
            PeriodSeconds: '{{ PeriodSeconds }}'
            MetricDataQueries:
              - MetricStat:
                  Period: '{{ Period }}'
                  Metric:
                    MetricName: '{{ MetricName }}'
                    Dimensions:
                      - Value: '{{ Value }}'
                        Name: '{{ Name }}'
                    Namespace: '{{ Namespace }}'
                  Stat: '{{ Stat }}'
                  Unit: '{{ Unit }}'
                Id: '{{ Id }}'
                ReturnData: '{{ ReturnData }}'
                Expression: '{{ Expression }}'
                AccountId: '{{ AccountId }}'
          MetricThreshold: null
          ComparisonOperator: '{{ ComparisonOperator }}'
      - name: RequestBasedSli
        value:
          RequestBasedSliMetric:
            KeyAttributes: null
            OperationName: '{{ OperationName }}'
            MetricType: '{{ MetricType }}'
            TotalRequestCountMetric: null
            MonitoredRequestCountMetric:
              GoodCountMetric: null
              BadCountMetric: null
          MetricThreshold: null
          ComparisonOperator: '{{ ComparisonOperator }}'
      - name: Goal
        value:
          Interval:
            RollingInterval:
              DurationUnit: '{{ DurationUnit }}'
              Duration: '{{ Duration }}'
            CalendarInterval:
              StartTime: '{{ StartTime }}'
              DurationUnit: null
              Duration: null
          AttainmentGoal: null
          WarningThreshold: null
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: BurnRateConfigurations
        value:
          - LookBackWindowMinutes: '{{ LookBackWindowMinutes }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.applicationsignals.service_level_objectives
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>service_level_objectives</code> resource, the following permissions are required:

### Create
```json
application-signals:CreateServiceLevelObjective,
cloudwatch:GetMetricData,
application-signals:TagResource,
application-signals:GetServiceLevelObjective,
application-signals:ListTagsForResource,
iam:GetRole,
iam:CreateServiceLinkedRole
```

### Read
```json
application-signals:GetServiceLevelObjective,
application-signals:ListTagsForResource
```

### Update
```json
application-signals:UpdateServiceLevelObjective,
cloudwatch:GetMetricData,
application-signals:TagResource,
application-signals:UntagResource,
application-signals:GetServiceLevelObjective,
application-signals:ListTagsForResource
```

### Delete
```json
application-signals:DeleteServiceLevelObjective,
application-signals:UntagResource,
application-signals:GetServiceLevelObjective
```

### List
```json
application-signals:ListServiceLevelObjectives,
application-signals:ListTagsForResource
```
