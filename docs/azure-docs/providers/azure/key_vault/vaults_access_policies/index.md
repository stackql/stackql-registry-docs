---
title: vaults_access_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - vaults_access_policies
  - key_vault
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

Creates, updates, deletes, gets or lists a <code>vaults_access_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vaults_access_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.key_vault.vaults_access_policies" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="operationKind, resourceGroupName, subscriptionId, vaultName, data__properties" /> | Update access policies in a key vault in the specified subscription. |

## `REPLACE` example

Replaces all fields in the specified <code>vaults_access_policies</code> resource.

```sql
/*+ update */
REPLACE azure.key_vault.vaults_access_policies
SET 
properties = '{{ properties }}'
WHERE 
operationKind = '{{ operationKind }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}'
AND data__properties = '{{ data__properties }}';
```
