
---
title: feature_views_feature_values
hide_title: false
hide_table_of_contents: false
keywords:
  - feature_views_feature_values
  - aiplatform
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

Creates, updates, deletes or gets an <code>feature_views_feature_value</code> resource or lists <code>feature_views_feature_values</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>feature_views_feature_values</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.feature_views_feature_values" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dataKey" /> | `object` | Lookup key for a feature view. |
| <CopyableCode code="keyValues" /> | `object` | Response structure in the format of key (feature name) and (feature) value pair. |
| <CopyableCode code="protoStruct" /> | `object` | Feature values in proto Struct format. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_feature_values" /> | `SELECT` | <CopyableCode code="featureOnlineStoresId, featureViewsId, locationsId, projectsId" /> | Fetch feature values under a FeatureView. |

## `SELECT` examples

Fetch feature values under a FeatureView.

```sql
SELECT
dataKey,
keyValues,
protoStruct
FROM google.aiplatform.feature_views_feature_values
WHERE featureOnlineStoresId = '{{ featureOnlineStoresId }}'
AND featureViewsId = '{{ featureViewsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
