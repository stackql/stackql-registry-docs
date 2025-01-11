---
title: anomaly_monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - anomaly_monitors
  - ce
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

Creates, updates, deletes or gets an <code>anomaly_monitor</code> resource or lists <code>anomaly_monitors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>anomaly_monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Cost Anomaly Detection leverages advanced Machine Learning technologies to identify anomalous spend and root causes, so you can quickly take action. You can use Cost Anomaly Detection by creating monitor.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ce.anomaly_monitors" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="monitor_arn" /></td><td><code>string</code></td><td>Subscription ARN</td></tr>
<tr><td><CopyableCode code="monitor_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="monitor_name" /></td><td><code>string</code></td><td>The name of the monitor.</td></tr>
<tr><td><CopyableCode code="creation_date" /></td><td><code>string</code></td><td>The date when the monitor was created.</td></tr>
<tr><td><CopyableCode code="last_evaluated_date" /></td><td><code>string</code></td><td>The date when the monitor last evaluated for anomalies.</td></tr>
<tr><td><CopyableCode code="last_updated_date" /></td><td><code>string</code></td><td>The date when the monitor was last updated.</td></tr>
<tr><td><CopyableCode code="monitor_dimension" /></td><td><code>string</code></td><td>The dimensions to evaluate</td></tr>
<tr><td><CopyableCode code="monitor_specification" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="dimensional_value_count" /></td><td><code>integer</code></td><td>The value for evaluated dimensions.</td></tr>
<tr><td><CopyableCode code="resource_tags" /></td><td><code>array</code></td><td>Tags to assign to monitor.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html"><code>AWS::CE::AnomalyMonitor</code></a>.

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
    <td><CopyableCode code="MonitorName, MonitorType, region" /></td>
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
Gets all <code>anomaly_monitors</code> in a region.
```sql
SELECT
region,
monitor_arn,
monitor_type,
monitor_name,
creation_date,
last_evaluated_date,
last_updated_date,
monitor_dimension,
monitor_specification,
dimensional_value_count,
resource_tags
FROM aws.ce.anomaly_monitors
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>anomaly_monitor</code>.
```sql
SELECT
region,
monitor_arn,
monitor_type,
monitor_name,
creation_date,
last_evaluated_date,
last_updated_date,
monitor_dimension,
monitor_specification,
dimensional_value_count,
resource_tags
FROM aws.ce.anomaly_monitors
WHERE region = 'us-east-1' AND data__Identifier = '<MonitorArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>anomaly_monitor</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ce.anomaly_monitors (
 MonitorType,
 MonitorName,
 region
)
SELECT 
'{{ MonitorType }}',
 '{{ MonitorName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ce.anomaly_monitors (
 MonitorType,
 MonitorName,
 MonitorDimension,
 MonitorSpecification,
 ResourceTags,
 region
)
SELECT 
 '{{ MonitorType }}',
 '{{ MonitorName }}',
 '{{ MonitorDimension }}',
 '{{ MonitorSpecification }}',
 '{{ ResourceTags }}',
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
  - name: anomaly_monitor
    props:
      - name: MonitorType
        value: '{{ MonitorType }}'
      - name: MonitorName
        value: '{{ MonitorName }}'
      - name: MonitorDimension
        value: '{{ MonitorDimension }}'
      - name: MonitorSpecification
        value: '{{ MonitorSpecification }}'
      - name: ResourceTags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ce.anomaly_monitors
WHERE data__Identifier = '<MonitorArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>anomaly_monitors</code> resource, the following permissions are required:

### Create
```json
ce:CreateAnomalyMonitor,
ce:TagResource
```

### Read
```json
ce:GetAnomalyMonitors
```

### Update
```json
ce:UpdateAnomalyMonitor
```

### Delete
```json
ce:DeleteAnomalyMonitor
```

### List
```json
ce:GetAnomalyMonitors
```
