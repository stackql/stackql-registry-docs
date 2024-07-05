---
title: queues_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - queues_list_only
  - deadline
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

Lists <code>queues</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/queues/"><code>queues</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queues_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Deadline::Queue Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.deadline.queues_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="allowed_storage_profile_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="default_budget_action" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="farm_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="job_attachment_settings" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="job_run_as_user" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="queue_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="required_file_system_location_names" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>queues</code> in a region.
```sql
SELECT
region,
arn
FROM aws.deadline.queues_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>queues_list_only</code> resource, see <a href="/providers/aws/deadline/queues/#permissions"><code>queues</code></a>


