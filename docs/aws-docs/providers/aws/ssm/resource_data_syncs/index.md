---
title: resource_data_syncs
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_data_syncs
  - ssm
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>resource_data_syncs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_data_syncs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SSM::ResourceDataSync</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ssm.resource_data_syncs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>sync_name</code></td><td><code>string</code></td><td></td></tr>
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
sync_name
FROM aws.ssm.resource_data_syncs
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>resource_data_syncs</code> resource, the following permissions are required:

### Create
```json
ssm:CreateResourceDataSync,
ssm:ListResourceDataSync
```

### List
```json
ssm:ListResourceDataSync
```

