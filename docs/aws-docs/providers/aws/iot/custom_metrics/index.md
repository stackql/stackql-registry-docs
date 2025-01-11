---
title: custom_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_metrics
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

Creates, updates, deletes or gets a <code>custom_metric</code> resource or lists <code>custom_metrics</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A custom metric published by your devices to Device Defender.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.custom_metrics" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="metric_name" /></td><td><code>string</code></td><td>The name of the custom metric. This will be used in the metric report submitted from the device/thing. Shouldn't begin with aws: . Cannot be updated once defined.</td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td>Field represents a friendly name in the console for the custom metric; it doesn't have to be unique. Don't use this name as the metric identifier in the device metric report. Can be updated once defined.</td></tr>
<tr><td><CopyableCode code="metric_type" /></td><td><code>string</code></td><td>The type of the custom metric. Types include string-list, ip-address-list, number-list, and number.</td></tr>
<tr><td><CopyableCode code="metric_arn" /></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) of the custom metric.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html"><code>AWS::IoT::CustomMetric</code></a>.

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
    <td><CopyableCode code="MetricType, region" /></td>
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
Gets all <code>custom_metrics</code> in a region.
```sql
SELECT
region,
metric_name,
display_name,
metric_type,
metric_arn,
tags
FROM aws.iot.custom_metrics
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>custom_metric</code>.
```sql
SELECT
region,
metric_name,
display_name,
metric_type,
metric_arn,
tags
FROM aws.iot.custom_metrics
WHERE region = 'us-east-1' AND data__Identifier = '<MetricName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>custom_metric</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iot.custom_metrics (
 MetricType,
 region
)
SELECT 
'{{ MetricType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iot.custom_metrics (
 MetricName,
 DisplayName,
 MetricType,
 Tags,
 region
)
SELECT 
 '{{ MetricName }}',
 '{{ DisplayName }}',
 '{{ MetricType }}',
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
  - name: custom_metric
    props:
      - name: MetricName
        value: '{{ MetricName }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: MetricType
        value: '{{ MetricType }}'
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
DELETE FROM aws.iot.custom_metrics
WHERE data__Identifier = '<MetricName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>custom_metrics</code> resource, the following permissions are required:

### Create
```json
iot:CreateCustomMetric,
iot:TagResource
```

### Read
```json
iot:DescribeCustomMetric,
iot:ListTagsForResource
```

### Update
```json
iot:UpdateCustomMetric,
iot:ListTagsForResource,
iot:UntagResource,
iot:TagResource
```

### Delete
```json
iot:DescribeCustomMetric,
iot:DeleteCustomMetric
```

### List
```json
iot:ListCustomMetrics
```
