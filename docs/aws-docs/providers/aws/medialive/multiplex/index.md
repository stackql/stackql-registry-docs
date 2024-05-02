---
title: multiplex
hide_title: false
hide_table_of_contents: false
keywords:
  - multiplex
  - medialive
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>multiplex</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>multiplex</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaLive::Multiplex</td></tr>
<tr><td><b>Id</b></td><td><code>aws.medialive.multiplex</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The unique arn of the multiplex.</td></tr>
<tr><td><code>availability_zones</code></td><td><code>array</code></td><td>A list of availability zones for the multiplex.</td></tr>
<tr><td><code>destinations</code></td><td><code>array</code></td><td>A list of the multiplex output destinations.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The unique id of the multiplex.</td></tr>
<tr><td><code>multiplex_settings</code></td><td><code>object</code></td><td>Configuration for a multiplex event.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of multiplex.</td></tr>
<tr><td><code>pipelines_running_count</code></td><td><code>integer</code></td><td>The number of currently healthy pipelines.</td></tr>
<tr><td><code>program_count</code></td><td><code>integer</code></td><td>The number of programs in the multiplex.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A collection of key-value pairs.</td></tr>
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
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn,
availability_zones,
destinations,
id,
multiplex_settings,
name,
pipelines_running_count,
program_count,
state,
tags
FROM aws.medialive.multiplex
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>multiplex</code> resource, the following permissions are required:

### Read
```json
medialive:DescribeMultiplex
```

### Update
```json
medialive:UpdateMultiplex,
medialive:DescribeMultiplex,
medialive:CreateTags,
medialive:DeleteTags
```

### Delete
```json
medialive:DeleteMultiplex,
medialive:DescribeMultiplex
```

