---
title: integration_accounts_key_vault_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_accounts_key_vault_keys
  - logic_apps
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

Creates, updates, deletes, gets or lists a <code>integration_accounts_key_vault_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_accounts_key_vault_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.integration_accounts_key_vault_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="attributes" /> | `object` | The key attributes. |
| <CopyableCode code="kid" /> | `string` | The key id. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="integrationAccountName, resourceGroupName, subscriptionId, data__keyVault" /> | Gets the integration account's Key Vault keys. |

## `SELECT` examples

Gets the integration account's Key Vault keys.


```sql
SELECT
attributes,
kid
FROM azure.logic_apps.integration_accounts_key_vault_keys
WHERE integrationAccountName = '{{ integrationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__keyVault = '{{ data__keyVault }}';
```