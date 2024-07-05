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

Creates, updates, deletes or gets an <code>endpoint_group</code> resource or lists <code>endpoint_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::GlobalAccelerator::EndpointGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.globalaccelerator.endpoint_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="listener_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the listener</td></tr>
<tr><td><CopyableCode code="endpoint_group_region" /></td><td><code>string</code></td><td>The name of the AWS Region where the endpoint group is located</td></tr>
<tr><td><CopyableCode code="endpoint_configurations" /></td><td><code>array</code></td><td>The list of endpoint objects.</td></tr>
<tr><td><CopyableCode code="traffic_dial_percentage" /></td><td><code>number</code></td><td>The percentage of traffic to sent to an AWS Region</td></tr>
<tr><td><CopyableCode code="health_check_port" /></td><td><code>integer</code></td><td>The port that AWS Global Accelerator uses to check the health of endpoints in this endpoint group.</td></tr>
<tr><td><CopyableCode code="health_check_protocol" /></td><td><code>string</code></td><td>The protocol that AWS Global Accelerator uses to check the health of endpoints in this endpoint group.</td></tr>
<tr><td><CopyableCode code="health_check_path" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="health_check_interval_seconds" /></td><td><code>integer</code></td><td>The time in seconds between each health check for an endpoint. Must be a value of 10 or 30</td></tr>
<tr><td><CopyableCode code="threshold_count" /></td><td><code>integer</code></td><td>The number of consecutive health checks required to set the state of the endpoint to unhealthy.</td></tr>
<tr><td><CopyableCode code="endpoint_group_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the endpoint group</td></tr>
<tr><td><CopyableCode code="port_overrides" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="ListenerArn, EndpointGroupRegion, region" /></td>
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
Gets all <code>endpoint_groups</code> in a region.
```sql
SELECT
region,
listener_arn,
endpoint_group_region,
endpoint_configurations,
traffic_dial_percentage,
health_check_port,
health_check_protocol,
health_check_path,
health_check_interval_seconds,
threshold_count,
endpoint_group_arn,
port_overrides
FROM aws.globalaccelerator.endpoint_groups
;
```
Gets all properties from an individual <code>endpoint_group</code>.
```sql
SELECT
region,
listener_arn,
endpoint_group_region,
endpoint_configurations,
traffic_dial_percentage,
health_check_port,
health_check_protocol,
health_check_path,
health_check_interval_seconds,
threshold_count,
endpoint_group_arn,
port_overrides
FROM aws.globalaccelerator.endpoint_groups
WHERE data__Identifier = '<EndpointGroupArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>endpoint_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.globalaccelerator.endpoint_groups (
 ListenerArn,
 EndpointGroupRegion,
 region
)
SELECT 
'{{ ListenerArn }}',
 '{{ EndpointGroupRegion }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ ListenerArn }}',
 '{{ EndpointGroupRegion }}',
 '{{ EndpointConfigurations }}',
 '{{ TrafficDialPercentage }}',
 '{{ HealthCheckPort }}',
 '{{ HealthCheckProtocol }}',
 '{{ HealthCheckPath }}',
 '{{ HealthCheckIntervalSeconds }}',
 '{{ ThresholdCount }}',
 '{{ PortOverrides }}',
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
  - name: endpoint_group
    props:
      - name: ListenerArn
        value: '{{ ListenerArn }}'
      - name: EndpointGroupRegion
        value: '{{ EndpointGroupRegion }}'
      - name: EndpointConfigurations
        value:
          - EndpointId: '{{ EndpointId }}'
            AttachmentArn: '{{ AttachmentArn }}'
            Weight: '{{ Weight }}'
            ClientIPPreservationEnabled: '{{ ClientIPPreservationEnabled }}'
      - name: TrafficDialPercentage
        value: null
      - name: HealthCheckPort
        value: '{{ HealthCheckPort }}'
      - name: HealthCheckProtocol
        value: '{{ HealthCheckProtocol }}'
      - name: HealthCheckPath
        value: '{{ HealthCheckPath }}'
      - name: HealthCheckIntervalSeconds
        value: '{{ HealthCheckIntervalSeconds }}'
      - name: ThresholdCount
        value: '{{ ThresholdCount }}'
      - name: PortOverrides
        value:
          - ListenerPort: '{{ ListenerPort }}'
            EndpointPort: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
globalaccelerator:DescribeEndpointGroup
```

### Update
```json
globalaccelerator:UpdateEndpointGroup,
globalaccelerator:DescribeEndpointGroup,
globalaccelerator:DescribeListener,
globalaccelerator:DescribeAccelerator
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

