---
title: accounts_account_sas
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts_account_sas
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

Creates, updates, deletes, gets or lists a <code>accounts_account_sas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts_account_sas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.accounts_account_sas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountSasToken" /> | `string` | List SAS credentials of storage account. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__signedExpiry, data__signedPermission, data__signedResourceTypes, data__signedServices" /> | List SAS credentials of a storage account. |

## `SELECT` examples

List SAS credentials of a storage account.


```sql
SELECT
accountSasToken
FROM azure.storage.accounts_account_sas
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__signedExpiry = '{{ data__signedExpiry }}'
AND data__signedPermission = '{{ data__signedPermission }}'
AND data__signedResourceTypes = '{{ data__signedResourceTypes }}'
AND data__signedServices = '{{ data__signedServices }}';
```