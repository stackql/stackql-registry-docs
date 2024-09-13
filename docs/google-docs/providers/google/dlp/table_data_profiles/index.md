---
title: table_data_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - table_data_profiles
  - dlp
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

Creates, updates, deletes, gets or lists a <code>table_data_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>table_data_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dlp.table_data_profiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the profile. |
| <CopyableCode code="configSnapshot" /> | `object` | Snapshot of the configurations used to generate the profile. |
| <CopyableCode code="createTime" /> | `string` | The time at which the table was created. |
| <CopyableCode code="dataRiskLevel" /> | `object` | Score is a summary of all elements in the data profile. A higher number means more risk. |
| <CopyableCode code="dataSourceType" /> | `object` | Message used to identify the type of resource being profiled. |
| <CopyableCode code="datasetId" /> | `string` | If the resource is BigQuery, the dataset ID. |
| <CopyableCode code="datasetLocation" /> | `string` | If supported, the location where the dataset's data is stored. See https://cloud.google.com/bigquery/docs/locations for supported locations. |
| <CopyableCode code="datasetProjectId" /> | `string` | The Google Cloud project ID that owns the resource. |
| <CopyableCode code="encryptionStatus" /> | `string` | How the table is encrypted. |
| <CopyableCode code="expirationTime" /> | `string` | Optional. The time when this table expires. |
| <CopyableCode code="failedColumnCount" /> | `string` | The number of columns skipped in the table because of an error. |
| <CopyableCode code="fullResource" /> | `string` | The resource name of the resource profiled. https://cloud.google.com/apis/design/resource_names#full_resource_name |
| <CopyableCode code="lastModifiedTime" /> | `string` | The time when this table was last modified |
| <CopyableCode code="otherInfoTypes" /> | `array` | Other infoTypes found in this table's data. |
| <CopyableCode code="predictedInfoTypes" /> | `array` | The infoTypes predicted from this table's data. |
| <CopyableCode code="profileLastGenerated" /> | `string` | The last time the profile was generated. |
| <CopyableCode code="profileStatus" /> | `object` | Success or errors for the profile generation. |
| <CopyableCode code="projectDataProfile" /> | `string` | The resource name of the project data profile for this table. |
| <CopyableCode code="resourceLabels" /> | `object` | The labels applied to the resource at the time the profile was generated. |
| <CopyableCode code="resourceVisibility" /> | `string` | How broadly a resource has been shared. |
| <CopyableCode code="rowCount" /> | `string` | Number of rows in the table when the profile was generated. This will not be populated for BigLake tables. |
| <CopyableCode code="scannedColumnCount" /> | `string` | The number of columns profiled in the table. |
| <CopyableCode code="sensitivityScore" /> | `object` | Score is calculated from of all elements in the data profile. A higher level means the data is more sensitive. |
| <CopyableCode code="state" /> | `string` | State of a profile. |
| <CopyableCode code="tableId" /> | `string` | If the resource is BigQuery, the BigQuery table ID. |
| <CopyableCode code="tableSizeBytes" /> | `string` | The size of the table when the profile was generated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_locations_table_data_profiles_get" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId, tableDataProfilesId" /> | Gets a table data profile. |
| <CopyableCode code="organizations_locations_table_data_profiles_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists table data profiles for an organization. |
| <CopyableCode code="projects_locations_table_data_profiles_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, tableDataProfilesId" /> | Gets a table data profile. |
| <CopyableCode code="projects_locations_table_data_profiles_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists table data profiles for an organization. |
| <CopyableCode code="organizations_locations_table_data_profiles_delete" /> | `DELETE` | <CopyableCode code="locationsId, organizationsId, tableDataProfilesId" /> | Delete a TableDataProfile. Will not prevent the profile from being regenerated if the table is still included in a discovery configuration. |
| <CopyableCode code="projects_locations_table_data_profiles_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, tableDataProfilesId" /> | Delete a TableDataProfile. Will not prevent the profile from being regenerated if the table is still included in a discovery configuration. |

## `SELECT` examples

Lists table data profiles for an organization.

```sql
SELECT
name,
configSnapshot,
createTime,
dataRiskLevel,
dataSourceType,
datasetId,
datasetLocation,
datasetProjectId,
encryptionStatus,
expirationTime,
failedColumnCount,
fullResource,
lastModifiedTime,
otherInfoTypes,
predictedInfoTypes,
profileLastGenerated,
profileStatus,
projectDataProfile,
resourceLabels,
resourceVisibility,
rowCount,
scannedColumnCount,
sensitivityScore,
state,
tableId,
tableSizeBytes
FROM google.dlp.table_data_profiles
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `DELETE` example

Deletes the specified <code>table_data_profiles</code> resource.

```sql
/*+ delete */
DELETE FROM google.dlp.table_data_profiles
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND tableDataProfilesId = '{{ tableDataProfilesId }}';
```
