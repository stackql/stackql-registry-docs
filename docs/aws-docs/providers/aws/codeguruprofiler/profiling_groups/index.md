---
title: profiling_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - profiling_groups
  - codeguruprofiler
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>profiling_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profiling_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This resource schema represents the Profiling Group resource in the Amazon CodeGuru Profiler service.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.codeguruprofiler.profiling_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>profiling_group_name</code></td><td><code>string</code></td><td>The name of the profiling group.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
profiling_group_name
FROM aws.codeguruprofiler.profiling_groups
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>profiling_groups</code> resource, the following permissions are required:

### Create
```json
sns:Publish,
codeguru-profiler:AddNotificationChannels,
codeguru-profiler:CreateProfilingGroup,
codeguru-profiler:PutPermission,
codeguru-profiler:TagResource
```

### List
```json
codeguru-profiler:ListProfilingGroups,
codeguru-profiler:ListTagsForResource
```

