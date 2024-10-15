---
title: namespaces_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces_keys
  - relay
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

Creates, updates, deletes, gets or lists a <code>namespaces_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>namespaces_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.relay.namespaces_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="keyName" /> | `string` | A string that describes the authorization rule. |
| <CopyableCode code="primaryConnectionString" /> | `string` | Primary connection string of the created namespace authorization rule. |
| <CopyableCode code="primaryKey" /> | `string` | A base64-encoded 256-bit primary key for signing and validating the SAS token. |
| <CopyableCode code="secondaryConnectionString" /> | `string` | Secondary connection string of the created namespace authorization rule. |
| <CopyableCode code="secondaryKey" /> | `string` | A base64-encoded 256-bit secondary key for signing and validating the SAS token. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="authorizationRuleName, namespaceName, resourceGroupName, subscriptionId" /> | Primary and secondary connection strings to the namespace. |

## `SELECT` examples

Primary and secondary connection strings to the namespace.


```sql
SELECT
keyName,
primaryConnectionString,
primaryKey,
secondaryConnectionString,
secondaryKey
FROM azure.relay.namespaces_keys
WHERE authorizationRuleName = '{{ authorizationRuleName }}'
AND namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```