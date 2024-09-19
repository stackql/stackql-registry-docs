---
title: api_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - api_operations
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

Creates, updates, deletes, gets or lists a <code>api_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apim.api_operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Name of resource |
| <CopyableCode code="count" /> | `string` | The number of occurrences of this API Operation. |
| <CopyableCode code="firstSeenTime" /> | `string` | First seen time stamp |
| <CopyableCode code="httpOperation" /> | `object` | An HTTP-based API Operation, sometimes called a "REST" Operation. |
| <CopyableCode code="lastSeenTime" /> | `string` | Last seen time stamp |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiObservationsId, apiOperationsId, locationsId, observationJobsId, projectsId" /> | GetApiOperation retrieves a single ApiOperation by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="apiObservationsId, locationsId, observationJobsId, projectsId" /> | ListApiOperations gets all ApiOperations for a given project and location and ObservationJob and ApiObservation. |

## `SELECT` examples

ListApiOperations gets all ApiOperations for a given project and location and ObservationJob and ApiObservation.

```sql
SELECT
name,
count,
firstSeenTime,
httpOperation,
lastSeenTime
FROM google.apim.api_operations
WHERE apiObservationsId = '{{ apiObservationsId }}'
AND locationsId = '{{ locationsId }}'
AND observationJobsId = '{{ observationJobsId }}'
AND projectsId = '{{ projectsId }}';
```
