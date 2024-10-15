---
title: plans_web_apps_by_hybrid_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - plans_web_apps_by_hybrid_connections
  - app_service
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

Creates, updates, deletes, gets or lists a <code>plans_web_apps_by_hybrid_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>plans_web_apps_by_hybrid_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.plans_web_apps_by_hybrid_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, namespaceName, relayName, resourceGroupName, subscriptionId" /> | Description for Get all apps that use a Hybrid Connection in an App Service Plan. |

## `SELECT` examples

Description for Get all apps that use a Hybrid Connection in an App Service Plan.


```sql
SELECT
column_anon
FROM azure.app_service.plans_web_apps_by_hybrid_connections
WHERE name = '{{ name }}'
AND namespaceName = '{{ namespaceName }}'
AND relayName = '{{ relayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```