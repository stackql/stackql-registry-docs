---
title: signal_catalog
hide_title: false
hide_table_of_contents: false
keywords:
  - signal_catalog
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
Gets an individual <code>signal_catalog</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>signal_catalog</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>signal_catalog</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotfleetwise.signal_catalog</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>last_modification_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>node_counts</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>nodes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
creation_time,
description,
last_modification_time,
name,
node_counts,
nodes,
tags
FROM awscc.iotfleetwise.signal_catalog
WHERE region = 'us-east-1'
AND data__Identifier = '{Name}';
```

## Permissions

To operate on the <code>signal_catalog</code> resource, the following permissions are required:

### Read
```json
iotfleetwise:GetSignalCatalog,
iotfleetwise:ListSignalCatalogNodes,
iotfleetwise:ListTagsForResource
```

### Update
```json
iotfleetwise:GetSignalCatalog,
iotfleetwise:UpdateSignalCatalog,
iotfleetwise:ListSignalCatalogNodes,
iotfleetwise:ListTagsForResource,
iotfleetwise:TagResource,
iotfleetwise:UntagResource
```

### Delete
```json
iotfleetwise:GetSignalCatalog,
iotfleetwise:DeleteSignalCatalog
```

