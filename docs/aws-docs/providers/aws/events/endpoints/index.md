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


Used to retrieve a list of <code>endpoints</code> in a region or to create or delete a <code>endpoints</code> resource, use <code>endpoint</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Events::Endpoint.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.events.endpoints" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
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
name
FROM aws.events.endpoints
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
 "RoutingConfig": {
  "FailoverConfig": {
   "Primary": {
    "HealthCheck": "{{ HealthCheck }}"
   },
   "Secondary": {
    "Route": "{{ Route }}"
   }
  }
 },
 "EventBuses": [
  {
   "EventBusArn": "{{ EventBusArn }}"
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.events.endpoints (
 RoutingConfig,
 EventBuses,
 region
)
SELECT 
{{ RoutingConfig }},
 {{ EventBuses }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "RoleArn": "{{ RoleArn }}",
 "Description": "{{ Description }}",
 "RoutingConfig": {
  "FailoverConfig": {
   "Primary": {
    "HealthCheck": "{{ HealthCheck }}"
   },
   "Secondary": {
    "Route": "{{ Route }}"
   }
  }
 },
 "ReplicationConfig": {
  "State": "{{ State }}"
 },
 "EventBuses": [
  {
   "EventBusArn": "{{ EventBusArn }}"
  }
 ]
}
>>>
--all properties
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
 {{ Name }},
 {{ RoleArn }},
 {{ Description }},
 {{ RoutingConfig }},
 {{ ReplicationConfig }},
 {{ EventBuses }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
events:DeleteEndpoint,
events:DescribeEndpoint
```

### List
```json
events:ListEndpoints
```

