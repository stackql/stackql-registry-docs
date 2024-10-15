---
title: accounts_customer_initiated_migrations
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts_customer_initiated_migrations
  - storage
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>accounts_customer_initiated_migrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts_customer_initiated_migrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.accounts_customer_initiated_migrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Migration Resource Id |
| <CopyableCode code="name" /> | `string` | current value is 'default' for customer initiated migration |
| <CopyableCode code="properties" /> | `object` | The properties of a storage account’s ongoing or enqueued migration. |
| <CopyableCode code="type" /> | `string` | SrpAccountMigrationType in ARM contract which is 'accountMigrations' |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, migrationName, resourceGroupName, subscriptionId" /> | Gets the status of the ongoing migration for the specified storage account. |

## `SELECT` examples

Gets the status of the ongoing migration for the specified storage account.


```sql
SELECT
id,
name,
properties,
type
FROM azure.storage.accounts_customer_initiated_migrations
WHERE accountName = '{{ accountName }}'
AND migrationName = '{{ migrationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```