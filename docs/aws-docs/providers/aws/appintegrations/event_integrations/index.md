---
title: event_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - event_integrations
  - appintegrations
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>event_integrations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppIntegrations::EventIntegration</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appintegrations.event_integrations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the event integration.</td></tr>
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
name
FROM aws.appintegrations.event_integrations
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>event_integrations</code> resource, the following permissions are required:

### Create
```json
app-integrations:CreateEventIntegration,
app-integrations:TagResource
```

### List
```json
app-integrations:ListEventIntegrations
```

