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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>server</code> resource, use <code>servers</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::OpsWorksCM::Server</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.opsworkscm.server" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="key_pair" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="engine_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="disable_automated_backup" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="backup_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="engine_model" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="preferred_maintenance_window" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="associate_public_ip_address" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="instance_profile_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="custom_certificate" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="preferred_backup_window" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="custom_domain" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="custom_private_key" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="server_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="engine_attributes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="backup_retention_count" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="instance_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="engine" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.opsworkscm.server
WHERE region = 'us-east-1' AND data__Identifier = '<ServerName>';
```


## Permissions

To operate on the <code>server</code> resource, the following permissions are required:

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

