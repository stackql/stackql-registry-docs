---
title: workspace_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_keys
  - quantum
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

Creates, updates, deletes, gets or lists a <code>workspace_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.quantum.workspace_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiKeyEnabled" /> | `boolean` | Indicator of enablement of the Quantum workspace Api keys. |
| <CopyableCode code="primaryConnectionString" /> | `string` | The connection string of the primary api key. |
| <CopyableCode code="primaryKey" /> | `object` | Azure quantum workspace Api key details. |
| <CopyableCode code="secondaryConnectionString" /> | `string` | The connection string of the secondary api key. |
| <CopyableCode code="secondaryKey" /> | `object` | Azure quantum workspace Api key details. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Get the keys to use with the Quantum APIs. A key is used to authenticate and authorize access to the Quantum REST APIs. Only one key is needed at a time; two are given to provide seamless key regeneration. |

## `SELECT` examples

Get the keys to use with the Quantum APIs. A key is used to authenticate and authorize access to the Quantum REST APIs. Only one key is needed at a time; two are given to provide seamless key regeneration.


```sql
SELECT
apiKeyEnabled,
primaryConnectionString,
primaryKey,
secondaryConnectionString,
secondaryKey
FROM azure.quantum.workspace_keys
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```