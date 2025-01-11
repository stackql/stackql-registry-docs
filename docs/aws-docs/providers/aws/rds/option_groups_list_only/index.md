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
<tr><td><b>Description</b></td><td>The <code>AWS::RDS::OptionGroup</code> resource creates or updates an option group, to enable and configure features that are specific to a particular DB engine.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.option_groups_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="option_group_name" /></td><td><code>string</code></td><td>The name of the option group to be created.<br />Constraints:<br />+ Must be 1 to 255 letters, numbers, or hyphens<br />+ First character must be a letter<br />+ Can't end with a hyphen or contain two consecutive hyphens<br /><br />Example: <code>myoptiongroup</code> <br />If you don't specify a value for <code>OptionGroupName</code> property, a name is automatically created for the option group.<br />This value is stored as a lowercase string.</td></tr>
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

