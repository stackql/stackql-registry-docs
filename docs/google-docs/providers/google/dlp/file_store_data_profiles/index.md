---
title: file_store_data_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - file_store_data_profiles
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

Creates, updates, deletes or gets an <code>file_store_data_profile</code> resource or lists <code>file_store_data_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>file_store_data_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dlp.file_store_data_profiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the profile. |
| <CopyableCode code="configSnapshot" /> | `object` | Snapshot of the configurations used to generate the profile. |
| <CopyableCode code="createTime" /> | `string` | The time the file store was first created. |
| <CopyableCode code="dataRiskLevel" /> | `object` | Score is a summary of all elements in the data profile. A higher number means more risk. |
| <CopyableCode code="dataSourceType" /> | `object` | Message used to identify the type of resource being profiled. |
| <CopyableCode code="dataStorageLocations" /> | `array` | For resources that have multiple storage locations, these are those regions. For Cloud Storage this is the list of regions chosen for dual-region storage. `file_store_location` will normally be the corresponding multi-region for the list of individual locations. The first region is always picked as the processing and storage location for the data profile. |
| <CopyableCode code="fileClusterSummaries" /> | `array` | FileClusterSummary per each cluster. |
| <CopyableCode code="fileStoreInfoTypeSummaries" /> | `array` | InfoTypes detected in this file store. |
| <CopyableCode code="fileStoreIsEmpty" /> | `boolean` | The file store does not have any files. |
| <CopyableCode code="fileStoreLocation" /> | `string` | The location of the file store. * Cloud Storage: https://cloud.google.com/storage/docs/locations#available-locations |
| <CopyableCode code="fileStorePath" /> | `string` | The file store path. * Cloud Storage: `gs://{bucket}` |
| <CopyableCode code="fullResource" /> | `string` | The resource name of the resource profiled. https://cloud.google.com/apis/design/resource_names#full_resource_name |
| <CopyableCode code="lastModifiedTime" /> | `string` | The time the file store was last modified. |
| <CopyableCode code="locationType" /> | `string` | The location type of the bucket (region, dual-region, multi-region, etc). If dual-region, expect data_storage_locations to be populated. |
| <CopyableCode code="profileLastGenerated" /> | `string` | The last time the profile was generated. |
| <CopyableCode code="profileStatus" /> | `object` | Success or errors for the profile generation. |
| <CopyableCode code="projectDataProfile" /> | `string` | The resource name of the project data profile for this file store. |
| <CopyableCode code="projectId" /> | `string` | The Google Cloud project ID that owns the resource. |
| <CopyableCode code="resourceAttributes" /> | `object` | Attributes of the resource being profiled. Currently used attributes: * customer_managed_encryption: boolean - true: the resource is encrypted with a customer-managed key. - false: the resource is encrypted with a provider-managed key. |
| <CopyableCode code="resourceLabels" /> | `object` | The labels applied to the resource at the time the profile was generated. |
| <CopyableCode code="resourceVisibility" /> | `string` | How broadly a resource has been shared. |
| <CopyableCode code="sensitivityScore" /> | `object` | Score is calculated from of all elements in the data profile. A higher level means the data is more sensitive. |
| <CopyableCode code="state" /> | `string` | State of a profile. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_locations_file_store_data_profiles_get" /> | `SELECT` | <CopyableCode code="fileStoreDataProfilesId, locationsId, organizationsId" /> | Gets a file store data profile. |
| <CopyableCode code="organizations_locations_file_store_data_profiles_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists file store data profiles for an organization. |
| <CopyableCode code="projects_locations_file_store_data_profiles_get" /> | `SELECT` | <CopyableCode code="fileStoreDataProfilesId, locationsId, projectsId" /> | Gets a file store data profile. |
| <CopyableCode code="projects_locations_file_store_data_profiles_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists file store data profiles for an organization. |
| <CopyableCode code="organizations_locations_file_store_data_profiles_delete" /> | `DELETE` | <CopyableCode code="fileStoreDataProfilesId, locationsId, organizationsId" /> | Delete a FileStoreDataProfile. Will not prevent the profile from being regenerated if the resource is still included in a discovery configuration. |
| <CopyableCode code="projects_locations_file_store_data_profiles_delete" /> | `DELETE` | <CopyableCode code="fileStoreDataProfilesId, locationsId, projectsId" /> | Delete a FileStoreDataProfile. Will not prevent the profile from being regenerated if the resource is still included in a discovery configuration. |

## `SELECT` examples

Lists file store data profiles for an organization.

```sql
SELECT
name,
configSnapshot,
createTime,
dataRiskLevel,
dataSourceType,
dataStorageLocations,
fileClusterSummaries,
fileStoreInfoTypeSummaries,
fileStoreIsEmpty,
fileStoreLocation,
fileStorePath,
fullResource,
lastModifiedTime,
locationType,
profileLastGenerated,
profileStatus,
projectDataProfile,
projectId,
resourceAttributes,
resourceLabels,
resourceVisibility,
sensitivityScore,
state
FROM google.dlp.file_store_data_profiles
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `DELETE` example

Deletes the specified file_store_data_profile resource.

```sql
DELETE FROM google.dlp.file_store_data_profiles
WHERE fileStoreDataProfilesId = '{{ fileStoreDataProfilesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
