---
title: container_apps_revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - container_apps_revisions
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

Creates, updates, deletes, gets or lists a <code>container_apps_revisions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>container_apps_revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.container_apps_revisions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="location" /> | `string` | Resource Location. |
| <CopyableCode code="properties" /> | `object` | Revision resource specific properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="containerAppName, name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="containerAppName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="activate_revision" /> | `EXEC` | <CopyableCode code="containerAppName, name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="deactivate_revision" /> | `EXEC` | <CopyableCode code="containerAppName, name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="restart_revision" /> | `EXEC` | <CopyableCode code="containerAppName, name, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
id,
name,
kind,
location,
properties,
tags,
type
FROM azure.app_service.container_apps_revisions
WHERE containerAppName = '{{ containerAppName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```