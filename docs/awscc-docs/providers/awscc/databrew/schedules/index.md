---
title: schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - schedules
  - databrew
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>schedules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>schedules</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.databrew.schedules</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Schedule Name</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>schedules</code> resource, the following permissions are required:

### Create
```json
databrew:CreateSchedule,
databrew:TagResource,
databrew:UntagResource,
iam:PassRole
```

### List
```json
databrew:ListSchedules,
databrew:ListTagsForResource,
iam:ListRoles
```


## Example
```sql
SELECT
region,
name
FROM awscc.databrew.schedules
WHERE region = 'us-east-1'
```
