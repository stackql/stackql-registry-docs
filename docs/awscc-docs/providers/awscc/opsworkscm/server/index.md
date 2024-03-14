---
title: server
hide_title: false
hide_table_of_contents: false
keywords:
  - server
  - opsworkscm
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>server</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>server</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.opsworkscm.server</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>key_pair</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>engine_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>disable_automated_backup</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>backup_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>engine_model</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>preferred_maintenance_window</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>associate_public_ip_address</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>instance_profile_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>custom_certificate</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>preferred_backup_window</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>security_group_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>subnet_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>custom_domain</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>endpoint</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>custom_private_key</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>server_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>engine_attributes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>backup_retention_count</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>instance_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>engine</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
key_pair,
engine_version,
service_role_arn,
disable_automated_backup,
backup_id,
engine_model,
preferred_maintenance_window,
associate_public_ip_address,
instance_profile_arn,
custom_certificate,
preferred_backup_window,
security_group_ids,
subnet_ids,
custom_domain,
endpoint,
custom_private_key,
server_name,
engine_attributes,
backup_retention_count,
arn,
instance_type,
tags,
engine
FROM awscc.opsworkscm.server
WHERE data__Identifier = '<ServerName>';
```

## Permissions

To operate on the <code>server</code> resource, the following permissions are required:

### Delete
```json
opsworks-cm:DeleteServer,
opsworks-cm:DescribeServers
```

### Update
```json
opsworks-cm:UpdateServer,
opsworks-cm:TagResource,
opsworks-cm:UntagResource,
opsworks-cm:DescribeServers
```

### Read
```json
opsworks-cm:DescribeServers
```

