---
title: revision_replicas
hide_title: false
hide_table_of_contents: false
keywords:
  - revision_replicas
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

Creates, updates, deletes, gets or lists a <code>revision_replicas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>revision_replicas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.revision_replicas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Replica resource specific properties |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="containerAppName, replicaName, resourceGroupName, revisionName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="containerAppName, resourceGroupName, revisionName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
properties
FROM azure.container_apps.revision_replicas
WHERE containerAppName = '{{ containerAppName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND revisionName = '{{ revisionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```