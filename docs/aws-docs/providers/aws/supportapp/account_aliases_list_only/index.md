---
title: account_aliases_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - account_aliases_list_only
  - supportapp
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

Lists <code>account_aliases</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/account_aliases/"><code>account_aliases</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account_aliases_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An AWS Support App resource that creates, updates, reads, and deletes a customer's account alias.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.supportapp.account_aliases_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="account_alias" /></td><td><code>string</code></td><td>An account alias associated with a customer's account.</td></tr>
<tr><td><CopyableCode code="account_alias_resource_id" /></td><td><code>string</code></td><td>Unique identifier representing an alias tied to an account</td></tr>
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
Lists all <code>account_aliases</code> in a region.
```sql
SELECT
region,
account_alias_resource_id
FROM aws.supportapp.account_aliases_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>account_aliases_list_only</code> resource, see <a href="/providers/aws/supportapp/account_aliases/#permissions"><code>account_aliases</code></a>


