---
title: profiles_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles_list_only
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

Lists <code>profiles</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/profiles/"><code>profiles</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profiles_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RolesAnywhere::Profile Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rolesanywhere.profiles_list_only" /></td></tr>
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
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="attribute_mappings" /></td><td><code>array</code></td><td></td></tr>
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
Lists all <code>profiles</code> in a region.
```sql
SELECT
region,
profile_id
FROM aws.rolesanywhere.profiles_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>profiles_list_only</code> resource, see <a href="/providers/aws/rolesanywhere/profiles/#permissions"><code>profiles</code></a>


