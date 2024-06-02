---
title: reference_images
hide_title: false
hide_table_of_contents: false
keywords:
  - reference_images
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reference_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vision.reference_images" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the reference image. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID/referenceImages/IMAGE_ID`. This field is ignored when creating a reference image. |
| <CopyableCode code="boundingPolys" /> | `array` | Optional. Bounding polygons around the areas of interest in the reference image. If this field is empty, the system will try to detect regions of interest. At most 10 bounding polygons will be used. The provided shape is converted into a non-rotated rectangle. Once converted, the small edge of the rectangle must be greater than or equal to 300 pixels. The aspect ratio must be 1:4 or less (i.e. 1:3 is ok; 1:5 is not). |
| <CopyableCode code="uri" /> | `string` | Required. The Google Cloud Storage URI of the reference image. The URI must start with `gs://`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_products_reference_images_get" /> | `SELECT` | <CopyableCode code="locationsId, productsId, projectsId, referenceImagesId" /> | Gets information associated with a ReferenceImage. Possible errors: * Returns NOT_FOUND if the specified image does not exist. |
| <CopyableCode code="projects_locations_products_reference_images_list" /> | `SELECT` | <CopyableCode code="locationsId, productsId, projectsId" /> | Lists reference images. Possible errors: * Returns NOT_FOUND if the parent product does not exist. * Returns INVALID_ARGUMENT if the page_size is greater than 100, or less than 1. |
| <CopyableCode code="projects_locations_products_reference_images_create" /> | `INSERT` | <CopyableCode code="locationsId, productsId, projectsId" /> | Creates and returns a new ReferenceImage resource. The `bounding_poly` field is optional. If `bounding_poly` is not specified, the system will try to detect regions of interest in the image that are compatible with the product_category on the parent product. If it is specified, detection is ALWAYS skipped. The system converts polygons into non-rotated rectangles. Note that the pipeline will resize the image if the image resolution is too large to process (above 50MP). Possible errors: * Returns INVALID_ARGUMENT if the image_uri is missing or longer than 4096 characters. * Returns INVALID_ARGUMENT if the product does not exist. * Returns INVALID_ARGUMENT if bounding_poly is not provided, and nothing compatible with the parent product's product_category is detected. * Returns INVALID_ARGUMENT if bounding_poly contains more than 10 polygons. |
| <CopyableCode code="projects_locations_products_reference_images_delete" /> | `DELETE` | <CopyableCode code="locationsId, productsId, projectsId, referenceImagesId" /> | Permanently deletes a reference image. The image metadata will be deleted right away, but search queries against ProductSets containing the image may still work until all related caches are refreshed. The actual image files are not deleted from Google Cloud Storage. |
| <CopyableCode code="_projects_locations_products_reference_images_list" /> | `EXEC` | <CopyableCode code="locationsId, productsId, projectsId" /> | Lists reference images. Possible errors: * Returns NOT_FOUND if the parent product does not exist. * Returns INVALID_ARGUMENT if the page_size is greater than 100, or less than 1. |
