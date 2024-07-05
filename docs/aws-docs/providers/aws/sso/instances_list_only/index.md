---
title: instances_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_list_only
  - sso
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

Lists <code>instances</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/instances/"><code>instances</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for Identity Center (SSO) Instance</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sso.instances_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name you want to assign to this Identity Center (SSO) Instance</td></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The SSO Instance ARN that is returned upon creation of the Identity Center (SSO) Instance</td></tr>
<tr><td><CopyableCode code="owner_account_id" /></td><td><code>string</code></td><td>The AWS accountId of the owner of the Identity Center (SSO) Instance</td></tr>
<tr><td><CopyableCode code="identity_store_id" /></td><td><code>string</code></td><td>The ID of the identity store associated with the created Identity Center (SSO) Instance</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the Identity Center (SSO) Instance, create_in_progress/delete_in_progress/active</td></tr>
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
Lists all <code>instances</code> in a region.
```sql
SELECT
region,
instance_arn
FROM aws.sso.instances_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>instances_list_only</code> resource, see <a href="/providers/aws/sso/instances/#permissions"><code>instances</code></a>


