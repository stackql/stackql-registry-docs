---
title: profile_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - profile_tags
  - rolesanywhere
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

Expands all tag keys and values for <code>profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profile_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RolesAnywhere::Profile Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rolesanywhere.profile_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="duration_seconds" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="enabled" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="managed_policy_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="profile_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="profile_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="require_instance_properties" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="session_policy" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="attribute_mappings" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="accept_role_session_name" /></td><td><code>boolean</code></td><td></td></tr>
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
Expands tags for all <code>profiles</code> in a region.
```sql
SELECT
region,
duration_seconds,
enabled,
managed_policy_arns,
name,
profile_arn,
profile_id,
require_instance_properties,
role_arns,
session_policy,
attribute_mappings,
accept_role_session_name,
tag_key,
tag_value
FROM aws.rolesanywhere.profile_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>profile_tags</code> resource, see <a href="/providers/aws/rolesanywhere/profiles/#permissions"><code>profiles</code></a>

