---
title: work_group_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - work_group_tags
  - athena
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

Expands all tag keys and values for <code>work_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>work_group_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Athena::WorkGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.athena.work_group_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The workGroup name.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The workgroup description.</td></tr>
<tr><td><CopyableCode code="work_group_configuration" /></td><td><code>object</code></td><td>The workgroup configuration</td></tr>
<tr><td><CopyableCode code="work_group_configuration_updates" /></td><td><code>object</code></td><td>The workgroup configuration update object</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The date and time the workgroup was created.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the workgroup: ENABLED or DISABLED.</td></tr>
<tr><td><CopyableCode code="recursive_delete_option" /></td><td><code>boolean</code></td><td>The option to delete the workgroup and its contents even if the workgroup contains any named queries.</td></tr>
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
Expands tags for all <code>work_groups</code> in a region.
```sql
SELECT
region,
name,
description,
work_group_configuration,
work_group_configuration_updates,
creation_time,
state,
recursive_delete_option,
tag_key,
tag_value
FROM aws.athena.work_group_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>work_group_tags</code> resource, see <a href="/providers/aws/athena/work_groups/#permissions"><code>work_groups</code></a>


