---
title: database_accounts_connection_strings
hide_title: false
hide_table_of_contents: false
keywords:
  - database_accounts_connection_strings
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

Creates, updates, deletes, gets or lists a <code>database_accounts_connection_strings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>database_accounts_connection_strings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.database_accounts_connection_strings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="connectionStrings" /> | `array` | An array that contains the connection strings for the Cosmos DB account. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists the connection strings for the specified Azure Cosmos DB database account. |

## `SELECT` examples

Lists the connection strings for the specified Azure Cosmos DB database account.


```sql
SELECT
connectionStrings
FROM azure.cosmos_db.database_accounts_connection_strings
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```