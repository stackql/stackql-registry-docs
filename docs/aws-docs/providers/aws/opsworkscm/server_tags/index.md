---
title: server_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - server_tags
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

Expands all tag keys and values for <code>servers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::OpsWorksCM::Server</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.opsworkscm.server_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="key_pair" /></td><td><code>string</code></td><td></td></tr>
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
<tr><td><CopyableCode code="engine" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>servers</code> in a region.
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
engine,
tag_key,
tag_value
FROM aws.opsworkscm.server_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>server_tags</code> resource, see <a href="/providers/aws/opsworkscm/servers/#permissions"><code>servers</code></a>

