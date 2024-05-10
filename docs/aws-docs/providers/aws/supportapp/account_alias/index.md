---
title: account_alias
hide_title: false
hide_table_of_contents: false
keywords:
  - account_alias
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


Gets or updates an individual <code>account_alias</code> resource, use <code>account_aliases</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account_alias</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An AWS Support App resource that creates, updates, reads, and deletes a customer's account alias.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.supportapp.account_alias" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="account_alias" /></td><td><code>string</code></td><td>An account alias associated with a customer's account.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
account_alias,
account_alias_resource_id
FROM aws.supportapp.account_alias
WHERE region = 'us-east-1' AND data__Identifier = '<AccountAliasResourceId>';
```


## Permissions

To operate on the <code>account_alias</code> resource, the following permissions are required:

### Read
```json
supportapp:GetAccountAlias
```

### Update
```json
supportapp:PutAccountAlias,
supportapp:GetAccountAlias
```

