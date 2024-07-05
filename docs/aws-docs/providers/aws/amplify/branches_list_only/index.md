---
title: branches_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - branches_list_only
  - amplify
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

Lists <code>branches</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/branches/"><code>branches</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>branches_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Amplify::Branch resource creates a new branch within an app.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.amplify.branches_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="app_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="basic_auth_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="backend" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="branch_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="build_spec" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="enable_auto_build" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="enable_performance_mode" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="enable_pull_request_preview" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="environment_variables" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="framework" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="pull_request_environment_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stage" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
Lists all <code>branches</code> in a region.
```sql
SELECT
region,
arn
FROM aws.amplify.branches_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>branches_list_only</code> resource, see <a href="/providers/aws/amplify/branches/#permissions"><code>branches</code></a>


