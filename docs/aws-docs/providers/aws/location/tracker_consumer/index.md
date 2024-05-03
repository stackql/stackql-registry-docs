---
title: tracker_consumer
hide_title: false
hide_table_of_contents: false
keywords:
  - tracker_consumer
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

Gets or operates on an individual <code>tracker_consumer</code> resource, use <code>tracker_consumers</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tracker_consumer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Location::TrackerConsumer Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.location.tracker_consumer" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="consumer_arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
consumer_arn,
tracker_name
FROM aws.location.tracker_consumer
WHERE data__Identifier = '<TrackerName>|<ConsumerArn>';
```

## Permissions

To operate on the <code>tracker_consumer</code> resource, the following permissions are required:

### Delete
```json
geo:DisassociateTrackerConsumer,
geo:ListTrackerConsumers
```

### Read
```json
geo:ListTrackerConsumers
```

