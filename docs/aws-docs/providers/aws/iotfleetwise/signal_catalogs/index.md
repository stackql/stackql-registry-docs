---
title: signal_catalogs
hide_title: false
hide_table_of_contents: false
keywords:
  - signal_catalogs
  - iotfleetwise
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Used to retrieve a list of <code>signal_catalogs</code> in a region or create a <code>signal_catalogs</code> resource, use <code>signal_catalog</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>signal_catalogs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::IoTFleetWise::SignalCatalog Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iotfleetwise.signal_catalogs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
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
FROM aws.iotfleetwise.signal_catalogs
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>signal_catalogs</code> resource, the following permissions are required:

### Create
```json
iotfleetwise:GetSignalCatalog,
iotfleetwise:CreateSignalCatalog,
iotfleetwise:ListSignalCatalogNodes,
iotfleetwise:ListTagsForResource,
iotfleetwise:TagResource
```

### List
```json
iotfleetwise:ListSignalCatalogs
```

