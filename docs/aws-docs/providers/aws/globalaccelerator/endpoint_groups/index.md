---
title: endpoint_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint_groups
  - globalaccelerator
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


Used to retrieve a list of <code>endpoint_groups</code> in a region or to create or delete a <code>endpoint_groups</code> resource, use <code>endpoint_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::GlobalAccelerator::EndpointGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.globalaccelerator.endpoint_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="endpoint_group_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the endpoint group</td></tr>
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
endpoint_group_arn
FROM aws.globalaccelerator.endpoint_groups
;
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
 "ListenerArn": "{{ ListenerArn }}",
 "EndpointGroupRegion": "{{ EndpointGroupRegion }}"
}
>>>
--required properties only
INSERT INTO aws.globalaccelerator.endpoint_groups (
 ListenerArn,
 EndpointGroupRegion,
 region
)
SELECT 
{{ .ListenerArn }},
 {{ .EndpointGroupRegion }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ListenerArn": "{{ ListenerArn }}",
 "EndpointGroupRegion": "{{ EndpointGroupRegion }}",
 "EndpointConfigurations": [
  {
   "EndpointId": "{{ EndpointId }}",
   "AttachmentArn": "{{ AttachmentArn }}",
   "Weight": "{{ Weight }}",
   "ClientIPPreservationEnabled": "{{ ClientIPPreservationEnabled }}"
  }
 ],
 "TrafficDialPercentage": null,
 "HealthCheckPort": "{{ HealthCheckPort }}",
 "HealthCheckProtocol": "{{ HealthCheckProtocol }}",
 "HealthCheckPath": "{{ HealthCheckPath }}",
 "HealthCheckIntervalSeconds": "{{ HealthCheckIntervalSeconds }}",
 "ThresholdCount": "{{ ThresholdCount }}",
 "PortOverrides": [
  {
   "ListenerPort": "{{ ListenerPort }}",
   "EndpointPort": null
  }
 ]
}
>>>
--all properties
INSERT INTO aws.globalaccelerator.endpoint_groups (
 ListenerArn,
 EndpointGroupRegion,
 EndpointConfigurations,
 TrafficDialPercentage,
 HealthCheckPort,
 HealthCheckProtocol,
 HealthCheckPath,
 HealthCheckIntervalSeconds,
 ThresholdCount,
 PortOverrides,
 region
)
SELECT 
 {{ .ListenerArn }},
 {{ .EndpointGroupRegion }},
 {{ .EndpointConfigurations }},
 {{ .TrafficDialPercentage }},
 {{ .HealthCheckPort }},
 {{ .HealthCheckProtocol }},
 {{ .HealthCheckPath }},
 {{ .HealthCheckIntervalSeconds }},
 {{ .ThresholdCount }},
 {{ .PortOverrides }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.globalaccelerator.endpoint_groups
WHERE data__Identifier = '<EndpointGroupArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>endpoint_groups</code> resource, the following permissions are required:

### Create
```json
globalaccelerator:CreateEndpointGroup,
globalaccelerator:DescribeEndpointGroup,
globalaccelerator:DescribeAccelerator,
globalaccelerator:DescribeListener,
globalaccelerator:ListAccelerators,
globalaccelerator:ListListeners
```

### Delete
```json
globalaccelerator:DeleteEndpointGroup,
globalaccelerator:DescribeEndpointGroup,
globalaccelerator:DescribeAccelerator
```

### List
```json
globalaccelerator:ListEndpointGroups
```

