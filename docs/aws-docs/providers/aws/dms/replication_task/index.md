---
title: replication_task
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_task
  - dms
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>replication_task</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_task</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.dms.replication_task</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ReplicationTaskSettings</code></td><td><code>string</code></td><td></td></tr><tr><td><code>CdcStartPosition</code></td><td><code>string</code></td><td></td></tr><tr><td><code>CdcStopPosition</code></td><td><code>string</code></td><td></td></tr><tr><td><code>MigrationType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>TargetEndpointArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ReplicationInstanceArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>TaskData</code></td><td><code>string</code></td><td></td></tr><tr><td><code>CdcStartTime</code></td><td><code>number</code></td><td></td></tr><tr><td><code>ResourceIdentifier</code></td><td><code>string</code></td><td></td></tr><tr><td><code>TableMappings</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ReplicationTaskIdentifier</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SourceEndpointArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.dms.replication_task
WHERE region = 'us-east-1' AND data__Identifier = '{Id}'
```
