---
title: partitions
hide_title: false
hide_table_of_contents: false
keywords:
  - partitions
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>partitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="dataplex.partitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Partition values used in the HTTP URL must be double encoded. For example, url_encode(url_encode(value)) can be used to encode "US:CA/CA#Sunnyvale so that the request URL ends with "/partitions/US%253ACA/CA%2523Sunnyvale". The name field in the response retains the encoded format. |
| <CopyableCode code="etag" /> | `string` | Optional. The etag for this partition. |
| <CopyableCode code="location" /> | `string` | Required. Immutable. The location of the entity data within the partition, for example, gs://bucket/path/to/entity/key1=value1/key2=value2. Or projects//datasets//tables/ |
| <CopyableCode code="values" /> | `array` | Required. Immutable. The set of values representing the partition, which correspond to the partition schema defined in the parent entity. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_lakes_zones_entities_partitions_get" /> | `SELECT` | <CopyableCode code="entitiesId, lakesId, locationsId, partitionsId, projectsId, zonesId" /> | Get a metadata partition of an entity. |
| <CopyableCode code="projects_locations_lakes_zones_entities_partitions_list" /> | `SELECT` | <CopyableCode code="entitiesId, lakesId, locationsId, projectsId, zonesId" /> | List metadata partitions of an entity. |
| <CopyableCode code="projects_locations_lakes_zones_entities_partitions_create" /> | `INSERT` | <CopyableCode code="entitiesId, lakesId, locationsId, projectsId, zonesId" /> | Create a metadata partition. |
| <CopyableCode code="projects_locations_lakes_zones_entities_partitions_delete" /> | `DELETE` | <CopyableCode code="entitiesId, lakesId, locationsId, partitionsId, projectsId, zonesId" /> | Delete a metadata partition. |
| <CopyableCode code="_projects_locations_lakes_zones_entities_partitions_list" /> | `EXEC` | <CopyableCode code="entitiesId, lakesId, locationsId, projectsId, zonesId" /> | List metadata partitions of an entity. |
