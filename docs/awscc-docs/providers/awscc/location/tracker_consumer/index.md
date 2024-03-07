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
Gets an individual <code>tracker_consumer</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tracker_consumer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>tracker_consumer</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.location.tracker_consumer</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>consumer_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tracker_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

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


## Example
```sql
SELECT
region,
consumer_arn,
tracker_name
FROM awscc.location.tracker_consumer
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;TrackerName&gt;'
AND data__Identifier = '&lt;ConsumerArn&gt;'
```
