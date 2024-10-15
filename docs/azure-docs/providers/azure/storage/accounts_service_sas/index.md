---
title: accounts_service_sas
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts_service_sas
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

Creates, updates, deletes, gets or lists a <code>accounts_service_sas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts_service_sas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.accounts_service_sas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="serviceSasToken" /> | `string` | List service SAS credentials of specific resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__canonicalizedResource" /> | List service SAS credentials of a specific resource. |

## `SELECT` examples

List service SAS credentials of a specific resource.


```sql
SELECT
serviceSasToken
FROM azure.storage.accounts_service_sas
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__canonicalizedResource = '{{ data__canonicalizedResource }}';
```