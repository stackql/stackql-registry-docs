---
title: storage_systems_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_systems_list_only
  - datasync
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

Lists <code>storage_systems</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/storage_systems/"><code>storage_systems</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_systems_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::StorageSystem.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.storage_systems_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="server_configuration" /></td><td><code>object</code></td><td>The server name and network port required to connect with the management interface of the on-premises storage system.</td></tr>
<tr><td><CopyableCode code="server_credentials" /></td><td><code>object</code></td><td>The username and password for accessing your on-premises storage system's management interface.</td></tr>
<tr><td><CopyableCode code="secrets_manager_arn" /></td><td><code>string</code></td><td>The ARN of a secret stored by AWS Secrets Manager.</td></tr>
<tr><td><CopyableCode code="system_type" /></td><td><code>string</code></td><td>The type of on-premises storage system that DataSync Discovery will analyze.</td></tr>
<tr><td><CopyableCode code="agent_arns" /></td><td><code>array</code></td><td>The ARN of the DataSync agent that connects to and reads from the on-premises storage system's management interface.</td></tr>
<tr><td><CopyableCode code="cloud_watch_log_group_arn" /></td><td><code>string</code></td><td>The ARN of the Amazon CloudWatch log group used to monitor and log discovery job events.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A familiar name for the on-premises storage system.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="storage_system_arn" /></td><td><code>string</code></td><td>The ARN of the on-premises storage system added to DataSync Discovery.</td></tr>
<tr><td><CopyableCode code="connectivity_status" /></td><td><code>string</code></td><td>Indicates whether the DataSync agent can access the on-premises storage system.</td></tr>
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
Lists all <code>storage_systems</code> in a region.
```sql
SELECT
region,
storage_system_arn
FROM aws.datasync.storage_systems_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>storage_systems_list_only</code> resource, see <a href="/providers/aws/datasync/storage_systems/#permissions"><code>storage_systems</code></a>


