---
title: alarms
hide_title: false
hide_table_of_contents: false
keywords:
  - alarms
  - lightsail
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>alarms</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alarms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lightsail::Alarm</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lightsail.alarms</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>alarm_name</code></td><td><code>string</code></td><td>The name for the alarm. Specify the name of an existing alarm to update, and overwrite the previous configuration of the alarm.</td></tr>
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
alarm_name
FROM aws.lightsail.alarms
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>alarms</code> resource, the following permissions are required:

### Create
```json
lightsail:PutAlarm,
lightsail:GetAlarms
```

### List
```json
lightsail:GetAlarms
```

