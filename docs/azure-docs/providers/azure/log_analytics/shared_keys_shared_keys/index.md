---
title: shared_keys_shared_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - shared_keys_shared_keys
  - log_analytics
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

Creates, updates, deletes, gets or lists a <code>shared_keys_shared_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>shared_keys_shared_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.shared_keys_shared_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="primarySharedKey" /> | `string` | The primary shared key of a workspace. |
| <CopyableCode code="secondarySharedKey" /> | `string` | The secondary shared key of a workspace. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets the shared keys for a workspace. |

## `SELECT` examples

Gets the shared keys for a workspace.


```sql
SELECT
primarySharedKey,
secondarySharedKey
FROM azure.log_analytics.shared_keys_shared_keys
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```