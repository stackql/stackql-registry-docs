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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_classes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.speech.custom_classes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the custom class. |
| `items` | `array` | A collection of class items. |
| `kmsKeyName` | `string` | Output only. The [KMS key name](https://cloud.google.com/kms/docs/resource-hierarchy#keys) with which the content of the ClassItem is encrypted. The expected format is `projects/&#123;project&#125;/locations/&#123;location&#125;/keyRings/&#123;key_ring&#125;/cryptoKeys/&#123;crypto_key&#125;`. |
| `kmsKeyVersionName` | `string` | Output only. The [KMS key version name](https://cloud.google.com/kms/docs/resource-hierarchy#key_versions) with which content of the ClassItem is encrypted. The expected format is `projects/&#123;project&#125;/locations/&#123;location&#125;/keyRings/&#123;key_ring&#125;/cryptoKeys/&#123;crypto_key&#125;/cryptoKeyVersions/&#123;crypto_key_version&#125;`. |
| `customClassId` | `string` | If this custom class is a resource, the custom_class_id is the resource id of the CustomClass. Case sensitive. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `customClassesId, locationsId, projectsId` | Get a custom class. |
| `list` | `SELECT` | `locationsId, projectsId` | List custom classes. |
| `create` | `INSERT` | `locationsId, projectsId` | Create a custom class. |
| `delete` | `DELETE` | `customClassesId, locationsId, projectsId` | Delete a custom class. |
| `_list` | `EXEC` | `locationsId, projectsId` | List custom classes. |
| `patch` | `EXEC` | `customClassesId, locationsId, projectsId` | Update a custom class. |
