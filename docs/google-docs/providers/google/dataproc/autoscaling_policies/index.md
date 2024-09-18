---
title: autoscaling_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - autoscaling_policies
  - dataproc
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

Creates, updates, deletes, gets or lists a <code>autoscaling_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>autoscaling_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataproc.autoscaling_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Required. The policy id.The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). Cannot begin or end with underscore or hyphen. Must consist of between 3 and 50 characters. |
| <CopyableCode code="name" /> | `string` | Output only. The "resource name" of the autoscaling policy, as described in https://cloud.google.com/apis/design/resource_names. For projects.regions.autoscalingPolicies, the resource name of the policy has the following format: projects/{project_id}/regions/{region}/autoscalingPolicies/{policy_id} For projects.locations.autoscalingPolicies, the resource name of the policy has the following format: projects/{project_id}/locations/{location}/autoscalingPolicies/{policy_id} |
| <CopyableCode code="basicAlgorithm" /> | `object` | Basic algorithm for autoscaling. |
| <CopyableCode code="labels" /> | `object` | Optional. The labels to associate with this autoscaling policy. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with an autoscaling policy. |
| <CopyableCode code="secondaryWorkerConfig" /> | `object` | Configuration for the size bounds of an instance group, including its proportional size to other groups. |
| <CopyableCode code="workerConfig" /> | `object` | Configuration for the size bounds of an instance group, including its proportional size to other groups. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_autoscaling_policies_get" /> | `SELECT` | <CopyableCode code="autoscalingPoliciesId, locationsId, projectsId" /> | Retrieves autoscaling policy. |
| <CopyableCode code="projects_locations_autoscaling_policies_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists autoscaling policies in the project. |
| <CopyableCode code="projects_regions_autoscaling_policies_get" /> | `SELECT` | <CopyableCode code="autoscalingPoliciesId, projectsId, regionsId" /> | Retrieves autoscaling policy. |
| <CopyableCode code="projects_regions_autoscaling_policies_list" /> | `SELECT` | <CopyableCode code="projectsId, regionsId" /> | Lists autoscaling policies in the project. |
| <CopyableCode code="projects_locations_autoscaling_policies_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates new autoscaling policy. |
| <CopyableCode code="projects_regions_autoscaling_policies_create" /> | `INSERT` | <CopyableCode code="projectsId, regionsId" /> | Creates new autoscaling policy. |
| <CopyableCode code="projects_locations_autoscaling_policies_delete" /> | `DELETE` | <CopyableCode code="autoscalingPoliciesId, locationsId, projectsId" /> | Deletes an autoscaling policy. It is an error to delete an autoscaling policy that is in use by one or more clusters. |
| <CopyableCode code="projects_regions_autoscaling_policies_delete" /> | `DELETE` | <CopyableCode code="autoscalingPoliciesId, projectsId, regionsId" /> | Deletes an autoscaling policy. It is an error to delete an autoscaling policy that is in use by one or more clusters. |
| <CopyableCode code="projects_locations_autoscaling_policies_update" /> | `REPLACE` | <CopyableCode code="autoscalingPoliciesId, locationsId, projectsId" /> | Updates (replaces) autoscaling policy.Disabled check for update_mask, because all updates will be full replacements. |
| <CopyableCode code="projects_regions_autoscaling_policies_update" /> | `REPLACE` | <CopyableCode code="autoscalingPoliciesId, projectsId, regionsId" /> | Updates (replaces) autoscaling policy.Disabled check for update_mask, because all updates will be full replacements. |

## `SELECT` examples

Lists autoscaling policies in the project.

```sql
SELECT
id,
name,
basicAlgorithm,
labels,
secondaryWorkerConfig,
workerConfig
FROM google.dataproc.autoscaling_policies
WHERE projectsId = '{{ projectsId }}'
AND regionsId = '{{ regionsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>autoscaling_policies</code> resource.

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
INSERT INTO google.dataproc.autoscaling_policies (
projectsId,
regionsId,
basicAlgorithm,
workerConfig,
secondaryWorkerConfig,
labels
)
SELECT 
'{{ projectsId }}',
'{{ regionsId }}',
'{{ basicAlgorithm }}',
'{{ workerConfig }}',
'{{ secondaryWorkerConfig }}',
'{{ labels }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
id: string
name: string
basicAlgorithm:
  yarnConfig:
    gracefulDecommissionTimeout: string
    scaleUpFactor: number
    scaleDownFactor: number
    scaleUpMinWorkerFraction: number
    scaleDownMinWorkerFraction: number
  sparkStandaloneConfig:
    gracefulDecommissionTimeout: string
    scaleUpFactor: number
    scaleDownFactor: number
    scaleUpMinWorkerFraction: number
    scaleDownMinWorkerFraction: number
    removeOnlyIdleWorkers: boolean
  cooldownPeriod: string
workerConfig:
  minInstances: integer
  maxInstances: integer
  weight: integer
labels: object

```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>autoscaling_policies</code> resource.

```sql
/*+ update */
REPLACE google.dataproc.autoscaling_policies
SET 
basicAlgorithm = '{{ basicAlgorithm }}',
workerConfig = '{{ workerConfig }}',
secondaryWorkerConfig = '{{ secondaryWorkerConfig }}',
labels = '{{ labels }}'
WHERE 
autoscalingPoliciesId = '{{ autoscalingPoliciesId }}'
AND projectsId = '{{ projectsId }}'
AND regionsId = '{{ regionsId }}';
```

## `DELETE` example

Deletes the specified <code>autoscaling_policies</code> resource.

```sql
/*+ delete */
DELETE FROM google.dataproc.autoscaling_policies
WHERE autoscalingPoliciesId = '{{ autoscalingPoliciesId }}'
AND projectsId = '{{ projectsId }}'
AND regionsId = '{{ regionsId }}';
```
