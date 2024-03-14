---
title: archive
hide_title: false
hide_table_of_contents: false
keywords:
  - archive
  - events
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>archive</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>archive</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>archive</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.events.archive</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>archive_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>source_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>event_pattern</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>retention_days</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
archive_name,
source_arn,
description,
event_pattern,
arn,
retention_days
FROM awscc.events.archive
WHERE data__Identifier = '<ArchiveName>';
```

## Permissions

To operate on the <code>archive</code> resource, the following permissions are required:

### Delete
```json
events:DescribeArchive,
events:DeleteArchive
```

### Update
```json
events:DescribeArchive,
events:UpdateArchive
```

### Read
```json
events:DescribeArchive
```

