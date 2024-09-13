---
title: api_observations
hide_title: false
hide_table_of_contents: false
keywords:
  - api_observations
  - apim
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

Creates, updates, deletes or gets an <code>api_observation</code> resource or lists <code>api_observations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_observations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apim.api_observations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Name of resource |
| <CopyableCode code="apiOperationCount" /> | `string` | The number of observed API Operations. |
| <CopyableCode code="createTime" /> | `string` | Create time stamp |
| <CopyableCode code="hostname" /> | `string` | The hostname of requests processed for this Observation. |
| <CopyableCode code="lastEventDetectedTime" /> | `string` | Last event detected time stamp |
| <CopyableCode code="serverIps" /> | `array` | The IP address (IPv4 or IPv6) of the origin server that the request was sent to. This field can include port information. Examples: `"192.168.1.1"`, `"10.0.0.1:80"`, `"FE80::0202:B3FF:FE1E:8329"`. |
| <CopyableCode code="sourceLocations" /> | `array` | Location of the Observation Source, for example "us-central1" or "europe-west1." |
| <CopyableCode code="style" /> | `string` | Style of ApiObservation |
| <CopyableCode code="tags" /> | `array` | User-defined tags to organize and sort |
| <CopyableCode code="updateTime" /> | `string` | Update time stamp |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiObservationsId, locationsId, observationJobsId, projectsId" /> | GetApiObservation retrieves a single ApiObservation by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, observationJobsId, projectsId" /> | ListApiObservations gets all ApiObservations for a given project and location and ObservationJob. |
| <CopyableCode code="batch_edit_tags" /> | `EXEC` | <CopyableCode code="locationsId, observationJobsId, projectsId" /> | BatchEditTagsApiObservations adds or removes Tags for ApiObservations. |

## `SELECT` examples

ListApiObservations gets all ApiObservations for a given project and location and ObservationJob.

```sql
SELECT
name,
apiOperationCount,
createTime,
hostname,
lastEventDetectedTime,
serverIps,
sourceLocations,
style,
tags,
updateTime
FROM google.apim.api_observations
WHERE locationsId = '{{ locationsId }}'
AND observationJobsId = '{{ observationJobsId }}'
AND projectsId = '{{ projectsId }}'; 
```
