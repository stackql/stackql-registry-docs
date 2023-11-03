---
title: sync_job
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_job
  - iottwinmaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>sync_job</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sync_job</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.iottwinmaker.sync_job</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>WorkspaceId</code></td><td><code>string</code></td><td>The ID of the workspace.</td></tr><tr><td><code>SyncSource</code></td><td><code>string</code></td><td>The source of the SyncJob.</td></tr><tr><td><code>SyncRole</code></td><td><code>string</code></td><td>The IAM Role that execute SyncJob.</td></tr><tr><td><code>CreationDateTime</code></td><td><code>undefined</code></td><td>The date and time when the sync job was created.</td></tr><tr><td><code>UpdateDateTime</code></td><td><code>undefined</code></td><td>The date and time when the sync job was updated.</td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td>The ARN of the SyncJob.</td></tr><tr><td><code>State</code></td><td><code>string</code></td><td>The state of SyncJob.</td></tr><tr><td><code>Tags</code></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.iottwinmaker.sync_job
WHERE region = 'us-east-1' AND data__Identifier = '<WorkspaceId>' AND data__Identifier = '<SyncSource>'
</pre>
