---
title: incidents_entities
hide_title: false
hide_table_of_contents: false
keywords:
  - incidents_entities
  - sentinel
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

Creates, updates, deletes, gets or lists a <code>incidents_entities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>incidents_entities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.incidents_entities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="entities" /> | `array` | Array of the incident related entities. |
| <CopyableCode code="metaData" /> | `array` | The metadata from the incident related entities results. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="incidentId, resourceGroupName, subscriptionId, workspaceName" /> | Gets all entities for an incident. |

## `SELECT` examples

Gets all entities for an incident.


```sql
SELECT
entities,
metaData
FROM azure.sentinel.incidents_entities
WHERE incidentId = '{{ incidentId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```