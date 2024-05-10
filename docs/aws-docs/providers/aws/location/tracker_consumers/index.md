---
title: tracker_consumers
hide_title: false
hide_table_of_contents: false
keywords:
  - tracker_consumers
  - location
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


Used to retrieve a list of <code>tracker_consumers</code> in a region or to create or delete a <code>tracker_consumers</code> resource, use <code>tracker_consumer</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tracker_consumers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Location::TrackerConsumer Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.location.tracker_consumers" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="tracker_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="consumer_arn" /></td><td><code>string</code></td><td></td></tr>
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
tracker_name,
consumer_arn
FROM aws.location.tracker_consumers
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>tracker_consumer</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- tracker_consumer.iql (required properties only)
INSERT INTO aws.location.tracker_consumers (
 ConsumerArn,
 TrackerName,
 region
)
SELECT 
'{{ ConsumerArn }}',
 '{{ TrackerName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- tracker_consumer.iql (all properties)
INSERT INTO aws.location.tracker_consumers (
 ConsumerArn,
 TrackerName,
 region
)
SELECT 
 '{{ ConsumerArn }}',
 '{{ TrackerName }}',
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
  - name: tracker_consumer
    props:
      - name: ConsumerArn
        value: '{{ ConsumerArn }}'
      - name: TrackerName
        value: '{{ TrackerName }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.location.tracker_consumers
WHERE data__Identifier = '<TrackerName|ConsumerArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>tracker_consumers</code> resource, the following permissions are required:

### Create
```json
geo:AssociateTrackerConsumer,
geo:ListTrackerConsumers
```

### Delete
```json
geo:DisassociateTrackerConsumer,
geo:ListTrackerConsumers
```

### List
```json
geo:ListTrackerConsumers
```

