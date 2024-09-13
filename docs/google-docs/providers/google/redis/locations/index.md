---
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
  - redis
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.redis.locations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Full resource name for the region. For example: "projects/example-project/locations/us-east1". |
| <CopyableCode code="displayName" /> | `string` | The friendly name for this location, typically a nearby city name. For example, "Tokyo". |
| <CopyableCode code="labels" /> | `object` | Cross-service attributes for the location. For example {"cloud.googleapis.com/region": "us-east1"} |
| <CopyableCode code="locationId" /> | `string` | Resource ID for the region. For example: "us-east1". |
| <CopyableCode code="metadata" /> | `object` | Output only. The set of available zones in the location. The map is keyed by the lowercase ID of each zone, as defined by Compute Engine. These keys can be specified in `location_id` or `alternative_location_id` fields when creating a Redis instance. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Gets information about a location. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists information about the supported locations for this service. |

## `SELECT` examples

Lists information about the supported locations for this service.

```sql
SELECT
name,
displayName,
labels,
locationId,
metadata
FROM google.redis.locations
WHERE projectsId = '{{ projectsId }}'; 
```
