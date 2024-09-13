---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - dialogflow
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

Creates, updates, deletes or gets an <code>deployment</code> resource or lists <code>deployments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dialogflow.deployments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the deployment. Format: projects//locations//agents//environments//deployments/. |
| <CopyableCode code="endTime" /> | `string` | End time of this deployment. |
| <CopyableCode code="flowVersion" /> | `string` | The name of the flow version for this deployment. Format: projects//locations//agents//flows//versions/. |
| <CopyableCode code="result" /> | `object` | Result of the deployment. |
| <CopyableCode code="startTime" /> | `string` | Start time of this deployment. |
| <CopyableCode code="state" /> | `string` | The current state of the deployment. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_agents_environments_deployments_get" /> | `SELECT` | <CopyableCode code="agentsId, deploymentsId, environmentsId, locationsId, projectsId" /> | Retrieves the specified Deployment. |
| <CopyableCode code="projects_locations_agents_environments_deployments_list" /> | `SELECT` | <CopyableCode code="agentsId, environmentsId, locationsId, projectsId" /> | Returns the list of all deployments in the specified Environment. |

## `SELECT` examples

Returns the list of all deployments in the specified Environment.

```sql
SELECT
name,
endTime,
flowVersion,
result,
startTime,
state
FROM google.dialogflow.deployments
WHERE agentsId = '{{ agentsId }}'
AND environmentsId = '{{ environmentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
