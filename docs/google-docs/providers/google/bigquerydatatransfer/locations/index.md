---
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
  - bigquerydatatransfer
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

Creates, updates, deletes or gets an <code>location</code> resource or lists <code>locations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.bigquerydatatransfer.locations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name for the location, which may vary between implementations. For example: `"projects/example-project/locations/us-east1"` |
| <CopyableCode code="displayName" /> | `string` | The friendly name for this location, typically a nearby city name. For example, "Tokyo". |
| <CopyableCode code="labels" /> | `object` | Cross-service attributes for the location. For example {"cloud.googleapis.com/region": "us-east1"} |
| <CopyableCode code="locationId" /> | `string` | The canonical id for this location. For example: `"us-east1"`. |
| <CopyableCode code="metadata" /> | `object` | Service-specific metadata. For example the available capacity at the given location. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Gets information about a location. |
| <CopyableCode code="projects_locations_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists information about the supported locations for this service. |
| <CopyableCode code="projects_locations_enroll_data_sources" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Enroll data sources in a user project. This allows users to create transfer configurations for these data sources. They will also appear in the ListDataSources RPC and as such, will appear in the [BigQuery UI](https://console.cloud.google.com/bigquery), and the documents can be found in the public guide for [BigQuery Web UI](https://cloud.google.com/bigquery/bigquery-web-ui) and [Data Transfer Service](https://cloud.google.com/bigquery/docs/working-with-transfers). |
| <CopyableCode code="projects_locations_unenroll_data_sources" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Unenroll data sources in a user project. This allows users to remove transfer configurations for these data sources. They will no longer appear in the ListDataSources RPC and will also no longer appear in the [BigQuery UI](https://console.cloud.google.com/bigquery). Data transfers configurations of unenrolled data sources will not be scheduled. |

## `SELECT` examples

Lists information about the supported locations for this service.

```sql
SELECT
name,
displayName,
labels,
locationId,
metadata
FROM google.bigquerydatatransfer.locations
WHERE projectsId = '{{ projectsId }}'; 
```
