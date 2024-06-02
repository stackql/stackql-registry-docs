---
title: custom_classes
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_classes
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
<tr><td><b>Name</b></td><td><code>custom_classes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="speech.custom_classes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the custom class. |
| <CopyableCode code="annotations" /> | `object` | Output only. Allows users to store small amounts of arbitrary data. Both the key and the value must be 63 characters or less each. At most 100 annotations. This field is not used. |
| <CopyableCode code="customClassId" /> | `string` | If this custom class is a resource, the custom_class_id is the resource id of the CustomClass. Case sensitive. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. The time at which this resource was requested for deletion. This field is not used. |
| <CopyableCode code="displayName" /> | `string` | Output only. User-settable, human-readable name for the CustomClass. Must be 63 characters or less. This field is not used. |
| <CopyableCode code="etag" /> | `string` | Output only. This checksum is computed by the server based on the value of other fields. This may be sent on update, undelete, and delete requests to ensure the client has an up-to-date value before proceeding. This field is not used. |
| <CopyableCode code="expireTime" /> | `string` | Output only. The time at which this resource will be purged. This field is not used. |
| <CopyableCode code="items" /> | `array` | A collection of class items. |
| <CopyableCode code="kmsKeyName" /> | `string` | Output only. The [KMS key name](https://cloud.google.com/kms/docs/resource-hierarchy#keys) with which the content of the ClassItem is encrypted. The expected format is `projects/&#123;project&#125;/locations/&#123;location&#125;/keyRings/&#123;key_ring&#125;/cryptoKeys/&#123;crypto_key&#125;`. |
| <CopyableCode code="kmsKeyVersionName" /> | `string` | Output only. The [KMS key version name](https://cloud.google.com/kms/docs/resource-hierarchy#key_versions) with which content of the ClassItem is encrypted. The expected format is `projects/&#123;project&#125;/locations/&#123;location&#125;/keyRings/&#123;key_ring&#125;/cryptoKeys/&#123;crypto_key&#125;/cryptoKeyVersions/&#123;crypto_key_version&#125;`. |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. Whether or not this CustomClass is in the process of being updated. This field is not used. |
| <CopyableCode code="state" /> | `string` | Output only. The CustomClass lifecycle state. This field is not used. |
| <CopyableCode code="uid" /> | `string` | Output only. System-assigned unique identifier for the CustomClass. This field is not used. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customClassesId, locationsId, projectsId" /> | Get a custom class. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List custom classes. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a custom class. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customClassesId, locationsId, projectsId" /> | Delete a custom class. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | List custom classes. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="customClassesId, locationsId, projectsId" /> | Update a custom class. |
