---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
  - events
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

Creates, updates, deletes or gets an <code>endpoint</code> resource or lists <code>endpoints</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Events::Endpoint.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.events.endpoints" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="routing_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="replication_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="event_buses" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint_url" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="state_reason" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="RoutingConfig, EventBuses, region" /></td>
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
List all <code>endpoints</code> in a region.
```sql
SELECT
region,
name
FROM aws.events.endpoints
WHERE region = 'us-east-1';
```
Gets all properties from an <code>endpoint</code>.
```sql
SELECT
region,
name,
arn,
role_arn,
description,
routing_config,
replication_config,
event_buses,
endpoint_id,
endpoint_url,
state,
state_reason
FROM aws.events.endpoints
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>endpoint</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.events.endpoints (
 RoutingConfig,
 EventBuses,
 region
)
SELECT 
'{{ RoutingConfig }}',
 '{{ EventBuses }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.events.endpoints (
 Name,
 RoleArn,
 Description,
 RoutingConfig,
 ReplicationConfig,
 EventBuses,
 region
)
SELECT 
 '{{ Name }}',
 '{{ RoleArn }}',
 '{{ Description }}',
 '{{ RoutingConfig }}',
 '{{ ReplicationConfig }}',
 '{{ EventBuses }}',
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
  - name: endpoint
    props:
      - name: Name
        value: '{{ Name }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Description
        value: '{{ Description }}'
      - name: RoutingConfig
        value:
          FailoverConfig:
            Primary:
              HealthCheck: '{{ HealthCheck }}'
            Secondary:
              Route: '{{ Route }}'
      - name: ReplicationConfig
        value:
          State: '{{ State }}'
      - name: EventBuses
        value:
          - EventBusArn: '{{ EventBusArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.events.endpoints
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>endpoints</code> resource, the following permissions are required:

### Create
```json
events:CreateEndpoint,
events:DescribeEndpoint,
route53:GetHealthCheck,
iam:PassRole
```

### Read
```json
events:DescribeEndpoint
```

### Update
```json
events:DescribeEndpoint,
events:UpdateEndpoint,
route53:GetHealthCheck,
iam:PassRole
```

### Delete
```json
events:DeleteEndpoint,
events:DescribeEndpoint
```

### List
```json
events:ListEndpoints
```

