---
title: export
hide_title: false
hide_table_of_contents: false
keywords:
  - export
  - bcmdataexports
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>export</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>export</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::BCMDataExports::Export Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.bcmdataexports.export</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>export</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>export_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
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
export,
export_arn,
tags
FROM aws.bcmdataexports.export
WHERE data__Identifier = '<ExportArn>';
```

## Permissions

To operate on the <code>export</code> resource, the following permissions are required:

### Read
```json
bcm-data-exports:GetExport,
bcm-data-exports:ListTagsForResource
```

### Update
```json
bcm-data-exports:UpdateExport,
bcm-data-exports:TagResource,
bcm-data-exports:UntagResource,
bcm-data-exports:GetExport,
bcm-data-exports:ListTagsForResource
```

### Delete
```json
bcm-data-exports:DeleteExport
```

