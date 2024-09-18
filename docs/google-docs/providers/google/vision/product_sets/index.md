---
title: product_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - product_sets
  - vision
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

Creates, updates, deletes, gets or lists a <code>product_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>product_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vision.product_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the ProductSet. Format is: `projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID`. This field is ignored when creating a ProductSet. |
| <CopyableCode code="displayName" /> | `string` | The user-provided name for this ProductSet. Must not be empty. Must be at most 4096 characters long. |
| <CopyableCode code="indexError" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="indexTime" /> | `string` | Output only. The time at which this ProductSet was last indexed. Query results will reflect all updates before this time. If this ProductSet has never been indexed, this timestamp is the default value "1970-01-01T00:00:00Z". This field is ignored when creating a ProductSet. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_product_sets_get" /> | `SELECT` | <CopyableCode code="locationsId, productSetsId, projectsId" /> | Gets information associated with a ProductSet. Possible errors: * Returns NOT_FOUND if the ProductSet does not exist. |
| <CopyableCode code="projects_locations_product_sets_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists ProductSets in an unspecified order. Possible errors: * Returns INVALID_ARGUMENT if page_size is greater than 100, or less than 1. |
| <CopyableCode code="projects_locations_product_sets_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates and returns a new ProductSet resource. Possible errors: * Returns INVALID_ARGUMENT if display_name is missing, or is longer than 4096 characters. |
| <CopyableCode code="projects_locations_product_sets_delete" /> | `DELETE` | <CopyableCode code="locationsId, productSetsId, projectsId" /> | Permanently deletes a ProductSet. Products and ReferenceImages in the ProductSet are not deleted. The actual image files are not deleted from Google Cloud Storage. |
| <CopyableCode code="projects_locations_product_sets_patch" /> | `UPDATE` | <CopyableCode code="locationsId, productSetsId, projectsId" /> | Makes changes to a ProductSet resource. Only display_name can be updated currently. Possible errors: * Returns NOT_FOUND if the ProductSet does not exist. * Returns INVALID_ARGUMENT if display_name is present in update_mask but missing from the request or longer than 4096 characters. |
| <CopyableCode code="projects_locations_product_sets_import" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Asynchronous API that imports a list of reference images to specified product sets based on a list of image information. The google.longrunning.Operation API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress) `Operation.response` contains `ImportProductSetsResponse`. (results) The input source of this method is a csv file on Google Cloud Storage. For the format of the csv file please see ImportProductSetsGcsSource.csv_file_uri. |

## `SELECT` examples

Lists ProductSets in an unspecified order. Possible errors: * Returns INVALID_ARGUMENT if page_size is greater than 100, or less than 1.

```sql
SELECT
name,
displayName,
indexError,
indexTime
FROM google.vision.product_sets
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>product_sets</code> resource.

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
INSERT INTO google.vision.product_sets (
locationsId,
projectsId,
name,
displayName
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
displayName: string
indexTime: string
indexError:
  code: integer
  message: string
  details:
    - type: string
      additionalProperties: any

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>product_sets</code> resource.

```sql
/*+ update */
UPDATE google.vision.product_sets
SET 
name = '{{ name }}',
displayName = '{{ displayName }}'
WHERE 
locationsId = '{{ locationsId }}'
AND productSetsId = '{{ productSetsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>product_sets</code> resource.

```sql
/*+ delete */
DELETE FROM google.vision.product_sets
WHERE locationsId = '{{ locationsId }}'
AND productSetsId = '{{ productSetsId }}'
AND projectsId = '{{ projectsId }}';
```
