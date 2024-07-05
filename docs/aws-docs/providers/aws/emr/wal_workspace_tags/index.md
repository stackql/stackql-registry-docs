---
title: wal_workspace_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - wal_workspace_tags
  - emr
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

Expands all tag keys and values for <code>wal_workspaces</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>wal_workspace_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::EMR::WALWorkspace Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.emr.wal_workspace_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="wal_workspace_name" /></td><td><code>string</code></td><td>The name of the emrwal container</td></tr>
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
Expands tags for all <code>wal_workspaces</code> in a region.
```sql
SELECT
region,
wal_workspace_name,
tag_key,
tag_value
FROM aws.emr.wal_workspace_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>wal_workspace_tags</code> resource, see <a href="/providers/aws/emr/wal_workspaces/#permissions"><code>wal_workspaces</code></a>


