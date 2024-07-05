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

Creates, updates, deletes or gets a <code>tracker_consumer</code> resource or lists <code>tracker_consumers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tracker_consumers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Location::TrackerConsumer Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.location.tracker_consumers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="consumer_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tracker_name" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="ConsumerArn, TrackerName, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>tracker_consumers</code> in a region.
```sql
SELECT
region,
consumer_arn,
tracker_name
FROM aws.location.tracker_consumers
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>tracker_consumer</code>.
```sql
SELECT
region,
consumer_arn,
tracker_name
FROM aws.location.tracker_consumers
WHERE region = 'us-east-1' AND data__Identifier = '<TrackerName>|<ConsumerArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tracker_consumer</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
geo:ListTrackerConsumers
```

