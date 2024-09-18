---
title: feature_online_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - feature_online_stores
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

Creates, updates, deletes, gets or lists a <code>feature_online_stores</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>feature_online_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.feature_online_stores" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Name of the FeatureOnlineStore. Format: `projects/{project}/locations/{location}/featureOnlineStores/{featureOnlineStore}` |
| <CopyableCode code="bigtable" /> | `object` |  |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this FeatureOnlineStore was created. |
| <CopyableCode code="dedicatedServingEndpoint" /> | `object` | The dedicated serving endpoint for this FeatureOnlineStore. Only need to set when you choose Optimized storage type. Public endpoint is provisioned by default. |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| <CopyableCode code="etag" /> | `string` | Optional. Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="labels" /> | `object` | Optional. The labels with user-defined metadata to organize your FeatureOnlineStore. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one FeatureOnlineStore(System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. |
| <CopyableCode code="optimized" /> | `object` | Optimized storage type |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="state" /> | `string` | Output only. State of the featureOnlineStore. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this FeatureOnlineStore was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="featureOnlineStoresId, locationsId, projectsId" /> | Gets details of a single FeatureOnlineStore. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists FeatureOnlineStores in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new FeatureOnlineStore in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="featureOnlineStoresId, locationsId, projectsId" /> | Deletes a single FeatureOnlineStore. The FeatureOnlineStore must not contain any FeatureViews. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="featureOnlineStoresId, locationsId, projectsId" /> | Updates the parameters of a single FeatureOnlineStore. |

## `SELECT` examples

Lists FeatureOnlineStores in a given project and location.

```sql
SELECT
name,
bigtable,
createTime,
dedicatedServingEndpoint,
encryptionSpec,
etag,
labels,
optimized,
satisfiesPzi,
satisfiesPzs,
state,
updateTime
FROM google.aiplatform.feature_online_stores
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>feature_online_stores</code> resource.

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
INSERT INTO google.aiplatform.feature_online_stores (
locationsId,
projectsId,
dedicatedServingEndpoint,
etag,
labels,
optimized,
name,
bigtable,
encryptionSpec
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ dedicatedServingEndpoint }}',
'{{ etag }}',
'{{ labels }}',
'{{ optimized }}',
'{{ name }}',
'{{ bigtable }}',
'{{ encryptionSpec }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
dedicatedServingEndpoint:
  privateServiceConnectConfig:
    serviceAttachment: string
    enablePrivateServiceConnect: boolean
    projectAllowlist:
      - type: string
  publicEndpointDomainName: string
  serviceAttachment: string
updateTime: string
etag: string
satisfiesPzs: boolean
labels: object
createTime: string
optimized: {}
name: string
bigtable:
  autoScaling:
    cpuUtilizationTarget: integer
    minNodeCount: integer
    maxNodeCount: integer
state: string
encryptionSpec:
  kmsKeyName: string
satisfiesPzi: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>feature_online_stores</code> resource.

```sql
/*+ update */
UPDATE google.aiplatform.feature_online_stores
SET 
dedicatedServingEndpoint = '{{ dedicatedServingEndpoint }}',
etag = '{{ etag }}',
labels = '{{ labels }}',
optimized = '{{ optimized }}',
name = '{{ name }}',
bigtable = '{{ bigtable }}',
encryptionSpec = '{{ encryptionSpec }}'
WHERE 
featureOnlineStoresId = '{{ featureOnlineStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>feature_online_stores</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.feature_online_stores
WHERE featureOnlineStoresId = '{{ featureOnlineStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
