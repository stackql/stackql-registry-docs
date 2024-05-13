---
title: metric_streams
hide_title: false
hide_table_of_contents: false
keywords:
  - metric_streams
  - cloudwatch
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


Used to retrieve a list of <code>metric_streams</code> in a region or to create or delete a <code>metric_streams</code> resource, use <code>metric_stream</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metric_streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for Metric Stream</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudwatch.metric_streams" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the metric stream.</td></tr>
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
    <td><CopyableCode code="FirehoseArn, RoleArn, OutputFormat, region" /></td>
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
FROM aws.cloudwatch.metric_streams
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>metric_stream</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cloudwatch.metric_streams (
 FirehoseArn,
 RoleArn,
 OutputFormat,
 region
)
SELECT 
'{{ FirehoseArn }}',
 '{{ RoleArn }}',
 '{{ OutputFormat }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cloudwatch.metric_streams (
 ExcludeFilters,
 FirehoseArn,
 IncludeFilters,
 Name,
 RoleArn,
 OutputFormat,
 StatisticsConfigurations,
 Tags,
 IncludeLinkedAccountsMetrics,
 region
)
SELECT 
 '{{ ExcludeFilters }}',
 '{{ FirehoseArn }}',
 '{{ IncludeFilters }}',
 '{{ Name }}',
 '{{ RoleArn }}',
 '{{ OutputFormat }}',
 '{{ StatisticsConfigurations }}',
 '{{ Tags }}',
 '{{ IncludeLinkedAccountsMetrics }}',
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
  - name: metric_stream
    props:
      - name: ExcludeFilters
        value:
          - Namespace: '{{ Namespace }}'
            MetricNames:
              - '{{ MetricNames[0] }}'
      - name: FirehoseArn
        value: '{{ FirehoseArn }}'
      - name: IncludeFilters
        value:
          - null
      - name: Name
        value: '{{ Name }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: OutputFormat
        value: '{{ OutputFormat }}'
      - name: StatisticsConfigurations
        value:
          - AdditionalStatistics:
              - '{{ AdditionalStatistics[0] }}'
            IncludeMetrics:
              - MetricName: '{{ MetricName }}'
                Namespace: '{{ Namespace }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: IncludeLinkedAccountsMetrics
        value: '{{ IncludeLinkedAccountsMetrics }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.cloudwatch.metric_streams
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>metric_streams</code> resource, the following permissions are required:

### Create
```json
cloudwatch:PutMetricStream,
cloudwatch:GetMetricStream,
cloudwatch:TagResource,
iam:PassRole
```

### Delete
```json
cloudwatch:DeleteMetricStream,
cloudwatch:GetMetricStream
```

### List
```json
cloudwatch:ListMetricStreams
```

