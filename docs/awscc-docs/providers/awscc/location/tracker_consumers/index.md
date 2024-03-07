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
Retrieves a list of <code>tracker_consumers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tracker_consumers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>tracker_consumers</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.location.tracker_consumers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>tracker_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>consumer_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>tracker_consumers</code> resource, the following permissions are required:

### Create
```json
geo:AssociateTrackerConsumer,
geo:ListTrackerConsumers
```

### List
```json
geo:ListTrackerConsumers
```


## Example
```sql
SELECT
region,
tracker_name,
consumer_arn
FROM awscc.location.tracker_consumers
WHERE region = 'us-east-1'
```
