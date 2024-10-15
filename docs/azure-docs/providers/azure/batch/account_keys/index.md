---
title: account_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - account_keys
  - batch
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

Creates, updates, deletes, gets or lists a <code>account_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch.account_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `string` | The Batch account name. |
| <CopyableCode code="primary" /> | `string` | The primary key associated with the account. |
| <CopyableCode code="secondary" /> | `string` | The secondary key associated with the account. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | This operation applies only to Batch accounts with allowedAuthenticationModes containing 'SharedKey'. If the Batch account doesn't contain 'SharedKey' in its allowedAuthenticationMode, clients cannot use shared keys to authenticate, and must use another allowedAuthenticationModes instead. In this case, getting the keys will fail. |

## `SELECT` examples

This operation applies only to Batch accounts with allowedAuthenticationModes containing 'SharedKey'. If the Batch account doesn't contain 'SharedKey' in its allowedAuthenticationMode, clients cannot use shared keys to authenticate, and must use another allowedAuthenticationModes instead. In this case, getting the keys will fail.


```sql
SELECT
accountName,
primary,
secondary
FROM azure.batch.account_keys
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```