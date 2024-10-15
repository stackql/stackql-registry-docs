---
title: database_accounts_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - database_accounts_keys
  - cosmos_db
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

Creates, updates, deletes, gets or lists a <code>database_accounts_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>database_accounts_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.database_accounts_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="primaryMasterKey" /> | `string` | Base 64 encoded value of the primary read-write key. |
| <CopyableCode code="primaryReadonlyMasterKey" /> | `string` | Base 64 encoded value of the primary read-only key. |
| <CopyableCode code="secondaryMasterKey" /> | `string` | Base 64 encoded value of the secondary read-write key. |
| <CopyableCode code="secondaryReadonlyMasterKey" /> | `string` | Base 64 encoded value of the secondary read-only key. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists the access keys for the specified Azure Cosmos DB database account. |

## `SELECT` examples

Lists the access keys for the specified Azure Cosmos DB database account.


```sql
SELECT
primaryMasterKey,
primaryReadonlyMasterKey,
secondaryMasterKey,
secondaryReadonlyMasterKey
FROM azure.cosmos_db.database_accounts_keys
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```