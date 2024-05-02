---
title: components
hide_title: false
hide_table_of_contents: false
keywords:
  - components
  - amplifyuibuilder
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>components</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>components</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::AmplifyUIBuilder::Component Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.amplifyuibuilder.components</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>app_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>environment_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
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
app_id,
environment_name,
id
FROM aws.amplifyuibuilder.components
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>components</code> resource, the following permissions are required:

### Create
```json
amplify:GetApp,
amplifyuibuilder:CreateComponent,
amplifyuibuilder:GetComponent,
amplifyuibuilder:TagResource
```

### List
```json
amplify:GetApp,
amplifyuibuilder:ListComponents
```

