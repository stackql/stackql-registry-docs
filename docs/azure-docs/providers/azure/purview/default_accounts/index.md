---
title: default_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - default_accounts
  - purview
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

Creates, updates, deletes, gets or lists a <code>default_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>default_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview.default_accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `string` | The name of the account that is set as the default. |
| <CopyableCode code="resourceGroupName" /> | `string` | The resource group name of the account that is set as the default. |
| <CopyableCode code="scope" /> | `string` | The scope object ID. For example, sub ID or tenant ID. |
| <CopyableCode code="scopeTenantId" /> | `string` | The scope tenant in which the default account is set. |
| <CopyableCode code="scopeType" /> | `string` | The scope where the default account is set. |
| <CopyableCode code="subscriptionId" /> | `string` | The subscription ID of the account that is set as the default. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="scopeTenantId, scopeType" /> | Get the default account for the scope. |
| <CopyableCode code="remove" /> | `EXEC` | <CopyableCode code="scopeTenantId, scopeType" /> | Removes the default account from the scope. |
| <CopyableCode code="set" /> | `EXEC` | <CopyableCode code="" /> | Sets the default account for the scope. |

## `SELECT` examples

Get the default account for the scope.


```sql
SELECT
accountName,
resourceGroupName,
scope,
scopeTenantId,
scopeType,
subscriptionId
FROM azure.purview.default_accounts
WHERE scopeTenantId = '{{ scopeTenantId }}'
AND scopeType = '{{ scopeType }}';
```