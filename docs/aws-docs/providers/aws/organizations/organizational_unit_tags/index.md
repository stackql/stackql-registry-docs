---
title: organizational_unit_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - organizational_unit_tags
  - organizations
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

Expands all tag keys and values for <code>organizational_units</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organizational_unit_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>You can use organizational units (OUs) to group accounts together to administer as a single unit. This greatly simplifies the management of your accounts. For example, you can attach a policy-based control to an OU, and all accounts within the OU automatically inherit the policy. You can create multiple OUs within a single organization, and you can create OUs within other OUs. Each OU can contain multiple accounts, and you can move accounts from one OU to another. However, OU names must be unique within a parent OU or root.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.organizations.organizational_unit_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of this OU.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique identifier (ID) associated with this OU.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The friendly name of this OU.</td></tr>
<tr><td><CopyableCode code="parent_id" /></td><td><code>string</code></td><td>The unique identifier (ID) of the parent root or OU that you want to create the new OU in.</td></tr>
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
Expands tags for all <code>organizational_units</code> in a region.
```sql
SELECT
region,
arn,
id,
name,
parent_id,
tag_key,
tag_value
FROM aws.organizations.organizational_unit_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>organizational_unit_tags</code> resource, see <a href="/providers/aws/organizations/organizational_units/#permissions"><code>organizational_units</code></a>

