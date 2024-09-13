---
title: site_search_engine_domain_verification_status
hide_title: false
hide_table_of_contents: false
keywords:
  - site_search_engine_domain_verification_status
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

Creates, updates, deletes or gets an <code>site_search_engine_domain_verification_status</code> resource or lists <code>site_search_engine_domain_verification_status</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>site_search_engine_domain_verification_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.discoveryengine.site_search_engine_domain_verification_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="nextPageToken" /> | `string` | A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| <CopyableCode code="targetSites" /> | `array` | List of TargetSites containing the site verification status. |
| <CopyableCode code="totalSize" /> | `integer` | The total number of items matching the request. This will always be populated in the response. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_collections_data_stores_site_search_engine_fetch_domain_verification_status" /> | `SELECT` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Returns list of target sites with its domain verification status. This method can only be called under data store with BASIC_SITE_SEARCH state at the moment. |

## `SELECT` examples

Returns list of target sites with its domain verification status. This method can only be called under data store with BASIC_SITE_SEARCH state at the moment.

```sql
SELECT
nextPageToken,
targetSites,
totalSize
FROM google.discoveryengine.site_search_engine_domain_verification_status
WHERE collectionsId = '{{ collectionsId }}'
AND dataStoresId = '{{ dataStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
