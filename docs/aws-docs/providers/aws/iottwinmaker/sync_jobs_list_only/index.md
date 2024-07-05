---
title: sync_jobs_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_jobs_list_only
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>sync_jobs</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/sync_jobs/"><code>sync_jobs</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sync_jobs_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTTwinMaker::SyncJob</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iottwinmaker.sync_jobs_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="workspace_id" /></td><td><code>string</code></td><td>The ID of the workspace.</td></tr>
<tr><td><CopyableCode code="sync_source" /></td><td><code>string</code></td><td>The source of the SyncJob.</td></tr>
<tr><td><CopyableCode code="sync_role" /></td><td><code>string</code></td><td>The IAM Role that execute SyncJob.</td></tr>
<tr><td><CopyableCode code="creation_date_time" /></td><td><code>string</code></td><td>The date and time when the sync job was created.</td></tr>
<tr><td><CopyableCode code="update_date_time" /></td><td><code>string</code></td><td>The date and time when the sync job was updated.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the SyncJob.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of SyncJob.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
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
Lists all <code>sync_jobs</code> in a region.
```sql
SELECT
region,
workspace_id,
sync_source
FROM aws.iottwinmaker.sync_jobs_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>sync_jobs_list_only</code> resource, see <a href="/providers/aws/iottwinmaker/sync_jobs/#permissions"><code>sync_jobs</code></a>


