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

Creates, updates, deletes or gets a <code>monitor</code> resource or lists <code>monitors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a monitor, which defines the monitoring boundaries for measurements that Internet Monitor publishes information about for an application</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.internetmonitor.monitors" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The date value in ISO 8601 format. The timezone is always UTC. (YYYY-MM-DDThh:mm:ssZ)</td></tr>
<tr><td><CopyableCode code="modified_at" /></td><td><code>string</code></td><td>The date value in ISO 8601 format. The timezone is always UTC. (YYYY-MM-DDThh:mm:ssZ)</td></tr>
<tr><td><CopyableCode code="monitor_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="monitor_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="linked_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="include_linked_accounts" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="processing_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="processing_status_info" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resources" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="resources_to_add" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="resources_to_remove" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="max_city_networks_to_monitor" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="traffic_percentage_to_monitor" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="internet_measurements_log_delivery" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="health_events_config" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="MonitorName, region" /></td>
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
List all <code>monitors</code> in a region.
```sql
SELECT
region,
monitor_name
FROM aws.internetmonitor.monitors
WHERE region = 'us-east-1';
```
Gets all properties from a <code>monitor</code>.
```sql
SELECT
region,
created_at,
modified_at,
monitor_arn,
monitor_name,
linked_account_id,
include_linked_accounts,
processing_status,
processing_status_info,
resources,
resources_to_add,
resources_to_remove,
status,
tags,
max_city_networks_to_monitor,
traffic_percentage_to_monitor,
internet_measurements_log_delivery,
health_events_config
FROM aws.internetmonitor.monitors
WHERE region = 'us-east-1' AND data__Identifier = '<MonitorName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>monitor</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.internetmonitor.monitors (
 MonitorName,
 region
)
SELECT 
'{{ MonitorName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ MonitorName }}',
 '{{ LinkedAccountId }}',
 '{{ IncludeLinkedAccounts }}',
 '{{ Resources }}',
 '{{ ResourcesToAdd }}',
 '{{ ResourcesToRemove }}',
 '{{ Status }}',
 '{{ Tags }}',
 '{{ MaxCityNetworksToMonitor }}',
 '{{ TrafficPercentageToMonitor }}',
 '{{ InternetMeasurementsLogDelivery }}',
 '{{ HealthEventsConfig }}',
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
  - name: monitor
    props:
      - name: MonitorName
        value: '{{ MonitorName }}'
      - name: LinkedAccountId
        value: '{{ LinkedAccountId }}'
      - name: IncludeLinkedAccounts
        value: '{{ IncludeLinkedAccounts }}'
      - name: Resources
        value:
          - '{{ Resources[0] }}'
      - name: ResourcesToAdd
        value:
          - '{{ ResourcesToAdd[0] }}'
      - name: ResourcesToRemove
        value:
          - '{{ ResourcesToRemove[0] }}'
      - name: Status
        value: '{{ Status }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: MaxCityNetworksToMonitor
        value: '{{ MaxCityNetworksToMonitor }}'
      - name: TrafficPercentageToMonitor
        value: '{{ TrafficPercentageToMonitor }}'
      - name: InternetMeasurementsLogDelivery
        value:
          S3Config:
            BucketName: '{{ BucketName }}'
            BucketPrefix: '{{ BucketPrefix }}'
            LogDeliveryStatus: '{{ LogDeliveryStatus }}'
      - name: HealthEventsConfig
        value:
          AvailabilityScoreThreshold: null
          PerformanceScoreThreshold: null
          AvailabilityLocalHealthEventsConfig:
            Status: '{{ Status }}'
            HealthScoreThreshold: null
            MinTrafficImpact: null
          PerformanceLocalHealthEventsConfig: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
internetmonitor:GetMonitor,
internetmonitor:ListTagsForResource,
logs:GetLogDelivery
```

### Update
```json
internetmonitor:CreateMonitor,
internetmonitor:GetMonitor,
internetmonitor:UpdateMonitor,
internetmonitor:TagResource,
internetmonitor:UntagResource,
logs:CreateLogDelivery,
logs:GetLogDelivery,
logs:UpdateLogDelivery,
logs:DeleteLogDelivery,
logs:ListLogDeliveries,
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

