---
title: backup_selections
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_selections
  - backup
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>backup_selections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_selections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.backup.backup_selections</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>BackupPlanId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>BackupSelection</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>SelectionId</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.backup.backup_selections
WHERE region = 'us-east-1'
</pre>
