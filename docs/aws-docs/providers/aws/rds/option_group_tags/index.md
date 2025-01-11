---
title: option_group_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - option_group_tags
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

Expands all tag keys and values for <code>option_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>option_group_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::RDS::OptionGroup</code> resource creates or updates an option group, to enable and configure features that are specific to a particular DB engine.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.option_group_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="option_group_name" /></td><td><code>string</code></td><td>The name of the option group to be created.<br />Constraints:<br />+ Must be 1 to 255 letters, numbers, or hyphens<br />+ First character must be a letter<br />+ Can't end with a hyphen or contain two consecutive hyphens<br /><br />Example: <code>myoptiongroup</code> <br />If you don't specify a value for <code>OptionGroupName</code> property, a name is automatically created for the option group.<br />This value is stored as a lowercase string.</td></tr>
<tr><td><CopyableCode code="option_group_description" /></td><td><code>string</code></td><td>The description of the option group.</td></tr>
<tr><td><CopyableCode code="engine_name" /></td><td><code>string</code></td><td>Specifies the name of the engine that this option group should be associated with.<br />Valid Values: <br />+ <code>mariadb</code> <br />+ <code>mysql</code> <br />+ <code>oracle-ee</code> <br />+ <code>oracle-ee-cdb</code> <br />+ <code>oracle-se2</code> <br />+ <code>oracle-se2-cdb</code> <br />+ <code>postgres</code> <br />+ <code>sqlserver-ee</code> <br />+ <code>sqlserver-se</code> <br />+ <code>sqlserver-ex</code> <br />+ <code>sqlserver-web</code></td></tr>
<tr><td><CopyableCode code="major_engine_version" /></td><td><code>string</code></td><td>Specifies the major version of the engine that this option group should be associated with.</td></tr>
<tr><td><CopyableCode code="option_configurations" /></td><td><code>array</code></td><td>A list of all available options for an option group.</td></tr>
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
Expands tags for all <code>option_groups</code> in a region.
```sql
SELECT
region,
option_group_name,
option_group_description,
engine_name,
major_engine_version,
option_configurations,
tag_key,
tag_value
FROM aws.rds.option_group_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>option_group_tags</code> resource, see <a href="/providers/aws/rds/option_groups/#permissions"><code>option_groups</code></a>

