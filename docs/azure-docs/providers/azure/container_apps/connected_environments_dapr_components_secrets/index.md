---
title: connected_environments_dapr_components_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_environments_dapr_components_secrets
  - container_apps
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

Creates, updates, deletes, gets or lists a <code>connected_environments_dapr_components_secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connected_environments_dapr_components_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.connected_environments_dapr_components_secrets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Secret Name. |
| <CopyableCode code="value" /> | `string` | Secret Value. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="componentName, connectedEnvironmentName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
name,
value
FROM azure.container_apps.connected_environments_dapr_components_secrets
WHERE componentName = '{{ componentName }}'
AND connectedEnvironmentName = '{{ connectedEnvironmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```