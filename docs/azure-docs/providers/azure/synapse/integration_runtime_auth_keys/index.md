---
title: integration_runtime_auth_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtime_auth_keys
  - synapse
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

Creates, updates, deletes, gets or lists a <code>integration_runtime_auth_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_runtime_auth_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.integration_runtime_auth_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="authKey1" /> | `string` | The primary integration runtime authentication key. |
| <CopyableCode code="authKey2" /> | `string` | The secondary integration runtime authentication key. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName" /> | List authentication keys in an integration runtime |
| <CopyableCode code="regenerate" /> | `EXEC` | <CopyableCode code="integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName" /> | Regenerate the authentication key for an integration runtime |

## `SELECT` examples

List authentication keys in an integration runtime


```sql
SELECT
authKey1,
authKey2
FROM azure.synapse.integration_runtime_auth_keys
WHERE integrationRuntimeName = '{{ integrationRuntimeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```