---
title: storage_accounts_sas_tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_accounts_sas_tokens
  - data_lake_analytics
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

Creates, updates, deletes, gets or lists a <code>storage_accounts_sas_tokens</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_accounts_sas_tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_lake_analytics.storage_accounts_sas_tokens" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accessToken" /> | `string` | The access token for the associated Azure Storage Container. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, containerName, resourceGroupName, storageAccountName, subscriptionId" /> | Gets the SAS token associated with the specified Data Lake Analytics and Azure Storage account and container combination. |

## `SELECT` examples

Gets the SAS token associated with the specified Data Lake Analytics and Azure Storage account and container combination.


```sql
SELECT
accessToken
FROM azure.data_lake_analytics.storage_accounts_sas_tokens
WHERE accountName = '{{ accountName }}'
AND containerName = '{{ containerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageAccountName = '{{ storageAccountName }}'
AND subscriptionId = '{{ subscriptionId }}';
```