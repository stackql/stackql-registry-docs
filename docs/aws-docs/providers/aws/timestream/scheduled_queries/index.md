---
title: scheduled_queries
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_queries
  - timestream
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

Used to retrieve a list of <code>scheduled_queries</code> in a region or create a <code>scheduled_queries</code> resource, use <code>scheduled_query</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Timestream::ScheduledQuery resource creates a Timestream Scheduled Query.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.timestream.scheduled_queries" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn
FROM aws.timestream.scheduled_queries
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>scheduled_queries</code> resource, the following permissions are required:

### Create
```json
timestream:CreateScheduledQuery,
timestream:DescribeEndpoints
```

### List
```json
timestream:ListScheduledQueries,
timestream:DescribeEndpoints
```

