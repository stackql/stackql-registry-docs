---
title: photos_media
hide_title: false
hide_table_of_contents: false
keywords:
  - photos_media
  - places
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

Creates, updates, deletes, gets or lists a <code>photos_media</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>photos_media</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.places.photos_media" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of a photo media in the format: `places/{place_id}/photos/{photo_reference}/media`. |
| <CopyableCode code="photoUri" /> | `string` | A short-lived uri that can be used to render the photo. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_media" /> | `SELECT` | <CopyableCode code="photosId, placesId" /> | Get a photo media with a photo reference string. |

## `SELECT` examples

Get a photo media with a photo reference string.

```sql
SELECT
name,
photoUri
FROM google.places.photos_media
WHERE photosId = '{{ photosId }}'
AND placesId = '{{ placesId }}';
```
