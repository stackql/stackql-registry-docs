---
title: keyspace
hide_title: false
hide_table_of_contents: false
keywords:
  - keyspace
  - cassandra
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>keyspace</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keyspace</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>keyspace</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cassandra.keyspace</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>keyspace_name</code></td><td><code>string</code></td><td>Name for Cassandra keyspace</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>replication_specification</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
keyspace_name,
tags,
replication_specification
FROM awscc.cassandra.keyspace
WHERE data__Identifier = '<KeyspaceName>';
```

## Permissions

To operate on the <code>keyspace</code> resource, the following permissions are required:

### Read
```json
cassandra:Select,
cassandra:SelectMultiRegionResource
```

### Update
```json
cassandra:Alter,
cassandra:AlterMultiRegionResource,
cassandra:Select,
cassandra:SelectMultiRegionResource,
cassandra:TagResource,
cassandra:TagMultiRegionResource,
cassandra:UntagResource,
cassandra:UntagMultiRegionResource
```

### Delete
```json
cassandra:Drop,
cassandra:DropMultiRegionResource,
cassandra:Select,
cassandra:SelectMultiRegionResource
```

