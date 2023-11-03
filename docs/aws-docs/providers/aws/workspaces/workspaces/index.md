---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - workspaces
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>workspaces</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.workspaces.workspaces</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>BundleId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DirectoryId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>RootVolumeEncryptionEnabled</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr><tr><td><code>UserName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>UserVolumeEncryptionEnabled</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>VolumeEncryptionKey</code></td><td><code>string</code></td><td></td></tr><tr><td><code>WorkspaceProperties</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.workspaces.workspaces
WHERE region = 'us-east-1'
```
