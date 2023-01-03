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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>partitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataplex.partitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Partition values used in the HTTP URL must be double encoded. For example, url_encode(url_encode(value)) can be used to encode "US:CA/CA#Sunnyvale so that the request URL ends with "/partitions/US%253ACA/CA%2523Sunnyvale". The name field in the response retains the encoded format. |
| `location` | `string` | Required. Immutable. The location of the entity data within the partition, for example, gs://bucket/path/to/entity/key1=value1/key2=value2. Or projects//datasets//tables/ |
| `values` | `array` | Required. Immutable. The set of values representing the partition, which correspond to the partition schema defined in the parent entity. |
| `etag` | `string` | Optional. The etag for this partition. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_lakes_zones_entities_partitions_get` | `SELECT` | `entitiesId, lakesId, locationsId, partitionsId, projectsId, zonesId` | Get a metadata partition of an entity. |
| `projects_locations_lakes_zones_entities_partitions_list` | `SELECT` | `entitiesId, lakesId, locationsId, projectsId, zonesId` | List metadata partitions of an entity. |
| `projects_locations_lakes_zones_entities_partitions_create` | `INSERT` | `entitiesId, lakesId, locationsId, projectsId, zonesId` | Create a metadata partition. |
| `projects_locations_lakes_zones_entities_partitions_delete` | `DELETE` | `entitiesId, lakesId, locationsId, partitionsId, projectsId, zonesId` | Delete a metadata partition. |
