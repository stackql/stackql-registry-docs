---
title: option_groups_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - option_groups_list_only
  - rds
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

Lists <code>option_groups</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/option_groups/"><code>option_groups</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>option_groups_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::RDS::OptionGroup resource creates an option group, to enable and configure features that are specific to a particular DB engine.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.option_groups_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="option_group_name" /></td><td><code>string</code></td><td>Specifies the name of the option group.</td></tr>
<tr><td><CopyableCode code="option_group_description" /></td><td><code>string</code></td><td>Provides a description of the option group.</td></tr>
<tr><td><CopyableCode code="engine_name" /></td><td><code>string</code></td><td>Indicates the name of the engine that this option group can be applied to.</td></tr>
<tr><td><CopyableCode code="major_engine_version" /></td><td><code>string</code></td><td>Indicates the major engine version associated with this option group.</td></tr>
<tr><td><CopyableCode code="option_configurations" /></td><td><code>array</code></td><td>Indicates what options are available in the option group.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
Lists all <code>option_groups</code> in a region.
```sql
SELECT
region,
option_group_name
FROM aws.rds.option_groups_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>option_groups_list_only</code> resource, see <a href="/providers/aws/rds/option_groups/#permissions"><code>option_groups</code></a>


