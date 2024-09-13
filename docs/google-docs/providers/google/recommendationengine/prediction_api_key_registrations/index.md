
---
title: prediction_api_key_registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - prediction_api_key_registrations
  - recommendationengine
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

Creates, updates, deletes or gets an <code>prediction_api_key_registration</code> resource or lists <code>prediction_api_key_registrations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>prediction_api_key_registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.recommendationengine.prediction_api_key_registrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiKey" /> | `string` | The API key. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_catalogs_event_stores_prediction_api_key_registrations_list" /> | `SELECT` | <CopyableCode code="catalogsId, eventStoresId, locationsId, projectsId" /> | List the registered apiKeys for use with predict method. |
| <CopyableCode code="projects_locations_catalogs_event_stores_prediction_api_key_registrations_create" /> | `INSERT` | <CopyableCode code="catalogsId, eventStoresId, locationsId, projectsId" /> | Register an API key for use with predict method. |
| <CopyableCode code="projects_locations_catalogs_event_stores_prediction_api_key_registrations_delete" /> | `DELETE` | <CopyableCode code="catalogsId, eventStoresId, locationsId, predictionApiKeyRegistrationsId, projectsId" /> | Unregister an apiKey from using for predict method. |

## `SELECT` examples

List the registered apiKeys for use with predict method.

```sql
SELECT
apiKey
FROM google.recommendationengine.prediction_api_key_registrations
WHERE catalogsId = '{{ catalogsId }}'
AND eventStoresId = '{{ eventStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>prediction_api_key_registrations</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.recommendationengine.prediction_api_key_registrations (
catalogsId,
eventStoresId,
locationsId,
projectsId,
predictionApiKeyRegistration
)
SELECT 
'{{ catalogsId }}',
'{{ eventStoresId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ predictionApiKeyRegistration }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: predictionApiKeyRegistration
        value: '{{ predictionApiKeyRegistration }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified prediction_api_key_registration resource.

```sql
DELETE FROM google.recommendationengine.prediction_api_key_registrations
WHERE catalogsId = '{{ catalogsId }}'
AND eventStoresId = '{{ eventStoresId }}'
AND locationsId = '{{ locationsId }}'
AND predictionApiKeyRegistrationsId = '{{ predictionApiKeyRegistrationsId }}'
AND projectsId = '{{ projectsId }}';
```
