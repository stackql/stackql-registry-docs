---
title: matching_workflows_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - matching_workflows_list_only
  - entityresolution
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

Lists <code>matching_workflows</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/matching_workflows/"><code>matching_workflows</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>matching_workflows_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>MatchingWorkflow defined in AWS Entity Resolution service</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.entityresolution.matching_workflows_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="workflow_name" /></td><td><code>string</code></td><td>The name of the MatchingWorkflow</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the MatchingWorkflow</td></tr>
<tr><td><CopyableCode code="input_source_config" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="output_source_config" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="resolution_techniques" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="workflow_arn" /></td><td><code>string</code></td><td>The default MatchingWorkflow arn</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The time of this SchemaMapping got created</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>The time of this SchemaMapping got last updated at</td></tr>
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
Lists all <code>matching_workflows</code> in a region.
```sql
SELECT
region,
workflow_name
FROM aws.entityresolution.matching_workflows_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>matching_workflows_list_only</code> resource, see <a href="/providers/aws/entityresolution/matching_workflows/#permissions"><code>matching_workflows</code></a>


