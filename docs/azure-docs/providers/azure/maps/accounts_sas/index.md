---
title: accounts_sas
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts_sas
  - maps
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

Creates, updates, deletes, gets or lists a <code>accounts_sas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts_sas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maps.accounts_sas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountSasToken" /> | `string` | The shared access signature access token. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__expiry, data__maxRatePerSecond, data__principalId, data__signingKey, data__start" /> | Create and list an account shared access signature token. Use this SAS token for authentication to Azure Maps REST APIs through various Azure Maps SDKs. As prerequisite to create a SAS Token. 

Prerequisites:
1. Create or have an existing User Assigned Managed Identity in the same Azure region as the account. 
2. Create or update an Azure Maps account with the same Azure region as the User Assigned Managed Identity is placed. |

## `SELECT` examples

Create and list an account shared access signature token. Use this SAS token for authentication to Azure Maps REST APIs through various Azure Maps SDKs. As prerequisite to create a SAS Token. 

Prerequisites:
1. Create or have an existing User Assigned Managed Identity in the same Azure region as the account. 
2. Create or update an Azure Maps account with the same Azure region as the User Assigned Managed Identity is placed.


```sql
SELECT
accountSasToken
FROM azure.maps.accounts_sas
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__expiry = '{{ data__expiry }}'
AND data__maxRatePerSecond = '{{ data__maxRatePerSecond }}'
AND data__principalId = '{{ data__principalId }}'
AND data__signingKey = '{{ data__signingKey }}'
AND data__start = '{{ data__start }}';
```