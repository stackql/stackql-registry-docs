---
title: column_data_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - column_data_profiles
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

Creates, updates, deletes, gets or lists a <code>column_data_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>column_data_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dlp.column_data_profiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the profile. |
| <CopyableCode code="column" /> | `string` | The name of the column. |
| <CopyableCode code="columnInfoType" /> | `object` | The infoType details for this column. |
| <CopyableCode code="columnType" /> | `string` | The data type of a given column. |
| <CopyableCode code="dataRiskLevel" /> | `object` | Score is a summary of all elements in the data profile. A higher number means more risk. |
| <CopyableCode code="datasetId" /> | `string` | The BigQuery dataset ID. |
| <CopyableCode code="datasetLocation" /> | `string` | The BigQuery location where the dataset's data is stored. See https://cloud.google.com/bigquery/docs/locations for supported locations. |
| <CopyableCode code="datasetProjectId" /> | `string` | The Google Cloud project ID that owns the profiled resource. |
| <CopyableCode code="estimatedNullPercentage" /> | `string` | Approximate percentage of entries being null in the column. |
| <CopyableCode code="estimatedUniquenessScore" /> | `string` | Approximate uniqueness of the column. |
| <CopyableCode code="freeTextScore" /> | `number` | The likelihood that this column contains free-form text. A value close to 1 may indicate the column is likely to contain free-form or natural language text. Range in 0-1. |
| <CopyableCode code="otherMatches" /> | `array` | Other types found within this column. List will be unordered. |
| <CopyableCode code="policyState" /> | `string` | Indicates if a policy tag has been applied to the column. |
| <CopyableCode code="profileLastGenerated" /> | `string` | The last time the profile was generated. |
| <CopyableCode code="profileStatus" /> | `object` | Success or errors for the profile generation. |
| <CopyableCode code="sensitivityScore" /> | `object` | Score is calculated from of all elements in the data profile. A higher level means the data is more sensitive. |
| <CopyableCode code="state" /> | `string` | State of a profile. |
| <CopyableCode code="tableDataProfile" /> | `string` | The resource name of the table data profile. |
| <CopyableCode code="tableFullResource" /> | `string` | The resource name of the resource this column is within. |
| <CopyableCode code="tableId" /> | `string` | The BigQuery table ID. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_locations_column_data_profiles_get" /> | `SELECT` | <CopyableCode code="columnDataProfilesId, locationsId, organizationsId" /> | Gets a column data profile. |
| <CopyableCode code="organizations_locations_column_data_profiles_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists column data profiles for an organization. |
| <CopyableCode code="projects_locations_column_data_profiles_get" /> | `SELECT` | <CopyableCode code="columnDataProfilesId, locationsId, projectsId" /> | Gets a column data profile. |
| <CopyableCode code="projects_locations_column_data_profiles_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists column data profiles for an organization. |

## `SELECT` examples

Lists column data profiles for an organization.

```sql
SELECT
name,
column,
columnInfoType,
columnType,
dataRiskLevel,
datasetId,
datasetLocation,
datasetProjectId,
estimatedNullPercentage,
estimatedUniquenessScore,
freeTextScore,
otherMatches,
policyState,
profileLastGenerated,
profileStatus,
sensitivityScore,
state,
tableDataProfile,
tableFullResource,
tableId
FROM google.dlp.column_data_profiles
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
