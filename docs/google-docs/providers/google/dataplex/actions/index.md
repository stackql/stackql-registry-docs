---
title: actions
hide_title: false
hide_table_of_contents: false
keywords:
  - actions
  - dataplex
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

Creates, updates, deletes, gets or lists a <code>actions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.actions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the action, of the form: projects/{project}/locations/{location}/lakes/{lake}/actions/{action} projects/{project}/locations/{location}/lakes/{lake}/zones/{zone}/actions/{action} projects/{project}/locations/{location}/lakes/{lake}/zones/{zone}/assets/{asset}/actions/{action}. |
| <CopyableCode code="asset" /> | `string` | Output only. The relative resource name of the asset, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/assets/{asset_id}. |
| <CopyableCode code="category" /> | `string` | The category of issue associated with the action. |
| <CopyableCode code="dataLocations" /> | `array` | The list of data locations associated with this action. Cloud Storage locations are represented as URI paths(E.g. gs://bucket/table1/year=2020/month=Jan/). BigQuery locations refer to resource names(E.g. bigquery.googleapis.com/projects/project-id/datasets/dataset-id). |
| <CopyableCode code="detectTime" /> | `string` | The time that the issue was detected. |
| <CopyableCode code="failedSecurityPolicyApply" /> | `object` | Failed to apply security policy to the managed resource(s) under a lake, zone or an asset. For a lake or zone resource, one or more underlying assets has a failure applying security policy to the associated managed resource. |
| <CopyableCode code="incompatibleDataSchema" /> | `object` | Action details for incompatible schemas detected by discovery. |
| <CopyableCode code="invalidDataFormat" /> | `object` | Action details for invalid or unsupported data files detected by discovery. |
| <CopyableCode code="invalidDataOrganization" /> | `object` | Action details for invalid data arrangement. |
| <CopyableCode code="invalidDataPartition" /> | `object` | Action details for invalid or unsupported partitions detected by discovery. |
| <CopyableCode code="issue" /> | `string` | Detailed description of the issue requiring action. |
| <CopyableCode code="lake" /> | `string` | Output only. The relative resource name of the lake, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}. |
| <CopyableCode code="missingData" /> | `object` | Action details for absence of data detected by discovery. |
| <CopyableCode code="missingResource" /> | `object` | Action details for resource references in assets that cannot be located. |
| <CopyableCode code="unauthorizedResource" /> | `object` | Action details for unauthorized resource issues raised to indicate that the service account associated with the lake instance is not authorized to access or manage the resource associated with an asset. |
| <CopyableCode code="zone" /> | `string` | Output only. The relative resource name of the zone, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_lakes_actions_list" /> | `SELECT` | <CopyableCode code="lakesId, locationsId, projectsId" /> | Lists action resources in a lake. |
| <CopyableCode code="projects_locations_lakes_zones_actions_list" /> | `SELECT` | <CopyableCode code="lakesId, locationsId, projectsId, zonesId" /> | Lists action resources in a zone. |
| <CopyableCode code="projects_locations_lakes_zones_assets_actions_list" /> | `SELECT` | <CopyableCode code="assetsId, lakesId, locationsId, projectsId, zonesId" /> | Lists action resources in an asset. |

## `SELECT` examples

Lists action resources in a lake.

```sql
SELECT
name,
asset,
category,
dataLocations,
detectTime,
failedSecurityPolicyApply,
incompatibleDataSchema,
invalidDataFormat,
invalidDataOrganization,
invalidDataPartition,
issue,
lake,
missingData,
missingResource,
unauthorizedResource,
zone
FROM google.dataplex.actions
WHERE lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
