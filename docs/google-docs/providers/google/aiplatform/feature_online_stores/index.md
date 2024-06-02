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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>feature_online_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aiplatform.feature_online_stores" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Name of the FeatureOnlineStore. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/featureOnlineStores/&#123;featureOnlineStore&#125;` |
| <CopyableCode code="bigtable" /> | `object` |  |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this FeatureOnlineStore was created. |
| <CopyableCode code="dedicatedServingEndpoint" /> | `object` | The dedicated serving endpoint for this FeatureOnlineStore. Only need to set when you choose Optimized storage type. Public endpoint is provisioned by default. |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| <CopyableCode code="etag" /> | `string` | Optional. Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="labels" /> | `object` | Optional. The labels with user-defined metadata to organize your FeatureOnlineStore. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one FeatureOnlineStore(System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. |
| <CopyableCode code="optimized" /> | `object` | Optimized storage type |
| <CopyableCode code="state" /> | `string` | Output only. State of the featureOnlineStore. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this FeatureOnlineStore was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="featureOnlineStoresId, locationsId, projectsId" /> | Gets details of a single FeatureOnlineStore. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists FeatureOnlineStores in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new FeatureOnlineStore in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="featureOnlineStoresId, locationsId, projectsId" /> | Deletes a single FeatureOnlineStore. The FeatureOnlineStore must not contain any FeatureViews. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists FeatureOnlineStores in a given project and location. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="featureOnlineStoresId, locationsId, projectsId" /> | Updates the parameters of a single FeatureOnlineStore. |
