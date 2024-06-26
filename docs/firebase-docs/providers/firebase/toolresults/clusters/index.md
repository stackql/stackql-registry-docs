---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - toolresults
  - firebase    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/firebase/stackql-firebase-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="firebase.toolresults.clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="activity" /> | `string` | A string that describes the activity of every screen in the cluster. |
| <CopyableCode code="clusterId" /> | `string` | A unique identifier for the cluster. @OutputOnly |
| <CopyableCode code="keyScreen" /> | `object` |  |
| <CopyableCode code="screens" /> | `array` | Full list of screens. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_histories_executions_clusters_get" /> | `SELECT` | <CopyableCode code="clusterId, executionId, historyId, projectId" /> | Retrieves a single screenshot cluster by its ID |
| <CopyableCode code="projects_histories_executions_clusters_list" /> | `SELECT` | <CopyableCode code="executionId, historyId, projectId" /> | Lists Screenshot Clusters Returns the list of screenshot clusters corresponding to an execution. Screenshot clusters are created after the execution is finished. Clusters are created from a set of screenshots. Between any two screenshots, a matching score is calculated based off their metadata that determines how similar they are. Screenshots are placed in the cluster that has screens which have the highest matching scores. |
