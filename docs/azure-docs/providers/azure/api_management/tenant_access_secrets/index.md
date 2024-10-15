---
title: tenant_access_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - tenant_access_secrets
  - api_management
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

Creates, updates, deletes, gets or lists a <code>tenant_access_secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tenant_access_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.tenant_access_secrets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Access Information type ('access' or 'gitAccess') |
| <CopyableCode code="enabled" /> | `boolean` | Determines whether direct access is enabled. |
| <CopyableCode code="primaryKey" /> | `string` | Primary access key. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value. |
| <CopyableCode code="principalId" /> | `string` | Principal (User) Identifier. |
| <CopyableCode code="secondaryKey" /> | `string` | Secondary access key. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accessName, resourceGroupName, serviceName, subscriptionId" /> | Get tenant access information details. |

## `SELECT` examples

Get tenant access information details.


```sql
SELECT
id,
enabled,
primaryKey,
principalId,
secondaryKey
FROM azure.api_management.tenant_access_secrets
WHERE accessName = '{{ accessName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```