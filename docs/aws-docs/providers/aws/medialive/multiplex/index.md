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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>multiplex</code> resource, use <code>multiplexes</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>multiplex</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaLive::Multiplex</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.medialive.multiplex" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The unique arn of the multiplex.</td></tr>
<tr><td><CopyableCode code="availability_zones" /></td><td><code>array</code></td><td>A list of availability zones for the multiplex.</td></tr>
<tr><td><CopyableCode code="destinations" /></td><td><code>array</code></td><td>A list of the multiplex output destinations.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique id of the multiplex.</td></tr>
<tr><td><CopyableCode code="multiplex_settings" /></td><td><code>object</code></td><td>Configuration for a multiplex event.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of multiplex.</td></tr>
<tr><td><CopyableCode code="pipelines_running_count" /></td><td><code>integer</code></td><td>The number of currently healthy pipelines.</td></tr>
<tr><td><CopyableCode code="program_count" /></td><td><code>integer</code></td><td>The number of programs in the multiplex.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of key-value pairs.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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

