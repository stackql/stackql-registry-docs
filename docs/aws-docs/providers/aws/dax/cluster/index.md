---
title: cluster
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster
  - dax
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>cluster</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cluster</td></tr>
<tr><td><b>Id</b></td><td><code>aws.dax.cluster</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>s_se_specification</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>cluster_discovery_endpoint_ur_l</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>replication_factor</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>parameter_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>availability_zones</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>i_am_role_ar_n</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>subnet_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>preferred_maintenance_window</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>cluster_endpoint_encryption_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>notification_topic_ar_n</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>security_group_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>node_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>cluster_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>cluster_discovery_endpoint</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
s_se_specification,
cluster_discovery_endpoint_ur_l,
description,
replication_factor,
parameter_group_name,
availability_zones,
i_am_role_ar_n,
subnet_group_name,
preferred_maintenance_window,
cluster_endpoint_encryption_type,
notification_topic_ar_n,
security_group_ids,
node_type,
cluster_name,
cluster_discovery_endpoint,
id,
arn,
tags
FROM aws.dax.cluster
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
