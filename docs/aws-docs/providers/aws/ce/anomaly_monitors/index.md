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


Used to retrieve a list of <code>anomaly_monitors</code> in a region or to create or delete a <code>anomaly_monitors</code> resource, use <code>anomaly_monitor</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>anomaly_monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Cost Anomaly Detection leverages advanced Machine Learning technologies to identify anomalous spend and root causes, so you can quickly take action. You can use Cost Anomaly Detection by creating monitor.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ce.anomaly_monitors" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="monitor_arn" /></td><td><code>undefined</code></td><td></td></tr>
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
monitor_arn
FROM aws.ce.anomaly_monitors
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
 "MonitorType": "{{ MonitorType }}",
 "MonitorName": "{{ MonitorName }}"
}
>>>
--required properties only
INSERT INTO aws.ce.anomaly_monitors (
 MonitorType,
 MonitorName,
 region
)
SELECT 
{{ .MonitorType }},
 {{ .MonitorName }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "MonitorType": "{{ MonitorType }}",
 "MonitorName": "{{ MonitorName }}",
 "MonitorDimension": "{{ MonitorDimension }}",
 "MonitorSpecification": "{{ MonitorSpecification }}",
 "ResourceTags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.ce.anomaly_monitors (
 MonitorType,
 MonitorName,
 MonitorDimension,
 MonitorSpecification,
 ResourceTags,
 region
)
SELECT 
 {{ .MonitorType }},
 {{ .MonitorName }},
 {{ .MonitorDimension }},
 {{ .MonitorSpecification }},
 {{ .ResourceTags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
ce:DeleteAnomalyMonitor
```

### List
```json
ce:GetAnomalyMonitors
```

