---
title: scheduled_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_actions
  - redshift
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>scheduled_actions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>scheduled_actions</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.redshift.scheduled_actions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>scheduled_action_name</code></td><td><code>string</code></td><td>The name of the scheduled action. The name must be unique within an account.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>scheduled_actions</code> resource, the following permissions are required:

### Create
<pre>
redshift:CreateScheduledAction,
redshift:DescribeScheduledActions,
redshift:DescribeTags,
redshift:PauseCluster,
redshift:ResumeCluster,
redshift:ResizeCluster,
iam:PassRole</pre>

### List
<pre>
redshift:DescribeTags,
redshift:DescribeScheduledActions</pre>


## Example
```sql
SELECT
region,
scheduled_action_name
FROM awscc.redshift.scheduled_actions
WHERE region = 'us-east-1'
```
