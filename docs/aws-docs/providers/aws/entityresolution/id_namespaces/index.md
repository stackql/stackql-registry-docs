---
title: id_namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - id_namespaces
  - entityresolution
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>id_namespaces</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>id_namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>IdNamespace defined in AWS Entity Resolution service</td></tr>
<tr><td><b>Id</b></td><td><code>aws.entityresolution.id_namespaces</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id_namespace_name</code></td><td><code>undefined</code></td><td></td></tr>
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
id_namespace_name
FROM aws.entityresolution.id_namespaces
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>id_namespaces</code> resource, the following permissions are required:

### Create
```json
entityresolution:CreateIdNamespace,
entityresolution:TagResource,
iam:PassRole
```

### List
```json
entityresolution:ListIdNamespaces
```

