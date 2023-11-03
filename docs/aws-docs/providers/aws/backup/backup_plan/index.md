---
title: backup_plan
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_plan
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
Gets an individual <code>backup_plan</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_plan</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.backup.backup_plan</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>BackupPlan</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>BackupPlanTags</code></td><td><code>object</code></td><td></td></tr><tr><td><code>BackupPlanArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>BackupPlanId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>VersionId</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.backup.backup_plan
WHERE region = 'us-east-1' AND data__Identifier = '{BackupPlanId}'
</pre>
