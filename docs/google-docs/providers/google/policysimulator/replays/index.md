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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replays</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.policysimulator.replays" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the `Replay`, which has the following format: `&#123;projects\|folders\|organizations&#125;/&#123;resource-id&#125;/locations/global/replays/&#123;replay-id&#125;`, where `&#123;resource-id&#125;` is the ID of the project, folder, or organization that owns the Replay. Example: `projects/my-example-project/locations/global/replays/506a5f7f-38ce-4d7d-8e03-479ce1833c36` |
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
