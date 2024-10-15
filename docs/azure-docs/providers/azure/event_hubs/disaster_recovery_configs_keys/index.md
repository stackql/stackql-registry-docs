---
title: disaster_recovery_configs_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - disaster_recovery_configs_keys
  - event_hubs
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

Creates, updates, deletes, gets or lists a <code>disaster_recovery_configs_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>disaster_recovery_configs_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_hubs.disaster_recovery_configs_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="aliasPrimaryConnectionString" /> | `string` | Primary connection string of the alias if GEO DR is enabled |
| <CopyableCode code="aliasSecondaryConnectionString" /> | `string` | Secondary  connection string of the alias if GEO DR is enabled |
| <CopyableCode code="keyName" /> | `string` | A string that describes the AuthorizationRule. |
| <CopyableCode code="primaryConnectionString" /> | `string` | Primary connection string of the created namespace AuthorizationRule. |
| <CopyableCode code="primaryKey" /> | `string` | A base64-encoded 256-bit primary key for signing and validating the SAS token. |
| <CopyableCode code="secondaryConnectionString" /> | `string` | Secondary connection string of the created namespace AuthorizationRule. |
| <CopyableCode code="secondaryKey" /> | `string` | A base64-encoded 256-bit primary key for signing and validating the SAS token. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="alias, authorizationRuleName, namespaceName, resourceGroupName, subscriptionId" /> | Gets the primary and secondary connection strings for the Namespace. |

## `SELECT` examples

Gets the primary and secondary connection strings for the Namespace.


```sql
SELECT
aliasPrimaryConnectionString,
aliasSecondaryConnectionString,
keyName,
primaryConnectionString,
primaryKey,
secondaryConnectionString,
secondaryKey
FROM azure.event_hubs.disaster_recovery_configs_keys
WHERE alias = '{{ alias }}'
AND authorizationRuleName = '{{ authorizationRuleName }}'
AND namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```