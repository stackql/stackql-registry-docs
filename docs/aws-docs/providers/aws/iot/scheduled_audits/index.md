---
title: scheduled_audits
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_audits
  - iot
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>scheduled_audits</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_audits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Scheduled audits can be used to specify the checks you want to perform during an audit and how often the audit should be run.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iot.scheduled_audits</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>scheduled_audit_name</code></td><td><code>string</code></td><td>The name you want to give to the scheduled audit.</td></tr>
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
scheduled_audit_name
FROM aws.iot.scheduled_audits
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>scheduled_audits</code> resource, the following permissions are required:

### Create
```json
iot:CreateScheduledAudit,
iot:DescribeScheduledAudit,
iot:TagResource
```

### List
```json
iot:ListScheduledAudits
```

