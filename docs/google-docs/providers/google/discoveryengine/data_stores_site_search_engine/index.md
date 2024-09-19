---
title: data_stores_site_search_engine
hide_title: false
hide_table_of_contents: false
keywords:
  - data_stores_site_search_engine
  - discoveryengine
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

Creates, updates, deletes, gets or lists a <code>data_stores_site_search_engine</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_stores_site_search_engine</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.discoveryengine.data_stores_site_search_engine" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The fully qualified resource name of the site search engine. Format: `projects/*/locations/*/dataStores/*/siteSearchEngine` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_collections_data_stores_get_site_search_engine" /> | `SELECT` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Gets the SiteSearchEngine. |
| <CopyableCode code="projects_locations_data_stores_get_site_search_engine" /> | `SELECT` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Gets the SiteSearchEngine. |

## `SELECT` examples

Gets the SiteSearchEngine.

```sql
SELECT
name
FROM google.discoveryengine.data_stores_site_search_engine
WHERE dataStoresId = '{{ dataStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
