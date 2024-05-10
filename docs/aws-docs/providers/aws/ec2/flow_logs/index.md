---
title: flow_logs
hide_title: false
hide_table_of_contents: false
keywords:
  - flow_logs
  - ec2
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


Used to retrieve a list of <code>flow_logs</code> in a region or to create or delete a <code>flow_logs</code> resource, use <code>flow_log</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a VPC flow log, which enables you to capture IP traffic for a specific network interface, subnet, or VPC.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.flow_logs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The Flow Log ID</td></tr>
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
id
FROM aws.ec2.flow_logs
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
 "ResourceId": "{{ ResourceId }}",
 "ResourceType": "{{ ResourceType }}"
}
>>>
--required properties only
INSERT INTO aws.ec2.flow_logs (
 ResourceId,
 ResourceType,
 region
)
SELECT 
{{ .ResourceId }},
 {{ .ResourceType }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "DeliverCrossAccountRole": "{{ DeliverCrossAccountRole }}",
 "DeliverLogsPermissionArn": "{{ DeliverLogsPermissionArn }}",
 "LogDestination": "{{ LogDestination }}",
 "LogDestinationType": "{{ LogDestinationType }}",
 "LogFormat": "{{ LogFormat }}",
 "LogGroupName": "{{ LogGroupName }}",
 "MaxAggregationInterval": "{{ MaxAggregationInterval }}",
 "ResourceId": "{{ ResourceId }}",
 "ResourceType": "{{ ResourceType }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "TrafficType": "{{ TrafficType }}",
 "DestinationOptions": {
  "FileFormat": "{{ FileFormat }}",
  "HiveCompatiblePartitions": "{{ HiveCompatiblePartitions }}",
  "PerHourPartition": "{{ PerHourPartition }}"
 }
}
>>>
--all properties
INSERT INTO aws.ec2.flow_logs (
 DeliverCrossAccountRole,
 DeliverLogsPermissionArn,
 LogDestination,
 LogDestinationType,
 LogFormat,
 LogGroupName,
 MaxAggregationInterval,
 ResourceId,
 ResourceType,
 Tags,
 TrafficType,
 DestinationOptions,
 region
)
SELECT 
 {{ .DeliverCrossAccountRole }},
 {{ .DeliverLogsPermissionArn }},
 {{ .LogDestination }},
 {{ .LogDestinationType }},
 {{ .LogFormat }},
 {{ .LogGroupName }},
 {{ .MaxAggregationInterval }},
 {{ .ResourceId }},
 {{ .ResourceType }},
 {{ .Tags }},
 {{ .TrafficType }},
 {{ .DestinationOptions }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.flow_logs
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>flow_logs</code> resource, the following permissions are required:

### Create
```json
ec2:CreateFlowLogs,
ec2:DescribeFlowLogs,
ec2:CreateTags,
iam:PassRole,
logs:CreateLogDelivery,
s3:GetBucketPolicy,
s3:PutBucketPolicy
```

### Delete
```json
ec2:DeleteFlowLogs,
ec2:DescribeFlowLogs,
logs:DeleteLogDelivery
```

### List
```json
ec2:DescribeFlowLogs
```

