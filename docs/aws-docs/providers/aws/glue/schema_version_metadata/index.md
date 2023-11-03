---
title: schema_version_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - schema_version_metadata
  - glue
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>schema_version_metadata</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schema_version_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.glue.schema_version_metadata</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>SchemaVersionId</code></td><td><code>string</code></td><td>Represents the version ID associated with the schema version.</td></tr><tr><td><code>Key</code></td><td><code>string</code></td><td>Metadata key</td></tr><tr><td><code>Value</code></td><td><code>string</code></td><td>Metadata value</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.glue.schema_version_metadata
WHERE region = 'us-east-1' AND data__Identifier = '{SchemaVersionId}' AND data__Identifier = '{Key}' AND data__Identifier = '{Value}'
</pre>
