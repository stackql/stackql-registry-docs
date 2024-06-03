---
title: phrase_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - phrase_sets
  - speech
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
<tr><td><b>Name</b></td><td><code>phrase_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.speech.phrase_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the phrase set. |
| <CopyableCode code="annotations" /> | `object` | Output only. Allows users to store small amounts of arbitrary data. Both the key and the value must be 63 characters or less each. At most 100 annotations. This field is not used. |
| <CopyableCode code="boost" /> | `number` | Hint Boost. Positive value will increase the probability that a specific phrase will be recognized over other similar sounding phrases. The higher the boost, the higher the chance of false positive recognition as well. Negative boost values would correspond to anti-biasing. Anti-biasing is not enabled, so negative boost will simply be ignored. Though `boost` can accept a wide range of positive values, most use cases are best served with values between 0 (exclusive) and 20. We recommend using a binary search approach to finding the optimal value for your use case as well as adding phrases both with and without boost to your requests. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. The time at which this resource was requested for deletion. This field is not used. |
| <CopyableCode code="displayName" /> | `string` | Output only. User-settable, human-readable name for the PhraseSet. Must be 63 characters or less. This field is not used. |
| <CopyableCode code="etag" /> | `string` | Output only. This checksum is computed by the server based on the value of other fields. This may be sent on update, undelete, and delete requests to ensure the client has an up-to-date value before proceeding. This field is not used. |
| <CopyableCode code="expireTime" /> | `string` | Output only. The time at which this resource will be purged. This field is not used. |
| <CopyableCode code="kmsKeyName" /> | `string` | Output only. The [KMS key name](https://cloud.google.com/kms/docs/resource-hierarchy#keys) with which the content of the PhraseSet is encrypted. The expected format is `projects/&#123;project&#125;/locations/&#123;location&#125;/keyRings/&#123;key_ring&#125;/cryptoKeys/&#123;crypto_key&#125;`. |
| <CopyableCode code="kmsKeyVersionName" /> | `string` | Output only. The [KMS key version name](https://cloud.google.com/kms/docs/resource-hierarchy#key_versions) with which content of the PhraseSet is encrypted. The expected format is `projects/&#123;project&#125;/locations/&#123;location&#125;/keyRings/&#123;key_ring&#125;/cryptoKeys/&#123;crypto_key&#125;/cryptoKeyVersions/&#123;crypto_key_version&#125;`. |
| <CopyableCode code="phrases" /> | `array` | A list of word and phrases. |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. Whether or not this PhraseSet is in the process of being updated. This field is not used. |
| <CopyableCode code="state" /> | `string` | Output only. The CustomClass lifecycle state. This field is not used. |
| <CopyableCode code="uid" /> | `string` | Output only. System-assigned unique identifier for the PhraseSet. This field is not used. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, phraseSetsId, projectsId" /> | Get a phrase set. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List phrase sets. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a set of phrase hints. Each item in the set can be a single word or a multi-word phrase. The items in the PhraseSet are favored by the recognition model when you send a call that includes the PhraseSet. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, phraseSetsId, projectsId" /> | Delete a phrase set. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, phraseSetsId, projectsId" /> | Update a phrase set. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | List phrase sets. |
