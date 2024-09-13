
---
title: replays
hide_title: false
hide_table_of_contents: false
keywords:
  - replays
  - policysimulator
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

Creates, updates, deletes or gets an <code>replay</code> resource or lists <code>replays</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replays</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.policysimulator.replays" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the `Replay`, which has the following format: `{projects|folders|organizations}/{resource-id}/locations/global/replays/{replay-id}`, where `{resource-id}` is the ID of the project, folder, or organization that owns the Replay. Example: `projects/my-example-project/locations/global/replays/506a5f7f-38ce-4d7d-8e03-479ce1833c36` |
| <CopyableCode code="config" /> | `object` | The configuration used for a Replay. |
| <CopyableCode code="resultsSummary" /> | `object` | Summary statistics about the replayed log entries. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the `Replay`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_locations_replays_get" /> | `SELECT` | <CopyableCode code="foldersId, locationsId, replaysId" /> | Gets the specified Replay. Each `Replay` is available for at least 7 days. |
| <CopyableCode code="organizations_locations_replays_get" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId, replaysId" /> | Gets the specified Replay. Each `Replay` is available for at least 7 days. |
| <CopyableCode code="projects_locations_replays_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, replaysId" /> | Gets the specified Replay. Each `Replay` is available for at least 7 days. |
| <CopyableCode code="folders_locations_replays_create" /> | `INSERT` | <CopyableCode code="foldersId, locationsId" /> | Creates and starts a Replay using the given ReplayConfig. |
| <CopyableCode code="organizations_locations_replays_create" /> | `INSERT` | <CopyableCode code="locationsId, organizationsId" /> | Creates and starts a Replay using the given ReplayConfig. |
| <CopyableCode code="projects_locations_replays_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates and starts a Replay using the given ReplayConfig. |

## `SELECT` examples

Gets the specified Replay. Each `Replay` is available for at least 7 days.

```sql
SELECT
name,
config,
resultsSummary,
state
FROM google.policysimulator.replays
WHERE foldersId = '{{ foldersId }}'
AND locationsId = '{{ locationsId }}'
AND replaysId = '{{ replaysId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>replays</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.policysimulator.replays (
foldersId,
locationsId,
name,
config,
state,
resultsSummary
)
SELECT 
'{{ foldersId }}',
'{{ locationsId }}',
'{{ name }}',
'{{ config }}',
'{{ state }}',
'{{ resultsSummary }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: config
        value: '{{ config }}'
      - name: state
        value: '{{ state }}'
      - name: resultsSummary
        value: '{{ resultsSummary }}'

```
</TabItem>
</Tabs>
