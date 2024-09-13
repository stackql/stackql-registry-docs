
---
title: entity_types_feature_values
hide_title: false
hide_table_of_contents: false
keywords:
  - entity_types_feature_values
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

Creates, updates, deletes or gets an <code>entity_types_feature_value</code> resource or lists <code>entity_types_feature_values</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entity_types_feature_values</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.entity_types_feature_values" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete_feature_values" /> | `DELETE` | <CopyableCode code="entityTypesId, featurestoresId, locationsId, projectsId" /> | Delete Feature values from Featurestore. The progress of the deletion is tracked by the returned operation. The deleted feature values are guaranteed to be invisible to subsequent read operations after the operation is marked as successfully done. If a delete feature values operation fails, the feature values returned from reads and exports may be inconsistent. If consistency is required, the caller must retry the same delete request again and wait till the new operation returned is marked as successfully done. |

## `DELETE` example

Deletes the specified entity_types_feature_value resource.

```sql
DELETE FROM google.aiplatform.entity_types_feature_values
WHERE entityTypesId = '{{ entityTypesId }}'
AND featurestoresId = '{{ featurestoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
