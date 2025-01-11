---
title: organizational_units_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - organizational_units_list_only
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

Lists <code>organizational_units</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/organizational_units/"><code>organizational_units</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organizational_units_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>You can use organizational units (OUs) to group accounts together to administer as a single unit. This greatly simplifies the management of your accounts. For example, you can attach a policy-based control to an OU, and all accounts within the OU automatically inherit the policy. You can create multiple OUs within a single organization, and you can create OUs within other OUs. Each OU can contain multiple accounts, and you can move accounts from one OU to another. However, OU names must be unique within a parent OU or root.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.organizations.organizational_units_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique identifier (ID) associated with this OU.</td></tr>
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
Lists all <code>organizational_units</code> in a region.
```sql
SELECT
region,
id
FROM aws.organizations.organizational_units_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>organizational_units_list_only</code> resource, see <a href="/providers/aws/organizations/organizational_units/#permissions"><code>organizational_units</code></a>

